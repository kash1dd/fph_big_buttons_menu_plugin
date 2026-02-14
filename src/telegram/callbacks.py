from __future__ import annotations

from funpayhub.lib.telegram.callback_data import CallbackData


class ShowKbCD(CallbackData, identifier='keyboard_menu_plugin_show'): ...


class HideKbCD(CallbackData, identifier='keyboard_menu_plugin_hide'): ...
