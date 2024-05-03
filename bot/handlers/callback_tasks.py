from aiogram import Router
from aiogram.types import CallbackQuery
from bot.keyboards.complete_kb import completed_tasks_keyboard
from bot.keyboards.main_kb import create_task_keyboard
from database.ORM import get_data, get_tasks, get_all_tasks_with_users
from datetime import date

router = Router()


@router.callback_query(lambda callback_query: callback_query.data == 'задачи')
async def tasks_handler(query: CallbackQuery):
    user_id, *_ = await get_data(query)
    tasks_with_creators = await get_tasks(query)
    if user_id == query.from_user.id:
        # Сортировка задач по создателям
        tasks_by_creator = {}
        for task, creator in tasks_with_creators:
            if creator in tasks_by_creator:
                tasks_by_creator[creator].append(task)
            else:
                tasks_by_creator[creator] = [task]

        # Формирование строки для вывода задач, сгруппированных по создателям
        tasks_display = []
        for creator, tasks in tasks_by_creator.items():
            tasks_display.append(f'@{creator}:\n' + '\n'.join(tasks))
        tasks_str = '\n\n'.join(tasks_display)

        await query.message.answer(f'Ваши задачи на {date.today().strftime("%d-%m-%Y")}:\n\n{tasks_str}')



@router.callback_query(lambda c: c.data == 'all_tasks')
async def all_tasks_handler(query: CallbackQuery,):
    tasks = await get_all_tasks_with_users(query)
    await query.message.answer(f'Все задачи:\n\n{tasks}\n\nВыберите действие',
                               reply_markup=create_task_keyboard)
