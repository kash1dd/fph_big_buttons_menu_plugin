from __future__ import annotations

from aiogram import Router as TGRouter

from funpayhub.lib.telegram.ui import MenuModification

from funpayhub.app.plugin import Plugin
from funpayhub.app.telegram.ui.ids import MenuIds

from .telegram.menus import TelegramAppearanceModification
from .telegram.router import router as big_buttons_menu_tg_router


class KeyboardMenuPlugin(Plugin):
    async def menu_modifications(
        self,
    ) -> dict[str, type[MenuModification] | list[type[MenuModification]]]:
        return {
            MenuIds.props_node: TelegramAppearanceModification,
        }

    async def telegram_routers(self) -> TGRouter | list[TGRouter]:
        return big_buttons_menu_tg_router
