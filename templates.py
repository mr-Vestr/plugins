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
__version__ = "1.0"
__min_version__ = "11.12.0"
__icon__ = "mr_vestr/2"

TEMPLATE_COUNT = 30
_update_check_in_progress = False

LANG = {
    'ru': {
        'open_settings_error': 'Не удалось открыть настройки: {error}',
        'templates': 'Шаблоны',
        'link_open_error': 'Ошибка при открытии ссылки: {error}',
        'checking_version': 'Проверяем версию...',
        'current_version': 'У вас актуальная версия: {version}',
        'parse_version_error': 'Не удалось распарсить версию',
        'version_format_error': 'Неверный формат информации о версии',
        'version_not_found': 'Не удалось найти информацию о версии',
        'version_check_error': 'Произошла ошибка при проверке!',
        'update_available': 'Доступно обновление: {version}',
        'update_question': 'Хотите обновить плагин?',
        'update': 'Обновить',
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
        'yes': 'Да',
        'no': 'Нет',
        'settings': 'Настройки',
        'drawer_menu': 'Значок в боковом меню',
        'drawer_menu_sub': 'Добавляет кнопку настроек шаблонов в боковое меню.',
        'chat_menu': 'Значок в меню чата',
        'chat_menu_sub': 'Добавляет кнопку настроек шаблонов в меню чата.',
        'send_cmd': 'Команда отправки шаблона',
        'send_cmd_sub': 'Введите команду для отправки шаблонов:',
        'template_n': 'Шаблон №{n}',
        'disable_template': 'Выключить шаблон',
        'enable_template': 'Включить шаблон',
        'template_name': 'Название шаблона',
        'template_name_sub': 'Придумайте название шаблона.',
        'template_text': 'Текст шаблона',
        'template_text_sub': 'Придумайте текст шаблона.',
        'send_template': 'Отправить шаблон',
        'contacts': 'Мои контакты',
        'channel': 'Мой канал — @I_am_Vestr',
        'personal': 'Моя личка — @mr_Vestr',
        'other': 'Другое',
        'plugin_version': 'Версия плагина — 1.0',
        'reset_templates_btn': 'Сбросить шаблоны',
        'edit_template': 'Редактировать шаблон {n}',
        'save': 'Сохранить',
        'cancel': 'Отмена',
        'enter_template_name': 'Чтобы отправить шаблон, напишите его название.',
        'template_sent': 'Шаблон «{name}» отправлен!',
        'template_not_found': 'Шаблон не найден! Шаблоны добавляются в настройках плагина.',
        'fill_all_fields': 'Заполните все данные, для отправки шаблона!',
        'checking_updates': 'Проверяем обновления...',
        'plugin_up_to_date': 'У вас актуальная версия плагина!',
        'update_check_error': 'Ошибка при проверке обновлений!',
        'update_plugin': 'Обновление плагина...',
        'plugin_updated': 'Плагин успешно обновлён!',
        'close_menu_question': 'Хотите закрыть меню?',
        'templates_title': 'Шаблоны',
        'error_occurred': 'Произошла ошибка!',
        'support_me': 'Поддержать меня',
        'support_me_text': 'Если вы хотите меня поддержать, вы можете отправить мне подарок в Telegram или подарить Telegram Premium :)',
        'my_account': 'Мой аккаунт',
        'restart_error': 'Ошибка перезапуска: {error}',
        'download_error': 'Ошибка загрузки: {error}',
        'error_occurred_with_reason': 'Ошибка: {error}',
    },
    'en': {
        'open_settings_error': 'Failed to open settings: {error}',
        'templates': 'Templates',
        'link_open_error': 'Error opening link: {error}',
        'checking_version': 'Checking version...',
        'current_version': 'You have the latest version: {version}',
        'parse_version_error': 'Failed to parse version',
        'version_format_error': 'Invalid version info format',
        'version_not_found': 'Version info not found',
        'version_check_error': 'An error occurred during version check!',
        'update_available': 'Update available: {version}',
        'update_question': 'Do you want to update the plugin?',
        'update': 'Update',
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
        'yes': 'Yes',
        'no': 'No',
        'settings': 'Settings',
        'drawer_menu': 'Drawer menu icon',
        'drawer_menu_sub': 'Adds a template settings button to the drawer menu.',
        'chat_menu': 'Chat menu icon',
        'chat_menu_sub': 'Adds a template settings button to the chat menu.',
        'send_cmd': 'Template send command',
        'send_cmd_sub': 'Enter the command to send templates:',
        'template_n': 'Template #{n}',
        'disable_template': 'Disable template',
        'enable_template': 'Enable template',
        'template_name': 'Template name',
        'template_name_sub': 'Come up with a template name.',
        'template_text': 'Template text',
        'template_text_sub': 'Come up with template text.',
        'send_template': 'Send template',
        'contacts': 'My contacts',
        'channel': 'My channel — @I_am_Vestr',
        'personal': 'My DM — @mr_Vestr',
        'other': 'Other',
        'plugin_version': 'Plugin version — 1.0',
        'reset_templates_btn': 'Reset templates',
        'edit_template': 'Edit template {n}',
        'save': 'Save',
        'cancel': 'Cancel',
        'enter_template_name': 'To send a template, enter its name.',
        'template_sent': 'Template "{name}" sent!',
        'template_not_found': 'Template not found! Add templates in plugin settings.',
        'fill_all_fields': 'Fill in all fields to send a template!',
        'checking_updates': 'Checking for updates...',
        'plugin_up_to_date': 'You have the latest plugin version!',
        'update_check_error': 'Error checking for updates!',
        'update_plugin': 'Plugin update...',
        'plugin_updated': 'Plugin updated successfully!',
        'close_menu_question': 'Do you want to close the menu?',
        'error_occurred': 'An error occurred!',
        'templates_title': 'Templates',
        'support_me': 'Support me',
        'support_me_text': 'If you want to support me, you can send me a gift in Telegram or gift me Telegram Premium :)',
        'my_account': 'My account',
        'restart_error': 'Restart error: {error}',
        'download_error': 'Download error: {error}',
        'error_occurred_with_reason': 'Error: {error}',
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

class TemplatesPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.update_info_cache = None
        self.last_update_check = 0
        self._background_update_checker_running = True
        self._last_auto_update_time = 0
        try:
            from org.telegram.messenger import LocaleController
            lang_code = LocaleController.getInstance().getCurrentLocale().getLanguage()
        except Exception:
            lang_code = ''
        if lang_code.lower().startswith('en'):
            self.lang = 'en'
        else:
            self.lang = 'ru'
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
        self._background_update_checker_running = True
        self._update_drawer_menu()
        self._update_chat_menu()
        self.add_on_send_message_hook()
        self._add_url_hook()
        import threading
        def background_update_checker():
            import time
            while self._background_update_checker_running:
                try:
                    self.background_update_check()
                except Exception:
                    pass
                time.sleep(300)
        def delayed_start():
            import time
            time.sleep(10)
            threading.Thread(target=background_update_checker, daemon=True).start()
        threading.Thread(target=delayed_start, daemon=True).start()

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
        show_chat = self.get_setting('show_chat_menu', False)
        self.remove_menu_item('templates_chat')
        if show_chat:
            self.add_menu_item(MenuItemData(
                menu_type=MenuItemType.CHAT_ACTION_MENU,
                text=t('templates', lang=self.lang),
                icon='msg_info',
                item_id='templates_chat',
                on_click=lambda ctx: self.open_plugin_settings()
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

    def _show_version_info(self, _):
        from ui.bulletin import BulletinHelper
        from android_utils import run_on_ui_thread
        import urllib.request
        import re
        def check_version():
            try:
                run_on_ui_thread(lambda: BulletinHelper.show_info(t('checking_version', lang=self.lang)))
                url = "https://telegra.ph/Versions-07-04-3"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req)
                html_content = response.read().decode('utf-8')
                pattern = r'<meta property="og:description" content="([^"]+)">'
                match = re.search(pattern, html_content)
                if match:
                    version_info = match.group(1)
                    parts = version_info.split(' | ')
                    if len(parts) >= 2:
                        version_text = parts[0]
                        download_url = parts[1]
                        version_match = re.search(r'Templates:\s*(\d+\.\d+)', version_text)
                        if version_match:
                            online_version = version_match.group(1)
                            current_version = "1.0"
                            if self._compare_versions(online_version, current_version) > 0:
                                self._try_check_updates()
                            else:
                                run_on_ui_thread(lambda: BulletinHelper.show_success(t('current_version', lang=self.lang, version=current_version)))
                        else:
                            run_on_ui_thread(lambda: BulletinHelper.show_error(t('parse_version_error', lang=self.lang)))
                    else:
                        run_on_ui_thread(lambda: BulletinHelper.show_error(t('version_format_error', lang=self.lang)))
                else:
                    run_on_ui_thread(lambda: BulletinHelper.show_error(t('version_not_found', lang=self.lang)))
            except Exception as e:
                run_on_ui_thread(lambda: BulletinHelper.show_error(t('version_check_error', lang=self.lang)))
        import threading
        thread = threading.Thread(target=check_version)
        thread.start()

    def _compare_versions(self, version1, version2):
        v1_parts = [int(x) for x in version1.split('.')]
        v2_parts = [int(x) for x in version2.split('.')]
        max_len = max(len(v1_parts), len(v2_parts))
        v1_parts.extend([0] * (max_len - len(v1_parts)))
        v2_parts.extend([0] * (max_len - len(v2_parts)))
        for i in range(max_len):
            if v1_parts[i] > v2_parts[i]:
                return 1
            elif v1_parts[i] < v2_parts[i]:
                return -1
        return 0

    def _get_update_info(self):
        import time
        import urllib.request
        import re
        current_time = time.time()
        if (self.update_info_cache and 
            current_time - self.last_update_check < 3600):
            return self.update_info_cache
        try:
            url = "https://telegra.ph/Versions-07-04-3"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=5)
            html_content = response.read().decode('utf-8')
            pattern = r'<meta property="og:description" content="([^"]+)">'
            match = re.search(pattern, html_content)
            if match:
                version_info = match.group(1)
                parts = version_info.split(' | ')
                if len(parts) >= 2:
                    version_text = parts[0]
                    download_url = parts[1]
                    version_match = re.search(r'Templates:\s*(\d+\.\d+)', version_text)
                    if version_match:
                        online_version = version_match.group(1)
                        current_version = "1.0"
                        if self._compare_versions(online_version, current_version) > 0:
                            update_info = {
                                "version": online_version,
                                "url": download_url
                            }
                            return update_info
        except Exception:
            pass
        return None

    def _try_check_updates(self, show_dialog=True):
        global _update_check_in_progress
        if _update_check_in_progress:
            return
        _update_check_in_progress = True
        import threading
        import time
        def check_and_show():
            try:
                time.sleep(2)
                update_info = self._get_update_info()
                if update_info:
                    self.update_info_cache = update_info
                    self.last_update_check = time.time()
                    if show_dialog:
                        from android_utils import run_on_ui_thread
                        run_on_ui_thread(lambda: self._show_update_dialog(update_info["version"], update_info["url"]))
            except Exception as e:
                pass
            finally:
                global _update_check_in_progress
                _update_check_in_progress = False
        thread = threading.Thread(target=check_and_show)
        thread.start()

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

    def _open_update_link(self, url):
        from client_utils import get_last_fragment
        from org.telegram.messenger.browser import Browser
        from android.net import Uri
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if act:
            try:
                uri = Uri.parse(url)
                Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
            except Exception as e:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('link_open_error', lang=self.lang, error=str(e)))

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

    def _show_update_progress_sheet(self, url):
        from org.telegram.ui.ActionBar import BottomSheet
        from org.telegram.ui.Components import LayoutHelper, LineProgressView
        from android.widget import LinearLayout, TextView
        from android.view import Gravity
        from android.util import TypedValue
        from org.telegram.ui.ActionBar import Theme
        from org.telegram.messenger import AndroidUtilities
        from android_utils import run_on_ui_thread
        from com.exteragram.messenger.plugins import PluginsController
        from com.exteragram.messenger.plugins.ui import PluginSettingsActivity
        import threading
        import urllib.request
        import os
        import tempfile
        from client_utils import get_last_fragment
        ui_refs = {}
        def show_sheet():
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
            from org.telegram.ui.Components import BackupImageView
            from client_utils import get_media_data_controller
            iconView = BackupImageView(act)
            iconView.setRoundRadius(AndroidUtilities.dp(12))
            iconView.getImageReceiver().setAutoRepeat(1)
            iconView.getImageReceiver().setAutoRepeatCount(1)
            get_media_data_controller().setPlaceholderImageByIndex(iconView, "UtyaDuck", 16, "200_200")
            linearLayout.addView(iconView, LayoutHelper.createLinear(96, 96, Gravity.CENTER_HORIZONTAL, 0, 28, 0, 0))
            superTitleTextView = TextView(act)
            superTitleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray3))
            superTitleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 18)
            superTitleTextView.setGravity(Gravity.CENTER)
            superTitleTextView.setText(t('templates_title', lang=self.lang))
            linearLayout.addView(superTitleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 8, 0, 4))
            titleTextView = TextView(act)
            titleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            titleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 22)
            titleTextView.setGravity(Gravity.CENTER)
            titleTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
            titleTextView.setText(t('update_plugin', lang=self.lang))
            linearLayout.addView(titleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 0, 0, 8))
            progressView = LineProgressView(act)
            progressView.setProgressColor(Theme.getColor(Theme.key_dialogLineProgress))
            progressView.setProgress(0, True)
            linearLayout.addView(progressView, LayoutHelper.createFrame(-1, 4, Gravity.TOP, 26, 8, 26, 0))
            sheet = builder.show()
            ui_refs['sheet'] = sheet
            ui_refs['progressView'] = progressView
            ui_refs['titleTextView'] = titleTextView
            ui_refs['linearLayout'] = linearLayout
            ui_refs['act'] = act
            ui_refs['frag'] = frag
            ui_refs['iconView'] = iconView
        run_on_ui_thread(show_sheet)
        def set_progress(val, text):
            def _():
                if 'progressView' in ui_refs:
                    ui_refs['progressView'].setProgress(val, True)
            run_on_ui_thread(_)
        def finish_success():
            def _():
                if 'progressView' in ui_refs:
                    ui_refs['progressView'].setProgress(1, True)
                if 'titleTextView' in ui_refs:
                    ui_refs['titleTextView'].setText(t('plugin_updated', lang=self.lang))
                if 'iconView' in ui_refs:
                    from client_utils import get_media_data_controller
                    get_media_data_controller().setPlaceholderImageByIndex(ui_refs['iconView'], "mr_vestr", 5, "200_200")
                act = ui_refs.get('act')
                linearLayout = ui_refs.get('linearLayout')
                sheet = ui_refs.get('sheet')
                frag = ui_refs.get('frag')
                def close_and_open_settings(v=None):
                    from com.exteragram.messenger.plugins import PluginsController
                    from com.exteragram.messenger.plugins.ui import PluginSettingsActivity
                    plugin = PluginsController.getInstance().plugins.get(self.id)
                    if plugin and frag:
                        run_on_ui_thread(lambda: frag.presentFragment(PluginSettingsActivity(plugin)))
                    run_on_ui_thread(sheet.dismiss)
                if linearLayout is not None:
                    count = linearLayout.getChildCount()
                    if count >= 2:
                        last1 = linearLayout.getChildAt(count-1)
                        last2 = linearLayout.getChildAt(count-2)
                        if hasattr(last1, 'getText') and hasattr(last2, 'getText'):
                            if (str(last1.getText()) == t('close', lang=self.lang) or str(last2.getText()) == t('close', lang=self.lang)):
                                linearLayout.removeViewAt(count-1)
                                linearLayout.removeViewAt(count-2)
                subtitleTextView = TextView(act)
                subtitleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray3))
                subtitleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
                subtitleTextView.setGravity(Gravity.CENTER)
                subtitleTextView.setText(t('close_menu_question', lang=self.lang))
                linearLayout.addView(subtitleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 0, 0, 16))
                btn2 = TextView(act)
                btn2.setText(t('close', lang=self.lang))
                btn2.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
                btn2.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
                btn2.setGravity(Gravity.CENTER)
                btn2.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                    AndroidUtilities.dp(6),
                    Theme.getColor(Theme.key_featuredStickers_addButton),
                    Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
                ))
                btn2.setClickable(True)
                btn2.setOnClickListener(OnClickListener(close_and_open_settings))
                linearLayout.addView(btn2, LayoutHelper.createFrame(-1, 48, Gravity.TOP, 50, 8, 50, 16))
            run_on_ui_thread(_)
        def finish_error(error_text):
            def _():
                if 'progressView' in ui_refs:
                    ui_refs['progressView'].setProgress(1, True)
                if 'titleTextView' in ui_refs:
                    ui_refs['titleTextView'].setText(t('error_occurred', lang=self.lang))
                if 'iconView' in ui_refs:
                    from client_utils import get_media_data_controller
                    get_media_data_controller().setPlaceholderImageByIndex(ui_refs['iconView'], "mr_vestr", 6, "200_200")
                act = ui_refs.get('act')
                linearLayout = ui_refs.get('linearLayout')
                sheet = ui_refs.get('sheet')
                frag = ui_refs.get('frag')
                def close_and_open_settings(v=None):
                    from com.exteragram.messenger.plugins import PluginsController
                    from com.exteragram.messenger.plugins.ui import PluginSettingsActivity
                    plugin = PluginsController.getInstance().plugins.get(self.id)
                    if plugin and frag:
                        run_on_ui_thread(lambda: frag.presentFragment(PluginSettingsActivity(plugin)))
                    run_on_ui_thread(sheet.dismiss)
                subtitleTextView = TextView(act)
                subtitleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray3))
                subtitleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
                subtitleTextView.setGravity(Gravity.CENTER)
                subtitleTextView.setText(str(error_text))
                linearLayout.addView(subtitleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 0, 0, 16))
                btn2 = TextView(act)
                btn2.setText(t('close', lang=self.lang))
                btn2.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
                btn2.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
                btn2.setGravity(Gravity.CENTER)
                btn2.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                    AndroidUtilities.dp(6),
                    Theme.getColor(Theme.key_featuredStickers_addButton),
                    Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
                ))
                btn2.setClickable(True)
                btn2.setOnClickListener(OnClickListener(close_and_open_settings))
                linearLayout.addView(btn2, LayoutHelper.createFrame(-1, 48, Gravity.TOP, 50, 8, 50, 16))
            run_on_ui_thread(_)
        def download_and_update():
            temp_path = None
            try:
                if url.strip().lower().startswith('https://t.me'):
                    def open_in_browser_and_close():
                        act = ui_refs.get('act')
                        sheet = ui_refs.get('sheet')
                        from org.telegram.messenger.browser import Browser
                        from android.net import Uri
                        if act:
                            uri = Uri.parse(url)
                            Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
                        if sheet:
                            sheet.dismiss()
                    run_on_ui_thread(open_in_browser_and_close)
                    return
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req, timeout=15)
                data = response.read()
                tempdir = tempfile.gettempdir()
                temp_path = os.path.join(tempdir, f"{self.id}_update.plugin")
                with open(temp_path, "wb") as f:
                    f.write(data)
                def after_load(error):
                    try:
                        if error:
                            finish_error(t('download_error', lang=self.lang, error=str(error)))
                        else:
                            finish_success()
                    finally:
                        try:
                            if temp_path and os.path.exists(temp_path):
                                os.remove(temp_path)
                        except: pass
                PluginsController.getInstance().loadPluginFromFile(temp_path, Callback(after_load))
            except Exception as e:
                finish_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))
                try:
                    if temp_path and os.path.exists(temp_path):
                        os.remove(temp_path)
                except: pass
        threading.Thread(target=download_and_update, daemon=True).start()

    def _download_and_replace_plugin(self, url, builder=None):
        self._show_update_progress_sheet(url)

    def _show_update_dialog(self, online_version, download_url):
        from org.telegram.ui.ActionBar import BottomSheet
        from org.telegram.ui.Components import LayoutHelper
        from android.widget import LinearLayout, TextView
        from android.view import Gravity
        from android.util import TypedValue
        from org.telegram.ui.ActionBar import Theme
        from org.telegram.messenger import AndroidUtilities
        from android_utils import OnClickListener
        from client_utils import get_last_fragment
        from android.content import Intent
        from android.net import Uri
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
        from org.telegram.ui.Components import BackupImageView
        iconView = BackupImageView(act)
        iconView.setRoundRadius(AndroidUtilities.dp(12))
        iconView.getImageReceiver().setAutoRepeat(1)
        iconView.getImageReceiver().setAutoRepeatCount(1)
        from client_utils import get_media_data_controller
        get_media_data_controller().setPlaceholderImageByIndex(iconView, "mr_vestr", 1, "200_200")
        linearLayout.addView(iconView, LayoutHelper.createLinear(96, 96, Gravity.CENTER_HORIZONTAL, 0, 28, 0, 0))
        superTitleTextView = TextView(act)
        superTitleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray3))
        superTitleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 18)
        superTitleTextView.setGravity(Gravity.CENTER)
        superTitleTextView.setText(t('templates_title', lang=self.lang))
        linearLayout.addView(superTitleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 8, 0, 4))
        titleTextView = TextView(act)
        titleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        titleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 22)
        titleTextView.setGravity(Gravity.CENTER)
        titleTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
        titleTextView.setText(t('update_available', lang=self.lang, version=online_version))
        linearLayout.addView(titleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 0, 0, 8))
        subtitleTextView = TextView(act)
        subtitleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray3))
        subtitleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        subtitleTextView.setGravity(Gravity.CENTER)
        subtitleTextView.setText(t('update_question', lang=self.lang))
        linearLayout.addView(subtitleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 0, 0, 16))
        updateBtn = TextView(act)
        updateBtn.setText(t('update', lang=self.lang))
        updateBtn.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        updateBtn.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
        updateBtn.setGravity(Gravity.CENTER)
        updateBtn.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(6),
            Theme.getColor(Theme.key_featuredStickers_addButton),
            Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        ))
        updateBtn.setClickable(True)
        updateBtn.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        def on_update_click(v=None):
            try:
                builder.getDismissRunnable().run()
                self._download_and_replace_plugin(download_url, builder)
            except Exception as e:
                from ui.bulletin import BulletinHelper
                BulletinHelper.show_error(t('link_open_error', lang=self.lang, error=str(e)))
        updateBtn.setOnClickListener(OnClickListener(on_update_click))
        linearLayout.addView(updateBtn, LayoutHelper.createFrame(-1, 48, (Gravity.RIGHT if False else Gravity.LEFT) | Gravity.TOP, 50, 8, 50, 8))
        builder.show()

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

    def _show_reset_templates_dialog(self, _):
        from ui.alert import AlertDialogBuilder
        from client_utils import get_last_fragment
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        builder = AlertDialogBuilder(act)
        builder.set_title(t('reset_templates', lang=self.lang))
        def on_yes(b, w):
            self._reset_templates()
            b.dismiss()
        builder.set_positive_button(t('yes', lang=self.lang), on_yes)
        builder.set_negative_button(t('no', lang=self.lang), lambda b, w: b.dismiss())
        builder.show()

    def _reset_templates(self):
        templates = []
        for i in range(TEMPLATE_COUNT):
            tpl = {}
            tpl['enabled'] = True if i == 0 else False
            tpl['name'] = ''
            tpl['text'] = ''
            templates.append(tpl)
            self.set_setting(f'template_enabled_{i}', tpl['enabled'])
            self.set_setting(f'template_name_{i}', tpl['name'])
            self.set_setting(f'template_text_{i}', tpl['text'])
        self.templates = templates
        self.set_setting('templates', templates)

    def create_settings(self):
        self.templates = []
        for i in range(TEMPLATE_COUNT):
            enabled = self.get_setting(f"template_enabled_{i}", True if i == 0 else False)
            name = self.get_setting(f"template_name_{i}", "")
            text = self.get_setting(f"template_text_{i}", "")
            self.templates.append({
                "enabled": enabled,
                "name": name,
                "text": text
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
            default=self.get_setting('show_chat_menu', False),
            subtext=t('chat_menu_sub', lang=self.lang),
            on_change=self._on_chat_switch
        ))
        settings.append(Input(
            key='send_cmd',
            text=t('send_cmd', lang=self.lang),
            default=self.get_setting('send_cmd', '//'),
            subtext=t('send_cmd_sub', lang=self.lang)
        ))
        first_template = True
        for i in range(TEMPLATE_COUNT):
            if i == 0 or self.templates[i-1].get('enabled', False):
                tpl = self.templates[i] if i < len(self.templates) else {}
                enabled = True if i == 0 else tpl.get('enabled', False)
                name = tpl.get("name", "")
                text = tpl.get("text", "")
                if first_template:
                    settings.append(Divider())
                    settings.append(Divider())
                    first_template = False
                settings.append(Header(text=t('template_n', lang=self.lang, n=i+1)))
                if i == 0:
                    pass
                else:
                    switch_text = t('disable_template', lang=self.lang) if enabled else t('enable_template', lang=self.lang)
                    settings.append(Switch(
                        key=f"template_enabled_{i}",
                        text=switch_text,
                        default=enabled,
                        on_change=self._make_enabled_onchange(i)
                    ))
                    if not enabled:
                        settings.append(Divider())
                        continue
                if enabled:
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
                    settings.append(Divider())
                else:
                    settings.append(Divider())
            else:
                break
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
            on_click=lambda ctx: self.check_updates_with_loader()
        ))
        settings.append(Text(
            text=t('reset_templates_btn', lang=self.lang),
            icon='msg_delete',
            red=True,
            on_click=self._show_reset_templates_dialog
        ))
        settings.append(Divider())
        return settings

    def _on_drawer_switch(self, val):
        self.set_setting('show_drawer_menu', bool(val))
        run_on_ui_thread(self._update_drawer_menu)

    def _on_chat_switch(self, val):
        self.set_setting('show_chat_menu', bool(val))
        run_on_ui_thread(self._update_chat_menu)

    def _make_enabled_onchange(self, idx):
        def handler(val):
            tpl = self.templates[idx] if idx < len(self.templates) else {}
            tpl = tpl.copy()
            tpl['enabled'] = bool(val)
            self.templates[idx] = tpl
            self.set_setting("templates", self.templates)
        return handler

    def _make_onchange(self, idx, field):
        def handler(val):
            val = val.strip()
            tpl = self.templates[idx] if idx < len(self.templates) else {}
            tpl = tpl.copy()
            tpl[field] = val
            self.templates[idx] = tpl
            self.set_setting("templates", self.templates)
        return handler

    def _make_link_onclick(self):
        return lambda ctx: run_on_ui_thread(self.open_mr_vestr_link)

    def save_template(self, idx, val):
        val = val.strip()
        if ":" in val:
            name, text = map(str.strip, val.split(":", 1))
        else:
            name, text = val, ""
        self.templates[idx] = {"name": name, "text": text}
        self.set_setting("templates", self.templates)

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
        from ui.settings import Input
        from client_utils import get_last_fragment
        fragment = get_last_fragment()
        activity = fragment and fragment.getParentActivity()
        if not activity:
            return
        builder = AlertDialogBuilder(activity)
        builder.set_title(t('edit_template', lang=self.lang, n=idx+1))
        input_name = Input(activity)
        input_name.setText(self.templates[idx].get("name", ""))
        input_name.setHint(t('template_name', lang=self.lang))
        input_text = Input(activity)
        input_text.setText(self.templates[idx].get("text", ""))
        input_text.setHint(t('template_text', lang=self.lang))
        from android.widget import LinearLayout
        layout = LinearLayout(activity)
        layout.setOrientation(LinearLayout.VERTICAL)
        layout.addView(input_name)
        layout.addView(input_text)
        builder.set_view(layout)
        def on_done(b, w):
            name = input_name.getText().strip()
            text = input_text.getText().strip()
            self.templates[idx] = {"name": name, "text": text}
            self.set_setting("templates", self.templates)
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
                run_on_ui_thread(self.open_plugin_settings)
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
                        run_on_ui_thread(lambda: BulletinHelper.show_success(t('template_sent', lang=self.lang, name=name)))
                        return HookResult(strategy=HookStrategy.MODIFY, params=params)
            run_on_ui_thread(lambda: BulletinHelper.show_error(t('template_not_found', lang=self.lang)))
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
            run_on_ui_thread(lambda: BulletinHelper.show_success(t('template_sent', lang=self.lang, name=name)))
        delegate = TemplateDialogsDelegate(after_select)
        activity.setDelegate(delegate)
        last_fragment = LaunchActivity.getLastFragment()
        if last_fragment:
            last_fragment.presentFragment(activity)

    def check_updates_with_loader(self):
        from ui.bulletin import BulletinHelper
        from android_utils import run_on_ui_thread
        import threading
        def check():
            try:
                run_on_ui_thread(lambda: BulletinHelper.show_info(t('checking_updates', lang=self.lang)))
                update_info = self._get_update_info()
                if update_info:
                    run_on_ui_thread(lambda: self._show_update_dialog(update_info["version"], update_info["url"]))
                else:
                    run_on_ui_thread(lambda: BulletinHelper.show_success(t('plugin_up_to_date', lang=self.lang)))
            except Exception as e:
                run_on_ui_thread(lambda: BulletinHelper.show_error(t('update_check_error', lang=self.lang)))
        threading.Thread(target=check).start() 

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

    def background_update_check(self):
        import urllib.request
        import re
        import time
        def check():
            try:
                now = time.time()
                if hasattr(self, '_last_auto_update_time') and now - self._last_auto_update_time < 60:
                    return
                url = "https://telegra.ph/Versions-07-04-3"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req, timeout=5)
                html_content = response.read().decode('utf-8')
                pattern = r'<meta property=\"og:description\" content=\"([^\"]+)\">'
                match = re.search(pattern, html_content)
                if match:
                    version_info = match.group(1)
                    parts = version_info.split(' | ')
                    if len(parts) >= 2:
                        version_text = parts[0]
                        download_url = parts[1]
                        version_match = re.search(r'Templates:\s*(\d+\.\d+)', version_text)
                        if version_match:
                            online_version = version_match.group(1)
                            current_version = "1.0"
                            if self._compare_versions(online_version, current_version) > 0:
                                self._last_auto_update_time = now
                                self._background_download_and_apply_update(download_url)
                                return
            except Exception:
                self._last_auto_update_time = time.time()
        check() 

    def _background_download_and_apply_update(self, url):
        from com.exteragram.messenger.plugins import PluginsController
        import urllib.request
        import tempfile
        import os
        import time
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
        temp_path = None
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=15)
            data = response.read()
            tempdir = tempfile.gettempdir()
            temp_path = os.path.join(tempdir, f"{self.id}_auto_update.plugin")
            with open(temp_path, "wb") as f:
                f.write(data)
            def after_load(error):
                try:
                    self._background_update_checker_running = False
                    self._last_auto_update_time = time.time()
                finally:
                    try:
                        if temp_path and os.path.exists(temp_path):
                            os.remove(temp_path)
                    except: pass
            PluginsController.getInstance().loadPluginFromFile(temp_path, Callback(after_load))
        except Exception as e:
            self._last_auto_update_time = time.time()
            try:
                if temp_path and os.path.exists(temp_path):
                    os.remove(temp_path)
            except: pass 

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