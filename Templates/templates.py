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
            ⠫⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣹⢷⣿⡼⠋
            ⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⠄⠄
            ⠄⠄⢻⢹⣿⠸⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣿⡟⠄⠄
            ⠄⠄⠈⢸⣿⠄⠙⢿⣿⣿⣹⣿⣿⣿⣿⣟⡃⣽⣿⣿⡟⠁⣿⣿⢻⣿⣿⢿⠄⠄
            ⠄⠄⠄⠘⣿⡄⠄⠄⠙⢿⣿⣿⣾⣿⣷⣿⣿⣿⠟⠁⠄⠄⣿⣿⣾⣿⡟⣿⠄⠄
            ⠄⠄⠄⠄⢻⡇⠸⣆⠄⠄⠈⠻⣿⡿⠿⠛⠉⠄⠄⠄⠄⢸⣿⣇⣿⣿⢿⣿⠄⠄



                        INFORMATION:

Hi! If you want to borrow something from my plugin, please tag me @mr_Vestr.



"""

from base_plugin import BasePlugin, MenuItemData, MenuItemType, HookResult, HookStrategy
from ui.settings import Divider, Header, Input, Switch, Text
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


__id__ = "templates"
__name__ = "Templates | Шаблоны"
__description__ = """A plugin for creating, editing, and quickly sending message templates.

