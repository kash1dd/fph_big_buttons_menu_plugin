from __future__ import annotations

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def big_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.button(
        text='⚙️ Настройки',
    )
    builder.button(
        text='🐙 Меню',
    )
    builder.button(
        text='♻️ Перезапустить',
    )
    builder.adjust(2, 1)
    return builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder='🐙 FunPay HUB',
    )


def hide_kb() -> ReplyKeyboardRemove:
    return ReplyKeyboardRemove()
