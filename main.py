from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
# from connection import *
from connection import *
from service import *
import asyncio
import random
import os

load_dotenv()

token=os.getenv("BOT_TOKEN")
bot=Bot(token=token)
dp=Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    if await get_user_id(message.from_user.id):
        await message.answer(f"""
Assalom {message.from_user.first_name}! 
In bot baroi Khursandi va vaktguzaroni.

Comands:
    /start - Baroi boziro Ogoz namudan       

    /send_cube - Baroi partoftani kubikho!!!
      
    /coin - Tanga baroi Oryol Reshka!!!
      
    /help - Baroi Malumot!!!
    
    /get_user for looking after users of bot
""")
        
    else:
        user=message.from_user
        await create_user(user.username, user.full_name, user.id)
        await message.answer(f"Hello @{message.from_user.username}")
        
@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("""
This bot was crated by Python codes and it has 4 comands:

/help for helping before starting the game
/start is starting your games
/send_cube is for playing with
/coin is for playing with (Oryol & Reshka)
""")

@dp.message(Command("send_cube"))
async def send_cube(message: Message):
    number = random.randint(1, 6)
    await message.answer(f"The number was: {number} 🎲")

@dp.message(Command("coin"))
async def coin(message: Message):
    result = random.choice(["Oryol 🦅", "Reshka 🪙"])
    await message.answer(f"Natija: {result}")


@dp.message(Command("get_user"))
async def get_user(message: Message):
    users=await get_users()
    for user in users:
        await message.answer(f"""
Username: {user["username"]}
Full_name: {user["full_name"]}
Create_at: {user["create_at"]}
                             """)



async def main():
    await create_table()
    print("Start playing...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())