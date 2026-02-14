from __future__ import annotations

from aiogram import Router as TGRouter

from funpayhub.lib.telegram import Command

from funpayhub.app.plugin import Plugin

from .telegram.router import router as big_buttons_menu_tg_router


class BigButtonsMenuPlugin(Plugin):
    async def commands(self) -> Command | list[Command] | None:
        return [
            Command(
                command='show_kb',
                description='[Big Buttons Menu] Показать клавиатуру.',
                source=self.manifest.plugin_id,
                setup=True,
            ),
            Command(
                command='hide_kb',
                description='[Big Buttons Menu] Скрыть клавиатуру.',
                source=self.manifest.plugin_id,
                setup=True,
            ),
        ]

    async def telegram_routers(self) -> TGRouter | list[TGRouter]:
        return big_buttons_menu_tg_router
