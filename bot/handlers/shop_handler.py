from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.inline_buttons import shop_buttons
from bot.buttons.text import shop, shop_ru
from bot.dispatcher import dp


@dp.message_handler(Text(equals=[shop, shop_ru]))
async def shop_handler_1(msg: types.Message):
    if msg.text == shop:
        await msg.answer(text="Kutilmoqda 🕕")
    else:
        await msg.answer(text="Жду 🕕")
    # await msg.answer(text="Infin Marketga hush kelibsiz 😊", reply_markup=await shop_buttons())
