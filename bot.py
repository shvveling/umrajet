
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMINS

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("🕋 <b>UmraJet</b> botiga xush kelibsiz!\n\n🇸🇦 Umra xizmatlari | 🧳 Aerochipta | 🏨 Mehmonxona\n\nSavollar uchun @vip_arabiy")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