Плагин для создания, редактирования и быстрой отправки шаблонов сообщений."""
__author__ = "@mr_Vestr"
__version__ = "2.1"
__min_version__ = "11.12.0"
__icon__ = "mr_vestr/7"


TEMPLATE_COUNT = 30

LANG = {
    'ru': {
        'open_settings_error': 'Не удалось открыть настройки: {error}',
        'templates': 'Шаблоны',
        'link_open_error': 'Ошибка при открытии ссылки: {error}',
        
        'how_it_works': 'Как это работает?',
        'how_it_works_text': '''\
Шаблоны — заготовленные сообщения, которые можно быстро отправлять.

Чтобы создать шаблон нужно:
1. Открыть настройки плагина Templates;
2. Включить шаблон;
3. Настроить его название и отправляемое сообщение.

Отправить шаблон можно:
1. В настройках плагина, нажав кнопку «Отправить шаблон» и выбрав нужный чат;
2. Через поле ввода сообщения в уже открытом нужном чате, прописав команду и название шаблона. Пример: «// Название».

Также вы можете использовать режим форматирования: **жирный**, __подчёркнутый__, ~~зачёркнутый~~, `моноширинный`, --курсив--, ||спойлер||.

Если вы хотите предложить идею для улучшения плагина, сообщить об ошибке или что-то другое, то пишите в сообщения к каналу @I_am_Vestr или мне в личные сообщения @mr_Vestr.
''',
        'close': 'Закрыть',
        'reset_templates': 'Сбросить шаблоны?',
        'delete_button': 'Удалить',
        'yes': 'Да',
        'no': 'Нет',
        'settings': 'Настройки',
        'drawer_menu': 'Кнопка в боковом меню',
        'drawer_menu_sub': 'Добавляет кнопку настроек шаблонов в боковое меню.',
        'chat_menu': 'Кнопка в меню чата',
        'chat_menu_sub': 'Добавляет кнопку настроек шаблонов в меню чата.',
        'send_cmd': 'Команда отправки шаблона',
        'send_cmd_sub': 'Введите команду для отправки шаблонов.',
        'template_n': 'Шаблон №{n}',
        'template_name': 'Название шаблона',
        'template_name_sub': 'Придумайте название шаблона.',
        'template_text': 'Текст шаблона',
        'template_text_sub': 'Придумайте текст шаблона.',
        'send_template': 'Отправить шаблон',
        'delete_template': 'Удалить шаблон',
        'create_template': 'Создать шаблон',
        'contacts': 'Мои контакты',
        'channel': 'Мой канал — @I_am_Vestr',
        'personal': 'Моя личка — @mr_Vestr',
        'other': 'Другое',
        'plugin_version': 'Версия плагина — 2.1',
        'updates': 'Обновления',
        'current_version': 'Текущая версия: {version}',
        'updates_info': 'Новые версии будут в моём телеграм канале.',
        'check_updates': 'Проверить',
        'edit_template': 'Редактировать шаблон {n}',
        'save': 'Сохранить',
        'cancel': 'Отмена',
        'enter_template_name': 'Чтобы отправить шаблон, напишите его название.',
        'template_sent': 'Шаблон «{name}» отправлен.',
        'template_not_found': 'Шаблон не найден! Шаблоны добавляются в настройках плагина.',
        'fill_all_fields': 'Заполните все данные, для отправки шаблона.',
        'close_menu_question': 'Хотите закрыть меню?',
        'templates_title': 'Шаблоны',
        'error_occurred': 'Произошла ошибка!',
        'support_me': 'Поддержать меня',
        'support_me_text': 'Если вы хотите меня поддержать, вы можете отправить мне подарок в Telegram или подарить Telegram Premium :)',
        'my_account': 'Мой аккаунт',
        'restart_error': 'Ошибка перезапуска: {error}',
        'download_error': 'Ошибка загрузки: {error}',
        'error_occurred_with_reason': 'Ошибка: {error}',
        'select_template': 'Выберите шаблон',
        'no_templates_available': 'Нет доступных шаблонов',
        'export_templates': 'Экспорт шаблонов',
        'export_sent': 'Экспорт отправлен',
        'export_error': 'Ошибка экспорта: {error}',
        'export_success': 'Успешный экспорт.',
        'import_question': 'Импортировать шаблоны из файла?',
        'import_success': 'Импорт завершён.',
        'import_error': 'Ошибка импорта: {error}',
        'apply': 'Применить',
        'template_deleted': 'Шаблон удалён.',
        'template_deleted_n': 'Удалён шаблон №{n}.',
        'template_created_n': 'Создан шаблон №{n}.',
        'delete_template_title': 'Удаление шаблона',
        'delete_template_confirm': 'Точно удалить шаблон №{n}?',
        'undo': 'Вернуть',
        'template_n_sent': 'Шаблон №{n} отправлен.',
        'open': 'Открыть',
        'templates_exported': 'Шаблоны экспортированы.',
        'export_file_caption': 'Экспорт шаблонов',
        'import_dialog_title': 'Импорт шаблонов',
        'fill_prev_template': 'Заполните все поля предыдущего шаблона, чтобы создать другой.',
    },
    'en': {
        'open_settings_error': 'Failed to open settings: {error}',
        'templates': 'Templates',
        'link_open_error': 'Error opening link: {error}',
        
        'how_it_works': 'How does it work?',
        'how_it_works_text': '''\
Templates are pre-made messages you can quickly send.

To create a template:
1. Open Templates plugin settings;
2. Enable a template;
3. Set its name and message text.

To send a template:
1. In plugin settings, press "Send template" and choose a chat;
2. In the chat input, type the command and template name. Example: "// Name".

You can also use Parse mode: **bold**, __underlined__, ~~strikethrough~~, `monotype`, --italic--, ||spoiler||.

If you want to suggest an idea, report a bug, or anything else, write to the @I_am_Vestr channel or DM @mr_Vestr.
''',
        'close': 'Close',
        'reset_templates': 'Reset templates?',
        'delete_button': 'Delete',
        'yes': 'Yes',
        'no': 'No',
        'settings': 'Settings',
        'drawer_menu': 'Button in drawer menu',
        'drawer_menu_sub': 'Adds a template settings button to the drawer menu.',
        'chat_menu': 'Button in chat menu',
        'chat_menu_sub': 'Adds a template settings button to the chat menu.',
        'send_cmd': 'Template send command',
        'send_cmd_sub': 'Enter the command to send templates.',
        'template_n': 'Template #{n}',
        'template_name': 'Template name',
        'template_name_sub': 'Come up with a template name.',
        'template_text': 'Template text',
        'template_text_sub': 'Come up with template text.',
        'send_template': 'Send template',
        'delete_template': 'Delete template',
        'create_template': 'Create template',
        'contacts': 'My contacts',
        'channel': 'My channel — @I_am_Vestr',
        'personal': 'My DM — @mr_Vestr',
        'other': 'Other',
        'plugin_version': 'Plugin version — 2.1',
        'updates': 'Updates',
        'current_version': 'Current version: {version}',
        'updates_info': 'New versions are available in my Telegram channel.',
        'check_updates': 'Check updates',
        'edit_template': 'Edit template {n}',
        'save': 'Save',
        'cancel': 'Cancel',
        'enter_template_name': 'To send a template, enter its name.',
        'template_sent': 'Template "{name}" sent.',
        'template_not_found': 'Template not found! Add templates in plugin settings.',
        'fill_all_fields': 'Fill in all fields to send a template.',
        'close_menu_question': 'Do you want to close the menu?',
        'error_occurred': 'An error occurred!',
        'templates_title': 'Templates',
        'support_me': 'Support me',
        'support_me_text': 'If you want to support me, you can send me a gift in Telegram or gift me Telegram Premium :)',
        'my_account': 'My account',
        'restart_error': 'Restart error: {error}',
        'download_error': 'Download error: {error}',
        'error_occurred_with_reason': 'Error: {error}',
        'select_template': 'Select template',
        'no_templates_available': 'No templates available',
        'export_templates': 'Export templates',
        'export_sent': 'Export sent',
        'export_error': 'Export error: {error}',
        'export_success': 'Export successful.',
        'import_question': 'Import templates from file?',
        'import_success': 'Import completed.',
        'import_error': 'Import error: {error}',
        'apply': 'Apply',
        'template_deleted': 'Template deleted.',
        'template_deleted_n': 'Template #{n} deleted.',
        'template_created_n': 'Template #{n} created.',
        'delete_template_title': 'Deleting template',
        'delete_template_confirm': 'Are you sure you want to delete template #{n}?',
        'undo': 'Undo',
        'template_n_sent': 'Template #{n} sent.',
        'open': 'Open',
        'templates_exported': 'Templates exported.',
        'export_file_caption': 'Export templates',
        'import_dialog_title': 'Import templates',
        'fill_prev_template': 'Fill in all fields of the previous template to create another.',
    }
}

def t(key, lang='ru', **kwargs):
    return LANG[lang][key].format(**kwargs)

def preprocess_template_markdown(text):
    import re
    text = re.sub(r'--(.*?)--', r'_\1_', text)
    text = re.sub(r'~~(.*?)~~', r'~\1~', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'*\1*', text)
    return text

class _LocalFileSystem:
    @classmethod
    def tempdir(cls):
        base = ApplicationLoader.applicationContext.getExternalCacheDir()
        _dir = File(base, "templates_temp_files")
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

class TemplatesPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.update_info_cache = None
        self.last_update_check = 0
        self.menu_shown = False
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
            self.set_setting('show_chat_menu', True, reload_settings=False)
        templates = self.get_setting("templates", None)
        self.templates = []
        for i in range(TEMPLATE_COUNT):
            tpl = templates[i] if templates and i < len(templates) else {}
            tpl = dict(tpl) if tpl else {}
            if 'enabled' not in tpl:
                tpl['enabled'] = True if i == 0 else False
            if 'name' not in tpl:
                tpl['name'] = ''
            if 'text' not in tpl:
                tpl['text'] = ''
            self.templates.append(tpl)

    def on_plugin_load(self):
        self.update_info_cache = None
        self.last_update_check = 0
        if not hasattr(self, '_settings') or not self._settings:
            self.set_setting('show_chat_menu', True, reload_settings=False)
        self._update_drawer_menu()
        self._update_chat_menu()
        self.add_on_send_message_hook()
        self._add_url_hook()
        self._add_input_hook()
        self._add_document_hook()

    def _debug(self, msg):
        try:
            from android.util import Log
            Log.d("Templates", str(message))
            try:
                import os
                from java.io import File, FileOutputStream
                from android.os import Environment
                log_file = File(Environment.getExternalStorageDirectory(), "templates_plugin_log.txt")
                timestamp = ""
                try:
                    from datetime import datetime
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                except:
                    pass
                with open(log_file.getAbsolutePath(), 'a', encoding='utf-8') as f:
                    f.write(f"[{timestamp}] {str(message)}\n")
            except Exception as e:
                Log.e("Templates", f"Error writing to log file: {str(e)}")
        except Exception as e:
            try:
                print(f"[Templates] {str(message)}")
            except:
                pass

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
            except Exception as e:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('open_settings_error', lang=self.lang, error=str(e)))
        run_on_ui_thread(_open_settings)

    def _update_drawer_menu(self):
        show_drawer = self.get_setting('show_drawer_menu', False)
        self.remove_menu_item('templates_drawer')
        if show_drawer:
            self.add_menu_item(MenuItemData(
                menu_type=MenuItemType.DRAWER_MENU,
                text=t('templates', lang=self.lang),
                icon='msg_info',
                item_id='templates_drawer',
                on_click=lambda ctx: self.open_plugin_settings()
            ))

    def _update_chat_menu(self):
        show_chat = self.get_setting('show_chat_menu', True)
        self.remove_menu_item('templates_chat')
        if show_chat:
            self.add_menu_item(MenuItemData(
                menu_type=MenuItemType.CHAT_ACTION_MENU,
                text=t('templates', lang=self.lang),
                icon='msg_info',
                item_id='templates_chat',
                on_click=lambda ctx: self._show_template_popup_menu(None)
            ))

    def _open_channel_link(self, _):
        from client_utils import get_last_fragment
        from android_utils import run_on_ui_thread
        from client_utils import get_messages_controller
        run_on_ui_thread(lambda: get_messages_controller().openByUserName("I_am_Vestr", get_last_fragment(), 1))

    def _open_personal_link(self, _):
        from client_utils import get_last_fragment
        from org.telegram.messenger.browser import Browser
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if act:
            try:
                if self.lang == 'en':
                    text = 'Hello%21+I%27m+writing+regarding+the+%22Templates%22+plugin%3A%0D%0A'
                else:
                    text = '%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%21+%D0%9F%D0%B8%D1%88%D1%83+%D0%BF%D0%BE+%D0%BF%D0%BE%D0%B2%D0%BE%D0%B4%D1%83+%D0%BF%D0%BB%D0%B0%D0%B3%D0%B8%D0%B0+%C2%ABTemplates%C2%BB%3A%0D%0A'
                uri = Uri.parse(f"https://t.me/mr_vestr/?text={text}")
                Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
            except Exception as e:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('link_open_error', lang=self.lang, error=str(e)))

    def _add_url_hook(self):
        from hook_utils import find_class
        from base_plugin import MethodHook
        class UrlHandler(MethodHook):
            def __init__(self, plugin):
                self.plugin = plugin
            def before_hooked_method(self, param):
                try:
                    uri = str(param.args[1].toString())
                    if "t.me/I_am_Vestr" in uri or "t.me/mr_vestr" in uri:
                        pass
                except Exception as e:
                    pass
        try:
            browser_class = find_class("org.telegram.messenger.browser.Browser")
            open_url_method = None
            for method in browser_class.getClass().getDeclaredMethods():
                if (method.getName() == "openUrl" and 
                    "android.net.Uri" in str(method.getParameterTypes()[1])):
                    open_url_method = method
                    break
            if open_url_method:
                self.hook_method(open_url_method, UrlHandler(self), 0)
            else:
                pass
        except Exception as e:
            pass

    def _add_input_hook(self):
        from hook_utils import find_class
        from base_plugin import MethodHook
        from android_utils import run_on_ui_thread
        
        class InputHandler(MethodHook):
            def __init__(self, plugin):
                self.plugin = plugin
                self.last_text = ""
                self.menu_shown = False
                
            def before_hooked_method(self, param):
                try:
                    text_view = param.thisObject
                    if hasattr(text_view, 'getText'):
                        current_text = str(text_view.getText())
                        send_cmd = self.plugin.get_setting('send_cmd', '//').strip()
                        if not send_cmd:
                            send_cmd = '//'
                            
                        if (current_text.strip().lower().startswith(send_cmd.lower()) and 
                            not self.menu_shown and 
                            current_text.strip() == send_cmd):
                            self.menu_shown = True
                            run_on_ui_thread(lambda: self.plugin._show_template_popup_menu(text_view))

                        if current_text != self.last_text:
                            self.last_text = current_text
                            if not current_text.strip().startswith(send_cmd):
                                self.menu_shown = False
                except Exception:
                    pass
        try:
            edit_text_class = find_class("org.telegram.ui.Components.EditTextCaption")
            if edit_text_class:
                for method in edit_text_class.getClass().getDeclaredMethods():
                    if method.getName() == "setText":
                        self.hook_method(method, InputHandler(self), 0)
                        break
        except Exception:
            pass

    def _add_document_hook(self):
        from hook_utils import find_class
        from base_plugin import MethodHook
        class DocumentHandler(MethodHook):
            def __init__(self, plugin):
                self.plugin = plugin
            def before_hooked_method(self, param):
                try:
                    f = param.args[0]
                    filename = param.args[1]
                    if str(filename).split(".")[-1].lower() == "templates":
                        with open(f.getAbsolutePath(), "rb") as fh:
                            content = fh.read()
                        if not content:
                            return
                        try:
                            import json
                            data = json.loads(content.decode("utf-8"))
                        except Exception:
                            return
                        param.setResult(False)
                        self.plugin._show_import_templates_alert(data, act=param.args[3])
                except Exception:
                    pass
        try:
            android_utils = find_class("org.telegram.messenger.AndroidUtilities")
            target = None
            for method in android_utils.getClass().getDeclaredMethods():
                if repr(method) == (
                    "<java.lang.reflect.Method 'public static boolean org.telegram.messenger.AndroidUtilities.openForView"
                    "(java.io.File,java.lang.String,java.lang.String,android.app.Activity,org.telegram.ui.ActionBar.Theme$ResourcesProvider,boolean)'>"
                ):
                    target = method
                    break
            if target is not None:
                self.hook_method(target, DocumentHandler(self), 2147483647)
        except Exception:
            pass

    def _full_reload_plugin(self):
        from client_utils import get_last_fragment
        from com.exteragram.messenger.plugins import PluginsController
        from ui.bulletin import BulletinHelper
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if frag and hasattr(frag, 'finish'):
            try:
                frag.finish()
            except Exception:
                pass
        self.update_info_cache = None
        self.last_update_check = 0
        try:
            PluginsController.getInstance().reloadPlugin(self.id)
        except Exception as e:
            BulletinHelper.show_error(t('restart_error', lang=self.lang, error=str(e)))

    def _show_how_it_works(self, _):
        from ui.alert import AlertDialogBuilder
        from client_utils import get_last_fragment
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        builder = AlertDialogBuilder(act)
        builder.set_title(t('how_it_works', lang=self.lang))
        builder.set_message(t('how_it_works_text', lang=self.lang))
        builder.set_positive_button(t('close', lang=self.lang), lambda b, w: b.dismiss())
        builder.show()

    def _show_version_dialog(self, _):
        from ui.alert import AlertDialogBuilder
        from client_utils import get_last_fragment
        from org.telegram.messenger.browser import Browser
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        builder = AlertDialogBuilder(act)
        builder.set_title(t('current_version', lang=self.lang, version=__version__))
        builder.set_message(t('updates_info', lang=self.lang))

        def on_updates(b, w):
            try:
                uri = Uri.parse("https://t.me/I_am_Vestr")
                Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
            finally:
                b.dismiss()

        builder.set_positive_button(t('check_updates', lang=self.lang), on_updates)
        builder.set_negative_button(t('close', lang=self.lang), lambda b, w: b.dismiss())
        builder.show()

    def _show_reset_templates_dialog(self, _):
        pass

    def _reset_templates(self):
        pass

    def create_settings(self):
        self.templates = []
        for i in range(TEMPLATE_COUNT):
            name = self.get_setting(f"template_name_{i}", "")
            text = self.get_setting(f"template_text_{i}", "")
            self.templates.append({
                "name": name,
                "text": text,
                "enabled": True if i == 0 else bool(name and text)
            })
        settings = []
        settings.append(Header(text=t('settings', lang=self.lang)))
        settings.append(Switch(
            key='show_drawer_menu',
            text=t('drawer_menu', lang=self.lang),
            default=self.get_setting('show_drawer_menu', False),
            subtext=t('drawer_menu_sub', lang=self.lang),
            on_change=self._on_drawer_switch
        ))
        settings.append(Switch(
            key='show_chat_menu',
            text=t('chat_menu', lang=self.lang),
            default=self.get_setting('show_chat_menu', True),
            subtext=t('chat_menu_sub', lang=self.lang),
            on_change=self._on_chat_switch
        ))
        settings.append(Input(
            key='send_cmd',
            text=t('send_cmd', lang=self.lang),
            default=self.get_setting('send_cmd', '//'),
            subtext=t('send_cmd_sub', lang=self.lang)
        ))
        settings.append(Divider())
        settings.append(Header(text=t('templates_title', lang=self.lang)))
        settings.append(Text(
            text=t('create_template', lang=self.lang),
            icon='msg_addbot',
            accent=True,
            on_click=lambda ctx: self._create_new_template()
        ))
        settings.append(Text(
            text=t('export_templates', lang=self.lang),
            icon='msg_unarchive',
            accent=False,
            on_click=lambda ctx: self._export_templates_via_dialogs()
        ))
        settings.append(Divider())

        created_count = self._get_created_count()
        for i in range(created_count):
            tpl = self.templates[i] if i < len(self.templates) else {}
            name = tpl.get("name", "")
            text = tpl.get("text", "")
            settings.append(Header(text=t('template_n', lang=self.lang, n=i+1)))
            settings.append(Input(
                key=f"template_name_{i}",
                text=t('template_name', lang=self.lang),
                default=name,
                subtext=t('template_name_sub', lang=self.lang),
                icon="msg_edit",
                on_change=self._make_onchange(i, 'name')
            ))
            settings.append(Input(
                key=f"template_text_{i}",
                text=t('template_text', lang=self.lang),
                default=text,
                subtext=t('template_text_sub', lang=self.lang),
                icon="msg_edit",
                on_change=self._make_onchange(i, 'text')
            ))
            settings.append(Text(
                text=t('send_template', lang=self.lang),
                icon='msg_send',
                accent=True,
                on_click=lambda ctx, idx=i: self._send_template_by_index(idx)
            ))
            if created_count > 1:
                settings.append(Text(
                    text=t('delete_template', lang=self.lang),
                    icon='msg_delete',
                    red=True,
                    on_click=(lambda idx=i: (lambda ctx: self._delete_template(idx)))()
                ))
            settings.append(Divider())
        settings.append(Header(text=t('contacts', lang=self.lang)))
        settings.append(Text(
            text=t('support_me', lang=self.lang),
            icon='menu_feature_reactions',
            accent=True,
            on_click=self._show_support_dialog
        ))
        settings.append(Text(
            text=t('channel', lang=self.lang),
            icon='msg_channel',
            accent=False,
            on_click=self._open_channel_link
        ))
        settings.append(Text(
            text=t('personal', lang=self.lang),
            icon='msg_contacts',
            on_click=self._open_personal_link
        ))
        settings.append(Divider())
        settings.append(Header(text=t('other', lang=self.lang)))
        settings.append(Text(
            text=t('how_it_works', lang=self.lang),
            icon='msg_info',
            on_click=self._show_how_it_works
        ))
        settings.append(Text(
            text=t('plugin_version', lang=self.lang),
            icon='msg_settings_14',
            accent=True,
            on_click=self._show_version_dialog
        ))
        settings.append(Divider())
        settings.append(Divider())
        return settings

    def _on_drawer_switch(self, val):
        self.set_setting('show_drawer_menu', bool(val), reload_settings=True)
        run_on_ui_thread(self._update_drawer_menu)

    def _on_chat_switch(self, val):
        self.set_setting('show_chat_menu', bool(val), reload_settings=True)
        run_on_ui_thread(self._update_chat_menu)

    def _make_enabled_onchange(self, idx):
        return lambda val: None

    def _make_onchange(self, idx, field):
        def handler(val):
            val = val.strip()
            tpl = self.templates[idx] if idx < len(self.templates) else {}
            tpl = tpl.copy()
            tpl[field] = val
            if field == 'name' or field == 'text':
                tpl['enabled'] = bool(tpl.get('name', '') and tpl.get('text', ''))
            self.templates[idx] = tpl
            self.set_setting("templates", self.templates, reload_settings=True)
        return handler

    def _make_link_onclick(self):
        return lambda ctx: run_on_ui_thread(self.open_mr_vestr_link)

    def save_template(self, idx, val):
        val = val.strip()
        if ":" in val:
            name, text = map(str.strip, val.split(":", 1))
        else:
            name, text = val, ""
        self.templates[idx] = {"name": name, "text": text, "enabled": bool(name and text)}
        self.set_setting("templates", self.templates, reload_settings=True)

    def _create_new_template(self):
        try:
            self._debug("[Templates] create_template: clicked")
            last_idx = self._get_created_count() - 1
            last_tpl = self.templates[last_idx] if last_idx < len(self.templates) else {}
            self._debug(f"[Templates] last_tpl before create: name='{last_tpl.get('name')}', text_len={len(last_tpl.get('text',''))}")
            if not last_tpl.get("name") or not last_tpl.get("text"):
                from ui.bulletin import BulletinHelper
                from android_utils import run_on_ui_thread
                run_on_ui_thread(lambda: BulletinHelper.show_error(t('fill_prev_template', lang=self.lang)))
                return
            new_count = min(self._get_created_count() + 1, TEMPLATE_COUNT)
            self.set_setting("templates_created_count", new_count, reload_settings=True)
            from ui.bulletin import BulletinHelper
            from android_utils import run_on_ui_thread
            run_on_ui_thread(lambda: BulletinHelper.show_success(t('template_created_n', lang=self.lang, n=new_count)))
        except Exception as e:
            from ui.bulletin import BulletinHelper
            BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))

    def _templates_count(self):
        cnt = 0
        for tpl in self.templates:
            if tpl.get("name") or tpl.get("text"):
                cnt += 1
        return cnt

    def _get_created_count(self):
        count = self.get_setting("templates_created_count", 1)
        if not isinstance(count, int) or count < 1:
            count = 1
        return min(count, TEMPLATE_COUNT)

    def _delete_template(self, idx):
        try:
            from ui.alert import AlertDialogBuilder
            from client_utils import get_last_fragment
            frag = get_last_fragment()
            act = frag.getParentActivity() if frag else None
            if not act:
                return
            builder = AlertDialogBuilder(act)
            builder.set_title(t('delete_template_title', lang=self.lang))
            builder.set_message(t('delete_template_confirm', lang=self.lang, n=idx+1))
            def on_yes(b, w):
                try:
                    self._debug(f"[Templates] delete_template confirm idx={idx}, created_count={self._get_created_count()}")
                    old_count = self._get_created_count()
                    old_templates = [dict(t) for t in self.templates]
                    current_count = self._get_created_count()
                    if current_count <= 1:
                        self.templates[0] = {"name": "", "text": "", "enabled": False}
                        self.set_setting("template_name_0", "")
                        self.set_setting("template_text_0", "")
                        self.set_setting("templates_created_count", 1)
                    else:
                        if idx < current_count - 1:
                            for i in range(idx, current_count - 1):
                                self.templates[i] = dict(self.templates[i + 1])
                                self.templates[i]['enabled'] = bool(self.templates[i].get('name', '') and self.templates[i].get('text', ''))
                                self.set_setting(f"template_name_{i}", self.templates[i].get("name", ""))
                                self.set_setting(f"template_text_{i}", self.templates[i].get("text", ""))
                        last_created = current_count - 1
                        self.templates[last_created] = {"name": "", "text": "", "enabled": False}
                        self.set_setting(f"template_name_{last_created}", "")
                        self.set_setting(f"template_text_{last_created}", "")
                        self.set_setting("templates_created_count", current_count - 1)
                    self.set_setting("templates", self.templates, reload_settings=True)
                    from ui.bulletin import BulletinHelper
                    deleted_number = idx + 1
                    def on_undo():
                        try:
                            self.templates = [dict(t) for t in old_templates]
                            self.set_setting("templates_created_count", old_count)
                            for i in range(min(old_count, TEMPLATE_COUNT)):
                                tpl = self.templates[i] if i < len(self.templates) else {}
                                self.set_setting(f"template_name_{i}", tpl.get("name", ""))
                                self.set_setting(f"template_text_{i}", tpl.get("text", ""))
                            self.set_setting("templates", self.templates, reload_settings=True)
                        except Exception:
                            pass
                    try:
                        from org.telegram.messenger import R as R_tg
                        icon_attr = getattr(R_tg.raw, 'done', None)
                    except Exception:
                        icon_attr = None
                    try:
                        BulletinHelper.show_with_button(t('template_deleted_n', lang=self.lang, n=deleted_number), icon_attr if icon_attr else 0, t('undo', lang=self.lang), lambda: on_undo(), None)
                    except Exception:
                        from android_utils import run_on_ui_thread
                        run_on_ui_thread(lambda: BulletinHelper.show_success(t('template_deleted_n', lang=self.lang, n=deleted_number)))
                finally:
                    b.dismiss()
            builder.set_positive_button(t('delete_button', lang=self.lang), on_yes)
            builder.set_negative_button(t('close', lang=self.lang), lambda b, w: b.dismiss())
            builder.show()
        except Exception as e:
            from ui.bulletin import BulletinHelper
            BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))
    def open_mr_vestr_link(self):
        from client_utils import get_last_fragment
        from android.content import Intent, Uri
        fragment = get_last_fragment()
        activity = fragment and fragment.getParentActivity()
        if not activity:
            return
        intent = Intent(Intent.ACTION_VIEW)
        intent.setData(Uri.parse("https://t.me/mr_vestr"))
        activity.startActivity(intent)

    def edit_template_dialog(self, idx):
        from ui.alert import AlertDialogBuilder
        from client_utils import get_last_fragment
        fragment = get_last_fragment()
        activity = fragment and fragment.getParentActivity()
        if not activity:
            return
        builder = AlertDialogBuilder(activity)
        builder.set_title(t('edit_template', lang=self.lang, n=idx+1))
        from android.widget import LinearLayout, EditText
        nameEdit = EditText(activity)
        nameEdit.setText(self.templates[idx].get("name", ""))
        nameEdit.setHint(t('template_name', lang=self.lang))
        textEdit = EditText(activity)
        textEdit.setText(self.templates[idx].get("text", ""))
        textEdit.setHint(t('template_text', lang=self.lang))
        layout = LinearLayout(activity)
        layout.setOrientation(LinearLayout.VERTICAL)
        layout.addView(nameEdit)
        layout.addView(textEdit)
        builder.set_view(layout)
        def on_done(b, w):
            name = str(nameEdit.getText()).strip()
            text = str(textEdit.getText()).strip()
            self.templates[idx] = {"name": name, "text": text, "enabled": bool(name and text)}
            self.set_setting("templates", self.templates, reload_settings=True)
            b.dismiss()
        builder.set_positive_button(t('save', lang=self.lang), on_done)
        builder.set_negative_button(t('cancel', lang=self.lang), lambda b, w: b.dismiss())
        builder.show()

    def send_template(self, idx):
        pass

    def _open_share_link(self, url):
        from client_utils import get_last_fragment
        from android.content import Intent
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if act:
            act.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))

    def _open_chat_by_dialog_id(self, dialog_id):
        try:
            self._debug(f"[Templates] Opening chat with dialog_id: {dialog_id}")
            from client_utils import get_last_fragment, get_messages_controller
            from android_utils import run_on_ui_thread
            try:
                did = int(dialog_id)
                self._debug(f"[Templates] Converted dialog_id to int: {did}")
            except Exception as e:
                self._debug(f"[Templates] Using dialog_id as is (not an int): {dialog_id}")
                did = dialog_id
            fragment = get_last_fragment()
            if not fragment:
                self._debug("[Templates] Error: Could not get last fragment")
                return
            self._debug(f"[Templates] Found fragment: {fragment}")
            def _open():
                try:
                    self._debug("[Templates] Calling openByChatId...")
                    get_messages_controller().openByChatId(did, fragment, 1)
                    self._debug("[Templates] openByChatId called successfully")
                except Exception as e:
                    self._debug(f"[Templates] Error in openByChatId: {str(e)}")
                    try:
                        from android.content import Intent
                        from android.net import Uri
                        from org.telegram.messenger.browser import Browser
                        self._debug("[Templates] Trying fallback with Browser...")
                        if isinstance(did, int):
                            if did > 0:
                                Browser.openUrl(fragment.getParentActivity(), f"tg://user?id={did}")
                            else:
                                Browser.openUrl(fragment.getParentActivity(), f"tg://resolve?domain={abs(did)}")
                        else:
                            Browser.openUrl(fragment.getParentActivity(), f"tg://resolve?domain={did}")
                        self._debug("[Templates] Fallback Browser.openUrl called")
                    except Exception as e2:
                        self._debug(f"[Templates] Fallback also failed: {str(e2)}")
            run_on_ui_thread(_open)
        except Exception as e:
            self._debug(f"[Templates] _open_chat_by_dialog_id error: {str(e)}")
            try:
                import traceback
                self._debug(f"[Templates] Stack trace: {traceback.format_exc()}")
            except:
                pass

    def on_send_message_hook(self, account, params):
        if not hasattr(params, "message") or not isinstance(params.message, str):
            return HookResult(strategy=HookStrategy.NONE)
        msg = params.message.strip()
        send_cmd = self.get_setting('send_cmd', '//').strip()
        if not send_cmd:
            send_cmd = '//'
        if msg.lower().startswith(send_cmd.lower()):
            from ui.bulletin import BulletinHelper
            from android_utils import run_on_ui_thread
            parts = msg[len(send_cmd):].strip()
            if not parts:
                run_on_ui_thread(lambda: self._show_template_popup_menu(None))
                return HookResult(strategy=HookStrategy.CANCEL)
            query = parts.lower()
            for i, tpl in enumerate(self.templates):
                if tpl.get('enabled', False):
                    name = self.get_setting(f"template_name_{i}", "").strip()
                    text = self.get_setting(f"template_text_{i}", "").strip()
                    if name.lower() == query and text:
                        preprocessed = preprocess_template_markdown(text)
                        parsed = parse_markdown(preprocessed)
                        params.message = parsed.text
                        if hasattr(params, 'entities') and params.entities is not None:
                            params.entities.clear()
                        else:
                            from java.util import ArrayList
                            params.entities = ArrayList()
                        for ent in parsed.entities:
                            params.entities.add(ent.to_tlrpc_object())
                        try:
                            from org.telegram.messenger import R as R_tg
                            icon_attr = getattr(R_tg.raw, 'done', None)
                        except Exception:
                            icon_attr = None
                        dialog_id = None
                        try:
                            from client_utils import get_last_fragment
                            from org.telegram.ui import ChatActivity
                            frag = get_last_fragment()
                            if isinstance(frag, ChatActivity):
                                try:
                                    dialog_id = frag.getDialogId()
                                except Exception:
                                    dialog_id = None
                        except Exception:
                            dialog_id = None
                        def _open():
                            try:
                                if dialog_id:
                                    self._open_chat_by_dialog_id(dialog_id)
                            except Exception:
                                pass
                        run_on_ui_thread(lambda: BulletinHelper.show_success(t('template_n_sent', lang=self.lang, n=i+1)))
                        return HookResult(strategy=HookStrategy.MODIFY, params=params)
            matching_templates = []
            for i, tpl in enumerate(self.templates):
                if tpl.get('enabled', False):
                    name = self.get_setting(f"template_name_{i}", "").strip()
                    text = self.get_setting(f"template_text_{i}", "").strip()
                    if name.lower().startswith(query) and text:
                        matching_templates.append({
                            'index': i,
                            'name': name,
                            'text': text
                        })
            if matching_templates:
                run_on_ui_thread(lambda: self._show_filtered_template_menu(matching_templates))
                return HookResult(strategy=HookStrategy.CANCEL)
            else:
                run_on_ui_thread(lambda: self._show_template_popup_menu(None))
                return HookResult(strategy=HookStrategy.CANCEL)
        return HookResult(strategy=HookStrategy.NONE)

    def _send_template_by_index(self, idx):
        name = self.get_setting(f"template_name_{idx}", "").strip()
        text = self.get_setting(f"template_text_{idx}", "").strip()
        if not name or not text:
            from ui.bulletin import BulletinHelper
            from android_utils import run_on_ui_thread
            run_on_ui_thread(lambda: BulletinHelper.show_error(t('fill_all_fields', lang=self.lang)))
            return
        self._showDialogsActivity_for_template(idx, name, text)

    def _showDialogsActivity_for_template(self, idx, name, text):
        args = Bundle()
        args.putBoolean("onlySelect", True)
        args.putBoolean("checkCanWrite", True)
        args.putInt("dialogsType", 0)
        args.putBoolean("allowGlobalSearch", True)
        activity = DialogsActivity(args)
        def after_select(fragment, dids, message, param, notify, scheduleDate, topicsFragment):
            activity.finishFragment()
            if dids.isEmpty():
                return
            selected_id = dids.get(0).dialogId
            peer_id = int(str(selected_id))
            preprocessed = preprocess_template_markdown(text)
            parsed = parse_markdown(preprocessed)
            from client_utils import send_message
            send_message({
                "peer": peer_id,
                "message": parsed.text,
                "entities": [ent.to_tlrpc_object() for ent in parsed.entities]
            })
            from android_utils import run_on_ui_thread
            try:
                from org.telegram.messenger import R as R_tg
                icon_attr = getattr(R_tg.raw, 'done', None)
            except Exception:
                icon_attr = None
            def _open():
                try:
                    self._open_chat_by_dialog_id(peer_id)
                except Exception:
                    pass
            run_on_ui_thread(lambda: BulletinHelper.show_with_button(t('template_n_sent', lang=self.lang, n=idx+1), icon_attr if icon_attr else 0, t('open', lang=self.lang), _open, None))
        delegate = TemplateDialogsDelegate(after_select)
        activity.setDelegate(delegate)
        last_fragment = LaunchActivity.getLastFragment()
        if last_fragment:
            last_fragment.presentFragment(activity)

    def _show_support_dialog(self, _):
        from ui.alert import AlertDialogBuilder
        from client_utils import get_last_fragment
        from org.telegram.messenger.browser import Browser
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        builder = AlertDialogBuilder(act)
        builder.set_title(t('support_me', lang=self.lang))
        builder.set_message(t('support_me_text', lang=self.lang))
        def on_account(b, w):
            uri = Uri.parse("https://t.me/mr_Vestr")
            Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
            b.dismiss()
        builder.set_positive_button(t('my_account', lang=self.lang), on_account)
        builder.set_negative_button(t('close', lang=self.lang), lambda b, w: b.dismiss())
        builder.show() 

    def _show_template_popup_menu(self, input_field):
        from org.telegram.ui.ActionBar import BottomSheet
        from org.telegram.ui.Components import LayoutHelper
        from android.widget import LinearLayout, TextView, ScrollView
        from android.view import Gravity
        from android.util import TypedValue
        from org.telegram.ui.ActionBar import Theme
        from org.telegram.messenger import AndroidUtilities
        from android_utils import OnClickListener
        from client_utils import get_last_fragment
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        active_templates = []
        for i, tpl in enumerate(self.templates):
            if tpl.get('enabled', False):
                name = self.get_setting(f"template_name_{i}", "").strip()
                text = self.get_setting(f"template_text_{i}", "").strip()
                if name and text:
                    active_templates.append({
                        'index': i,
                        'name': name,
                        'text': text
                    })
        self.menu_shown = True
        builder = BottomSheet.Builder(act)
        builder.setApplyTopPadding(False)
        builder.setApplyBottomPadding(False)
        linearLayout = LinearLayout(act)
        builder.setCustomView(linearLayout)
        linearLayout.setOrientation(LinearLayout.VERTICAL)
        titleTextView = TextView(act)
        titleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        titleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 20)
        titleTextView.setGravity(Gravity.CENTER)
        titleTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
        if active_templates:
            titleTextView.setText(t('select_template', lang=self.lang))
        else:
            titleTextView.setText(t('no_templates_available', lang=self.lang))
        linearLayout.addView(titleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 16, 0, 8))
        if active_templates:
            scrollView = ScrollView(act)
            scrollView.setFillViewport(True)
            buttonsLayout = LinearLayout(act)
            buttonsLayout.setOrientation(LinearLayout.VERTICAL)
            def create_template_button(template):
                def send_template(v=None):
                    try:
                        builder.getDismissRunnable().run()
                        self.menu_shown = False
                        self._send_template_to_current_chat(template['index'], template['name'], template['text'])
                    except Exception as e:
                        from ui.bulletin import BulletinHelper
                        BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))
                from android.widget import LinearLayout
                buttonContainer = LinearLayout(act)
                buttonContainer.setOrientation(LinearLayout.VERTICAL)
                buttonContainer.setPadding(AndroidUtilities.dp(16), AndroidUtilities.dp(12), AndroidUtilities.dp(16), AndroidUtilities.dp(12))
                buttonContainer.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                    AndroidUtilities.dp(8),
                    Theme.getColor(Theme.key_dialogBackground),
                    Theme.getColor(Theme.key_dialogBackgroundGray)
                ))
                buttonContainer.setClickable(True)
                buttonContainer.setOnClickListener(OnClickListener(send_template))
                nameTextView = TextView(act)
                nameTextView.setText(template['name'])
                nameTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
                nameTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
                nameTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
                nameTextView.setGravity(Gravity.LEFT)
                buttonContainer.addView(nameTextView)
                text = template['text']
                maxLength = 50
                if len(text) > maxLength:
                    text = text[:maxLength] + "..."
                textTextView = TextView(act)
                textTextView.setText(text)
                textTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray))
                textTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
                textTextView.setGravity(Gravity.LEFT)
                textTextView.setPadding(0, AndroidUtilities.dp(4), 0, 0)
                buttonContainer.addView(textTextView)
                return buttonContainer
            for i, template in enumerate(active_templates):
                btn = create_template_button(template)
                buttonsLayout.addView(btn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 4, 16, 4))
                if i < len(active_templates) - 1:
                    divider = TextView(act)
                    divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
                    buttonsLayout.addView(divider, LayoutHelper.createFrame(-1, 1, Gravity.TOP, 16, 0, 16, 0))
            scrollView.addView(buttonsLayout)
            linearLayout.addView(scrollView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 8, 0, 16))
        settingsBtn = TextView(act)
        settingsBtn.setText(t('settings', lang=self.lang))
        settingsBtn.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        settingsBtn.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        settingsBtn.setGravity(Gravity.CENTER)
        settingsBtn.setPadding(AndroidUtilities.dp(16), AndroidUtilities.dp(12), AndroidUtilities.dp(16), AndroidUtilities.dp(12))
        settingsBtn.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(8),
            Theme.getColor(Theme.key_featuredStickers_addButton),
            Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        ))
        settingsBtn.setClickable(True)
        def on_settings(v=None):
            builder.getDismissRunnable().run()
            self.menu_shown = False
            self.open_plugin_settings()
        settingsBtn.setOnClickListener(OnClickListener(on_settings))
        linearLayout.addView(settingsBtn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 8, 16, 8))
        cancelBtn = TextView(act)
        cancelBtn.setText(t('cancel', lang=self.lang))
        cancelBtn.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        cancelBtn.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        cancelBtn.setGravity(Gravity.CENTER)
        cancelBtn.setPadding(AndroidUtilities.dp(16), AndroidUtilities.dp(12), AndroidUtilities.dp(16), AndroidUtilities.dp(12))
        cancelBtn.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(8),
            Theme.getColor(Theme.key_dialogBackground),
            Theme.getColor(Theme.key_dialogBackgroundGray)
        ))
        cancelBtn.setClickable(True)
        def on_cancel(v=None):
            builder.getDismissRunnable().run()
            self.menu_shown = False
        cancelBtn.setOnClickListener(OnClickListener(on_cancel))
        linearLayout.addView(cancelBtn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 8, 16, 16))
        sheet = builder.show()
        def on_dismiss():
            self.menu_shown = False
        try:
            sheet.setOnDismissListener(dynamic_proxy(android.content.DialogInterface.OnDismissListener)(on_dismiss))
        except Exception:
            pass
        return sheet

    def _export_templates_via_dialogs(self):
        try:
            import json
            self._debug("[Templates] export: start")
            export_items = []
            for i in range(TEMPLATE_COUNT):
                name = self.get_setting(f"template_name_{i}", "").strip()
                text = self.get_setting(f"template_text_{i}", "").strip()
                if name or text:
                    export_items.append({
                        "index": i,
                        "name": name,
                        "text": text
                    })
            self._debug(f"[Templates] export: items={len(export_items)}")
            args = Bundle()
            args.putBoolean("onlySelect", True)
            args.putBoolean("checkCanWrite", True)
            args.putInt("dialogsType", 0)
            args.putBoolean("allowGlobalSearch", True)
            activity = DialogsActivity(args)

            def after_select(fragment, dids, message, param, notify, scheduleDate, topicsFragment):
                try:
                    activity.finishFragment()
                    if dids.isEmpty():
                        return
                    selected_id = dids.get(0).dialogId
                    peer_id = int(str(selected_id))
                    self._debug(f"[Templates] export: peer_id={peer_id}")
                    try:
                        data_bytes = json.dumps({"templates": export_items}, ensure_ascii=False).encode("utf-8")
                        self._debug(f"[Templates] export: json_size={len(data_bytes)}")
                    except Exception as e:
                        from ui.bulletin import BulletinHelper
                        BulletinHelper.show_error(t('export_error', lang=self.lang, error=str(e)))
                        return
                    path = _LocalFileSystem.write_temp_file("export.templates", data_bytes, delete_after=30)
                    self._debug(f"[Templates] export: path={path}")
                    self._debug("[Templates] export: sending file")
                    self._send_file(peer_id, path, t('export_file_caption', lang=self.lang))
                    from android_utils import run_on_ui_thread
                    from ui.bulletin import BulletinHelper
                    try:
                        from org.telegram.messenger import R as R_tg
                        icon_attr = getattr(R_tg.raw, 'done', None)
                    except Exception:
                        icon_attr = None
                    def _open():
                        try:
                            self._open_chat_by_dialog_id(peer_id)
                        except Exception:
                            pass
                    run_on_ui_thread(lambda: BulletinHelper.show_with_button(t('templates_exported', lang=self.lang), icon_attr if icon_attr else 0, t('open', lang=self.lang), _open, None))
                except Exception as e:
                    from ui.bulletin import BulletinHelper
                    self._debug(f"[Templates] export error: {str(e)}")
                    BulletinHelper.show_error(t('export_error', lang=self.lang, error=str(e)))

            delegate = TemplateDialogsDelegate(after_select)
            activity.setDelegate(delegate)
            last_fragment = LaunchActivity.getLastFragment()
            if last_fragment:
                last_fragment.presentFragment(activity)
        except Exception as e:
            from ui.bulletin import BulletinHelper
            self._debug(f"[Templates] export outer error: {str(e)}")
            BulletinHelper.show_error(t('export_error', lang=self.lang, error=str(e)))

    def _show_import_templates_alert(self, data, act=None):
        try:
            from ui.alert import AlertDialogBuilder
            from client_utils import get_last_fragment
            from android_utils import run_on_ui_thread
            if act is None:
                frag = get_last_fragment()
                act = frag.getParentActivity() if frag else None
            if not act:
                return
            def _show():
                builder = AlertDialogBuilder(act)
                builder.set_title(t('import_dialog_title', lang=self.lang))
                builder.set_message(t('import_question', lang=self.lang))
                def on_apply(b, w):
                    try:
                        templates = data.get("templates", []) if isinstance(data, dict) else []
                        if not isinstance(templates, list):
                            templates = []
                        self.set_setting("templates_created_count", min(max(len(templates), 1), TEMPLATE_COUNT), reload_settings=True)
                        self.templates = []
                        for i in range(TEMPLATE_COUNT):
                            if i < len(templates):
                                item = templates[i] or {}
                                name = str(item.get("name", ""))
                                text = str(item.get("text", ""))
                            else:
                                name = ""
                                text = ""
                            self.set_setting(f"template_name_{i}", name, reload_settings=True)
                            self.set_setting(f"template_text_{i}", text, reload_settings=True)
                            self.templates.append({"name": name, "text": text, "enabled": True if i == 0 else bool(name and text)})
                        self.set_setting("templates", self.templates, reload_settings=True)
                        from ui.bulletin import BulletinHelper
                        from android_utils import run_on_ui_thread
                        try:
                            from org.telegram.messenger import R as R_tg
                            icon_attr = getattr(R_tg.raw, 'settings', None)
                        except Exception:
                            icon_attr = None
                        def _open_settings():
                            try:
                                self.open_plugin_settings()
                            except Exception as e:
                                from ui.bulletin import BulletinHelper
                                BulletinHelper.show_error(t('open_settings_error', lang=self.lang, error=str(e)))
                        run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                            t('import_success', lang=self.lang),
                            icon_attr if icon_attr else 0,
                            t('settings', lang=self.lang),
                            _open_settings,
                            None
                        ))
                    except Exception as e:
                        from ui.bulletin import BulletinHelper
                        run_on_ui_thread(lambda: BulletinHelper.show_error(t('import_error', lang=self.lang, error=str(e))))
                    finally:
                        b.dismiss()
                builder.set_positive_button(t('apply', lang=self.lang), on_apply)
                builder.set_negative_button(t('cancel', lang=self.lang), lambda b, w: b.dismiss())
                builder.show()
            run_on_ui_thread(_show)
        except Exception as e:
            from ui.bulletin import BulletinHelper
            BulletinHelper.show_error(t('import_error', lang=self.lang, error=str(e)))

    def _send_file(self, peer_id, path, caption=None):
        try:
            self._debug(f"[Templates] send_file: start peer={peer_id} path={path} caption={'yes' if caption else 'no'}")
            from org.telegram.messenger import SendMessagesHelper
            from client_utils import get_account_instance
            from java import jarray, jint, jlong
            try:
                from java.lang import Integer
            except Exception:
                Integer = int
            try:
                from java.io import File as JFile
                size = JFile(path).length()
                self._debug(f"[Templates] send_file: size={size}")
            except Exception:
                pass
            methods = SendMessagesHelper.getClass().getDeclaredMethods()
            target = None
            self._debug("[Templates] send_file: scanning methods")
            use_uri = False
            for m in methods:
                if m.getName() == "prepareSendingDocumentInternal":
                    try:
                        params = m.getParameterTypes()
                        if len(params) > 1 and "android.net.Uri" in str(params[1]):
                            use_uri = True
                            self._debug("[Templates] send_file: using Uri parameters for document")
                        else:
                            self._debug("[Templates] send_file: using String path parameters for document")
                    except Exception:
                        pass
                    target = m
                    break
            if target is None:
                try:
                    names = ", ".join([mm.getName() for mm in methods])
                    self._debug(f"[Templates] send_file: target not found; available methods: {names}")
                except Exception:
                    pass
                raise Exception("prepareSendingDocumentInternal not found")
            target.setAccessible(True)
            mime = "application/json"
            self._debug(f"[Templates] send_file: invoking mime={mime}")
            if use_uri:
                try:
                    from android.net import Uri as AndroidUri
                    from java.io import File as JFile
                    fileUri = AndroidUri.fromFile(JFile(path))
                    arg1 = fileUri
                    arg2 = fileUri
                except Exception:
                    arg1 = path
                    arg2 = path
            else:
                arg1 = path
                arg2 = path
            params = target.getParameterTypes()
            try:
                types_str = ", ".join([p.getName() for p in params])
                self._debug(f"[Templates] send_file: param_types=[{types_str}]")
            except Exception:
                pass
            int_array_value = None
            try:
                types_names = [p.getName() for p in params]
                if any((n.startswith('[L') and 'java.lang.Integer' in n) or 'java.lang.Integer[]' in n for n in types_names):
                    int_array_value = jarray(Integer)([0])
                    self._debug("[Templates] send_file: int array type=Integer[]")
                elif any(n == '[I' or 'int[]' in n for n in types_names):
                    int_array_value = jarray(jint)([0])
                    self._debug("[Templates] send_file: int array type=int[]")
                else:
                    int_array_value = jarray(jint)([0])
            except Exception:
                int_array_value = jarray(jint)([0])
            args = [
                get_account_instance(), arg1, arg2, None, mime,
                peer_id, None, None,
                None, None, None,
                None, jarray(jlong)([0]), True, caption, True,
                jint(0), int_array_value, True,
                None, jint(0),
                0, False, 0,
                0
            ]
            try:
                self._debug(f"[Templates] send_file: param_count={len(params)} base_args={len(args)}")
            except Exception:
                pass
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
                    return None
                if len(params) > len(args):
                    for k in range(len(args), len(params)):
                        args.append(_def_for(params[k]))
                else:
                    args = args[:len(params)]
            target.invoke(None, *args)
            self._debug("[Templates] send_file: invoke completed")
        except Exception as e:
            from ui.bulletin import BulletinHelper
            self._debug(f"[Templates] send_file error: {str(e)}")
            BulletinHelper.show_error(t('export_error', lang=self.lang, error=str(e)))
    def _show_filtered_template_menu(self, templates):
        from org.telegram.ui.ActionBar import BottomSheet
        from org.telegram.ui.Components import LayoutHelper
        from android.widget import LinearLayout, TextView, ScrollView
        from android.view import Gravity
        from android.util import TypedValue
        from org.telegram.ui.ActionBar import Theme
        from org.telegram.messenger import AndroidUtilities
        from android_utils import OnClickListener
        from client_utils import get_last_fragment
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        builder = BottomSheet.Builder(act)
        builder.setApplyTopPadding(False)
        builder.setApplyBottomPadding(False)
        linearLayout = LinearLayout(act)
        builder.setCustomView(linearLayout)
        linearLayout.setOrientation(LinearLayout.VERTICAL)
        titleTextView = TextView(act)
        titleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        titleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 20)
        titleTextView.setGravity(Gravity.CENTER)
        titleTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
        if templates:
            titleTextView.setText(t('select_template', lang=self.lang))
        else:
            titleTextView.setText(t('no_templates_available', lang=self.lang))
        linearLayout.addView(titleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 16, 0, 8))
        scrollView = ScrollView(act)
        scrollView.setFillViewport(True)
        buttonsLayout = LinearLayout(act)
        buttonsLayout.setOrientation(LinearLayout.VERTICAL)
        def create_template_button(template):
            def send_template(v=None):
                try:
                    builder.getDismissRunnable().run()
                    self.menu_shown = False
                    self._send_template_to_current_chat(template['index'], template['name'], template['text'])
                except Exception as e:
                    from ui.bulletin import BulletinHelper
                    BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))
            from android.widget import LinearLayout
            buttonContainer = LinearLayout(act)
            buttonContainer.setOrientation(LinearLayout.VERTICAL)
            buttonContainer.setPadding(AndroidUtilities.dp(16), AndroidUtilities.dp(12), AndroidUtilities.dp(16), AndroidUtilities.dp(12))
            buttonContainer.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                AndroidUtilities.dp(8),
                Theme.getColor(Theme.key_dialogBackground),
                Theme.getColor(Theme.key_dialogBackgroundGray)
            ))
            buttonContainer.setClickable(True)
            buttonContainer.setOnClickListener(OnClickListener(send_template))
            nameTextView = TextView(act)
            nameTextView.setText(template['name'])
            nameTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            nameTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            nameTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
            nameTextView.setGravity(Gravity.LEFT)
            buttonContainer.addView(nameTextView)
            text = template['text']
            maxLength = 50
            if len(text) > maxLength:
                text = text[:maxLength] + "..."
            
            textTextView = TextView(act)
            textTextView.setText(text)
            textTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray))
            textTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            textTextView.setGravity(Gravity.LEFT)
            textTextView.setPadding(0, AndroidUtilities.dp(4), 0, 0)
            buttonContainer.addView(textTextView)
            return buttonContainer

        for i, template in enumerate(templates):
            btn = create_template_button(template)
            buttonsLayout.addView(btn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 4, 16, 4))
            if i < len(templates) - 1:
                divider = TextView(act)
                divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
                buttonsLayout.addView(divider, LayoutHelper.createFrame(-1, 1, Gravity.TOP, 16, 0, 16, 0))
        scrollView.addView(buttonsLayout)
        linearLayout.addView(scrollView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 8, 0, 16))
        settingsBtn = TextView(act)
        settingsBtn.setText(t('settings', lang=self.lang))
        settingsBtn.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        settingsBtn.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        settingsBtn.setGravity(Gravity.CENTER)
        settingsBtn.setPadding(AndroidUtilities.dp(16), AndroidUtilities.dp(12), AndroidUtilities.dp(16), AndroidUtilities.dp(12))
        settingsBtn.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(8),
            Theme.getColor(Theme.key_dialogBackground),
            Theme.getColor(Theme.key_dialogBackgroundGray)
        ))
        settingsBtn.setClickable(True)
        def on_settings(v=None):
            builder.getDismissRunnable().run()
            self.menu_shown = False
            self.open_plugin_settings()
        settingsBtn.setOnClickListener(OnClickListener(on_settings))
        linearLayout.addView(settingsBtn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 8, 16, 8))
        cancelBtn = TextView(act)
        cancelBtn.setText(t('cancel', lang=self.lang))
        cancelBtn.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        cancelBtn.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        cancelBtn.setGravity(Gravity.CENTER)
        cancelBtn.setPadding(AndroidUtilities.dp(16), AndroidUtilities.dp(12), AndroidUtilities.dp(16), AndroidUtilities.dp(12))
        cancelBtn.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(8),
            Theme.getColor(Theme.key_featuredStickers_addButton),
            Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        ))
        cancelBtn.setClickable(True)
        def on_cancel(v=None):
            builder.getDismissRunnable().run()
            self.menu_shown = False
        cancelBtn.setOnClickListener(OnClickListener(on_cancel))
        linearLayout.addView(cancelBtn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 8, 16, 16))
        sheet = builder.show()
        def on_dismiss():
            self.menu_shown = False
        try:
            sheet.setOnDismissListener(dynamic_proxy(android.content.DialogInterface.OnDismissListener)(on_dismiss))
        except Exception:
            pass
        return sheet

    def _send_template_to_current_chat(self, template_index, template_name, template_text):
        import time
        try:
            from client_utils import get_last_fragment
            from org.telegram.ui import ChatActivity
            frag = get_last_fragment()
            if not frag:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('error_occurred', lang=self.lang))
                return
            if not isinstance(frag, ChatActivity):
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('error_occurred', lang=self.lang))
                return
            current_chat = None
            chat_id = None
            try:
                current_chat = frag.getCurrentChat()
                if current_chat and hasattr(current_chat, 'id'):
                    chat_id = current_chat.id
            except Exception:
                pass
            if not chat_id:
                try:
                    current_user = frag.getCurrentUser()
                    if current_user and hasattr(current_user, 'id'):
                        chat_id = current_user.id
                except Exception:
                    pass
            if not chat_id:
                try:
                    dialog_id = frag.getDialogId()
                    if dialog_id:
                        chat_id = dialog_id
                except Exception:
                    pass
            if not chat_id:
                try:
                    current_peer = frag.getCurrentPeer()
                    if current_peer and hasattr(current_peer, 'id'):
                        chat_id = current_peer.id
                except Exception:
                    pass
            if not chat_id:
                try:
                    args = frag.getArguments()
                    if args:
                        dialog_id = args.getLong("dialog_id", 0)
                        if dialog_id:
                            chat_id = dialog_id
                except Exception:
                    pass
            if not chat_id:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('error_occurred', lang=self.lang))
                return
            preprocessed = preprocess_template_markdown(template_text)
            parsed = parse_markdown(preprocessed)
            try:
                from client_utils import send_message
                message_data = {
                    "peer": chat_id,
                    "message": parsed.text,
                    "entities": [ent.to_tlrpc_object() for ent in parsed.entities]
                }
                
                send_message(message_data)
            except Exception:
                try:
                    from org.telegram.messenger import SendMessagesHelper
                    from org.telegram.tgnet import TLRPC
                    message = TLRPC.TL_message()
                    message.message = parsed.text
                    message.dialog_id = chat_id
                    message.date = int(time.time())
                    message.out = True
                    if parsed.entities:
                        message.entities = [ent.to_tlrpc_object() for ent in parsed.entities]
                    SendMessagesHelper.getInstance().sendMessage(message)
                except Exception as e2:
                    raise e2
            from ui.bulletin import BulletinHelper
            from android_utils import run_on_ui_thread
            try:
                from org.telegram.messenger import R as R_tg
                icon_attr = getattr(R_tg.raw, 'done', None)
            except Exception:
                icon_attr = None
            def _open():
                try:
                    if chat_id:
                        self._open_chat_by_dialog_id(chat_id)
                except Exception:
                    pass
            run_on_ui_thread(lambda: BulletinHelper.show_success(t('template_n_sent', lang=self.lang, n=template_index+1)))
        except Exception as e:
            from ui.bulletin import BulletinHelper
            BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))

class TemplateDialogsDelegate(dynamic_proxy(DialogsActivity.DialogsActivityDelegate)):
    def __init__(self, fn):
        super().__init__()
        self._fn = fn
    def didSelectDialogs(self, fragment, dids, message, param, notify, scheduleDate, topicsFragment):
        try:
            self._fn(fragment, dids, message, param, notify, scheduleDate, topicsFragment)
        except Exception as e:
            from ui.bulletin import BulletinHelper
            BulletinHelper.show_error(f"Error: {e}") 