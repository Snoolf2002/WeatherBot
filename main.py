import logging
# import os

# import updater
# import updater as updater
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '5526964591:AAH_oDmeH7hFjUCYVxc62DwB646GElrDoWU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start`  command
    """
    await message.answer("Bu bot orqali ayni damda istalgan shaxardagi havo haroratini bilishingiz mumkin. Iltimos shaxar nomini kiriting: ")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Shaxar nomini yuboring, sizga shu shaxarda ayni damdagi havo harorati necha gradus ekanligini yuboramiz!")


@dp.message_handler()
async def weather(message: types.Message):
    city_user = message.text.lower()

    url = "https://api.weatherapi.com/v1/current.json?key=7ee2e5e2c64c4bb18c621610221107&q="+city_user
    r = requests.get(url)
    res = r.json()
    if 'error' in res.keys():
        await message.answer("Shaxar nomini to'g'ri kiriting!")
    else:
        daraja = res["current"]["temp_c"]
        await message.answer(f"{city_user.capitalize()} → {daraja}°.")

# PORT = int(os.environ.get("PORT", 13978))
# updater.start_webhook(listen="0.0.0.0",
#                           port=PORT,
#                           url_path=API_TOKEN)
# updater.bot.setWebhook('https://rocky-castle-64391.herokuapp.com/' + API_TOKEN)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
