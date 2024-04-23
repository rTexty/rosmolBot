from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tasks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мои задачи", callback_data="задачи")
        ],
    ]
)

all_tasks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Все задачи", callback_data="all_tasks")
        ]
    ]
)

create_task_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Создать задачу", callback_data="create")
        ]
    ]
)


admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Камиль(Разработчик)", callback_data="admin_5944980799")
        ],
        [
            InlineKeyboardButton(text="Эльнур(Дизайн)", callback_data="admin_821572310")
        ],
        [
            InlineKeyboardButton(text="Геворг(Контент)", callback_data="admin_1067026582")
        ],
        [
            InlineKeyboardButton(text="Шариф(Рассылки)", callback_data="admin_5783300854")
        ],
    ]
)
