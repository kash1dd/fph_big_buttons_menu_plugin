from __future__ import annotations

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from funpayhub import exit_codes
from funpayhub.lib import Translater

from funpayhub.lib.telegram.ui import UIRegistry, MenuContext
from funpayhub.lib.base_app.telegram.app.ui.callbacks import OpenMenu
from funpayhub.lib.base_app.telegram.app.properties.ui import NodeMenuContext

from funpayhub.app.main import FunPayHub
from funpayhub.app.telegram.ui.ids import MenuIds

from .kb import big_kb, hide_kb


router = Router()


@router.message(Command('show_kb'))
async def show_kb_handler(message: Message) -> None:
    await message.answer(
        '🤩 <b>Вот твоя большая клавиатура!</b>',
        reply_markup=big_kb(),
    )


@router.message(Command('hide_kb'))
async def hide_kb_handler(message: Message) -> None:
    await message.answer(
        '😢 <b>Клавиатура скрыта :(</b>',
        reply_markup=hide_kb(),
    )


@router.message(F.text == '⚙️ Настройки')
async def settings_handler(message: Message, tg_ui: UIRegistry) -> None:
    await NodeMenuContext(
        menu_id=MenuIds.props_node,
        trigger=message,
        entry_path=[],
        callback_override=OpenMenu(menu_id=MenuIds.props_node, context_data={'entry_path': []}),
    ).build_and_answer(tg_ui, message)


@router.message(F.text == '🐙 Меню')
async def menu_handler(message: Message, tg_ui: UIRegistry) -> None:
    await MenuContext(
        menu_id=MenuIds.main_menu,
        trigger=message,
        callback_override=OpenMenu(menu_id=MenuIds.main_menu),
    ).build_and_answer(tg_ui, message)


@router.message(F.text == '♻️ Перезапустить')
async def restart_handler(message: Message, translater: Translater, hub: FunPayHub) -> None:
    await message.reply(translater.translate('♻️ Перезапускаюсь...'))
    await hub.shutdown(exit_codes.RESTART)
