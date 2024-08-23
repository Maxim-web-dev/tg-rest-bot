from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, WebAppData

#config
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.configs import config

#project-files
import keyboards

#other modules
import asyncio

class Telegram_rest_bot:
    def __init__(self, TOKEN: str, ADMIN: str) -> None:
        self.admin = ADMIN
        
        self.bot = Bot(TOKEN)
        self.dp = Dispatcher() 
        
    async def listen(self) -> None:
        # == start ==
        @self.dp.message(Command('start'))
        async def start(message: Message) -> None:
            #start-message
            await message.answer(config.welcome_text,
                                 parse_mode = 'html',
                                 reply_markup = keyboards.main_keyboard)
        
        # -- echo -- 
        @self.dp.message()
        async def echo(message: Message):
            if message.text.lower() == 'информация о заказе':
                await message.answer(text = f"Данные о вашем заказе: {message.web_app_data.data}")
 
    async def main(self) -> None:
        print(f"{self.admin} is started bot !")
        await self.bot.delete_webhook(drop_pending_updates = True)
        await self.dp.start_polling(self.bot)
        
        
if __name__ == '__main__':
    tg_bot = Telegram_rest_bot(TOKEN = config.TOKEN, ADMIN = config.j['ADMIN'])
    
    asyncio.run(tg_bot.listen())
    asyncio.run(tg_bot.main())
        