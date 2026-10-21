from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()
pasw=os.getenv("PASSWORD_DB")

async def connection_db():
    try:
        conn=await asyncpg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            database="bot_db",
            password=pasw
        )
        return conn
    except Exception as error:
        print(f"Connection Error: {error}")
        
    
async def create_table():
    try:
        conn=await connection_db()
        await conn.execute("""
            Create table if not exists users(
                user_id serial primary key,
                username varchar(200),
                full_name varchar(200),
                telegram_id varchar(300),
                create_at timestamp default now(),
                is_active boolean default true
            )
                           """)
        print("Table is created Sucsessfully")
    except Exception as error:
        print(f"reate Error: {error}")
    finally:
        await conn.close()
        