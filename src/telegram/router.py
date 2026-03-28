from __future__ import annotations

from contextlib import suppress

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from funpayhub import exit_codes
from funpayhub.lib import Translater

from funpayhub.lib.telegram.ui import MenuContext
from funpayhub.lib.base_app.telegram.app.properties.ui import NodeMenuContext

from funpayhub.app.main import FunPayHub
from funpayhub.app.telegram.ui.ids import MenuIds

from .kb import big_kb, hide_kb
from .callbacks import HideKbCD, ShowKbCD


router = Router()
last_msg = None


@router.callback_query(ShowKbCD.filter())
async def show_kb_handler(call: CallbackQuery) -> None:
    global last_msg

    if last_msg:
        with suppress(Exception):
            await last_msg.delete()

    last_msg = await call.message.answer(
        '<tg-emoji emoji-id="5461014912153165940">⌨️</tg-emoji>',
        reply_markup=big_kb(),
    )
    await call.answer()


@router.callback_query(HideKbCD.filter())
async def hide_kb_handler(call: CallbackQuery) -> None:
    global last_msg

    if last_msg:
        with suppress(Exception):
            await last_msg.delete()

    last_msg = await call.message.answer(
        '<tg-emoji emoji-id="5460641228523576168">👋</tg-emoji>',
        reply_markup=hide_kb(),
    )
    await call.answer()


@router.message(F.text == '⚙️ Настройки')
async def settings_handler(message: Message) -> None:
    await NodeMenuContext(
        menu_id=MenuIds.props_node,
        trigger=message,
        entry_path=[],
    ).answer_to(message)


@router.message(F.text == '🐙 Меню')
async def menu_handler(message: Message) -> None:
    await MenuContext(
        menu_id=MenuIds.main_menu,
        trigger=message,
    ).answer_to(message)


@router.message(F.text == '♻️ Перезапустить')
async def restart_handler(message: Message, translater: Translater, hub: FunPayHub) -> None:
    await message.reply(translater.translate('♻️ Перезапускаюсь...'))
    await hub.shutdown(exit_codes.RESTART)
