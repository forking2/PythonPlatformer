
import asyncio, logging, sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6790307425:AAGlCR-uKs6o2bIwVyyTPNaeYDwQASjunZk'
dp = Dispatcher()


@dp.message(CommandStart())  # /start
async def command_start(message: Message):
    await  message.answer(f'Hi,{html.bold(message.from_user.full_name)}!')


@dp.message(Command('url'))
async def command_url(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Mystat", url='https://playvalorant.com/ua-ua/'))
    builder.row(InlineKeyboardButton(text="Photo",
                                     url='https://media.npr.org/assets/img/2014/08/07/monkey-selfie_custom-6624e8356a07d872997e801d7a04aa8cdc8fbaac.jpg?s=1100&c=50&f=jpeg'))

    userId = message.from_user.id
    chatInfo = await bot.get_chat(userId)
    if not chatInfo.has_private_forwards:
        builder.row(InlineKeyboardButton(text='User', url=f'tg://user?id={userId}'))
        await message.answer('Oберіть питання:', reply_markup=builder.as_markup())


@dp.message(Command('button'))
async def cmd_button(messege: Message):
    kb = [
        [KeyboardButton(text='hi')],
        [KeyboardButton(text='install')],
        [KeyboardButton(text='help')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='оберіть команду')
    await messege.answer("Наші команди", reply_markup=keyboard)


@dp.message(F.text == "hi")
async def command_hi(message: Message):
    await  message.answer(f'Hello,{html.bold(message.from_user.full_name)}!')


@dp.message(F.text == "help")
async def command_hi(message: Message):
    await  message.answer(f'rothberisja sam,{html.bold(message.from_user.full_name)}!')


@dp.message(F.text == "install")
async def command_hi(message: Message):
    await  message.answer(f'https://store.steampowered.com/?l=ukranian,{html.bold(message.from_user.full_name)}!')


@dp.message()
async def commane_echo(message):
    await message.send_copy(chat_id=message.chat.id)


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await  dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())






