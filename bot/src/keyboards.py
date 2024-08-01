from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonPollType
)
main_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Сделать заказ"),
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
