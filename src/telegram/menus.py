from __future__ import annotations

from funpayhub.lib.telegram.ui import Menu, Button, MenuModification
from funpayhub.lib.base_app.telegram.app.properties.ui import NodeMenuContext

from funpayhub.app.properties import FunPayHubProperties

from .callbacks import HideKbCD, ShowKbCD


class TelegramAppearanceModification(
    MenuModification,
    modification_id='fph:keyboard_menu_plugin:tg:appearance',
):
    async def filter(
        self, ctx: NodeMenuContext, menu: Menu, properties: FunPayHubProperties
    ) -> bool:
        return ctx.entry_path == properties.telegram.appearance.path

    async def modify(self, ctx: NodeMenuContext, menu: Menu) -> Menu:
        menu.main_keyboard.add_row(
            Button.callback_button(
                button_id='fph:keyboard_menu_plugin:show',
                text='⌨️ Отобразить клавиатуру',
                callback_data=ShowKbCD().pack(),
            ),
            Button.callback_button(
                button_id='fph:keyboard_menu_plugin:hide',
                text='🙈 Скрыть клавиатуру',
                callback_data=HideKbCD().pack(),
            ),
        )

        return menu
