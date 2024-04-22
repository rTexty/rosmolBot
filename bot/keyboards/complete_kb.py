from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

completed_tasks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Отметить выполненным ✅", callback_data="completed_tasks")
        ]
    ]
)