"""     
                        ИНФОРМАЦИЯ:

Привет! Если хочешь взять решения из моего плагина, пожалуйста, отметь меня @mr_Vestr.



            ⣿⣿⣿⣿⣯⣿⣿⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠈⣿⣿⣿⣿⣿⣿⣆⠄
            ⢻⣿⣿⣿⣾⣿⢿⣢⣞⣿⣿⣿⣿⣷⣶⣿⣯⣟⣿⢿⡇⢃⢻⣿⣿⣿⣿⣿⢿⡄
            ⠄⢿⣿⣯⣏⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⣾⢿⣮⣿⣿⣿⣿⣾⣷
            ⠄⣈⣽⢾⣿⣿⣿⣟⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣯⢿⣿⣿⣿⣿
            ⣿⠟⣫⢸⣿⢿⣿⣾⣿⢿⣿⣿⢻⣿⣿⣿⢿⣿⣿⣿⢸⣿⣼⣿⣿⣿⣿⣿⣿⣿
            ⡟⢸⣟⢸⣿⠸⣷⣝⢻⠘⣿⣿⢸⢿⣿⣿⠄⣿⣿⣿⡆⢿⣿⣼⣿⣿⣿⣿⢹⣿
            ⡇⣿⡿⣿⣿⢟⠛⠛⠿⡢⢻⣿⣾⣞⣿⡏⠖⢸⣿⢣⣷⡸⣇⣿⣿⣿⢼⡿⣿⣿
            ⣡⢿⡷⣿⣿⣾⣿⣷⣶⣮⣄⣿⣏⣸⣻⣃⠭⠄⠛⠙⠛⠳⠋⣿⣿⣇⠙⣿⢸⣿
            ⠫⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣹⢷⣿⡼⠋
            ⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⠄⠄
            ⠄⠄⢻⢹⣿⠸⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣿⡟⠄⠄
            ⠄⠄⠈⢸⣿⠄⠙⢿⣿⣿⣹⣿⣿⣿⣿⣟⡃⣽⣿⣿⡟⠁⣿⣿⢻⣿⣿⢿⠄⠄
            ⠄⠄⠄⠘⣿⡄⠄⠄⠙⢿⣿⣿⣾⣿⣷⣿⣿⣿⠟⠁⠄⠄⣿⣿⣾⣿⡟⣿⠄⠄
            ⠄⠄⠄⠄⢻⡇⠸⣆⠄⠄⠈⠻⣿⡿⠿⠛⠉⠄⠄⠄⠄⢸⣿⣇⣿⣿⢿⣿⠄⠄



                        INFORMATION:

Hi! If you want to borrow something from my plugin, please tag me @mr_Vestr.



"""

from base_plugin import BasePlugin, MenuItemData, MenuItemType, HookResult, HookStrategy
from ui.settings import Divider, Header, Input, Switch, Text
from ui.alert import AlertDialogBuilder
from android_utils import run_on_ui_thread
import urllib.parse
import locale
import os
import re
from markdown_utils import parse_markdown
from org.telegram.ui import DialogsActivity, LaunchActivity
from android.os import Bundle
from java import dynamic_proxy
from ui.bulletin import BulletinHelper
from org.telegram.messenger import ApplicationLoader
from java.io import File
from org.telegram.ui.Components import EditTextBoldCursor
from android.text import InputType
from android.widget import ScrollView
from android.util import TypedValue

try:
    from android_utils import Callback
except ImportError:
    from java import dynamic_proxy
    from org.telegram.messenger import Utilities
    class Callback(dynamic_proxy(Utilities.Callback)):
        def __init__(self, fn):
            super().__init__()
            self._fn = fn
        def run(self, arg):
            self._fn(arg)

try:
    from android_utils import OnClickListener
except ImportError:
    from java import dynamic_proxy
    from android.view import View
    class OnClickListener(dynamic_proxy(View.OnClickListener)):
        def __init__(self, fn):
            super().__init__()
            self._fn = fn
        def onClick(self, v):
            self._fn(v)


__id__ = "plugin_creator"
__name__ = "Plugin creator"
__description__ = """Плагин для быстрого создания плагинов из кода.

Plugin for quick plugin creation from code."""
__author__ = "@mr_Vestr"
__version__ = "1.1"
__min_version__ = "12.1.1"
__icon__ = "mr_vestr/12"


LANG = {
    'ru': {
        'settings': 'Настройки',
        'chat_menu': 'Кнопка в меню чата',
        'chat_menu_sub': 'Добавляет кнопку настроек создателя плагинов в обычное меню чата.',
        'drawer_menu': 'Кнопка в боковом меню',
        'drawer_menu_sub': 'Добавляет кнопку настроек создателя плагинов в боковое меню.',
        'chat_plugins_menu': 'Кнопка в плагинах в чате',
        'chat_plugins_menu_sub': 'Добавляет кнопку настроек создателя плагинов в меню плагинов в чате.',
        'send_name': 'Название файла',
        'send_name_sub': 'Введите имя для файлов плагинов.',
        'send_message': 'Текст сообщения',
        'send_message_sub': 'Текст сообщения при отправке плагина (пусто = без текста).',
        'create_plugin': 'Создать плагин',
        'contacts': 'Мои контакты',
        'channel_1': 'Мой канал — @I_am_Vestr',
        'personal_1': 'Моя личка — @mr_Vestr',
        'other': 'Другое',
        'plugin_version': 'Версия плагина — 1.1',
        'updates': 'Обновления',
        'current_version': 'Текущая версия: {version}',
        'updates_info': 'Новые версии будут в моём телеграм канале.',
        'check_updates': 'Проверить обновление',
        'close': 'Закрыть',
        'send': 'Отправить',
        'enter_plugin_code': 'Введите код плагина',
        'plugin_created': 'Плагин создан и отправлен',
        'error_occurred': 'Произошла ошибка!',
        'support_me': 'Поддержать меня',
        'support_me_text': 'Если вы хотите меня поддержать, вы можете отправить мне подарок в Telegram или подарить Telegram Premium :)',
        'my_account': 'Мой аккаунт',
        'restart_error': 'Ошибка перезапуска: {error}',
        'download_error': 'Ошибка загрузки: {error}',
        'error_occurred_with_reason': 'Ошибка: {error}',
        'link_open_error': 'Ошибка при открытии ссылки: {error}',
        'channel': 'Мой канал',
        'personal': 'Моя личка',
        'link_copied': 'Ссылка скопирована',
        'copied_to_clipboard': 'Скопировано в буфер обмена',
        'error_prefix': 'Ошибка:',
        'how_it_works': 'Как это работает?',
        'how_it_works_text': '''**Plugin creator — позволяет удобно создавать файл плагинов из готового кода, есть много настроек и быстрая вставка.**

**Возможности:**
• Быстро из текста создать файл плагина. Например, вы попросили ИИ создать плагин, он написал вам код, и вы можете обернуть этот код в плагин прямо в Telegram;
• В чате, куда хотите отправить плагин, нажмите «⁝» → «Создать плагин». Тут можно писать текст или быстро вставить его и нажать «Отправить»;
• Поддерживаются два языка (русский и английский).

**Настройки:**
• Возможность добавить кнопку «Создать плагин» в меню чата или меню плагинов в чате;
• Также можно изменить имя отправляемого файла;
• И можно изменить текст в сообщении у файла.

**Если вы хотите предложить идею для улучшения плагина, сообщить об ошибке или что-то другое, то пишите в сообщения к каналу @I_am_Vestr или мне в личные сообщения @mr_Vestr.**''',
    },
    'en': {
        'settings': 'Settings',
        'chat_menu': 'Button in chat menu',
        'chat_menu_sub': 'Adds a plugin creator settings button to the regular chat menu.',
        'drawer_menu': 'Button in drawer menu',
        'drawer_menu_sub': 'Adds a plugin creator settings button to the drawer menu.',
        'chat_plugins_menu': 'Button in plugins chat menu',
        'chat_plugins_menu_sub': 'Adds a plugin creator settings button to the plugins menu in chat.',
        'send_name': 'Plugin file names',
        'send_name_sub': 'Enter the name for plugin files.',
        'send_message': 'Message text',
        'send_message_sub': 'Message text when sending plugin (empty = no text).',
        'create_plugin': 'Create plugin',
        'contacts': 'My contacts',
        'channel_1': 'My channel — @I_am_Vestr',
        'personal_1': 'My DM — @mr_Vestr',
        'other': 'Other',
        'plugin_version': 'Plugin version — 1.1',
        'updates': 'Updates',
        'current_version': 'Current version: {version}',
        'updates_info': 'New versions are available in my Telegram channel.',
        'check_updates': 'Check updates',
        'close': 'Close',
        'send': 'Send',
        'enter_plugin_code': 'Enter plugin code',
        'plugin_created': 'Plugin created and sent',
        'error_occurred': 'An error occurred!',
        'support_me': 'Support me',
        'support_me_text': 'If you want to support me, you can send me a gift in Telegram or gift me Telegram Premium :)',
        'my_account': 'My account',
        'restart_error': 'Restart error: {error}',
        'download_error': 'Download error: {error}',
        'error_occurred_with_reason': 'Error: {error}',
        'link_open_error': 'Error opening link: {error}',
        'channel': 'My channel',
        'personal': 'My DM',
        'link_copied': 'Link copied',
        'copied_to_clipboard': 'Copied to clipboard',
        'error_prefix': 'Error:',
        'how_it_works': 'How does it work?',
        'how_it_works_text': '''**Plugin creator — allows you to easily create plugin files from ready-made code, has many settings and quick insertion.**

**Features:**
• Quickly create a plugin file from text. For example, you asked AI to create a plugin, it wrote you code, and you can wrap this code into a plugin right in Telegram;
• In the chat where you want to send the plugin, tap "⁝" → "Create plugin". Here you can write text or quickly paste it and tap "Send";
• Two languages are supported (Russian and English).

**Settings:**
• Ability to add "Create plugin" button to chat menu or plugins menu in chat;
• You can also change the name of the sent file;
• And you can change the text in the file message.

**If you want to suggest an idea for improving the plugin, report a bug, or anything else, write to the @I_am_Vestr channel or DM @mr_Vestr.**''',
    }
}

