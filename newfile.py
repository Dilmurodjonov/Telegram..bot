import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# Bot tokenini kiriting
TOKEN = "7450693776:AAHgcEe-m7hH1zwlNxiufwsMeOYRzjR3bv4"

# Kanallar ro‘yxati
CHANNELS = [
    ("Obuna boʻling➕", "https://t.me/+h0-JlzGvpOJjMGFi", "-1001234567890"),  
    ("Obuna boʻling➕", "https://t.me/+KG8pHrZzuoEyOGJi", "-1002345678901"),  
    ("Obuna boʻling➕", "https://t.me/+7npaFgqzKbY5NTky", "-1003456789012"),  
    ("Obuna boʻling➕", "https://t.me/+GLxWIR97uCY0NDZi", "-1004567890123"),  
    ("Obuna boʻling➕", "https://t.me/+Eb6SimPEEN8xNGIy", "-1005678901234"),
    ("Obuna boʻling➕", "https://www.instagram.com/full_hd_kinolar?igsh=MWZ4czJvbDZyMGJvOA==", None)  # Instagram uchun
]

# Logging yoqish
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Obuna bo‘lish tugmalari
def subscribe_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    for name, link, chat_id in CHANNELS:
        keyboard.add(InlineKeyboardButton(text=name, url=link))
    keyboard.add(InlineKeyboardButton(text="Tasdiqlash✅", callback_data="check_subscription"))
    keyboard.add(InlineKeyboardButton(text="Ochish⬅️", url="http://t.me/Kinolarfullhdbot/Obuna6"))  # Yangi tugma
    return keyboard

# Start komandasi
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Bu kanallarga obuna boʻlib kinolarni koʻrishingiz mumkin🎬🎬🎬\n\nObuna boʻling➕",
        reply_markup=subscribe_keyboard()
    )

# Obuna tekshirish
@dp.callback_query_handler(lambda call: call.data == "check_subscription")
async def check_subscription(call: types.CallbackQuery):
    user_id = call.from_user.id
    not_subscribed = []

    for name, _, chat_id in CHANNELS:
        if chat_id is not None:  # Instagram uchun tekshirmaymiz
            try:
                chat_member = await bot.get_chat_member(chat_id, user_id)
                if chat_member.status not in ["member", "administrator", "creator"]:
                    not_subscribed.append(name)
            except Exception:
                not_subscribed.append(name)

    if not_subscribed:
        await call.message.edit_text(
            "Siz kanallarga obuna boʻlmadiz❌\n\nIltimos, quyidagi kanallarga obuna boʻling:",
            reply_markup=subscribe_keyboard()
        )
    else:
        await call.message.edit_text("Rahmat! Siz kanallarga obuna boʻldingiz ✅")

# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)