from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Bot, Router
from datetime import date
from database.ORM import get_data
from bot.keyboards.complete_kb import completed_tasks_keyboard
from bot.keyboards.main_kb import tasks_keyboard, all_tasks_keyboard

router = Router()



@router.message(CommandStart())
async def start_handler(message: Message, bot: Bot):
    try:
        user_id, name, direction, manager = await get_data(message)
        if user_id:
            if manager is True:
                await message.answer(f'Добро пожаловать в систему!\nВаше имя: {name}\nВаше направление: {direction}\n',
                                     reply_markup=all_tasks_keyboard)
            else:
                await bot.send_message(message.from_user.id,
                                        f'Добро пожаловать в систему!\nВаше имя: {name}\nВаше направление: {direction}\n',
                                        reply_markup=tasks_keyboard)
    except TypeError:
        await bot.send_message(message.from_user.id, 'Доступ Запрещен!\nОбратитесь к Администратору(@rtexty)')

