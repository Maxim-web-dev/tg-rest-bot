from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

#config
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.configs import config

#other modules
import asyncio

class Telegram_rest_bot:
    def __init__(self, TOKEN: str, ADMIN: str) -> None:
        self.admin = ADMIN
        
        self.bot = Bot(TOKEN)
        self.dp = Dispatcher()
        
    async def start(self) -> None:
        await self.bot.delete_webhook(drop_pending_updates = True)
        await self.dp.start_polling(self.bot)
        
if __name__ == '__main__':
    tg_bot = Telegram_rest_bot(TOKEN = config.TOKEN, ADMIN = config.j['ADMIN'])
    asyncio.run(tg_bot.start())
        