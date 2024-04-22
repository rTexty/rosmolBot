from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мои задачи", callback_data="задачи")
        ],
    ]
)
