from bot.keyboards.main_kb import admin_keyboard
from database.ORM import create_task
from aiogram.types import CallbackQuery, Message
from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class FSM(StatesGroup):
    executor = State()
    text_of_task = State()

    async def clear(self) -> None:
        await self.set_state(state=None)
        await self.set_data({})


router = Router()


@router.callback_query(lambda c: c.data == 'create')
async def choose_creator(query: CallbackQuery, state: FSMContext):
    await state.set_state(FSM.executor)
    # Отправляем сообщение с клавиатурой пользователю
    await query.message.answer('Выберите исполнителя ⬇️:', reply_markup=admin_keyboard)


@router.callback_query(lambda c: c.data.startswith('admin_'))
async def create_task_handler(query: CallbackQuery, state: FSMContext):
    # Обрабатываем выбор пользователя
    await state.update_data(executor=int(query.data.split('_')[1]))
    await state.set_state(FSM.text_of_task)
    await query.message.answer('Отправьте текст задачи:')


@router.message(FSM.text_of_task)
async def task_description_handler(message: Message, state: FSMContext, bot: Bot,):
    await state.update_data(text_of_task=message.text)
    data = await state.get_data()
    admin_id = data.get('executor')
    text = data.get('text_of_task')

    if admin_id is None:
        # Отправляем сообщение об ошибке пользователю
        await message.answer('Вы не выбрали исполнителя!')
    else:
        await message.answer('Задача успешно создана!')
        await create_task(admin_id=admin_id, task_description=text, message=message)
        await bot.send_message(chat_id=admin_id, text=f"Администратор - {message.from_user.username}\n"
                                                      f"Создал вам новую задачу:\n\n{text}")
        await state.clear()
