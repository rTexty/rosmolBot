from aiogram.utils import keyboard

from bot.keyboards.main_kb import admin_keyboard
from database.ORM import create_task, get_admins
from aiogram.types import CallbackQuery, Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class FSM(StatesGroup):
    creator = State()
    text_of_task = State()

    async def clear(self) -> None:
        await self.set_state(state=None)
        await self.set_data({})


router = Router()


@router.callback_query(lambda c: c.data == 'create')
async def choose_creator(query: CallbackQuery, state: FSMContext):
    state.set_state(FSM.creator)

    # Получаем список исполнителей из базы данных
    admins = await get_admins(query)


    # Отправляем сообщение с клавиатурой пользователю
    await query.message.answer('Выберите исполнителя ⬇️:', reply_markup=admin_keyboard)


@router.callback_query(lambda c: c.data.startswith('admin_'))
async def create_task_handler(query: CallbackQuery, state: FSMContext):
    await state.update_data(creator=int(query.data.split('_')[1]))
    await state.set_state(FSM.text_of_task)
    await query.message.answer('Отправьте текст задачи:')


@router.message(FSM.text_of_task)
async def task_description_handler(message: Message, state: FSMContext):
    await state.update_data(text_of_task=message.text)
    admin_id = await state.get_data()
    text = await state.get_data()

    if admin_id is None:
        # Отправляем сообщение об ошибке пользователю
        await message.answer('Вы не выбрали исполнителя!')
    else:
        await create_task(admin_id=admin_id['creator'], task_description=text['text_of_task'])
        await message.answer('Задача успешно создана!')
        await state.clear()