def t(key, lang='ru', **kwargs):
    return LANG[lang][key].format(**kwargs)

class _LocalFileSystem:
    @classmethod
    def tempdir(cls):
        base = ApplicationLoader.applicationContext.getExternalCacheDir()
        _dir = File(base, "plugin_creator_temp_files")
        if not _dir.exists():
            _dir.mkdirs()
        return _dir

    @classmethod
    def write_temp_file(cls, filename: str, content: bytes, mode: str = "wb", delete_after: int = 0):
        import os, threading
        path = File(cls.tempdir(), filename).getAbsolutePath()
        with open(path, mode) as f:
            f.write(content)
        if delete_after > 0:
            try:
                threading.Timer(delete_after, lambda: os.path.exists(path) and os.remove(path)).start()
            except Exception:
                pass
        return path

class PluginCreatorPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.menu_shown = False
        self.plugin_creator_menu_id = 880033
        try:
            from org.telegram.messenger import LocaleController
            lang_code = LocaleController.getInstance().getCurrentLocale().getLanguage()
        except Exception:
            lang_code = ''
        if lang_code.lower().startswith('ru'):
            self.lang = 'ru'
        else:
            self.lang = 'en'
        if not hasattr(self, '_settings') or not self._settings:
            self.set_setting('show_chat_menu', self.get_setting('show_chat_menu', True), reload_settings=False)
            self.set_setting('show_chat_plugins_menu', self.get_setting('show_chat_plugins_menu', False), reload_settings=False)

    def on_plugin_load(self):
        if not hasattr(self, '_settings') or not self._settings:
            self.set_setting('show_chat_menu', self.get_setting('show_chat_menu', True), reload_settings=False)
            self.set_setting('show_chat_plugins_menu', self.get_setting('show_chat_plugins_menu', False), reload_settings=False)
        self._update_chat_menu()
        self._update_chat_plugins_menu()
        try:
            from android_utils import run_on_ui_thread
            from org.telegram.messenger import AndroidUtilities
            def update_chat_menu():
                if self.get_setting('show_chat_menu', True):
                    self._add_plugin_creator_item_to_current_chat_header()
            AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(update_chat_menu), 500)
        except Exception:
            pass
        self._hook_chat_activity_resume()
        self._force_load_stickers()

    def set_setting(self, key, value, reload_settings=False):
        try:
            return super().set_setting(key, value, reload_settings=reload_settings)
        except TypeError:
            try:
                return super().set_setting(key, value)
            finally:
                if reload_settings:
                    try:
                        from client_utils import get_last_fragment
                        frag = get_last_fragment()
                        try:
                            frag.rebuildAllFragments(True)
                        except Exception:
                            pass
                    except Exception:
                        pass

    def open_plugin_settings(self):
        from client_utils import get_last_fragment
        from com.exteragram.messenger.plugins import PluginsController
        from com.exteragram.messenger.plugins.ui import PluginSettingsActivity
        def _open_settings():
            try:
                fragment = get_last_fragment()
                plugin = PluginsController.getInstance().plugins.get(self.id)
                if plugin:
                    fragment.presentFragment(PluginSettingsActivity(plugin))
                    self._force_load_stickers()
            except Exception as e:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('open_settings_error', lang=self.lang, error=str(e)))
        run_on_ui_thread(_open_settings)

    def _force_load_stickers(self):
        try:
            from client_utils import get_last_fragment
            from org.telegram.messenger import MediaDataController
            from org.telegram.tgnet import TLRPC

            def load_stickers():
                try:
                    fragment = get_last_fragment()
                    current_account = 0
                    try:
                        if fragment is not None and hasattr(fragment, 'getCurrentAccount'):
                            current_account = fragment.getCurrentAccount()
                        else:
                            from org.telegram.messenger import UserConfig
                            current_account = UserConfig.selectedAccount
                    except Exception:
                        try:
                            from org.telegram.messenger import UserConfig
                            current_account = UserConfig.selectedAccount
                        except Exception:
                            current_account = 0
                    media_controller = MediaDataController.getInstance(current_account)
                    if media_controller:
                        input_set = TLRPC.TL_inputStickerSetShortName()
                        input_set.short_name = "mr_vestr"
                        media_controller.getStickerSet(input_set, None, False, None)
                except Exception:
                    pass
            from android_utils import run_on_ui_thread
            from org.telegram.messenger import AndroidUtilities
            AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(load_stickers), 1000)
        except Exception:
            pass

    def _update_chat_menu(self):
        show_chat = self.get_setting('show_chat_menu', True)
        if show_chat:
            try:
                from android_utils import run_on_ui_thread
                run_on_ui_thread(self._add_plugin_creator_item_to_current_chat_header)
            except Exception:
                pass

    def _update_chat_plugins_menu(self):
        show_chat_plugins = self.get_setting('show_chat_plugins_menu', False)
        self.remove_menu_item('plugin_creator_chat_plugins')
        if show_chat_plugins:
            try:
                menu_type = MenuItemType.CHAT_ACTION_MENU
            except Exception:
                menu_type = None
            if menu_type:
                self.add_menu_item(MenuItemData(
                    menu_type=menu_type,
                    text=t('create_plugin', lang=self.lang),
                    icon='msg_addbot',
                    item_id='plugin_creator_chat_plugins',
                    on_click=lambda ctx: self._show_plugin_creator_popup_menu(None)
                ))

    def _get_private_field(self, obj, name):
        try:
            cls = obj.getClass()
        except Exception:
            return None
        while cls is not None:
            try:
                field = cls.getDeclaredField(name)
                field.setAccessible(True)
                return field.get(obj)
            except Exception:
                try:
                    cls = cls.getSuperclass()
                except Exception:
                    break
        return None

    def _add_plugin_creator_item_to_current_chat_header(self):
        try:
            from client_utils import get_last_fragment
            from org.telegram.ui import ChatActivity
            frag = get_last_fragment()
            if not frag or not isinstance(frag, ChatActivity):
                return
            chat_activity = frag
            headerItem = self._get_private_field(chat_activity, "headerItem")
            if headerItem is None:
                return
            from hook_utils import find_class
            R = find_class("org.telegram.messenger.R")
            try:
                icon_id = getattr(R.drawable, 'msg_addbot')
            except Exception:
                try:
                    icon_id = getattr(R.drawable, 'msg_settings_14')
                except Exception:
                    icon_id = 0
            lazy_list = self._get_private_field(headerItem, "lazyList")
            lazy_map = self._get_private_field(headerItem, "lazyMap")
            try:
                if lazy_map is not None and lazy_map.get(self.plugin_creator_menu_id) is not None:
                    self._hook_chat_action_bar_callback(chat_activity)
                    return
                if lazy_list is not None:
                    for i in range(lazy_list.size()):
                        item = lazy_list.get(i)
                        try:
                            item_id = self._get_private_field(item, "id")
                            if item_id == self.plugin_creator_menu_id:
                                self._hook_chat_action_bar_callback(chat_activity)
                                return
                        except Exception:
                            continue
            except Exception:
                pass
            insert_position = -1
            try:
                if lazy_list is not None:
                    insert_position = lazy_list.size()
                    admin_gap = self._get_private_field(chat_activity, "adminItemsGap")
                    if admin_gap is not None and lazy_map is not None:
                        for i in range(lazy_list.size()):
                            item = lazy_list.get(i)
                            if item == admin_gap:
                                insert_position = i
                                break
            except Exception:
                pass
            from java import jclass
            try:
                ItemClass = jclass("org.telegram.ui.ActionBar.ActionBarMenuItem$Item")
                item_java_class = ItemClass.getClass()
                Integer = jclass("java.lang.Integer")
                Boolean = jclass("java.lang.Boolean")
                asSubItemMethod = item_java_class.getDeclaredMethod(
                    "asSubItem",
                    Integer.TYPE,
                    Integer.TYPE,
                    jclass("android.graphics.drawable.Drawable"),
                    jclass("java.lang.CharSequence"),
                    Boolean.TYPE,
                    Boolean.TYPE
                )
                asSubItemMethod.setAccessible(True)
                our_item = asSubItemMethod.invoke(None,
                    Integer(self.plugin_creator_menu_id),
                    Integer(icon_id),
                    None,
                    t('create_plugin', lang=self.lang),
                    Boolean(True),
                    Boolean(False)
                )
                if lazy_list is not None and insert_position >= 0:
                    lazy_list.add(insert_position, our_item)
                    if lazy_map is not None:
                        lazy_map.put(self.plugin_creator_menu_id, our_item)
                else:
                    try:
                        headerItem.lazilyAddSubItem(self.plugin_creator_menu_id, icon_id, t('create_plugin', lang=self.lang))
                    except Exception:
                        pass
                self._hook_chat_action_bar_callback(chat_activity)
            except Exception:
                pass
        except Exception:
            pass

    def _hook_chat_action_bar_callback(self, chat_activity):
        try:
            from base_plugin import MethodHook
            action_bar = self._get_private_field(chat_activity, "actionBar")
            if action_bar is None:
                return
            current_callback = self._get_private_field(action_bar, "actionBarMenuOnItemClick")
            if current_callback is None:
                return
            callback_class = current_callback.getClass()
            from java import jclass
            jint = jclass("java.lang.Integer").TYPE
            onItemClickMethod = callback_class.getDeclaredMethod("onItemClick", jint)
            onItemClickMethod.setAccessible(True)
            plugin = self
            class PluginCreatorActionBarMenuItemClickHook(MethodHook):
                def __init__(self, plugin_ref, activity_ref):
                    self.plugin_ref = plugin_ref
                    self.activity_ref = activity_ref
                def before_hooked_method(self, param):
                    try:
                        item_id = int(param.args[0])
                        if item_id == self.plugin_ref.plugin_creator_menu_id:
                            from android_utils import run_on_ui_thread
                            run_on_ui_thread(lambda: self.plugin_ref._show_plugin_creator_popup_menu(None))
                            param.setResult(None)
                    except Exception:
                        pass
            self.hook_method(onItemClickMethod, PluginCreatorActionBarMenuItemClickHook(self, chat_activity))
        except Exception:
            pass

    def _hook_chat_activity_resume(self):
        try:
            from hook_utils import find_class
            from base_plugin import MethodHook
            ChatActivity = find_class("org.telegram.ui.ChatActivity")
            if ChatActivity is None:
                return
            target_method = None
            for m in ChatActivity.getClass().getDeclaredMethods():
                try:
                    name = m.getName()
                    if name == "onResume":
                        target_method = m
                        break
                except Exception:
                    pass
            if target_method is None:
                for m in ChatActivity.getClass().getDeclaredMethods():
                    try:
                        if m.getName() == "onFragmentCreate":
                            target_method = m
                            break
                    except Exception:
                        pass
            if target_method is None:
                return
            plugin = self
            class ChatResumeHook(MethodHook):
                def __init__(self, p):
                    self.p = p
                def after_hooked_method(self, param):
                    try:
                        if self.p.get_setting('show_chat_menu', True):
                            from android_utils import run_on_ui_thread
                            run_on_ui_thread(self.p._add_plugin_creator_item_to_current_chat_header)
                    except Exception:
                        pass
            self.hook_method(target_method, ChatResumeHook(self))
        except Exception:
            pass

    def _show_plugin_creator_popup_menu(self, text_view):
        try:
            from client_utils import get_last_fragment
            from org.telegram.ui.ActionBar import BottomSheet, Theme
            from org.telegram.ui.Components import LayoutHelper
            from org.telegram.messenger import AndroidUtilities
            from android.widget import LinearLayout, TextView, ScrollView, FrameLayout
            from android.view import Gravity
            from android.util import TypedValue
            from org.telegram.ui.Components import EditTextBoldCursor
            from android.text import InputType
            from android.graphics import Typeface
            from androidx.core.widget import NestedScrollView
            from android_utils import OnClickListener
            from android.graphics.drawable import GradientDrawable
            from android.content.res import ColorStateList
            from android.graphics import Color
            fragment = get_last_fragment()
            if not fragment or not hasattr(fragment, 'getParentActivity'):
                return
            context = fragment.getParentActivity()
            if not context:
                return
            sheet = BottomSheet(context, True)
            sheet.setAllowNestedScroll(True)
            try:
                sheet.setResizeKeyboardArea(True)
            except Exception:
                pass
            main_container = LinearLayout(context)
            main_container.setOrientation(LinearLayout.VERTICAL)
            main_container.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(20))
            try:
                main_container.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
            except Exception:
                pass
            title_view = TextView(context)
            title_view.setText("Создать плагин" if self.lang == 'ru' else "Create Plugin")
            title_view.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
            title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 20)
            title_view.setGravity(Gravity.CENTER)
            title_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            main_container.addView(title_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 20))
            input_container = FrameLayout(context)
            input_background = GradientDrawable()
            input_background.setShape(GradientDrawable.RECTANGLE)
            input_background.setCornerRadius(AndroidUtilities.dp(12))
            input_background.setStroke(AndroidUtilities.dp(2), Theme.getColor(Theme.key_dialogTextBlue))
            input_background.setColor(Theme.getColor(Theme.key_windowBackgroundWhite))
            input_container.setBackground(input_background)
            input_container.setPadding(AndroidUtilities.dp(4), AndroidUtilities.dp(4), AndroidUtilities.dp(4), AndroidUtilities.dp(4))
            edit_text = EditTextBoldCursor(context)
            edit_text.setText("")
            edit_text.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_FLAG_MULTI_LINE)
            edit_text.setHint("Код плагина" if self.lang == 'ru' else "Plugin Code")
            edit_text.setMaxHeight(AndroidUtilities.dp(300))
            edit_text.setMinHeight(AndroidUtilities.dp(80))
            edit_text.setVerticalScrollBarEnabled(True)
            edit_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
            edit_text.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            edit_text.setHintTextColor(Theme.getColor(Theme.key_dialogTextGray3))
            edit_text.setCursorColor(Theme.getColor(Theme.key_dialogTextLink))
            edit_text.setBackground(None)
            padding = AndroidUtilities.dp(16)
            edit_text.setPadding(padding, padding, padding, padding)
            input_container.addView(edit_text, FrameLayout.LayoutParams(-1, -2))
            main_container.addView(input_container, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 20))
            def create_settings_button(text: str, on_click):
                from androidx.core.content import ContextCompat
                from android.widget import ImageView
                btn_frame = FrameLayout(context)
                btn_bg = GradientDrawable()
                btn_bg.setCornerRadius(AndroidUtilities.dp(18))
                try:
                    bg_color = Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000
                except Exception:
                    bg_color = Color.parseColor("#F0F0F0")
                btn_bg.setColor(bg_color)
                try:
                    from android.graphics.drawable import RippleDrawable
                    from android.content.res import ColorStateList
                    ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
                    ripple_drawable = RippleDrawable(ripple_color, btn_bg, None)
                    btn_frame.setBackground(ripple_drawable)
                except Exception:
                    btn_frame.setBackground(btn_bg)
                btn_frame.setPadding(AndroidUtilities.dp(12), AndroidUtilities.dp(8), AndroidUtilities.dp(12), AndroidUtilities.dp(8))
                icon_view = ImageView(context)
                try:
                    from org.telegram.messenger import R as R_tg
                    icon_view.setImageResource(R_tg.drawable.msg_settings)
                except Exception:
                    pass
                icon_view.setScaleType(ImageView.ScaleType.CENTER)
                icon_view.setColorFilter(Theme.getColor(Theme.key_dialogTextBlue))
                text_view = TextView(context)
                text_view.setText(text)
                text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
                text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlue))
                text_view.setGravity(Gravity.CENTER_VERTICAL)
                btn_frame.addView(icon_view, LayoutHelper.createFrame(20, 20, Gravity.LEFT | Gravity.CENTER_VERTICAL, 0, 0, 8, 0))
                btn_frame.addView(text_view, LayoutHelper.createFrame(-2, -2, Gravity.LEFT | Gravity.CENTER_VERTICAL, 28, 0, 0, 0))
                btn_frame.setOnClickListener(OnClickListener(on_click))
                return btn_frame
            def create_paste_button(text: str, on_click):
                from androidx.core.content import ContextCompat
                from android.widget import ImageView
                btn_frame = FrameLayout(context)
                btn_bg = GradientDrawable()
                btn_bg.setCornerRadius(AndroidUtilities.dp(18))
                try:
                    bg_color = Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000
                except Exception:
                    bg_color = Color.parseColor("#F0F0F0")
                btn_bg.setColor(bg_color)
                try:
                    from android.graphics.drawable import RippleDrawable
                    from android.content.res import ColorStateList
                    ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
                    ripple_drawable = RippleDrawable(ripple_color, btn_bg, None)
                    btn_frame.setBackground(ripple_drawable)
                except Exception:
                    btn_frame.setBackground(btn_bg)
                btn_frame.setPadding(AndroidUtilities.dp(12), AndroidUtilities.dp(8), AndroidUtilities.dp(12), AndroidUtilities.dp(8))
                icon_view = ImageView(context)
                try:
                    from org.telegram.messenger import R as R_tg
                    icon_view.setImageResource(R_tg.drawable.msg_copy)
                except Exception:
                    pass
                icon_view.setScaleType(ImageView.ScaleType.CENTER)
                icon_view.setColorFilter(Theme.getColor(Theme.key_dialogTextBlue))
                text_view = TextView(context)
                text_view.setText(text)
                text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
                text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlue))
                text_view.setGravity(Gravity.CENTER_VERTICAL)
                btn_frame.addView(icon_view, LayoutHelper.createFrame(20, 20, Gravity.LEFT | Gravity.CENTER_VERTICAL, 0, 0, 8, 0))
                btn_frame.addView(text_view, LayoutHelper.createFrame(-2, -2, Gravity.LEFT | Gravity.CENTER_VERTICAL, 28, 0, 0, 0))
                btn_frame.setOnClickListener(OnClickListener(on_click))
                return btn_frame
            def paste_from_clipboard(v):
                try:
                    from android.content import ClipboardManager, ClipData, Context
                    clipboard_manager = context.getSystemService(Context.CLIPBOARD_SERVICE)
                    if clipboard_manager:
                        clip_data = clipboard_manager.getPrimaryClip()
                        if clip_data and clip_data.getItemCount() > 0:
                            item = clip_data.getItemAt(0)
                            text = item.getText()
                            if text:
                                edit_text.setText(str(text))
                                edit_text.setSelection(edit_text.getText().length())
                                return
                    self._show_error_with_copy("Буфер обмена пуст" if self.lang == 'ru' else "Clipboard is empty")
                except Exception as e:
                    error_msg = "Ошибка вставки" if self.lang == 'ru' else "Paste error"
                    try:
                        from android_utils import copy_to_clipboard
                        copy_to_clipboard(str(e))
                        from ui.bulletin import BulletinHelper
                        BulletinHelper.show_copied_to_clipboard("Ошибка скопирована" if self.lang == 'ru' else "Error copied")
                    except Exception:
                        from ui.bulletin import BulletinHelper
                        BulletinHelper.show_error(error_msg)
            buttons_container = LinearLayout(context)
            buttons_container.setOrientation(LinearLayout.HORIZONTAL)
            buttons_container.setGravity(Gravity.CENTER)
            settings_btn = create_settings_button("Настройки" if self.lang == 'ru' else "Settings", lambda *_: (sheet.dismiss(), self.open_plugin_settings()))
            paste_btn = create_paste_button("Вставить" if self.lang == 'ru' else "Paste", paste_from_clipboard)
            buttons_container.addView(settings_btn, LayoutHelper.createLinear(-2, -2, Gravity.CENTER, 0, 0, 8, 0))
            buttons_container.addView(paste_btn, LayoutHelper.createLinear(-2, -2, Gravity.CENTER, 0, 0, 0, 0))
            main_container.addView(buttons_container, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 16))
            send_btn = TextView(context)
            send_btn.setText("Отправить" if self.lang == 'ru' else "Send")
            send_btn.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
            send_btn.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            send_btn.setGravity(Gravity.CENTER)
            send_btn.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
            btn_background = GradientDrawable()
            btn_background.setShape(GradientDrawable.RECTANGLE)
            btn_background.setCornerRadius(AndroidUtilities.dp(8))
            btn_background.setColor(Theme.getColor(Theme.key_featuredStickers_addButton))
            send_btn.setBackground(btn_background)
            send_btn.setPadding(AndroidUtilities.dp(24), AndroidUtilities.dp(16), AndroidUtilities.dp(24), AndroidUtilities.dp(16))
            def on_send_click(v):
                plugin_code = str(edit_text.getText()).strip()
                if plugin_code:
                    sheet.dismiss()
                    self._send_plugin_file(plugin_code, None)
                else:
                    self._shake_view(input_container)
                    self._show_error_with_copy("Код плагина не может быть пустым" if self.lang == 'ru' else "Plugin code cannot be empty")
            send_btn.setOnClickListener(OnClickListener(on_send_click))
            main_container.addView(send_btn, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 0))
            sheet.setCustomView(main_container)
            sheet.show()
            from android_utils import run_on_ui_thread
            def focus_field():
                try:
                    edit_text.requestFocus()
                except Exception:
                    pass
            from org.telegram.messenger import AndroidUtilities
            from java import dynamic_proxy
            from java.lang import Runnable
            class FocusRunnable(dynamic_proxy(Runnable)):
                def __init__(self, func):
                    super().__init__()
                    self.func = func
                def run(self):
                    self.func()
            AndroidUtilities.runOnUIThread(FocusRunnable(lambda: run_on_ui_thread(focus_field)), 200)
        except Exception as e:
            self._show_error_with_copy(t('error_occurred_with_reason', lang=self.lang, error=str(e)))

    def _show_error_with_copy(self, error_text):
        try:
            from android_utils import copy_to_clipboard
            copy_to_clipboard(error_text)
            from ui.bulletin import BulletinHelper
            BulletinHelper.show_copied_to_clipboard("Ошибка скопирована" if self.lang == 'ru' else "Error copied")
        except Exception:
            try:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(error_text)
            except Exception:
                pass

    def _shake_view(self, view):
        try:
            from android.view import animation
            from android.view.animation import TranslateAnimation, AnimationSet
            from org.telegram.messenger import AndroidUtilities
            shake = AnimationSet(True)
            shake.setDuration(500)
            left_move = TranslateAnimation(
                animation.Animation.ABSOLUTE, 0,
                animation.Animation.ABSOLUTE, -AndroidUtilities.dp(10),
                animation.Animation.RELATIVE_TO_SELF, 0,
                animation.Animation.RELATIVE_TO_SELF, 0
            )
            left_move.setDuration(100)
            left_move.setStartOffset(0)
            right_move = TranslateAnimation(
                animation.Animation.ABSOLUTE, -AndroidUtilities.dp(10),
                animation.Animation.ABSOLUTE, AndroidUtilities.dp(10),
                animation.Animation.RELATIVE_TO_SELF, 0,
                animation.Animation.RELATIVE_TO_SELF, 0
            )
            right_move.setDuration(100)
            right_move.setStartOffset(100)
            left_move2 = TranslateAnimation(
                animation.Animation.ABSOLUTE, AndroidUtilities.dp(10),
                animation.Animation.ABSOLUTE, -AndroidUtilities.dp(5),
                animation.Animation.RELATIVE_TO_SELF, 0,
                animation.Animation.RELATIVE_TO_SELF, 0
            )
            left_move2.setDuration(100)
            left_move2.setStartOffset(200)
            center_move = TranslateAnimation(
                animation.Animation.ABSOLUTE, -AndroidUtilities.dp(5),
                animation.Animation.ABSOLUTE, 0,
                animation.Animation.RELATIVE_TO_SELF, 0,
                animation.Animation.RELATIVE_TO_SELF, 0
            )
            center_move.setDuration(100)
            center_move.setStartOffset(300)
            shake.addAnimation(left_move)
            shake.addAnimation(right_move)
            shake.addAnimation(left_move2)
            shake.addAnimation(center_move)
            view.startAnimation(shake)
        except Exception:
            pass

    
    def _create_button(self, act, text, theme_key, on_click):
        from android.widget import TextView, FrameLayout
        from android.view import Gravity
        from android.util import TypedValue
        from org.telegram.ui.Components import LayoutHelper
        from org.telegram.messenger import AndroidUtilities
        btn_frame = FrameLayout(act)
        btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(10),
            Theme.getColor(theme_key),
            Theme.getColor(theme_key + "Pressed")
        ))
        btn_frame.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(12), AndroidUtilities.dp(20), AndroidUtilities.dp(12))
        btn_frame.setClickable(True)
        btn_frame.setFocusable(True)
        btn_text = TextView(act)
        btn_text.setText(text)
        btn_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        btn_text.setTypeface(AndroidUtilities.bold())
        btn_text.setGravity(Gravity.CENTER)
        btn_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        btn_frame.addView(btn_text, FrameLayout.LayoutParams(-1, -2))
        def handle_click(v):
            try:
                result = on_click()
                if hasattr(result, 'dismiss'):
                    result.dismiss()
            except Exception:
                pass
        btn_frame.setOnClickListener(OnClickListener(handle_click))
        return btn_frame
    def _send_plugin_file(self, plugin_code, sheet=None):
        try:
            if not plugin_code or not plugin_code.strip():
                return
            if sheet and hasattr(sheet, 'dismiss'):
                sheet.dismiss()
            filename = self.get_setting('send_name', 'main')
            if not filename:
                filename = 'main'
            message = self.get_setting('send_message', '').strip()
            if not message:
                message = None
            content = plugin_code.encode('utf-8')
            temp_path = _LocalFileSystem.write_temp_file(f"{filename}.plugin", content)
            from client_utils import get_last_fragment, get_account_instance
            from java import jarray, jint, jlong
            try:
                from java.lang import Integer
            except Exception:
                Integer = int
            try:
                from java.io import File as JFile
                size = JFile(temp_path).length()
            except Exception:
                pass
            frag = get_last_fragment()
            if not frag:
                return
            dialog_id = frag.getDialogId()
            if dialog_id is None:
                return
            from org.telegram.messenger import SendMessagesHelper
            methods = SendMessagesHelper.getClass().getDeclaredMethods()
            target = None
            use_uri = False
            for m in methods:
                if m.getName() == "prepareSendingDocumentInternal":
                    try:
                        params = m.getParameterTypes()
                        if len(params) > 1 and "android.net.Uri" in str(params[1]):
                            use_uri = True
                    except Exception:
                        pass
                    target = m
                    break
            if target is None:
                raise Exception("prepareSendingDocumentInternal not found")
            target.setAccessible(True)
            mime = "text/plain"
            if use_uri:
                try:
                    from android.net import Uri as AndroidUri
                    from java.io import File as JFile
                    fileUri = AndroidUri.fromFile(JFile(temp_path))
                    arg1 = fileUri
                    arg2 = fileUri
                except Exception:
                    arg1 = temp_path
                    arg2 = temp_path
            else:
                arg1 = temp_path
                arg2 = temp_path
            params = target.getParameterTypes()
            int_array_value = None
            int_value = None
            try:
                types_names = [p.getName() for p in params]
                if any((n.startswith('[L') and 'java.lang.Integer' in n) or 'java.lang.Integer[]' in n for n in types_names):
                    int_array_value = jarray(Integer)([0])
                elif any(n == '[I' or 'int[]' in n for n in types_names):
                    int_array_value = jarray(jint)([0])
                else:
                    int_array_value = jarray(jint)([0])
                int_value = jint(0)
            except Exception:
                int_array_value = jarray(jint)([0])
                int_value = jint(0)
            args = []
            base_args = [
                get_account_instance(), arg1, arg2, None, mime,
                dialog_id, None, None,
                None, None, None,
                None, jarray(jlong)([0]), True, message, True
            ]
            for i, arg in enumerate(base_args):
                if i < len(params):
                    args.append(arg)
                else:
                    break
            remaining_args_start = len(base_args)
            for i in range(remaining_args_start, len(params)):
                param_type = params[i].getName()
                arg_value = None
                if param_type == 'int':
                    arg_value = jint(0)
                elif param_type == 'boolean':
                    arg_value = False
                elif param_type == 'long':
                    arg_value = 0
                elif param_type == 'float' or param_type == 'double':
                    arg_value = 0.0
                elif param_type == 'java.lang.String':
                    arg_value = None
                elif param_type == 'java.lang.Integer':
                    try:
                        arg_value = Integer(0)
                    except Exception:
                        arg_value = jint(0)
                elif param_type == 'java.lang.Boolean':
                    arg_value = False
                elif param_type == 'java.lang.Long':
                    arg_value = 0
                elif param_type == 'int[]':
                    arg_value = jarray(jint)([0])
                elif param_type == 'long[]':
                    arg_value = jarray(jlong)([0])
                elif param_type == 'java.lang.Integer[]':
                    arg_value = jarray(Integer)([0])
                elif ('java.lang.Integer' in param_type and '[' in param_type):
                    arg_value = int_array_value
                else:
                    arg_value = None
                args.append(arg_value)
            if len(params) != len(args):
                def _def_for(t):
                    try:
                        name = t.getName()
                    except Exception:
                        name = str(t)
                    if name == 'boolean':
                        return False
                    if name == 'int':
                        return jint(0)
                    if name == 'java.lang.Integer':
                        try:
                            return Integer(0)
                        except Exception:
                            return jint(0)
                    if name == 'long':
                        return 0
                    if name == 'float' or name == 'double':
                        return 0.0
                    if name == 'int[]':
                        return jarray(jint)([0])
                    if name == 'long[]':
                        return jarray(jlong)([0])
                    if name == 'java.lang.Integer[]':
                        return jarray(Integer)([0])
                    return None
                new_args = []
                for i, param_type in enumerate(params):
                    if i < len(args):
                        new_args.append(args[i])
                    else:
                        default_val = _def_for(param_type)
                        new_args.append(default_val)
                args = new_args
            target.invoke(None, *args)
            from ui.bulletin import BulletinHelper
            BulletinHelper.show_success(t('plugin_created', lang=self.lang))
        except Exception as e:
            self._show_error_with_copy(t('error_occurred_with_reason', lang=self.lang, error=str(e)))

    def _show_support_me_menu(self, _):
        self._force_load_stickers()
        from org.telegram.ui.ActionBar import BottomSheet, Theme
        from android.widget import LinearLayout, TextView, ScrollView, FrameLayout, ImageView
        from android.view import Gravity, View
        from android.util import TypedValue
        from org.telegram.ui.Components import LayoutHelper, BackupImageView
        from org.telegram.messenger import AndroidUtilities, MediaDataController, ImageLocation
        from android.graphics.drawable import GradientDrawable
        from android.graphics import Color
        from android_utils import OnClickListener, run_on_ui_thread
        from client_utils import get_last_fragment
        from org.telegram.messenger.browser import Browser
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        sheet = BottomSheet(act, False)
        root_layout = LinearLayout(act)
        root_layout.setOrientation(LinearLayout.VERTICAL)
        root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(20))
        try:
            root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
        except Exception:
            pass
        try:
            avatar_view = BackupImageView(act)
            avatar_view.setRoundRadius(AndroidUtilities.dp(45))
            root_layout.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, 0, 0, 12))
            try:
                current_account = frag.getCurrentAccount()
            except Exception:
                current_account = 0
            media_controller = MediaDataController.getInstance(current_account)
            if media_controller:
                sticker_set = media_controller.getStickerSetByName("mr_vestr")
                if not sticker_set or not sticker_set.documents or sticker_set.documents.size() <= 9:
                    from org.telegram.tgnet import TLRPC
                    input_set = TLRPC.TL_inputStickerSetShortName()
                    input_set.short_name = "mr_vestr"
                    media_controller.getStickerSet(input_set, None, False, None)
                    def retry_load_sticker(attempt=0):
                        try:
                            if attempt < 5:
                                sticker_set = media_controller.getStickerSetByName("mr_vestr")
                                if sticker_set and sticker_set.documents and sticker_set.documents.size() > 9:
                                    sticker_document = sticker_set.documents.get(9)
                                    image_location = ImageLocation.getForDocument(sticker_document)
                                    avatar_view.setImage(image_location, "90_90", None, 0, sticker_document)
                                else:
                                    AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(lambda: retry_load_sticker(attempt + 1)), 300)
                        except Exception:
                            if attempt < 5:
                                AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(lambda: retry_load_sticker(attempt + 1)), 300)
                    AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(lambda: retry_load_sticker(0)), 500)
                elif sticker_set.documents.size() > 9:
                    sticker_document = sticker_set.documents.get(9)
                    image_location = ImageLocation.getForDocument(sticker_document)
                    avatar_view.setImage(image_location, "90_90", None, 0, sticker_document)
        except Exception:
            pass
        title_view = TextView(act)
        title_view.setTypeface(AndroidUtilities.bold())
        title_view.setGravity(Gravity.CENTER)
        title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
        title_view.setText(t('support_me', lang=self.lang))
        try:
            title_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            pass
        root_layout.addView(title_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 12))
        body_scroll = ScrollView(act)
        body_scroll.setVerticalScrollBarEnabled(False)
        body_scroll.setPadding(AndroidUtilities.dp(4), 0, AndroidUtilities.dp(4), 0)
        try:
            body_scroll.setNestedScrollingEnabled(True)
        except Exception:
            pass
        body_tv = TextView(act)
        body_tv.setText(t('support_me_text', lang=self.lang))
        body_tv.setTextIsSelectable(True)
        body_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
        body_tv.setGravity(Gravity.CENTER)
        try:
            body_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            pass
        try:
            body_tv.setLineSpacing(AndroidUtilities.dp(4), 1.15)
        except Exception:
            pass
        body_scroll.addView(body_tv)
        root_layout.addView(body_scroll, LayoutHelper.createLinear(-1, 0, 1.0))
        divider = View(act)
        try:
            divider_color = Theme.getColor(Theme.key_divider)
        except Exception:
            divider_color = Color.parseColor("#E0E0E0")
        divider.setBackgroundColor(divider_color)
        root_layout.addView(divider, LayoutHelper.createLinear(-1, 1, 0, 16, 0, 12))
        support_btn_frame = FrameLayout(act)
        support_btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(10),
            Theme.getColor(Theme.key_featuredStickers_addButton),
            Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        ))
        support_btn_frame.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
        support_btn_frame.setClickable(True)
        support_btn_frame.setFocusable(True)
        support_btn_text = TextView(act)
        support_btn_text.setText(t('support_me', lang=self.lang))
        support_btn_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        support_btn_text.setTypeface(AndroidUtilities.bold())
        support_btn_text.setGravity(Gravity.CENTER)
        support_btn_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        support_btn_frame.addView(support_btn_text, FrameLayout.LayoutParams(-1, -2))
        def on_support(v):
            try:
                sheet.dismiss()
                from org.telegram.ui import LaunchActivity
                from org.telegram.messenger import UserConfig
                from java.lang import Integer
                if not hasattr(LaunchActivity, 'instance') or LaunchActivity.instance is None:
                    return
                launch_activity = LaunchActivity.instance
                getSafeLastFragment_method = launch_activity.getClass().getDeclaredMethod("getSafeLastFragment")
                getSafeLastFragment_method.setAccessible(True)
                last_fragment = getSafeLastFragment_method.invoke(launch_activity)
                if last_fragment is None or last_fragment.getContext() is None:
                    return
                target_user_id = 2037728749
                current_account = UserConfig.selectedAccount
                from org.telegram.ui.Gifts import GiftSheet
                gift_sheet = GiftSheet(
                    last_fragment.getContext(),
                    current_account,
                    target_user_id,
                    None,
                    None
                )
                gift_sheet.show()
            except Exception:
                pass
        support_btn_frame.setOnClickListener(OnClickListener(lambda *_: on_support(support_btn_frame)))
        root_layout.addView(support_btn_frame, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 0))
        sheet.setCustomView(root_layout)
        sheet.show()

    def _open_channel_link(self, _):
        from client_utils import get_last_fragment
        from android_utils import run_on_ui_thread
        from client_utils import get_messages_controller
        run_on_ui_thread(lambda: get_messages_controller().openByUserName("I_am_Vestr", get_last_fragment(), 1))

    def _copy_channel_link(self, _):
        try:
            from android_utils import run_on_ui_thread
            from client_utils import get_last_fragment
            run_on_ui_thread(lambda: self._copy_link_to_clipboard("https://t.me/I_am_Vestr"))
            try:
                from ui.bulletin import BulletinHelper
                from org.telegram.messenger import R as R_tg
                icon_attr = getattr(R_tg.raw, 'copy', None)
                BulletinHelper.show_with_button(t('link_copied', lang=self.lang), icon_attr if icon_attr else 0, t('close', lang=self.lang), lambda: None, None)
            except Exception:
                pass
        except Exception:
            pass

    def _copy_personal_link(self, _):
        try:
            from android_utils import run_on_ui_thread
            from client_utils import get_last_fragment
            run_on_ui_thread(lambda: self._copy_link_to_clipboard("https://t.me/mr_Vestr"))
            try:
                from ui.bulletin import BulletinHelper
                from org.telegram.messenger import R as R_tg
                icon_attr = getattr(R_tg.raw, 'copy', None)
                BulletinHelper.show_with_button(t('link_copied', lang=self.lang), icon_attr if icon_attr else 0, t('close', lang=self.lang), lambda: None, None)
            except Exception:
                pass
        except Exception:
            pass

    def _copy_link_to_clipboard(self, url):
        try:
            from client_utils import get_last_fragment
            fragment = get_last_fragment()
            if not fragment:
                return
            context = fragment.getParentActivity()
            if not context:
                return
            from android.content import ClipboardManager, ClipData
            clipboard = context.getSystemService(context.CLIPBOARD_SERVICE)
            clipboard.setPrimaryClip(ClipData.newPlainText("link", url))
        except Exception:
            pass

    def _open_personal_link(self, _):
        from client_utils import get_last_fragment
        from org.telegram.messenger.browser import Browser
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if act:
            try:
                if self.lang == 'en':
                    text = 'Hello%21+I%27m+writing+regarding+the+%22Plugin+Creator%22+plugin%3A%0D%0A'
                else:
                    text = '%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%21+%D0%9F%D0%B8%D1%88%D1%83+%D0%BF%D0%BE+%D0%BF%D0%BE%D0%B2%D0%BE%D0%B4%D1%83+%D0%BF%D0%BB%D0%B0%D0%B3%D0%B8%D0%B0+%C2%ABPlugin+Creator%C2%BB%3A%0D%0A'
                uri = Uri.parse(f"https://t.me/mr_vestr/?text={text}")
                Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
            except Exception as e:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('link_open_error', lang=self.lang, error=str(e)))

    def _show_how_it_works(self, _):
        from org.telegram.ui.ActionBar import BottomSheet, Theme
        from android.widget import LinearLayout, TextView, ScrollView, FrameLayout
        from android.view import Gravity, View
        from android.util import TypedValue
        from org.telegram.ui.Components import LayoutHelper
        from org.telegram.messenger import AndroidUtilities
        from android.graphics.drawable import GradientDrawable
        from android.graphics import Color
        from android_utils import OnClickListener
        from client_utils import get_last_fragment
        from markdown_utils import parse_markdown
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        sheet = BottomSheet(act, False)
        root_layout = LinearLayout(act)
        root_layout.setOrientation(LinearLayout.VERTICAL)
        root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(20))
        try:
            root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
        except Exception:
            pass
        title_view = TextView(act)
        title_view.setTypeface(AndroidUtilities.bold())
        title_view.setGravity(Gravity.CENTER)
        title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
        title_view.setText(t('how_it_works', lang=self.lang))
        try:
            title_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            pass
        root_layout.addView(title_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 12))
        body_scroll = ScrollView(act)
        body_scroll.setVerticalScrollBarEnabled(False)
        body_scroll.setPadding(AndroidUtilities.dp(4), 0, AndroidUtilities.dp(4), 0)
        try:
            body_scroll.setNestedScrollingEnabled(True)
        except Exception:
            pass
        body_tv = TextView(act)
        text = t('how_it_works_text', lang=self.lang)
        try:
            from android.text import SpannableString, Spannable
            from android.text.style import StyleSpan
            from android.graphics import Typeface
            import re
            parts = re.split(r'(\*\*.*?\*\*)', text)
            spannable = SpannableString(text.replace('**', ''))
            start = 0
            for i, part in enumerate(parts):
                if part.startswith('**') and part.endswith('**'):
                    clean_text = part[2:-2]
                    end = start + len(clean_text)
                    spannable.setSpan(StyleSpan(Typeface.BOLD), start, end, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE)
                    start = end
                else:
                    start += len(part)
            body_tv.setText(spannable)
        except Exception:
            body_tv.setText(text)
        body_tv.setTextIsSelectable(True)
        body_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
        try:
            body_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            pass
        try:
            body_tv.setLineSpacing(AndroidUtilities.dp(4), 1.15)
        except Exception:
            pass
        body_scroll.addView(body_tv)
        root_layout.addView(body_scroll, LayoutHelper.createLinear(-1, 0, 1.0))
        divider = View(act)
        try:
            divider_color = Theme.getColor(Theme.key_divider)
        except Exception:
            divider_color = Color.parseColor("#E0E0E0")
        divider.setBackgroundColor(divider_color)
        root_layout.addView(divider, LayoutHelper.createLinear(-1, 1, 0, 16, 0, 12))
        
        def create_link_button(text: str, icon_res: str, on_click):
            from androidx.core.content import ContextCompat
            from android.widget import ImageView
            btn_frame = FrameLayout(act)
            btn_bg = GradientDrawable()
            btn_bg.setCornerRadius(AndroidUtilities.dp(18))
            try:
                bg_color = Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000
            except Exception:
                bg_color = Color.parseColor("#F0F0F0")
            btn_bg.setColor(bg_color)
            try:
                from android.graphics.drawable import RippleDrawable
                from android.content.res import ColorStateList
                ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
                ripple_drawable = RippleDrawable(ripple_color, btn_bg, None)
                btn_frame.setBackground(ripple_drawable)
            except Exception:
                btn_frame.setBackground(btn_bg)
            btn_layout = LinearLayout(act)
            btn_layout.setOrientation(LinearLayout.HORIZONTAL)
            btn_layout.setGravity(Gravity.CENTER_VERTICAL)
            btn_layout.setPadding(AndroidUtilities.dp(14), AndroidUtilities.dp(10), AndroidUtilities.dp(14), AndroidUtilities.dp(10))
            btn_layout.setMinimumHeight(AndroidUtilities.dp(40))
            if icon_res:
                try:
                    from android.graphics import PorterDuff
                    icon_view = ImageView(act)
                    icon_view.setScaleType(ImageView.ScaleType.FIT_CENTER)
                    icon_drawable = ContextCompat.getDrawable(act, getattr(__import__('org.telegram.messenger', fromlist=['R']).R.drawable, icon_res))
                    icon_drawable.setColorFilter(Theme.getColor(Theme.key_dialogTextBlack), PorterDuff.Mode.SRC_IN)
                    icon_view.setImageDrawable(icon_drawable)
                    btn_layout.addView(icon_view, LayoutHelper.createLinear(16, 16, Gravity.CENTER_VERTICAL, 0, 0, 6, 0))
                except Exception:
                    pass
            label_text = TextView(act)
            label_text.setText(text)
            label_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            try:
                label_text.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                label_text.setTextColor(Color.parseColor("#000000"))
            label_text.setGravity(Gravity.CENTER_VERTICAL)
            btn_layout.addView(label_text, LayoutHelper.createLinear(-2, -2, Gravity.CENTER_VERTICAL))
            btn_frame.addView(btn_layout)
            btn_frame.setClickable(True)
            btn_frame.setFocusable(True)
            btn_frame.setOnClickListener(OnClickListener(lambda *_: on_click(btn_frame)))
            return btn_frame
        
        def on_channel(v):
            try:
                sheet.dismiss()
                self._open_channel_link(None)
            except Exception:
                pass
        
        def on_personal(v):
            try:
                sheet.dismiss()
                self._open_personal_link(None)
            except Exception:
                pass
        
        actions_row = LinearLayout(act)
        actions_row.setOrientation(LinearLayout.HORIZONTAL)
        actions_row.setGravity(Gravity.CENTER)
        channel_btn = create_link_button(t('channel', lang=self.lang), 'msg_channel', on_channel)
        personal_btn = create_link_button(t('personal', lang=self.lang), 'msg_contacts', on_personal)
        channel_btn.setMinimumWidth(AndroidUtilities.dp(100))
        personal_btn.setMinimumWidth(AndroidUtilities.dp(100))
        actions_row.addView(channel_btn, LayoutHelper.createLinear(-2, -2, Gravity.CENTER_VERTICAL, 0, 0, 6, 0))
        actions_row.addView(personal_btn, LayoutHelper.createLinear(-2, -2, Gravity.CENTER_VERTICAL, 0, 0, 0, 0))
        root_layout.addView(actions_row, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 12))
        close_btn_frame = FrameLayout(act)
        close_btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(10),
            Theme.getColor(Theme.key_featuredStickers_addButton),
            Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        ))
        close_btn_frame.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
        close_btn_frame.setClickable(True)
        close_btn_frame.setFocusable(True)
        close_btn_text = TextView(act)
        close_btn_text.setText(t('close', lang=self.lang))
        close_btn_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        close_btn_text.setTypeface(AndroidUtilities.bold())
        close_btn_text.setGravity(Gravity.CENTER)
        close_btn_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        close_btn_frame.addView(close_btn_text, FrameLayout.LayoutParams(-1, -2))
        close_btn_frame.setOnClickListener(OnClickListener(lambda *_: sheet.dismiss()))
        root_layout.addView(close_btn_frame, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 0))
        sheet.setCustomView(root_layout)
        sheet.setCanDismissWithSwipe(False)
        sheet.show()

    def _show_version_dialog(self, _):
        self._force_load_stickers()
        from org.telegram.ui.ActionBar import BottomSheet, Theme
        from android.widget import LinearLayout, TextView, ScrollView, FrameLayout
        from android.view import Gravity, View
        from android.util import TypedValue
        from org.telegram.ui.Components import LayoutHelper, BackupImageView
        from org.telegram.messenger import AndroidUtilities, MediaDataController, ImageLocation
        from android.graphics.drawable import GradientDrawable
        from android.graphics import Color
        from android_utils import OnClickListener, run_on_ui_thread
        from client_utils import get_last_fragment
        from org.telegram.messenger.browser import Browser
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        sheet = BottomSheet(act, False)
        root_layout = LinearLayout(act)
        root_layout.setOrientation(LinearLayout.VERTICAL)
        root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(20))
        try:
            root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
        except Exception:
            pass
        try:
            avatar_view = BackupImageView(act)
            avatar_view.setRoundRadius(AndroidUtilities.dp(45))
            root_layout.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, 0, 0, 12))
            try:
                current_account = frag.getCurrentAccount()
            except Exception:
                current_account = 0
            media_controller = MediaDataController.getInstance(current_account)
            if media_controller:
                sticker_set = media_controller.getStickerSetByName("mr_vestr")
                if not sticker_set or not sticker_set.documents or sticker_set.documents.size() <= 1:
                    from org.telegram.tgnet import TLRPC
                    input_set = TLRPC.TL_inputStickerSetShortName()
                    input_set.short_name = "mr_vestr"
                    media_controller.getStickerSet(input_set, None, False, None)
                    def retry_load_sticker(attempt=0):
                        try:
                            if attempt < 5:
                                sticker_set = media_controller.getStickerSetByName("mr_vestr")
                                if sticker_set and sticker_set.documents and sticker_set.documents.size() > 1:
                                    sticker_document = sticker_set.documents.get(1)
                                    image_location = ImageLocation.getForDocument(sticker_document)
                                    avatar_view.setImage(image_location, "90_90", None, 0, sticker_document)
                                else:
                                    AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(lambda: retry_load_sticker(attempt + 1)), 300)
                        except Exception:
                            if attempt < 5:
                                AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(lambda: retry_load_sticker(attempt + 1)), 300)
                    AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(lambda: retry_load_sticker(0)), 500)
                elif sticker_set.documents.size() > 1:
                    sticker_document = sticker_set.documents.get(1)
                    image_location = ImageLocation.getForDocument(sticker_document)
                    avatar_view.setImage(image_location, "90_90", None, 0, sticker_document)
        except Exception:
            pass
        title_view = TextView(act)
        title_view.setTypeface(AndroidUtilities.bold())
        title_view.setGravity(Gravity.CENTER)
        title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
        title_view.setText(t('current_version', lang=self.lang, version=__version__))
        try:
            title_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            pass
        root_layout.addView(title_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 12))
        body_scroll = ScrollView(act)
        body_scroll.setVerticalScrollBarEnabled(False)
        body_scroll.setPadding(AndroidUtilities.dp(4), 0, AndroidUtilities.dp(4), 0)
        try:
            body_scroll.setNestedScrollingEnabled(True)
        except Exception:
            pass
        body_tv = TextView(act)
        body_tv.setText(t('updates_info', lang=self.lang))
        body_tv.setTextIsSelectable(True)
        body_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
        body_tv.setGravity(Gravity.CENTER)
        try:
            body_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            pass
        try:
            body_tv.setLineSpacing(AndroidUtilities.dp(4), 1.15)
        except Exception:
            pass
        body_scroll.addView(body_tv)
        root_layout.addView(body_scroll, LayoutHelper.createLinear(-1, 0, 1.0))
        divider = View(act)
        try:
            divider_color = Theme.getColor(Theme.key_divider)
        except Exception:
            divider_color = Color.parseColor("#E0E0E0")
        divider.setBackgroundColor(divider_color)
        root_layout.addView(divider, LayoutHelper.createLinear(-1, 1, 0, 16, 0, 12))
        check_btn_frame = FrameLayout(act)
        check_btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(10),
            Theme.getColor(Theme.key_featuredStickers_addButton),
            Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        ))
        check_btn_frame.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
        check_btn_frame.setClickable(True)
        check_btn_frame.setFocusable(True)
        check_btn_text = TextView(act)
        check_btn_text.setText(t('check_updates', lang=self.lang))
        check_btn_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        check_btn_text.setTypeface(AndroidUtilities.bold())
        check_btn_text.setGravity(Gravity.CENTER)
        check_btn_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        check_btn_frame.addView(check_btn_text, FrameLayout.LayoutParams(-1, -2))
        def on_check(v):
            try:
                sheet.dismiss()
                uri = Uri.parse("https://t.me/I_am_Vestr")
                Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
            except Exception:
                pass
        check_btn_frame.setOnClickListener(OnClickListener(lambda *_: on_check(check_btn_frame)))
        root_layout.addView(check_btn_frame, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 0))
        sheet.setCustomView(root_layout)
        sheet.show()

    def _on_chat_switch(self, key, value, ctx):
        self.set_setting(key, value)
        if key == 'show_chat_menu':
            if value:
                try:
                    from android_utils import run_on_ui_thread
                    run_on_ui_thread(self._add_plugin_creator_item_to_current_chat_header)
                except Exception:
                    pass
            else:
                try:
                    from client_utils import get_last_fragment
                    from org.telegram.ui import ChatActivity
                    frag = get_last_fragment()
                    if frag and isinstance(frag, ChatActivity):
                        headerItem = self._get_private_field(frag, "headerItem")
                        if headerItem:
                            lazy_map = self._get_private_field(headerItem, "lazyMap")
                            if lazy_map:
                                lazy_map.remove(self.plugin_creator_menu_id)
                except Exception:
                    pass
        self._update_chat_menu()

    def _on_chat_plugins_switch(self, key, value, ctx):
        self.set_setting(key, value)
        self._update_chat_plugins_menu()

    def create_settings(self):
        settings = []
        settings.append(Header(text=t('settings', lang=self.lang)))
        settings.append(Switch(
            key='show_chat_menu',
            text=t('chat_menu', lang=self.lang),
            default=self.get_setting('show_chat_menu', True),
            subtext=t('chat_menu_sub', lang=self.lang),
            on_change=self._on_chat_switch,
            link_alias='show_chat_menu'
        ))
        settings.append(Switch(
            key='show_chat_plugins_menu',
            text=t('chat_plugins_menu', lang=self.lang),
            default=self.get_setting('show_chat_plugins_menu', False),
            subtext=t('chat_plugins_menu_sub', lang=self.lang),
            on_change=self._on_chat_plugins_switch,
            link_alias='show_chat_plugins_menu'
        ))
        settings.append(Input(
            key='send_name',
            text=t('send_name', lang=self.lang),
            default=self.get_setting('send_name', 'main'),
            subtext=t('send_name_sub', lang=self.lang),
            link_alias='send_name'
        ))
        settings.append(Input(
            key='send_message',
            text=t('send_message', lang=self.lang),
            default=self.get_setting('send_message', ''),
            subtext=t('send_message_sub', lang=self.lang),
            link_alias='send_message'
        ))
        settings.append(Divider())
        settings.append(Header(text=t('contacts', lang=self.lang)))
        settings.append(Text(
            text=t('support_me', lang=self.lang),
            icon='menu_feature_reactions',
            accent=True,
            on_click=self._show_support_me_menu,
            link_alias='support_me'
        ))
        settings.append(Text(
            text=t('channel_1', lang=self.lang),
            icon='msg_channel',
            on_click=self._open_channel_link,
            on_long_click=self._copy_channel_link
        ))
        settings.append(Text(
            text=t('personal_1', lang=self.lang),
            icon='msg_contacts',
            on_click=lambda ctx: self._open_personal_link(ctx),
            on_long_click=self._copy_personal_link
        ))
        settings.append(Divider())
        settings.append(Header(text=t('other', lang=self.lang)))
        settings.append(Text(
            text=t('how_it_works', lang=self.lang),
            icon='msg_info',
            on_click=self._show_how_it_works,
            link_alias='how_it_works'
        ))
        settings.append(Text(
            text=t('plugin_version', lang=self.lang),
            icon='msg_settings_14',
            accent=True,
            on_click=lambda ctx: self._show_version_dialog(ctx),
            link_alias='plugin_version'
        ))
        settings.append(Divider())
        settings.append(Divider())
        return settings
