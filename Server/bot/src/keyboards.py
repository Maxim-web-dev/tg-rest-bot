from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
# --config--
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.configs.config import j

main_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = "Сделать заказ", 
                web_app = WebAppInfo(url = j['link_to_WebApp'])
            ),
            KeyboardButton(text = "Тех-Поддержка")
        ],
        [
            KeyboardButton(text = "Информация о заказе")
        ]
    ],                  
    resize_keyboard = True,
    input_field_placeholder = 'Что хотите сделать? Нажмите на нужную вам кнопку.',
    selective = True
)
