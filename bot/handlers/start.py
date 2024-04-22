from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Bot, Router
from datetime import date
from database.ORM import get_data
from bot.keyboards.complete_kb import completed_tasks_keyboard
from bot.keyboards.main_kb import tasks_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, bot: Bot):
    user_id, name, direction = await get_data(message)

    if user_id:
        await bot.send_message(message.from_user.id,
                               f'Добро пожаловать в систему!\nВаше имя: {name}\nВаше направление: {direction}\n',
                               reply_markup=tasks_keyboard)
    else:
        await bot.send_message(message.from_user.id, 'Доступ Запрещен!\nОбратитесь к Администратору(@rtexty)')


@router.callback_query(lambda callback_query: callback_query.data == 'задачи')
async def tasks_handler(query: CallbackQuery,):
    user_id, _, _, = await get_data(query)
    if user_id == query.from_user.id:
        await query.message.answer(f'Ваши задачи на {date.today().strftime("%d-%m-%Y")}:\n\n{tasks}',
                                   reply_markup=completed_tasks_keyboard)
