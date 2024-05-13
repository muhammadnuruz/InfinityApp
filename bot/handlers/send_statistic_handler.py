import datetime
import json
import os

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import ChatNotFound

from bot.buttons.functions import create_statistic_image
from bot.buttons.inline_buttons import send_statistic_buttons
from bot.buttons.reply_buttons import back_admin_menu_button, admin_menu_buttons
from bot.buttons.text import send_statistic
from bot.dispatcher import dp, bot
from main import admins


@dp.message_handler(Text(send_statistic))
async def send_statistic_function_1(msg: types.Message, state: FSMContext):
    if msg.from_user.id in admins:
        await state.set_state("send_statistic_1")
        await msg.answer(text="Qaysi guruh statistikasini yubormoxchisiz ❓",
                         reply_markup=await send_statistic_buttons())
        await msg.answer(text="Guruhni tanlang ☝", reply_markup=await back_admin_menu_button())


@dp.callback_query_handler(state='send_statistic_1')
async def send_statistic_function_2(call: types.CallbackQuery, state: FSMContext):
    lesson = json.loads(requests.get(url=f"http://127.0.0.1:8000/lessons/{call.data}/").content)
    group = json.loads(requests.get(url=f"http://127.0.0.1:8000/groups/{lesson['group']}/").content)
    d = {}
    for i in group['students_id']:
        student = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/detail/{i}/").content)
        try:
            l_student = json.loads(requests.get(
                url=f"http://127.0.0.1:8000/lessons/lesson_student/{student['id']}/{lesson['id']}/").content)
            d.update({student['name'] + ' ' + student['surname']: l_student['evaluation']})
        except Exception:
            pass
    date_object = datetime.datetime.strptime(lesson['created_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
    year = date_object.year
    month = date_object.month
    day = date_object.day
    create_statistic_image(data=d, chat_id=call.from_user.id, name=f"Infin {lesson['group']} - {lesson['name']}",
                           date=f"{day}.{month}.{year}")
    await call.message.delete()
    message = await call.message.answer_photo(photo=open(f"images/{call.from_user.id}.png", "rb"),
                                              reply_markup=await admin_menu_buttons())
    await call.answer(text="Statistika o'quvchilarga yuborildi ✅", show_alert=True)
    for i in group['students_id']:
        try:
            student = json.loads(requests.get(url=f"http://127.0.0.1:8000/students/detail/{i}/").content)
            await bot.send_photo(chat_id=int(student['chat_id']), photo=open(f"images/{call.from_user.id}.png", "rb"),
                                 reply_markup=message.reply_markup)
        except ChatNotFound:
            pass
    os.remove(f"images/{call.from_user.id}.png")
    await state.finish()
