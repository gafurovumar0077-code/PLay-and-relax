from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
import asyncio
import random
import os

load_dotenv()

token=os.getenv("BOT_TOKEN")
bot=Bot(token=token)
dp=Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"""
Assalom {message.from_user.first_name}! 
In bot baroi Khursandi va vaktguzaroni.

Comands:
    /start - Baroi boziro Ogoz namudan       

    /send - Baroi partoftani kubikho!!!
      
    /coin - Tanga baroi Oryol Reshka!!!
      
    /help - Baroi Malumot!!!
""")
@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("In bot bo istifoda az zaboni barnomasozi Python sokhta shudaast! ")

@dp.message(Command("send"))
async def send(message: Message):
    number = random.randint(1, 6)
    await message.answer(f"The number was: {number} 🎲")

@dp.message(Command("coin"))
async def coin(message: Message):
    result = random.choice(["Oryol 🦅", "Reshka 🪙"])
    await message.answer(f"Natija: {result}")

async def main():
    print("Start playing...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())