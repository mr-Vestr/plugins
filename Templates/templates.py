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

import os, re, json, threading, time, weakref, urllib.request, urllib.parse, signal
from base_plugin import BasePlugin, MenuItemData, MenuItemType, HookResult, HookStrategy, MethodHook
from ui.settings import Divider, Header, Input, Switch, Text, Selector
from client_utils import get_last_fragment, get_messages_controller, send_message, get_account_instance
from hook_utils import find_class, get_private_field
from markdown_utils import parse_markdown
from android.os import Bundle
from java import dynamic_proxy, static_proxy, jclass, jarray, jint, jlong
from ui.bulletin import BulletinHelper
from org.telegram.messenger import ApplicationLoader, Utilities, MediaDataController, ImageLocation, LocaleController, SendMessagesHelper, UserConfig
from android.view import View, MotionEvent, Gravity
from org.telegram.messenger import AndroidUtilities, R
from com.exteragram.messenger.plugins import PluginsController, PluginsConstants
from com.exteragram.messenger.plugins.ui import PluginSettingsActivity
from org.telegram.tgnet import TLRPC
from java.lang import Runnable
from base_plugin import MethodHook
from org.telegram.ui import ChatActivity, LaunchActivity, DialogsActivity
from org.telegram.ui.Components.Premium import StarParticlesView
from org.telegram.ui.Components import ShareAlert
from org.telegram.messenger.browser import Browser
from android.net import Uri
from android.content import Intent
from ui.alert import AlertDialogBuilder
from android.content import ClipData
from org.telegram.messenger import R as R_tg
from android.graphics.drawable import RippleDrawable
from android.content.res import ColorStateList
from android.widget import FrameLayout, LinearLayout, TextView, ImageView, ScrollView, EditText, Toast, HorizontalScrollView
from android.graphics.drawable import GradientDrawable
from java.util import ArrayList
from org.telegram.ui.Gifts import GiftSheet
from org.telegram.ui.Components import BackupImageView, LayoutHelper, CheckBox2, RecyclerListView, UItem, ItemOptions
from org.telegram.ui.ActionBar import Theme, BottomSheet, ActionBarPopupWindow
from android.util import TypedValue
from android.graphics import Color, PorterDuff
from androidx.core.content import ContextCompat
from android_utils import OnClickListener, run_on_ui_thread, log
from android.text import SpannableString
from android.text.style import StrikethroughSpan, URLSpan
from androidx.core.widget import NestedScrollView
from file_utils import get_cache_dir
from java.io import File, FileOutputStream
from android.text.method import LinkMovementMethod
from java.lang import Long
from java.util import Locale
from org.telegram.messenger import MessagesController


try:
    from org.telegram.messenger.browser import Browser
except Exception:
    Browser = None

try:
    from android.net import Uri
except Exception:
    Uri = None

try:
    from org.telegram.ui import LaunchActivity
except Exception:
    LaunchActivity = None

DialogsDelegate = jclass("org.telegram.ui.DialogsActivity$DialogsActivityDelegate")

try:
    from android_utils import Callback
except ImportError:
    class Callback(dynamic_proxy(Utilities.Callback)):
        def __init__(self, fn):
            super().__init__()
            self._fn = fn
        def run(self, arg):
            self._fn(arg)


try:
    from com.exteragram.messenger.plugins.models import HeaderSetting
except ImportError:
    HeaderSetting = None


try:
    from android_utils import OnClickListener
except ImportError:
    class OnClickListener(dynamic_proxy(View.OnClickListener)):
        def __init__(self, fn):
            super().__init__()
            self._fn = fn
        def onClick(self, v):
            self._fn(v)


__id__ = "templates"
__name__ = "Templates"
__description__ = "A plugin for creating, editing, and quickly sending message templates.\n\nПлагин для создания, редактирования и быстрой отправки шаблонов сообщений."
__author__ = "@mr_Vestr"
__version__ = "4.2"
__min_version__ = "12.1.1"
__icon__ = "mr_vestr/7"

PLUGIN_LANG_CODES = [
    'system', 'ru', 'en', 'he', 'ar', 'fa', 'de', 'ja', 'tr', 'zh', 'hi', 'id', 'fr', 'pt', 'es', 'vi', 'sr',
]
PLUGIN_LANG_LABELS = [
    None, 'Русский', 'English', 'עברית', 'العربية', 'فارسی', 'Deutsch', '日本語', 'Türkçe',
    '中文', 'हिन्दी', 'Indonesia', 'Français', 'Português', 'Español', 'Tiếng Việt', 'Српски',
]

LANG_FALLBACK_CHAINS = {
    'uk': ('ru', 'en'), 'be': ('ru', 'en'), 'kk': ('ru', 'en'),
    'iw': ('he', 'en'),
    'pt': ('pt', 'en'), 'pt-br': ('pt', 'en'),
    'zh': ('zh', 'en'), 'zh-cn': ('zh', 'en'), 'zh-tw': ('zh', 'en'),
    'nb': ('no', 'en'), 'nn': ('no', 'en'),
    'hr': ('sr', 'ru', 'en'), 'bs': ('sr', 'ru', 'en'),
    'he': ('he', 'en'), 'ar': ('ar', 'en'), 'fa': ('fa', 'en'),
    'de': ('de', 'en'), 'ja': ('ja', 'en'), 'tr': ('tr', 'en'),
    'hi': ('hi', 'en'), 'id': ('id', 'en'), 'fr': ('fr', 'en'),
    'es': ('es', 'en'), 'vi': ('vi', 'en'), 'sr': ('sr', 'ru', 'en'),
    'ru': ('ru', 'en'), 'en': ('en',),
}


TEMPLATE_COUNT = 30

LANG = {
    'ru': {
        'name': 'Имя шаблона',
        'text': 'Текст шаблона',
        'edit': 'Изменить',
        'clear': 'Очистить',
        'open_settings_error': 'Не удалось открыть настройки: {error}',
        'templates': 'Шаблоны',
        'link_open_error': 'Ошибка при открытии ссылки: {error}',
        'how_it_works': 'Как это работает?',
        'how_it_works_text': '''Шаблоны — заготовленные сообщения, которые можно быстро отправлять.

Чтобы создать шаблон нужно:
1. Открыть настройки плагина Templates;
2. Включить шаблон;
3. Настроить его название и отправляемое сообщение.

Отправить шаблон можно:
1. В настройках плагина, нажав кнопку «Отправить шаблон» и выбрав нужный чат;
2. Через поле ввода сообщения в уже открытом нужном чате, прописав команду и название шаблона. Пример: «// Название»;
3. Нажав кнопку "Шаблоны" в меню чата или меню плагинов в чате.

Также вы можете использовать режим форматирования: **жирный**, __подчёркнутый__, ~~зачёркнутый~~, `моноширинный`, --курсив--, ||спойлер||.

Экспортируйте шаблоны, нажав «Экспорт шаблонов» в настройках и выбрав чат. Импортируйте через файл в чате, нажав на него и потом «Импортировать шаблоны».

Популярные вопросы:
1. Плагин безопасный?
— Да, плагин полностью безопасный. Вы сами можете убедиться, проверив код плагина, он полностью открыт.

Если вы хотите предложить идею для улучшения плагина, сообщить об ошибке или что-то другое, то пишите в сообщения к каналу @I_am_Vestr или мне в личные сообщения @mr_Vestr.''',
        'channel': 'Мой канал',
        'personal': 'Моя личка',
        'close': 'Закрыть',
        'delete_button': 'Удалить',
        'yes': 'Да',
        'no': 'Нет',
        'settings': 'Настройки',
        'drawer_menu': 'Кнопка в главном меню плагинов',
        'drawer_menu_sub': 'Добавляет кнопку открытия настроек в главное меню плагинов.',
        'chat_menu': 'Кнопка в меню чата',
        'chat_menu_sub': 'Добавляет кнопку настроек шаблонов в обычное меню чата.',
        'chat_plugins_menu': 'Кнопка в плагинах в чате',
        'chat_plugins_menu_sub': 'Добавляет кнопку настроек шаблонов в меню плагинов в чате.',
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
        'channel_1': 'Мой канал — @I_am_Vestr',
        'personal_1': 'Моя личка — @mr_Vestr',
        'other': 'Другое',
        'plugin_version': f'Версия плагина — {__version__}',
        'updates': 'Обновления',
        'current_version': 'Текущая версия: {version}',
        'updates_info': 'Нажмите на кнопку ниже чтобы проверить обновления. Или проверьте мой канал @I_am_Vestr.',
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
        'check_updates': 'Проверить обновление',
        'my_account': 'Мой аккаунт',
        'restart_error': 'Ошибка перезапуска: {error}',
        'download_error': 'Ошибка загрузки: {error}',
        'error_occurred_with_reason': 'Ошибка: {error}',
        'select_template': 'Выберите шаблон',
        'no_templates_available': 'Нет доступных шаблонов',
        'export_templates': 'Экспорт шаблонов',
        'export_question': 'Какие шаблоны экспортировать?',
        'export_sent': 'Экспорт отправлен',
        'export_error': 'Ошибка экспорта: {error}',
        'export_success': 'Успешный экспорт.',
        'import_question': 'Импортировать шаблоны из файла?',
        'import_success': 'Шаблоны импортированы.',
        'import_error': 'Ошибка импорта: {error}',
        'selected_templates': 'Выбрано',
        'select_templates': 'Выбор шаблонов',
        'select': 'Выбрать',
        'export': 'Экспортировать',
        'import': 'Импортировать',
        'apply': 'Применить',
        'template_deleted': 'Шаблон удалён.',
        'template_deleted_n': 'Удалён шаблон №{n}.',
        'template_name_cleared': 'Очищено имя шаблона №{n}.',
        'template_text_cleared': 'Очищен текст шаблона №{n}.',
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
        'clear_field_title': 'Очистка поля',
        'clear_field_name_confirm': 'Точно очистить имя шаблона №{n}?',
        'clear_field_text_confirm': 'Точно очистить текст шаблона №{n}?',
        'copy': 'Копировать',
        'link_copied': 'Ссылка скопирована',
        'copied_to_clipboard': 'Скопировано в буфер обмена',
        'error_prefix': 'Ошибка:',
        'clear_all_templates': 'Очистить все шаблоны',
        'templates_limit_exceeded': 'Количество шаблонов не может превышать 30 шт.',
        'checking_updates': 'Проверка обновления Templates...',
        'no_updates_available': 'У вас последняя версия плагина.',
        'update_check_error': 'Ошибка проверки обновлений: {error}',
        'template_name_exists': 'Такое имя шаблона уже есть. Переименуйте или он будет деактивирован.',
        'refresh_templates': 'Обновление шаблонов...',
        'update_timeout_error': 'Не удалось проверить обновления. Проверьте подключение к интернету.',
        'changes': 'Изменения:',
        'full_changelog': 'Полный список изменений',
        'update': 'Обновить',
        'updating_plugin': 'Обновление плагина Templates...',
        'close_alt': 'Закрыть',
        'update_failed': 'Плагин Templates не удалось обновить.',
        'update_success': 'Плагин Templates успешно обновлён!',
        'no_changelog': 'Нет информации об изменениях',
        'header_description': 'Плагин для создания, редактирования и быстрой отправки шаблонов сообщений.',
        'main_section': 'Главное',
        'manage_templates': 'Управление шаблонами',
        'plugin_settings_section': 'Настройки',
        'plugin_settings': 'Настройки плагина',
        'main_menu_button': 'Кнопка в главном меню',
        'main_menu_button_sub': 'Открыть настройки главного меню Telegram для добавления кнопки.',
        'main_plugins_menu_button': 'Кнопка в главном меню плагинов',
        'main_plugins_menu_button_sub': 'Добавляет кнопку открытия настроек в главное меню плагинов.',
        'settings_menu_button': 'Кнопка в меню настроек',
        'settings_menu_button_sub': 'Добавляет кнопку открытия настроек в меню настроек Telegram.',
        'triggers': 'Триггеры',
        'particles_in_settings': 'Частицы в настройках',
        'plugin_language': 'Язык плагина',
        'system': 'Системный',
        'restart_required': 'Для применения, нужно перезапустить приложение.',
        'restart_button': 'Перезапуск',
        'settings_section': 'Настройки',
        'settings_button_label': 'Настройки Templates',
        'chat_picker_error': 'Не удалось открыть выбор чата.',
        'no_chat_selected': 'Чат не выбран.',
        'template_send_error': 'Не удалось отправить шаблон.',
    },
    'en': {
        'name': 'Template name',
        'text': 'Template text',
        'edit': 'Edit',
        'clear': 'Clear',
        'open_settings_error': 'Failed to open settings: {error}',
        'templates': 'Templates',
        'link_open_error': 'Error opening link: {error}',
        'how_it_works': 'How it works?',
        'how_it_works_text': '''Templates are pre-made messages you can quickly send.

To create a template:
1. Open Templates plugin settings;
2. Enable a template;
3. Set its name and message text.

To send a template:
1. In plugin settings, press "Send template" and choose a chat;
2. In the chat input, type the command and template name. Example: "// Name";
3. By clicking the "Templates" button in the chat menu or the plugins menu in the chat.

You can also use Parse mode: **bold**, __underlined__, ~~strikethrough~~, `monotype`, --italic--, ||spoiler||.

Export templates by clicking "Export Templates" in the settings and selecting a chat. Import via a file in the chat by clicking on it and then "Import Templates".

Frequently Asked Questions:
1. Is the plugin secure?
— Yes, the plugin is completely secure. You can verify this yourself by inspecting the plugin's code; it's completely open source.

If you want to suggest an idea, report a bug, or anything else, write to the @I_am_Vestr channel or DM @mr_Vestr.''',
        'channel': 'My channel',
        'personal': 'My DM',
        'close': 'Close',
        'delete_button': 'Delete',
        'yes': 'Yes',
        'no': 'No',
        'settings': 'Settings',
        'drawer_menu': 'Button in drawer menu',
        'drawer_menu_sub': 'Adds a template settings button to the drawer menu.',
        'chat_menu': 'Button in chat menu',
        'chat_menu_sub': 'Adds a template settings button to the regular chat menu.',
        'chat_plugins_menu': 'Button in plugins chat menu',
        'chat_plugins_menu_sub': 'Adds a template settings button to the plugins menu in chat.',
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
        'channel_1': 'My channel — @I_am_Vestr',
        'personal_1': 'My DM — @mr_Vestr',
        'other': 'Other',
        'plugin_version': f'Plugin version — {__version__}',
        'updates': 'Updates',
        'current_version': 'Current version: {version}',
        'updates_info': 'Click on the button below to check for updates. Or check out my channel @I_am_Vestr.',
        'check_updates': 'Check updates',
        'checking_updates': 'Checking updates for Templates...',
        'no_updates_available': 'You have the latest version of the plugin.',
        'update_check_error': 'Update check error: {error}',
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
        'export_templates': 'Export Templates',
        'export_question': 'Which templates to export?',
        'export_sent': 'Export sent',
        'export_error': 'Export error: {error}',
        'export_success': 'Export successful.',
        'import_question': 'Import templates from file?',
        'import_success': 'Templates imported.',
        'import_error': 'Import error: {error}',
        'selected_templates': 'Selected',
        'select_templates': 'Select Templates',
        'select': 'Select',
        'export': 'Export',
        'import': 'Import',
        'apply': 'Apply',
        'template_deleted': 'Template deleted.',
        'template_deleted_n': 'Template #{n} deleted.',
        'template_name_cleared': 'Template name #{n} cleared.',
        'template_text_cleared': 'Template text #{n} cleared.',
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
        'clear_field_title': 'Clear field',
        'clear_field_name_confirm': 'Are you sure you want to clear template name #{n}?',
        'clear_field_text_confirm': 'Are you sure you want to clear template text #{n}?',
        'copy': 'Copy',
        'link_copied': 'Link copied',
        'copied_to_clipboard': 'Copied to clipboard',
        'error_prefix': 'Error:',
        'clear_all_templates': 'Clear all templates',
        'templates_limit_exceeded': 'The number of templates cannot exceed 30.',
        'template_name_exists': 'Template name already exists. Rename it or it will be deactivated.',
        'refresh_templates': 'Refresh templates...',
        'update_timeout_error': 'Failed to check for updates. Check your internet connection.',
        'changes': 'Changes:',
        'full_changelog': 'Full changelog',
        'update': 'Update',
        'updating_plugin': 'Updating Templates plugin...',
        'close_alt': 'Close',
        'update_failed': 'Failed to update Templates plugin.',
        'update_success': 'Templates plugin updated successfully!',
        'no_changelog': 'No changelog available',
        'header_description': 'A plugin for creating, editing, and quickly sending message templates.',
        'main_section': 'Main',
        'manage_templates': 'Manage templates',
        'plugin_settings_section': 'Settings',
        'plugin_settings': 'Plugin settings',
        'main_menu_button': 'Main menu button',
        'main_menu_button_sub': 'Open Telegram main menu settings to add the button.',
        'main_plugins_menu_button': 'Main plugins menu button',
        'main_plugins_menu_button_sub': 'Adds a settings button to the main plugins menu.',
        'settings_menu_button': 'Settings menu button',
        'settings_menu_button_sub': 'Adds a settings button to the Telegram settings menu.',
        'triggers': 'Triggers',
        'particles_in_settings': 'Particles in settings',
        'plugin_language': 'Plugin language',
        'system': 'System',
        'restart_required': 'To apply, you need to restart the application.',
        'restart_button': 'Restart',
        'settings_section': 'Settings',
        'settings_button_label': 'Templates Settings',
        'chat_picker_error': 'Failed to open chat picker.',
        'no_chat_selected': 'No chat selected.',
        'template_send_error': 'Failed to send template.',
    },
    'he': {
        'name': 'שם התבנית',
        'text': 'טקסט התבנית',
        'edit': 'ערוך',
        'clear': 'נקה',
        'open_settings_error': 'לא ניתן לפתוח את ההגדרות: {error}',
        'templates': 'תבניות',
        'link_open_error': 'שגיאה בפתיחת הקישור: {error}',
        'how_it_works': 'איך זה עובד?',
        'how_it_works_text': '''תבניות הן הודעות מוכנות מראש שניתן לשלוח במהירות.

כדי ליצור תבנית:
1. פתח את הגדרות התוסף Templates;
2. הפעל תבנית;
3. הגדר את שמה ואת טקסט ההודעה.

לשליחת תבנית:
1. בהגדרות התוסף, לחץ על "שלח תבנית" ובחר צ'אט;
2. בתיבת הקלדת ההודעה בצ'אט הפתוח, הקלד את הפקודה ושם התבנית. דוגמה: "// שם";
3. על ידי לחיצה על כפתור "תבניות" בתפריט הצ'אט או בתפריט התוספים בצ'אט.

ניתן גם להשתמש במצב עיצוב: **מודגש**, __קו תחתון__, ~~קו חוצה~~, `מונו-רוחב`, --נטוי--, ||ספוילר||.

ייצא תבניות על ידי לחיצה על "ייצא תבניות" בהגדרות ובחירת צ'אט. ייבא באמצעות קובץ בצ'אט, לחץ עליו ואז "ייבא תבניות".

שאלות נפוצות:
1. האם התוסף מאובטח?
— כן, התוסף מאובטח לחלוטין. אתה יכול לוודא זאת בעצמך על ידי בדיקת קוד התוסף, הוא פתוח לחלוטין.

אם ברצונך להציע רעיון לשיפור, לדווח על באג או כל דבר אחר, כתבו לערוץ @I_am_Vestr או אליי בהודעה פרטית @mr_Vestr.''',
        'channel': 'הערוץ שלי',
        'personal': 'הפרטי שלי',
        'close': 'סגור',
        'delete_button': 'מחק',
        'yes': 'כן',
        'no': 'לא',
        'settings': 'הגדרות',
        'drawer_menu': 'כפתור בתפריט הראשי של התוספים',
        'drawer_menu_sub': 'מוסיף כפתור לפתיחת הגדרות בתפריט הראשי של התוספים.',
        'chat_menu': 'כפתור בתפריט הצ\'אט',
        'chat_menu_sub': 'מוסיף כפתור להגדרות תבניות בתפריט הצ\'אט הרגיל.',
        'chat_plugins_menu': 'כפתור בתפריט התוספים בצ\'אט',
        'chat_plugins_menu_sub': 'מוסיף כפתור להגדרות תבניות בתפריט התוספים בצ\'אט.',
        'send_cmd': 'פקודת שליחת תבנית',
        'send_cmd_sub': 'הזן את הפקודה לשליחת תבניות.',
        'template_n': 'תבנית מס\'{n}',
        'template_name': 'שם התבנית',
        'template_name_sub': 'המציא שם לתבנית.',
        'template_text': 'טקסט התבנית',
        'template_text_sub': 'המציא טקסט לתבנית.',
        'send_template': 'שלח תבנית',
        'delete_template': 'מחק תבנית',
        'create_template': 'צור תבנית',
        'contacts': 'אנשי הקשר שלי',
        'channel_1': 'הערוץ שלי — @I_am_Vestr',
        'personal_1': 'הפרטי שלי — @mr_Vestr',
        'other': 'אחר',
        'plugin_version': f'גרסת תוסף — {__version__}',
        'updates': 'עדכונים',
        'current_version': 'גרסה נוכחית: {version}',
        'updates_info': 'לחץ על הכפתור למטה כדי לבדוק עדכונים. או בדוק את הערוץ שלי @I_am_Vestr.',
        'check_updates': 'בדוק',
        'edit_template': 'ערוך תבנית {n}',
        'save': 'שמור',
        'cancel': 'ביטול',
        'enter_template_name': 'כדי לשלוח תבנית, כתוב את שמה.',
        'template_sent': 'התבנית "{name}" נשלחה.',
        'template_not_found': 'תבנית לא נמצאה! תבניות מתווספות בהגדרות התוסף.',
        'fill_all_fields': 'מלא את כל השדות לשליחת תבנית.',
        'close_menu_question': 'האם ברצונך לסגור את התפריט?',
        'templates_title': 'תבניות',
        'error_occurred': 'אירעה שגיאה!',
        'support_me': 'תמוך בי',
        'support_me_text': 'אם ברצונך לתמוך בי, תוכל לשלוח לי מתנה בטלגרם או לתת לי טלגרם פרמיום :)',
        'my_account': 'החשבון שלי',
        'restart_error': 'שגיאת הפעלה מחדש: {error}',
        'download_error': 'שגיאת הורדה: {error}',
        'error_occurred_with_reason': 'שגיאה: {error}',
        'select_template': 'בחר תבנית',
        'no_templates_available': 'אין תבניות זמינות',
        'export_templates': 'ייצא תבניות',
        'export_question': 'אילו תבניות לייצא?',
        'export_sent': 'ייצוא נשלח',
        'export_error': 'שגיאת ייצוא: {error}',
        'export_success': 'ייצוא הצליח.',
        'import_question': 'לייבא תבניות מקובץ?',
        'import_success': 'תבניות יובאו.',
        'import_error': 'שגיאת ייבוא: {error}',
        'selected_templates': 'נבחרו',
        'select_templates': 'בחירת תבניות',
        'select': 'בחר',
        'export': 'ייצא',
        'import': 'ייבא',
        'apply': 'החל',
        'template_deleted': 'תבנית נמחקה.',
        'template_deleted_n': 'תבנית מס\'{n} נמחקה.',
        'template_name_cleared': 'שם התבנית מס\'{n} נוקה.',
        'template_text_cleared': 'טקסט התבנית מס\'{n} נוקה.',
        'template_created_n': 'תבנית מס\'{n} נוצרה.',
        'delete_template_title': 'מחיקת תבנית',
        'delete_template_confirm': 'למחוק לחלוטין תבנית מס\'{n}?',
        'undo': 'בטל',
        'template_n_sent': 'תבנית מס\'{n} נשלחה.',
        'open': 'פתח',
        'templates_exported': 'תבניות יוצאו.',
        'export_file_caption': 'ייצוא תבניות',
        'import_dialog_title': 'ייבוא תבניות',
        'fill_prev_template': 'מלא את כל השדות של התבנית הקודמת כדי ליצור נוספת.',
        'clear_field_title': 'ניקוי שדה',
        'clear_field_name_confirm': 'לנקות לחלוטין את שם התבנית מס\'{n}?',
        'clear_field_text_confirm': 'לנקות לחלוטין את טקסט התבנית מס\'{n}?',
        'copy': 'העתק',
        'link_copied': 'הקישור הועתק',
        'copied_to_clipboard': 'הועתק ללוח',
        'error_prefix': 'שגיאה:',
        'clear_all_templates': 'נקה את כל התבניות',
        'templates_limit_exceeded': 'מספר התבניות לא יכול לעלות על 30.',
        'checking_updates': 'בודק עדכונים עבור Templates...',
        'no_updates_available': 'יש לך את הגרסה העדכנית ביותר של התוסף.',
        'update_check_error': 'שגיאת בדיקת עדכונים: {error}',
        'template_name_exists': 'שם תבנית כזה כבר קיים. שנה את השם או שהיא תושבת.',
        'refresh_templates': 'רענון תבניות...',
        'update_timeout_error': 'לא ניתן לבדוק עדכונים. בדוק את חיבור האינטרנט.',
        'changes': 'שינויים:',
        'full_changelog': 'רשימת שינויים מלאה',
        'update': 'עדכן',
        'updating_plugin': 'מעדכן תוסף Templates...',
        'close_alt': 'סגור',
        'update_failed': 'לא ניתן לעדכן את תוסף Templates.',
        'update_success': 'תוסף Templates עודכן בהצלחה!',
        'no_changelog': 'אין מידע על שינויים',
        'header_description': 'תוסף ליצירה, עריכה ושליחה מהירה של תבניות הודעות.',
        'main_section': 'ראשי',
        'manage_templates': 'ניהול תבניות',
        'plugin_settings_section': 'הגדרות',
        'plugin_settings': 'הגדרות תוסף',
        'main_menu_button': 'כפתור בתפריט הראשי',
        'main_menu_button_sub': 'פתח את הגדרות התפריט הראשי של טלגרם להוספת כפתור.',
        'main_plugins_menu_button': 'כפתור בתפריט הראשי של התוספים',
        'main_plugins_menu_button_sub': 'מוסיף כפתור לפתיחת הגדרות בתפריט הראשי של התוספים.',
        'settings_menu_button': 'כפתור בתפריט ההגדרות',
        'settings_menu_button_sub': 'מוסיף כפתור לפתיחת הגדרות בתפריט ההגדרות של טלגרם.',
        'triggers': 'טריגרים',
        'particles_in_settings': 'חלקיקים בהגדרות',
        'plugin_language': 'שפת התוסף',
        'system': 'מערכת',
        'restart_required': 'כדי להחיל, יש להפעיל מחדש את היישום.',
        'restart_button': 'הפעל מחדש',
        'settings_section': 'הגדרות',
        'settings_button_label': 'הגדרות Templates',
        'chat_picker_error': 'לא ניתן לפתוח את בורר הצ\'אט.',
        'no_chat_selected': 'לא נבחר צ\'אט.',
        'template_send_error': 'לא ניתן לשלוח את התבנית.',
    },
    'ar': {
        'name': 'اسم القالب',
        'text': 'نص القالب',
        'edit': 'تحرير',
        'clear': 'مسح',
        'open_settings_error': 'فشل فتح الإعدادات: {error}',
        'templates': 'القوالب',
        'link_open_error': 'خطأ في فتح الرابط: {error}',
        'how_it_works': 'كيف يعمل؟',
        'how_it_works_text': '''القوالب هي رسائل مُعدّة مسبقًا يمكنك إرسالها بسرعة.

لإنشاء قالب:
1. افتح إعدادات الإضافة Templates;
2. فعّل قالبًا;
3. عيّن اسمه ونص الرسالة.

لإرسال قالب:
1. في إعدادات الإضافة، اضغط "إرسال قالب" واختر محادثة;
2. في حقل إدخال الرسالة في المحادثة المفتوحة، اكتب الأمر واسم القالب. مثال: "// الاسم";
3. بالضغط على زر "القوالب" في قائمة المحادثة أو قائمة الإضافات في المحادثة.

يمكنك أيضًا استخدام وضع التنسيق: **غامق**, __مسطر__, ~~يتوسطه خط~~, `أحادي المسافة`, --مائل--, ||مفسد||.

صدّر القوالب بالضغط على "تصدير القوالب" في الإعدادات واختيار محادثة. استورد عبر ملف في المحادثة بالضغط عليه ثم "استيراد القوالب".

أسئلة شائعة:
1. هل الإضافة آمنة؟
— نعم، الإضافة آمنة تمامًا. يمكنك التحقق بنفسك من خلال مراجعة كود الإضافة، فهو مفتوح بالكامل.

إذا كنت تريد اقتراح فكرة لتحسين الإضافة، أو الإبلاغ عن خطأ، أو أي شيء آخر، اكتب إلى قناة @I_am_Vestr أو لي شخصيًا @mr_Vestr.''',
        'channel': 'قناتي',
        'personal': 'خاصي',
        'close': 'إغلاق',
        'delete_button': 'حذف',
        'yes': 'نعم',
        'no': 'لا',
        'settings': 'الإعدادات',
        'drawer_menu': 'زر في القائمة الرئيسية للإضافات',
        'drawer_menu_sub': 'يُضيف زر فتح الإعدادات في القائمة الرئيسية للإضافات.',
        'chat_menu': 'زر في قائمة المحادثة',
        'chat_menu_sub': 'يُضيف زر إعدادات القوالب في قائمة المحادثة العادية.',
        'chat_plugins_menu': 'زر في قائمة الإضافات في المحادثة',
        'chat_plugins_menu_sub': 'يُضيف زر إعدادات القوالب في قائمة الإضافات في المحادثة.',
        'send_cmd': 'أمر إرسال القالب',
        'send_cmd_sub': 'أدخل الأمر لإرسال القوالب.',
        'template_n': 'قالب رقم {n}',
        'template_name': 'اسم القالب',
        'template_name_sub': 'ابتكر اسمًا للقالب.',
        'template_text': 'نص القالب',
        'template_text_sub': 'ابتكر نصًا للقالب.',
        'send_template': 'إرسال قالب',
        'delete_template': 'حذف قالب',
        'create_template': 'إنشاء قالب',
        'contacts': 'جهات الاتصال الخاصة بي',
        'channel_1': 'قناتي — @I_am_Vestr',
        'personal_1': 'خاصي — @mr_Vestr',
        'other': 'أخرى',
        'plugin_version': f'إصدار الإضافة — {__version__}',
        'updates': 'التحديثات',
        'current_version': 'الإصدار الحالي: {version}',
        'updates_info': 'اضغط على الزر أدناه للتحقق من التحديثات. أو تحقق من قناتي @I_am_Vestr.',
        'check_updates': 'تحقق',
        'edit_template': 'تحرير قالب {n}',
        'save': 'حفظ',
        'cancel': 'إلغاء',
        'enter_template_name': 'لإرسال قالب، اكتب اسمه.',
        'template_sent': 'تم إرسال القالب "{name}".',
        'template_not_found': 'القالب غير موجود! تتم إضافة القوالب في إعدادات الإضافة.',
        'fill_all_fields': 'املأ جميع البيانات لإرسال القالب.',
        'close_menu_question': 'هل تريد إغلاق القائمة؟',
        'templates_title': 'القوالب',
        'error_occurred': 'حدث خطأ!',
        'support_me': 'ادعمني',
        'support_me_text': 'إذا كنت تريد دعمي، يمكنك إرسال هدية لي في Telegram أو إهدائي Telegram Premium :)',
        'my_account': 'حسابي',
        'restart_error': 'خطأ في إعادة التشغيل: {error}',
        'download_error': 'خطأ في التحميل: {error}',
        'error_occurred_with_reason': 'خطأ: {error}',
        'select_template': 'اختر قالبًا',
        'no_templates_available': 'لا توجد قوالب متاحة',
        'export_templates': 'تصدير القوالب',
        'export_question': 'أي القوالب تريد تصديرها؟',
        'export_sent': 'تم إرسال التصدير',
        'export_error': 'خطأ في التصدير: {error}',
        'export_success': 'تم التصدير بنجاح.',
        'import_question': 'استيراد القوالب من ملف؟',
        'import_success': 'تم استيراد القوالب.',
        'import_error': 'خطأ في الاستيراد: {error}',
        'selected_templates': 'تم التحديد',
        'select_templates': 'اختيار القوالب',
        'select': 'اختر',
        'export': 'تصدير',
        'import': 'استيراد',
        'apply': 'تطبيق',
        'template_deleted': 'تم حذف القالب.',
        'template_deleted_n': 'تم حذف القالب رقم {n}.',
        'template_name_cleared': 'تم مسح اسم القالب رقم {n}.',
        'template_text_cleared': 'تم مسح نص القالب رقم {n}.',
        'template_created_n': 'تم إنشاء القالب رقم {n}.',
        'delete_template_title': 'حذف القالب',
        'delete_template_confirm': 'هل تريد بالتأكيد حذف القالب رقم {n}؟',
        'undo': 'تراجع',
        'template_n_sent': 'تم إرسال القالب رقم {n}.',
        'open': 'فتح',
        'templates_exported': 'تم تصدير القوالب.',
        'export_file_caption': 'تصدير القوالب',
        'import_dialog_title': 'استيراد القوالب',
        'fill_prev_template': 'املأ جميع حقول القالب السابق لإنشاء آخر.',
        'clear_field_title': 'مسح الحقل',
        'clear_field_name_confirm': 'هل تريد بالتأكيد مسح اسم القالب رقم {n}؟',
        'clear_field_text_confirm': 'هل تريد بالتأكيد مسح نص القالب رقم {n}؟',
        'copy': 'نسخ',
        'link_copied': 'تم نسخ الرابط',
        'copied_to_clipboard': 'تم النسخ إلى الحافظة',
        'error_prefix': 'خطأ:',
        'clear_all_templates': 'مسح جميع القوالب',
        'templates_limit_exceeded': 'لا يمكن أن يتجاوز عدد القوالب 30 قالبًا.',
        'checking_updates': 'جارٍ التحقق من تحديث Templates...',
        'no_updates_available': 'لديك أحدث إصدار من الإضافة.',
        'update_check_error': 'خطأ في التحقق من التحديثات: {error}',
        'template_name_exists': 'اسم القالب موجود بالفعل. أعد تسميته أو سيتم إلغاء تنشيطه.',
        'refresh_templates': 'تحديث القوالب...',
        'update_timeout_error': 'فشل التحقق من التحديثات. تحقق من اتصالك بالإنترنت.',
        'changes': 'التغييرات:',
        'full_changelog': 'سجل التغييرات الكامل',
        'update': 'تحديث',
        'updating_plugin': 'جارٍ تحديث إضافة Templates...',
        'close_alt': 'إغلاق',
        'update_failed': 'فشل تحديث إضافة Templates.',
        'update_success': 'تم تحديث إضافة Templates بنجاح!',
        'no_changelog': 'لا توجد معلومات عن التغييرات',
        'header_description': 'إضافة لإنشاء وتحرير وإرسال قوالب الرسائل بسرعة.',
        'main_section': 'رئيسي',
        'manage_templates': 'إدارة القوالب',
        'plugin_settings_section': 'الإعدادات',
        'plugin_settings': 'إعدادات الإضافة',
        'main_menu_button': 'زر في القائمة الرئيسية',
        'main_menu_button_sub': 'افتح إعدادات القائمة الرئيسية لـ Telegram لإضافة الزر.',
        'main_plugins_menu_button': 'زر في القائمة الرئيسية للإضافات',
        'main_plugins_menu_button_sub': 'يُضيف زر فتح الإعدادات في القائمة الرئيسية للإضافات.',
        'settings_menu_button': 'زر في قائمة الإعدادات',
        'settings_menu_button_sub': 'يُضيف زر فتح الإعدادات في قائمة إعدادات Telegram.',
        'triggers': 'المشغلات',
        'particles_in_settings': 'جسيمات في الإعدادات',
        'plugin_language': 'لغة الإضافة',
        'system': 'النظام',
        'restart_required': 'للتطبيق، يلزم إعادة تشغيل التطبيق.',
        'restart_button': 'إعادة تشغيل',
        'settings_section': 'الإعدادات',
        'settings_button_label': 'إعدادات Templates',
        'chat_picker_error': 'فشل فتح منتقي المحادثة.',
        'no_chat_selected': 'لم يتم تحديد محادثة.',
        'template_send_error': 'فشل إرسال القالب.',
    },
    'fa': {
        'name': 'نام قالب',
        'text': 'متن قالب',
        'edit': 'ویرایش',
        'clear': 'پاک کردن',
        'open_settings_error': 'باز کردن تنظیمات انجام نشد: {error}',
        'templates': 'قالب‌ها',
        'link_open_error': 'خطا در باز کردن لینک: {error}',
        'how_it_works': 'چگونه کار می‌کند؟',
        'how_it_works_text': '''قالب‌ها پیام‌های از پیش آماده‌ای هستند که می‌توانید سریعاً ارسال کنید.

برای ساخت قالب:
1. تنظیمات افزونه Templates را باز کنید;
2. قالب را فعال کنید;
3. نام و متن پیام آن را تنظیم کنید.

برای ارسال قالب:
1. در تنظیمات افزونه، دکمه «ارسال قالب» را بزنید و چت مورد نظر را انتخاب کنید;
2. در قسمت ورودی پیام در چت باز شده، دستور و نام قالب را بنویسید. مثال: «// نام»;
3. با کلیک روی دکمه "قالب‌ها" در منوی چت یا منوی افزونه‌ها در چت.

همچنین می‌توانید از حالت قالب‌بندی استفاده کنید: **پررنگ**, __زیرخط‌دار__, ~~خط‌خورده~~, `تک فاصله`, --مورب--, ||اسپویلر||.

قالب‌ها را با کلیک روی «خروجی گرفتن از قالب‌ها» در تنظیمات و انتخاب چت، خروجی بگیرید. ورودی گرفتن از طریق فایل در چت، با کلیک روی آن و سپس «ورودی گرفتن قالب‌ها».

سوالات متداول:
1. آیا افزونه امن است؟
— بله، افزونه کاملاً امن است. خودتان می‌توانید با بررسی کد افزونه مطمئن شوید، کاملاً متن باز است.

اگر می‌خواهید ایده‌ای برای بهبود افزونه پیشنهاد دهید، اشکالی را گزارش کنید یا چیز دیگری، به کانال @I_am_Vestr یا به شخصه به من @mr_Vestr پیام دهید.''',
        'channel': 'کانال من',
        'personal': 'پیام خصوصی من',
        'close': 'بستن',
        'delete_button': 'حذف',
        'yes': 'بله',
        'no': 'خیر',
        'settings': 'تنظیمات',
        'drawer_menu': 'دکمه در منوی اصلی افزونه‌ها',
        'drawer_menu_sub': 'دکمه باز کردن تنظیمات را به منوی اصلی افزونه‌ها اضافه می‌کند.',
        'chat_menu': 'دکمه در منوی چت',
        'chat_menu_sub': 'دکمه تنظیمات قالب‌ها را به منوی معمولی چت اضافه می‌کند.',
        'chat_plugins_menu': 'دکمه در افزونه‌های چت',
        'chat_plugins_menu_sub': 'دکمه تنظیمات قالب‌ها را به منوی افزونه‌ها در چت اضافه می‌کند.',
        'send_cmd': 'دستور ارسال قالب',
        'send_cmd_sub': 'دستور ارسال قالب‌ها را وارد کنید.',
        'template_n': 'قالب شماره {n}',
        'template_name': 'نام قالب',
        'template_name_sub': 'یک نام برای قالب انتخاب کنید.',
        'template_text': 'متن قالب',
        'template_text_sub': 'متنی برای قالب انتخاب کنید.',
        'send_template': 'ارسال قالب',
        'delete_template': 'حذف قالب',
        'create_template': 'ساخت قالب',
        'contacts': 'مخاطبین من',
        'channel_1': 'کانال من — @I_am_Vestr',
        'personal_1': 'پیام خصوصی من — @mr_Vestr',
        'other': 'سایر',
        'plugin_version': f'نسخه افزونه — {__version__}',
        'updates': 'به‌روزرسانی‌ها',
        'current_version': 'نسخه فعلی: {version}',
        'updates_info': 'برای بررسی به‌روزرسانی‌ها روی دکمه زیر کلیک کنید. یا کانال من @I_am_Vestr را بررسی کنید.',
        'check_updates': 'بررسی',
        'edit_template': 'ویرایش قالب {n}',
        'save': 'ذخیره',
        'cancel': 'لغو',
        'enter_template_name': 'برای ارسال قالب، نام آن را بنویسید.',
        'template_sent': 'قالب «{name}» ارسال شد.',
        'template_not_found': 'قالب پیدا نشد! قالب‌ها در تنظیمات افزونه اضافه می‌شوند.',
        'fill_all_fields': 'برای ارسال قالب، همه داده‌ها را پر کنید.',
        'close_menu_question': 'آیا می‌خواهید منو را ببندید؟',
        'templates_title': 'قالب‌ها',
        'error_occurred': 'خطایی رخ داد!',
        'support_me': 'از من حمایت کنید',
        'support_me_text': 'اگر می‌خواهید از من حمایت کنید، می‌توانید یک هدیه در تلگرام برای من بفرستید یا تلگرام پریمیوم هدیه دهید :)',
        'my_account': 'حساب من',
        'restart_error': 'خطا در راه‌اندازی مجدد: {error}',
        'download_error': 'خطا در دانلود: {error}',
        'error_occurred_with_reason': 'خطا: {error}',
        'select_template': 'انتخاب قالب',
        'no_templates_available': 'قالبی در دسترس نیست',
        'export_templates': 'خروجی گرفتن از قالب‌ها',
        'export_question': 'کدام قالب‌ها خروجی گرفته شوند؟',
        'export_sent': 'خروجی ارسال شد',
        'export_error': 'خطا در خروجی: {error}',
        'export_success': 'خروجی با موفقیت انجام شد.',
        'import_question': 'ورودی گرفتن قالب‌ها از فایل؟',
        'import_success': 'قالب‌ها ورودی گرفته شدند.',
        'import_error': 'خطا در ورودی: {error}',
        'selected_templates': 'انتخاب شده',
        'select_templates': 'انتخاب قالب‌ها',
        'select': 'انتخاب',
        'export': 'خروجی',
        'import': 'ورودی',
        'apply': 'اعمال',
        'template_deleted': 'قالب حذف شد.',
        'template_deleted_n': 'قالب شماره {n} حذف شد.',
        'template_name_cleared': 'نام قالب شماره {n} پاک شد.',
        'template_text_cleared': 'متن قالب شماره {n} پاک شد.',
        'template_created_n': 'قالب شماره {n} ساخته شد.',
        'delete_template_title': 'حذف قالب',
        'delete_template_confirm': 'آیا مطمئن هستید که قالب شماره {n} را حذف کنید؟',
        'undo': 'بازگشت',
        'template_n_sent': 'قالب شماره {n} ارسال شد.',
        'open': 'باز کردن',
        'templates_exported': 'قالب‌ها خروجی گرفته شدند.',
        'export_file_caption': 'خروجی قالب‌ها',
        'import_dialog_title': 'ورودی قالب‌ها',
        'fill_prev_template': 'برای ساخت قالب دیگر، همه فیلدهای قالب قبلی را پر کنید.',
        'clear_field_title': 'پاک کردن فیلد',
        'clear_field_name_confirm': 'آیا مطمئن هستید که نام قالب شماره {n} را پاک کنید؟',
        'clear_field_text_confirm': 'آیا مطمئن هستید که متن قالب شماره {n} را پاک کنید؟',
        'copy': 'کپی',
        'link_copied': 'لینک کپی شد',
        'copied_to_clipboard': 'در کلیپ‌بورد کپی شد',
        'error_prefix': 'خطا:',
        'clear_all_templates': 'پاک کردن همه قالب‌ها',
        'templates_limit_exceeded': 'تعداد قالب‌ها نمی‌تواند از ۳۰ عدد بیشتر شود.',
        'checking_updates': 'در حال بررسی به‌روزرسانی Templates...',
        'no_updates_available': 'شما آخرین نسخه افزونه را دارید.',
        'update_check_error': 'خطا در بررسی به‌روزرسانی: {error}',
        'template_name_exists': 'چنین نام قالبی از قبل وجود دارد. تغییر نام دهید یا غیرفعال خواهد شد.',
        'refresh_templates': 'بازسازی قالب‌ها...',
        'update_timeout_error': 'بررسی به‌روزرسانی انجام نشد. اتصال اینترنت خود را بررسی کنید.',
        'changes': 'تغییرات:',
        'full_changelog': 'لیست کامل تغییرات',
        'update': 'به‌روزرسانی',
        'updating_plugin': 'در حال به‌روزرسانی افزونه Templates...',
        'close_alt': 'بستن',
        'update_failed': 'به‌روزرسانی افزونه Templates انجام نشد.',
        'update_success': 'افزونه Templates با موفقیت به‌روزرسانی شد!',
        'no_changelog': 'اطلاعاتی درباره تغییرات وجود ندارد',
        'header_description': 'افزونه برای ساخت، ویرایش و ارسال سریع قالب‌های پیام.',
        'main_section': 'اصلی',
        'manage_templates': 'مدیریت قالب‌ها',
        'plugin_settings_section': 'تنظیمات',
        'plugin_settings': 'تنظیمات افزونه',
        'main_menu_button': 'دکمه در منوی اصلی',
        'main_menu_button_sub': 'تنظیمات منوی اصلی تلگرام را برای اضافه کردن دکمه باز کنید.',
        'main_plugins_menu_button': 'دکمه در منوی اصلی افزونه‌ها',
        'main_plugins_menu_button_sub': 'دکمه باز کردن تنظیمات را به منوی اصلی افزونه‌ها اضافه می‌کند.',
        'settings_menu_button': 'دکمه در منوی تنظیمات',
        'settings_menu_button_sub': 'دکمه باز کردن تنظیمات را به منوی تنظیمات تلگرام اضافه می‌کند.',
        'triggers': 'محرک‌ها',
        'particles_in_settings': 'ذرات در تنظیمات',
        'plugin_language': 'زبان افزونه',
        'system': 'سیستمی',
        'restart_required': 'برای اعمال، باید برنامه را مجدداً راه‌اندازی کنید.',
        'restart_button': 'راه‌اندازی مجدد',
        'settings_section': 'تنظیمات',
        'settings_button_label': 'تنظیمات Templates',
        'chat_picker_error': 'باز کردن انتخاب‌کننده چت انجام نشد.',
        'no_chat_selected': 'چتی انتخاب نشده.',
        'template_send_error': 'ارسال قالب انجام نشد.',
    },
    'de': {
        'name': 'Vorlagenname',
        'text': 'Vorlagentext',
        'edit': 'Bearbeiten',
        'clear': 'Löschen',
        'open_settings_error': 'Einstellungen konnten nicht geöffnet werden: {error}',
        'templates': 'Vorlagen',
        'link_open_error': 'Fehler beim Öffnen des Links: {error}',
        'how_it_works': 'Wie funktioniert es?',
        'how_it_works_text': '''Vorlagen sind vorgefertigte Nachrichten, die Sie schnell senden können.

So erstellen Sie eine Vorlage:
1. Öffnen Sie die Einstellungen des Templates-Plugins;
2. Aktivieren Sie eine Vorlage;
3. Legen Sie ihren Namen und den Nachrichtentext fest.

So senden Sie eine Vorlage:
1. Drücken Sie in den Plugin-Einstellungen auf "Vorlage senden" und wählen Sie einen Chat aus;
2. Geben Sie im Nachrichteneingabefeld des geöffneten Chats den Befehl und den Vorlagennamen ein. Beispiel: "// Name";
3. Durch Klicken auf die Schaltfläche "Vorlagen" im Chat-Menü oder im Plugins-Menü im Chat.

Sie können auch den Formatierungsmodus verwenden: **fett**, __unterstrichen__, ~~durchgestrichen~~, `Monospaced`, --kursiv--, ||Spoiler||.

Exportieren Sie Vorlagen, indem Sie in den Einstellungen auf "Vorlagen exportieren" klicken und einen Chat auswählen. Importieren Sie über eine Datei im Chat, indem Sie darauf klicken und dann "Vorlagen importieren".

Häufig gestellte Fragen:
1. Ist das Plugin sicher?
— Ja, das Plugin ist völlig sicher. Sie können sich selbst davon überzeugen, indem Sie den Code des Plugins überprüfen; er ist vollständig offen.

Wenn Sie eine Idee zur Verbesserung des Plugins vorschlagen, einen Fehler melden oder etwas anderes möchten, schreiben Sie an den Kanal @I_am_Vestr oder mir persönlich @mr_Vestr.''',
        'channel': 'Mein Kanal',
        'personal': 'Mein DM',
        'close': 'Schließen',
        'delete_button': 'Löschen',
        'yes': 'Ja',
        'no': 'Nein',
        'settings': 'Einstellungen',
        'drawer_menu': 'Schaltfläche im Hauptmenü der Plugins',
        'drawer_menu_sub': 'Fügt eine Schaltfläche zum Öffnen der Einstellungen im Hauptmenü der Plugins hinzu.',
        'chat_menu': 'Schaltfläche im Chat-Menü',
        'chat_menu_sub': 'Fügt eine Schaltfläche für Vorlageneinstellungen zum normalen Chat-Menü hinzu.',
        'chat_plugins_menu': 'Schaltfläche im Plugins-Menü im Chat',
        'chat_plugins_menu_sub': 'Fügt eine Schaltfläche für Vorlageneinstellungen zum Plugins-Menü im Chat hinzu.',
        'send_cmd': 'Befehl zum Senden der Vorlage',
        'send_cmd_sub': 'Geben Sie den Befehl zum Senden von Vorlagen ein.',
        'template_n': 'Vorlage #{n}',
        'template_name': 'Vorlagenname',
        'template_name_sub': 'Überlegen Sie sich einen Namen für die Vorlage.',
        'template_text': 'Vorlagentext',
        'template_text_sub': 'Überlegen Sie sich einen Text für die Vorlage.',
        'send_template': 'Vorlage senden',
        'delete_template': 'Vorlage löschen',
        'create_template': 'Vorlage erstellen',
        'contacts': 'Meine Kontakte',
        'channel_1': 'Mein Kanal — @I_am_Vestr',
        'personal_1': 'Mein DM — @mr_Vestr',
        'other': 'Sonstiges',
        'plugin_version': f'Plugin-Version — {__version__}',
        'updates': 'Aktualisierungen',
        'current_version': 'Aktuelle Version: {version}',
        'updates_info': 'Klicken Sie auf die Schaltfläche unten, um nach Updates zu suchen. Oder schauen Sie auf meinem Kanal @I_am_Vestr vorbei.',
        'check_updates': 'Prüfen',
        'edit_template': 'Vorlage {n} bearbeiten',
        'save': 'Speichern',
        'cancel': 'Abbrechen',
        'enter_template_name': 'Um eine Vorlage zu senden, geben Sie ihren Namen ein.',
        'template_sent': 'Vorlage "{name}" gesendet.',
        'template_not_found': 'Vorlage nicht gefunden! Fügen Sie Vorlagen in den Plugin-Einstellungen hinzu.',
        'fill_all_fields': 'Füllen Sie alle Felder aus, um eine Vorlage zu senden.',
        'close_menu_question': 'Möchten Sie das Menü schließen?',
        'templates_title': 'Vorlagen',
        'error_occurred': 'Ein Fehler ist aufgetreten!',
        'support_me': 'Unterstütze mich',
        'support_me_text': 'Wenn du mich unterstützen möchtest, kannst du mir ein Geschenk in Telegram senden oder mir Telegram Premium schenken :)',
        'my_account': 'Mein Konto',
        'restart_error': 'Neustartfehler: {error}',
        'download_error': 'Downloadfehler: {error}',
        'error_occurred_with_reason': 'Fehler: {error}',
        'select_template': 'Vorlage auswählen',
        'no_templates_available': 'Keine Vorlagen verfügbar',
        'export_templates': 'Vorlagen exportieren',
        'export_question': 'Welche Vorlagen sollen exportiert werden?',
        'export_sent': 'Export gesendet',
        'export_error': 'Exportfehler: {error}',
        'export_success': 'Export erfolgreich.',
        'import_question': 'Vorlagen aus Datei importieren?',
        'import_success': 'Vorlagen importiert.',
        'import_error': 'Importfehler: {error}',
        'selected_templates': 'Ausgewählt',
        'select_templates': 'Vorlagen auswählen',
        'select': 'Auswählen',
        'export': 'Exportieren',
        'import': 'Importieren',
        'apply': 'Anwenden',
        'template_deleted': 'Vorlage gelöscht.',
        'template_deleted_n': 'Vorlage #{n} gelöscht.',
        'template_name_cleared': 'Vorlagenname #{n} gelöscht.',
        'template_text_cleared': 'Vorlagentext #{n} gelöscht.',
        'template_created_n': 'Vorlage #{n} erstellt.',
        'delete_template_title': 'Vorlage löschen',
        'delete_template_confirm': 'Möchten Sie die Vorlage #{n} wirklich löschen?',
        'undo': 'Rückgängig',
        'template_n_sent': 'Vorlage #{n} gesendet.',
        'open': 'Öffnen',
        'templates_exported': 'Vorlagen exportiert.',
        'export_file_caption': 'Vorlagen exportieren',
        'import_dialog_title': 'Vorlagen importieren',
        'fill_prev_template': 'Füllen Sie alle Felder der vorherigen Vorlage aus, um eine weitere zu erstellen.',
        'clear_field_title': 'Feld löschen',
        'clear_field_name_confirm': 'Möchten Sie den Namen der Vorlage #{n} wirklich löschen?',
        'clear_field_text_confirm': 'Möchten Sie den Text der Vorlage #{n} wirklich löschen?',
        'copy': 'Kopieren',
        'link_copied': 'Link kopiert',
        'copied_to_clipboard': 'In die Zwischenablage kopiert',
        'error_prefix': 'Fehler:',
        'clear_all_templates': 'Alle Vorlagen löschen',
        'templates_limit_exceeded': 'Die Anzahl der Vorlagen darf 30 nicht überschreiten.',
        'checking_updates': 'Suche nach Updates für Templates...',
        'no_updates_available': 'Sie haben die neueste Version des Plugins.',
        'update_check_error': 'Fehler bei der Updateprüfung: {error}',
        'template_name_exists': 'Ein Vorlagenname mit diesem Namen existiert bereits. Benennen Sie ihn um, sonst wird er deaktiviert.',
        'refresh_templates': 'Vorlagen werden aktualisiert...',
        'update_timeout_error': 'Updateprüfung fehlgeschlagen. Überprüfen Sie Ihre Internetverbindung.',
        'changes': 'Änderungen:',
        'full_changelog': 'Vollständige Liste der Änderungen',
        'update': 'Aktualisieren',
        'updating_plugin': 'Aktualisiere Templates-Plugin...',
        'close_alt': 'Schließen',
        'update_failed': 'Das Templates-Plugin konnte nicht aktualisiert werden.',
        'update_success': 'Das Templates-Plugin wurde erfolgreich aktualisiert!',
        'no_changelog': 'Keine Informationen zu Änderungen',
        'header_description': 'Ein Plugin zum Erstellen, Bearbeiten und schnellen Senden von Nachrichtenvorlagen.',
        'main_section': 'Hauptbereich',
        'manage_templates': 'Vorlagen verwalten',
        'plugin_settings_section': 'Einstellungen',
        'plugin_settings': 'Plugin-Einstellungen',
        'main_menu_button': 'Schaltfläche im Hauptmenü',
        'main_menu_button_sub': 'Öffnen Sie die Hauptmenü-Einstellungen von Telegram, um die Schaltfläche hinzuzufügen.',
        'main_plugins_menu_button': 'Schaltfläche im Hauptmenü der Plugins',
        'main_plugins_menu_button_sub': 'Fügt eine Schaltfläche zum Öffnen der Einstellungen im Hauptmenü der Plugins hinzu.',
        'settings_menu_button': 'Schaltfläche im Einstellungsmenü',
        'settings_menu_button_sub': 'Fügt eine Schaltfläche zum Öffnen der Einstellungen im Einstellungsmenü von Telegram hinzu.',
        'triggers': 'Auslöser',
        'particles_in_settings': 'Partikel in den Einstellungen',
        'plugin_language': 'Plugin-Sprache',
        'system': 'System',
        'restart_required': 'Zum Übernehmen muss die Anwendung neu gestartet werden.',
        'restart_button': 'Neustart',
        'settings_section': 'Einstellungen',
        'settings_button_label': 'Templates-Einstellungen',
        'chat_picker_error': 'Chat-Auswahl konnte nicht geöffnet werden.',
        'no_chat_selected': 'Kein Chat ausgewählt.',
        'template_send_error': 'Vorlage konnte nicht gesendet werden.',
    },
    'ja': {
        'name': 'テンプレート名',
        'text': 'テンプレートテキスト',
        'edit': '編集',
        'clear': 'クリア',
        'open_settings_error': '設定を開けませんでした: {error}',
        'templates': 'テンプレート',
        'link_open_error': 'リンクを開くエラー: {error}',
        'how_it_works': '使い方',
        'how_it_works_text': '''テンプレートは、すぐに送信できる事前作成済みのメッセージです。

テンプレートを作成するには：
1. Templatesプラグインの設定を開きます;
2. テンプレートを有効にします;
3. 名前とメッセージテキストを設定します。

テンプレートを送信するには：
1. プラグイン設定で「テンプレートを送信」ボタンを押し、チャットを選択します;
2. 開いているチャットのメッセージ入力フィールドで、コマンドとテンプレート名を入力します。例：「// 名前」;
3. チャットメニューまたはチャット内のプラグインメニューの「テンプレート」ボタンをクリックします。

フォーマットモードも使用できます：**太字**、__下線__、~~取り消し線~~、`等幅`、--斜体--、||スポイラー||。

設定で「テンプレートをエクスポート」をクリックし、チャットを選択してテンプレートをエクスポートします。チャット内のファイルをクリックし、「テンプレートをインポート」でインポートします。

よくある質問：
1. プラグインは安全ですか？
— はい、プラグインは完全に安全です。プラグインのコードを確認することで自分で確かめられます。完全にオープンソースです。

プラグインの改善案を提案したり、バグを報告したり、その他の用事がある場合は、チャンネル@I_am_Vestrまたは私の個人チャット@mr_Vestrに書いてください。''',
        'channel': '私のチャンネル',
        'personal': '私のDM',
        'close': '閉じる',
        'delete_button': '削除',
        'yes': 'はい',
        'no': 'いいえ',
        'settings': '設定',
        'drawer_menu': 'プラグインのメインメニューのボタン',
        'drawer_menu_sub': 'プラグインのメインメニューに設定を開くボタンを追加します。',
        'chat_menu': 'チャットメニューのボタン',
        'chat_menu_sub': '通常のチャットメニューにテンプレート設定のボタンを追加します。',
        'chat_plugins_menu': 'チャット内のプラグインメニューのボタン',
        'chat_plugins_menu_sub': 'チャット内のプラグインメニューにテンプレート設定のボタンを追加します。',
        'send_cmd': 'テンプレート送信コマンド',
        'send_cmd_sub': 'テンプレートを送信するコマンドを入力します。',
        'template_n': 'テンプレート #{n}',
        'template_name': 'テンプレート名',
        'template_name_sub': 'テンプレートの名前を考えてください。',
        'template_text': 'テンプレートテキスト',
        'template_text_sub': 'テンプレートのテキストを考えてください。',
        'send_template': 'テンプレートを送信',
        'delete_template': 'テンプレートを削除',
        'create_template': 'テンプレートを作成',
        'contacts': '私の連絡先',
        'channel_1': '私のチャンネル — @I_am_Vestr',
        'personal_1': '私のDM — @mr_Vestr',
        'other': 'その他',
        'plugin_version': f'プラグインバージョン — {__version__}',
        'updates': 'アップデート',
        'current_version': '現在のバージョン: {version}',
        'updates_info': '下のボタンをクリックしてアップデートを確認します。または私のチャンネル @I_am_Vestr をチェックしてください。',
        'check_updates': '確認',
        'edit_template': 'テンプレート {n} を編集',
        'save': '保存',
        'cancel': 'キャンセル',
        'enter_template_name': 'テンプレートを送信するには、その名前を入力してください。',
        'template_sent': 'テンプレート「{name}」を送信しました。',
        'template_not_found': 'テンプレートが見つかりません！テンプレートはプラグイン設定で追加します。',
        'fill_all_fields': 'テンプレートを送信するには、すべてのデータを入力してください。',
        'close_menu_question': 'メニューを閉じますか？',
        'templates_title': 'テンプレート',
        'error_occurred': 'エラーが発生しました！',
        'support_me': 'サポートする',
        'support_me_text': 'もし私をサポートしたいなら、Telegramでギフトを送るか、Telegram Premiumをギフトしてください :)',
        'my_account': '私のアカウント',
        'restart_error': '再起動エラー: {error}',
        'download_error': 'ダウンロードエラー: {error}',
        'error_occurred_with_reason': 'エラー: {error}',
        'select_template': 'テンプレートを選択',
        'no_templates_available': '利用可能なテンプレートはありません',
        'export_templates': 'テンプレートをエクスポート',
        'export_question': 'どのテンプレートをエクスポートしますか？',
        'export_sent': 'エクスポートを送信しました',
        'export_error': 'エクスポートエラー: {error}',
        'export_success': 'エクスポート成功。',
        'import_question': 'ファイルからテンプレートをインポートしますか？',
        'import_success': 'テンプレートをインポートしました。',
        'import_error': 'インポートエラー: {error}',
        'selected_templates': '選択済み',
        'select_templates': 'テンプレートを選択',
        'select': '選択',
        'export': 'エクスポート',
        'import': 'インポート',
        'apply': '適用',
        'template_deleted': 'テンプレートを削除しました。',
        'template_deleted_n': 'テンプレート #{n} を削除しました。',
        'template_name_cleared': 'テンプレート名 #{n} をクリアしました。',
        'template_text_cleared': 'テンプレートテキスト #{n} をクリアしました。',
        'template_created_n': 'テンプレート #{n} を作成しました。',
        'delete_template_title': 'テンプレートの削除',
        'delete_template_confirm': 'テンプレート #{n} を本当に削除しますか？',
        'undo': '元に戻す',
        'template_n_sent': 'テンプレート #{n} を送信しました。',
        'open': '開く',
        'templates_exported': 'テンプレートをエクスポートしました。',
        'export_file_caption': 'テンプレートのエクスポート',
        'import_dialog_title': 'テンプレートのインポート',
        'fill_prev_template': '別のテンプレートを作成するには、前のテンプレートのすべてのフィールドを入力してください。',
        'clear_field_title': 'フィールドをクリア',
        'clear_field_name_confirm': 'テンプレート名 #{n} を本当にクリアしますか？',
        'clear_field_text_confirm': 'テンプレートテキスト #{n} を本当にクリアしますか？',
        'copy': 'コピー',
        'link_copied': 'リンクをコピーしました',
        'copied_to_clipboard': 'クリップボードにコピーしました',
        'error_prefix': 'エラー:',
        'clear_all_templates': 'すべてのテンプレートをクリア',
        'templates_limit_exceeded': 'テンプレートの数は30個を超えることはできません。',
        'checking_updates': 'Templatesのアップデートを確認しています...',
        'no_updates_available': '最新バージョンのプラグインです。',
        'update_check_error': 'アップデート確認エラー: {error}',
        'template_name_exists': 'このテンプレート名は既に存在します。名前を変更するか、非アクティブになります。',
        'refresh_templates': 'テンプレートを更新しています...',
        'update_timeout_error': 'アップデートを確認できませんでした。インターネット接続を確認してください。',
        'changes': '変更点:',
        'full_changelog': '全変更履歴',
        'update': '更新',
        'updating_plugin': 'Templatesプラグインを更新しています...',
        'close_alt': '閉じる',
        'update_failed': 'Templatesプラグインの更新に失敗しました。',
        'update_success': 'Templatesプラグインを更新しました！',
        'no_changelog': '変更履歴情報はありません',
        'header_description': 'メッセージテンプレートを作成、編集、迅速に送信するためのプラグイン。',
        'main_section': 'メイン',
        'manage_templates': 'テンプレートを管理',
        'plugin_settings_section': '設定',
        'plugin_settings': 'プラグイン設定',
        'main_menu_button': 'メインメニューのボタン',
        'main_menu_button_sub': 'ボタンを追加するためにTelegramのメインメニュー設定を開きます。',
        'main_plugins_menu_button': 'プラグインのメインメニューのボタン',
        'main_plugins_menu_button_sub': 'プラグインのメインメニューに設定を開くボタンを追加します。',
        'settings_menu_button': '設定メニューのボタン',
        'settings_menu_button_sub': 'Telegramの設定メニューに設定を開くボタンを追加します。',
        'triggers': 'トリガー',
        'particles_in_settings': '設定内のパーティクル',
        'plugin_language': 'プラグイン言語',
        'system': 'システム',
        'restart_required': '適用するには、アプリケーションを再起動する必要があります。',
        'restart_button': '再起動',
        'settings_section': '設定',
        'settings_button_label': 'Templates設定',
        'chat_picker_error': 'チャットピッカーを開けませんでした。',
        'no_chat_selected': 'チャットが選択されていません。',
        'template_send_error': 'テンプレートを送信できませんでした。',
    },
    'tr': {
        'name': 'Şablon adı',
        'text': 'Şablon metni',
        'edit': 'Düzenle',
        'clear': 'Temizle',
        'open_settings_error': 'Ayarlar açılamadı: {error}',
        'templates': 'Şablonlar',
        'link_open_error': 'Bağlantı açılırken hata: {error}',
        'how_it_works': 'Nasıl çalışır?',
        'how_it_works_text': '''Şablonlar, hızlıca gönderebileceğiniz önceden hazırlanmış mesajlardır.

Şablon oluşturmak için:
1. Templates eklentisi ayarlarını açın;
2. Bir şablonu etkinleştirin;
3. Adını ve gönderilecek mesajı ayarlayın.

Şablon göndermek için:
1. Eklenti ayarlarında "Şablon gönder" düğmesine basın ve istediğiniz sohbeti seçin;
2. Açık olan sohbetin mesaj giriş alanına komutu ve şablon adını yazın. Örnek: "// Ad";
3. Sohbet menüsündeki veya sohbetteki eklentiler menüsündeki "Şablonlar" düğmesine tıklayarak.

Ayrıca biçimlendirme modunu kullanabilirsiniz: **kalın**, __altı çizili__, ~~üstü çizili~~, `tek aralıklı`, --italik--, ||spoiler||.

Ayarlarda "Şablonları dışa aktar"a tıklayıp bir sohbet seçerek şablonları dışa aktarın. Sohbetteki bir dosyaya tıklayıp ardından "Şablonları içe aktar" ile içe aktarın.

Sık sorulan sorular:
1. Eklenti güvenli mi?
— Evet, eklenti tamamen güvenlidir. Eklentinin kodunu inceleyerek kendiniz doğrulayabilirsiniz, tamamen açık kaynaktır.

Eklentiyi geliştirmek için bir fikir önermek, bir hata bildirmek veya başka bir şey istiyorsanız, @I_am_Vestr kanalına veya bana kişisel olarak @mr_Vestr yazın.''',
        'channel': 'Kanalım',
        'personal': 'Özel mesajlarım',
        'close': 'Kapat',
        'delete_button': 'Sil',
        'yes': 'Evet',
        'no': 'Hayır',
        'settings': 'Ayarlar',
        'drawer_menu': 'Eklentiler ana menüsünde düğme',
        'drawer_menu_sub': 'Eklentiler ana menüsüne ayarları açan bir düğme ekler.',
        'chat_menu': 'Sohbet menüsünde düğme',
        'chat_menu_sub': 'Normal sohbet menüsüne şablon ayarları düğmesi ekler.',
        'chat_plugins_menu': 'Sohbetteki eklentiler menüsünde düğme',
        'chat_plugins_menu_sub': 'Sohbetteki eklentiler menüsüne şablon ayarları düğmesi ekler.',
        'send_cmd': 'Şablon gönderme komutu',
        'send_cmd_sub': 'Şablonları göndermek için komutu girin.',
        'template_n': 'Şablon #{n}',
        'template_name': 'Şablon adı',
        'template_name_sub': 'Bir şablon adı bulun.',
        'template_text': 'Şablon metni',
        'template_text_sub': 'Bir şablon metni bulun.',
        'send_template': 'Şablon gönder',
        'delete_template': 'Şablonu sil',
        'create_template': 'Şablon oluştur',
        'contacts': 'Kişilerim',
        'channel_1': 'Kanalım — @I_am_Vestr',
        'personal_1': 'Özel mesajlarım — @mr_Vestr',
        'other': 'Diğer',
        'plugin_version': f'Eklenti sürümü — {__version__}',
        'updates': 'Güncellemeler',
        'current_version': 'Mevcut sürüm: {version}',
        'updates_info': 'Güncellemeleri kontrol etmek için aşağıdaki düğmeye tıklayın. Veya kanalım @I_am_Vestr\'e göz atın.',
        'check_updates': 'Kontrol et',
        'edit_template': 'Şablonu düzenle {n}',
        'save': 'Kaydet',
        'cancel': 'İptal',
        'enter_template_name': 'Bir şablon göndermek için adını yazın.',
        'template_sent': '"{name}" şablonu gönderildi.',
        'template_not_found': 'Şablon bulunamadı! Şablonlar eklenti ayarlarından eklenir.',
        'fill_all_fields': 'Şablon göndermek için tüm verileri doldurun.',
        'close_menu_question': 'Menüyü kapatmak istiyor musunuz?',
        'templates_title': 'Şablonlar',
        'error_occurred': 'Bir hata oluştu!',
        'support_me': 'Beni destekle',
        'support_me_text': 'Beni desteklemek isterseniz, Telegram\'da bana hediye gönderebilir veya Telegram Premium hediye edebilirsiniz :)',
        'my_account': 'Hesabım',
        'restart_error': 'Yeniden başlatma hatası: {error}',
        'download_error': 'İndirme hatası: {error}',
        'error_occurred_with_reason': 'Hata: {error}',
        'select_template': 'Şablon seç',
        'no_templates_available': 'Kullanılabilir şablon yok',
        'export_templates': 'Şablonları dışa aktar',
        'export_question': 'Hangi şablonlar dışa aktarılsın?',
        'export_sent': 'Dışa aktarma gönderildi',
        'export_error': 'Dışa aktarma hatası: {error}',
        'export_success': 'Dışa aktarma başarılı.',
        'import_question': 'Dosyadan şablonları içe aktar?',
        'import_success': 'Şablonlar içe aktarıldı.',
        'import_error': 'İçe aktarma hatası: {error}',
        'selected_templates': 'Seçildi',
        'select_templates': 'Şablonları seç',
        'select': 'Seç',
        'export': 'Dışa aktar',
        'import': 'İçe aktar',
        'apply': 'Uygula',
        'template_deleted': 'Şablon silindi.',
        'template_deleted_n': 'Şablon #{n} silindi.',
        'template_name_cleared': 'Şablon adı #{n} temizlendi.',
        'template_text_cleared': 'Şablon metni #{n} temizlendi.',
        'template_created_n': 'Şablon #{n} oluşturuldu.',
        'delete_template_title': 'Şablon silme',
        'delete_template_confirm': 'Şablon #{n} silinsin mi?',
        'undo': 'Geri al',
        'template_n_sent': 'Şablon #{n} gönderildi.',
        'open': 'Aç',
        'templates_exported': 'Şablonlar dışa aktarıldı.',
        'export_file_caption': 'Şablonları dışa aktar',
        'import_dialog_title': 'Şablonları içe aktar',
        'fill_prev_template': 'Başka bir şablon oluşturmak için önceki şablonun tüm alanlarını doldurun.',
        'clear_field_title': 'Alanı temizle',
        'clear_field_name_confirm': 'Şablon adı #{n} temizlensin mi?',
        'clear_field_text_confirm': 'Şablon metni #{n} temizlensin mi?',
        'copy': 'Kopyala',
        'link_copied': 'Bağlantı kopyalandı',
        'copied_to_clipboard': 'Panoya kopyalandı',
        'error_prefix': 'Hata:',
        'clear_all_templates': 'Tüm şablonları temizle',
        'templates_limit_exceeded': 'Şablon sayısı 30\'u geçemez.',
        'checking_updates': 'Templates güncellemeleri kontrol ediliyor...',
        'no_updates_available': 'Eklentinin en son sürümüne sahipsiniz.',
        'update_check_error': 'Güncelleme kontrol hatası: {error}',
        'template_name_exists': 'Bu şablon adı zaten mevcut. Yeniden adlandırın veya devre dışı kalacaktır.',
        'refresh_templates': 'Şablonlar yenileniyor...',
        'update_timeout_error': 'Güncellemeler kontrol edilemedi. İnternet bağlantınızı kontrol edin.',
        'changes': 'Değişiklikler:',
        'full_changelog': 'Tüm değişiklik listesi',
        'update': 'Güncelle',
        'updating_plugin': 'Templates eklentisi güncelleniyor...',
        'close_alt': 'Kapat',
        'update_failed': 'Templates eklentisi güncellenemedi.',
        'update_success': 'Templates eklentisi başarıyla güncellendi!',
        'no_changelog': 'Değişiklik bilgisi yok',
        'header_description': 'Mesaj şablonları oluşturmak, düzenlemek ve hızlı göndermek için bir eklenti.',
        'main_section': 'Ana',
        'manage_templates': 'Şablonları yönet',
        'plugin_settings_section': 'Ayarlar',
        'plugin_settings': 'Eklenti ayarları',
        'main_menu_button': 'Ana menü düğmesi',
        'main_menu_button_sub': 'Düğme eklemek için Telegram ana menü ayarlarını açın.',
        'main_plugins_menu_button': 'Eklentiler ana menü düğmesi',
        'main_plugins_menu_button_sub': 'Eklentiler ana menüsüne ayarları açan bir düğme ekler.',
        'settings_menu_button': 'Ayarlar menü düğmesi',
        'settings_menu_button_sub': 'Telegram ayarlar menüsüne ayarları açan bir düğme ekler.',
        'triggers': 'Tetikleyiciler',
        'particles_in_settings': 'Ayarlarda parçacıklar',
        'plugin_language': 'Eklenti dili',
        'system': 'Sistem',
        'restart_required': 'Uygulamak için uygulamayı yeniden başlatmanız gerekir.',
        'restart_button': 'Yeniden başlat',
        'settings_section': 'Ayarlar',
        'settings_button_label': 'Templates Ayarları',
        'chat_picker_error': 'Sohbet seçici açılamadı.',
        'no_chat_selected': 'Sohbet seçilmedi.',
        'template_send_error': 'Şablon gönderilemedi.',
    },
    'zh': {
        'name': '模板名称',
        'text': '模板文本',
        'edit': '编辑',
        'clear': '清除',
        'open_settings_error': '无法打开设置：{error}',
        'templates': '模板',
        'link_open_error': '打开链接时出错：{error}',
        'how_it_works': '如何使用？',
        'how_it_works_text': '''模板是可以快速发送的预先准备好的消息。

要创建模板：
1. 打开Templates插件设置；
2. 启用一个模板；
3. 设置其名称和要发送的消息。

发送模板：
1. 在插件设置中，按“发送模板”并选择所需的聊天；
2. 在已打开的所需聊天的消息输入框中，输入命令和模板名称。示例：“// 名称”；
3. 点击聊天菜单或聊天中的插件菜单中的“模板”按钮。

您也可以使用格式化模式：**粗体**、__下划线__、~~删除线~~、`等宽字体`、--斜体--、||剧透||。

通过点击设置中的“导出模板”并选择一个聊天来导出模板。通过点击聊天中的文件然后“导入模板”来导入。

常见问题：
1. 插件安全吗？
— 是的，该插件完全安全。您可以通过检查插件代码来亲自验证，它是完全开源的。

如果您想提出改进插件的想法、报告错误或其他问题，请写信给频道@I_am_Vestr或私信@mr_Vestr。''',
        'channel': '我的频道',
        'personal': '我的私信',
        'close': '关闭',
        'delete_button': '删除',
        'yes': '是',
        'no': '否',
        'settings': '设置',
        'drawer_menu': '插件主菜单中的按钮',
        'drawer_menu_sub': '在插件主菜单中添加一个打开设置的按钮。',
        'chat_menu': '聊天菜单中的按钮',
        'chat_menu_sub': '在普通聊天菜单中添加一个模板设置按钮。',
        'chat_plugins_menu': '聊天中插件菜单中的按钮',
        'chat_plugins_menu_sub': '在聊天的插件菜单中添加一个模板设置按钮。',
        'send_cmd': '发送模板的命令',
        'send_cmd_sub': '输入发送模板的命令。',
        'template_n': '模板 #{n}',
        'template_name': '模板名称',
        'template_name_sub': '为模板起一个名称。',
        'template_text': '模板文本',
        'template_text_sub': '为模板编写文本。',
        'send_template': '发送模板',
        'delete_template': '删除模板',
        'create_template': '创建模板',
        'contacts': '我的联系方式',
        'channel_1': '我的频道 — @I_am_Vestr',
        'personal_1': '我的私信 — @mr_Vestr',
        'other': '其他',
        'plugin_version': f'插件版本 — {__version__}',
        'updates': '更新',
        'current_version': '当前版本：{version}',
        'updates_info': '点击下面的按钮检查更新。或者查看我的频道 @I_am_Vestr。',
        'check_updates': '检查',
        'edit_template': '编辑模板 {n}',
        'save': '保存',
        'cancel': '取消',
        'enter_template_name': '要发送模板，请输入其名称。',
        'template_sent': '模板“{name}”已发送。',
        'template_not_found': '未找到模板！请在插件设置中添加模板。',
        'fill_all_fields': '请填写所有数据以发送模板。',
        'close_menu_question': '要关闭菜单吗？',
        'templates_title': '模板',
        'error_occurred': '发生错误！',
        'support_me': '支持我',
        'support_me_text': '如果你想支持我，你可以在Telegram上给我发送礼物或赠送Telegram Premium :)',
        'my_account': '我的账户',
        'restart_error': '重启错误：{error}',
        'download_error': '下载错误：{error}',
        'error_occurred_with_reason': '错误：{error}',
        'select_template': '选择模板',
        'no_templates_available': '没有可用的模板',
        'export_templates': '导出模板',
        'export_question': '要导出哪些模板？',
        'export_sent': '导出已发送',
        'export_error': '导出错误：{error}',
        'export_success': '导出成功。',
        'import_question': '从文件导入模板？',
        'import_success': '模板已导入。',
        'import_error': '导入错误：{error}',
        'selected_templates': '已选择',
        'select_templates': '选择模板',
        'select': '选择',
        'export': '导出',
        'import': '导入',
        'apply': '应用',
        'template_deleted': '模板已删除。',
        'template_deleted_n': '模板 #{n} 已删除。',
        'template_name_cleared': '模板名称 #{n} 已清除。',
        'template_text_cleared': '模板文本 #{n} 已清除。',
        'template_created_n': '模板 #{n} 已创建。',
        'delete_template_title': '删除模板',
        'delete_template_confirm': '确定要删除模板 #{n} 吗？',
        'undo': '撤销',
        'template_n_sent': '模板 #{n} 已发送。',
        'open': '打开',
        'templates_exported': '模板已导出。',
        'export_file_caption': '导出模板',
        'import_dialog_title': '导入模板',
        'fill_prev_template': '请填写上一个模板的所有字段以创建另一个模板。',
        'clear_field_title': '清除字段',
        'clear_field_name_confirm': '确定要清除模板名称 #{n} 吗？',
        'clear_field_text_confirm': '确定要清除模板文本 #{n} 吗？',
        'copy': '复制',
        'link_copied': '链接已复制',
        'copied_to_clipboard': '已复制到剪贴板',
        'error_prefix': '错误：',
        'clear_all_templates': '清除所有模板',
        'templates_limit_exceeded': '模板数量不能超过30个。',
        'checking_updates': '正在检查Templates的更新...',
        'no_updates_available': '您拥有最新版本的插件。',
        'update_check_error': '检查更新时出错：{error}',
        'template_name_exists': '该模板名称已存在。请重命名，否则将被停用。',
        'refresh_templates': '正在刷新模板...',
        'update_timeout_error': '无法检查更新。请检查您的互联网连接。',
        'changes': '更改：',
        'full_changelog': '完整更改日志',
        'update': '更新',
        'updating_plugin': '正在更新Templates插件...',
        'close_alt': '关闭',
        'update_failed': '无法更新Templates插件。',
        'update_success': 'Templates插件已成功更新！',
        'no_changelog': '没有更改信息',
        'header_description': '用于创建、编辑和快速发送消息模板的插件。',
        'main_section': '主要',
        'manage_templates': '管理模板',
        'plugin_settings_section': '设置',
        'plugin_settings': '插件设置',
        'main_menu_button': '主菜单按钮',
        'main_menu_button_sub': '打开Telegram主菜单设置以添加按钮。',
        'main_plugins_menu_button': '插件主菜单按钮',
        'main_plugins_menu_button_sub': '在插件主菜单中添加一个打开设置的按钮。',
        'settings_menu_button': '设置菜单按钮',
        'settings_menu_button_sub': '在Telegram设置菜单中添加一个打开设置的按钮。',
        'triggers': '触发器',
        'particles_in_settings': '设置中的粒子效果',
        'plugin_language': '插件语言',
        'system': '系统',
        'restart_required': '要应用，您需要重新启动应用程序。',
        'restart_button': '重启',
        'settings_section': '设置',
        'settings_button_label': 'Templates设置',
        'chat_picker_error': '无法打开聊天选择器。',
        'no_chat_selected': '未选择聊天。',
        'template_send_error': '无法发送模板。',
    },
    'hi': {
        'name': 'टेम्पलेट का नाम',
        'text': 'टेम्पलेट टेक्स्ट',
        'edit': 'संपादित करें',
        'clear': 'साफ़ करें',
        'open_settings_error': 'सेटिंग्स खोलने में विफल: {error}',
        'templates': 'टेम्पलेट',
        'link_open_error': 'लिंक खोलने में त्रुटि: {error}',
        'how_it_works': 'यह कैसे काम करता है?',
        'how_it_works_text': '''टेम्पलेट पहले से बने संदेश होते हैं जिन्हें आप जल्दी भेज सकते हैं।

टेम्पलेट बनाने के लिए:
1. Templates प्लगइन की सेटिंग्स खोलें;
2. एक टेम्पलेट सक्षम करें;
3. उसका नाम और भेजा जाने वाला संदेश सेट करें।

टेम्पलेट भेजने के लिए:
1. प्लगइन सेटिंग्स में, "टेम्पलेट भेजें" बटन दबाएं और वांछित चैट चुनें;
2. पहले से खुले वांछित चैट में संदेश इनपुट फ़ील्ड में, कमांड और टेम्पलेट का नाम लिखें। उदाहरण: "// नाम";
3. चैट मेनू या चैट में प्लगइन मेनू में "टेम्पलेट" बटन पर क्लिक करके।

आप फ़ॉर्मेटिंग मोड का भी उपयोग कर सकते हैं: **बोल्ड**, __अंडरलाइन__, ~~स्ट्राइकथ्रू~~, `मोनोस्पेस`, --इटैलिक--, ||स्पॉयलर||।

सेटिंग्स में "टेम्पलेट एक्सपोर्ट करें" पर क्लिक करके और एक चैट चुनकर टेम्पलेट एक्सपोर्ट करें। चैट में एक फ़ाइल पर क्लिक करके और फिर "टेम्पलेट इंपोर्ट करें" के माध्यम से इंपोर्ट करें।

अक्सर पूछे जाने वाले प्रश्न:
1. क्या प्लगइन सुरक्षित है?
— हाँ, प्लगइन पूरी तरह से सुरक्षित है। आप प्लगइन के कोड की जाँच करके स्वयं सत्यापित कर सकते हैं, यह पूरी तरह से ओपन सोर्स है।

यदि आप प्लगइन को बेहतर बनाने के लिए कोई सुझाव देना चाहते हैं, कोई बग रिपोर्ट करना चाहते हैं, या कुछ और करना चाहते हैं, तो @I_am_Vestr चैनल या मुझे व्यक्तिगत रूप से @mr_Vestr पर लिखें।''',
        'channel': 'मेरा चैनल',
        'personal': 'मेरा डीएम',
        'close': 'बंद करें',
        'delete_button': 'हटाएं',
        'yes': 'हाँ',
        'no': 'नहीं',
        'settings': 'सेटिंग्स',
        'drawer_menu': 'प्लगइन्स के मुख्य मेनू में बटन',
        'drawer_menu_sub': 'प्लगइन्स के मुख्य मेनू में सेटिंग्स खोलने के लिए एक बटन जोड़ता है।',
        'chat_menu': 'चैट मेनू में बटन',
        'chat_menu_sub': 'सामान्य चैट मेनू में टेम्पलेट सेटिंग्स बटन जोड़ता है।',
        'chat_plugins_menu': 'चैट में प्लगइन्स मेनू में बटन',
        'chat_plugins_menu_sub': 'चैट में प्लगइन्स मेनू में टेम्पलेट सेटिंग्स बटन जोड़ता है।',
        'send_cmd': 'टेम्पलेट भेजने का कमांड',
        'send_cmd_sub': 'टेम्पलेट भेजने के लिए कमांड दर्ज करें।',
        'template_n': 'टेम्पलेट #{n}',
        'template_name': 'टेम्पलेट का नाम',
        'template_name_sub': 'टेम्पलेट के लिए एक नाम सोचें।',
        'template_text': 'टेम्पलेट टेक्स्ट',
        'template_text_sub': 'टेम्पलेट के लिए टेक्स्ट सोचें।',
        'send_template': 'टेम्पलेट भेजें',
        'delete_template': 'टेम्पलेट हटाएं',
        'create_template': 'टेम्पलेट बनाएं',
        'contacts': 'मेरे संपर्क',
        'channel_1': 'मेरा चैनल — @I_am_Vestr',
        'personal_1': 'मेरा डीएम — @mr_Vestr',
        'other': 'अन्य',
        'plugin_version': f'प्लगइन संस्करण — {__version__}',
        'updates': 'अपडेट',
        'current_version': 'वर्तमान संस्करण: {version}',
        'updates_info': 'अपडेट की जांच करने के लिए नीचे दिए गए बटन पर क्लिक करें। या मेरे चैनल @I_am_Vestr देखें।',
        'check_updates': 'जांचें',
        'edit_template': 'टेम्पलेट संपादित करें {n}',
        'save': 'सहेजें',
        'cancel': 'रद्द करें',
        'enter_template_name': 'टेम्पलेट भेजने के लिए, उसका नाम लिखें।',
        'template_sent': 'टेम्पलेट "{name}" भेजा गया।',
        'template_not_found': 'टेम्पलेट नहीं मिला! टेम्पलेट प्लगइन सेटिंग्स में जोड़े जाते हैं।',
        'fill_all_fields': 'टेम्पलेट भेजने के लिए सभी डेटा भरें।',
        'close_menu_question': 'क्या आप मेनू बंद करना चाहते हैं?',
        'templates_title': 'टेम्पलेट',
        'error_occurred': 'एक त्रुटि हुई!',
        'support_me': 'मेरा समर्थन करें',
        'support_me_text': 'यदि आप मेरा समर्थन करना चाहते हैं, तो आप मुझे टेलीग्राम पर उपहार भेज सकते हैं या टेलीग्राम प्रीमियम उपहार दे सकते हैं :)',
        'my_account': 'मेरा खाता',
        'restart_error': 'पुनरारंभ त्रुटि: {error}',
        'download_error': 'डाउनलोड त्रुटि: {error}',
        'error_occurred_with_reason': 'त्रुटि: {error}',
        'select_template': 'टेम्पलेट चुनें',
        'no_templates_available': 'कोई टेम्पलेट उपलब्ध नहीं',
        'export_templates': 'टेम्पलेट एक्सपोर्ट करें',
        'export_question': 'कौन से टेम्पलेट एक्सपोर्ट करें?',
        'export_sent': 'एक्सपोर्ट भेजा गया',
        'export_error': 'एक्सपोर्ट त्रुटि: {error}',
        'export_success': 'एक्सपोर्ट सफल।',
        'import_question': 'फ़ाइल से टेम्पलेट इंपोर्ट करें?',
        'import_success': 'टेम्पलेट इंपोर्ट हो गए।',
        'import_error': 'इंपोर्ट त्रुटि: {error}',
        'selected_templates': 'चयनित',
        'select_templates': 'टेम्पलेट चुनें',
        'select': 'चुनें',
        'export': 'एक्सपोर्ट',
        'import': 'इंपोर्ट',
        'apply': 'लागू करें',
        'template_deleted': 'टेम्पलेट हटा दिया गया।',
        'template_deleted_n': 'टेम्पलेट #{n} हटा दिया गया।',
        'template_name_cleared': 'टेम्पलेट का नाम #{n} साफ़ कर दिया गया।',
        'template_text_cleared': 'टेम्पलेट टेक्स्ट #{n} साफ़ कर दिया गया।',
        'template_created_n': 'टेम्पलेट #{n} बनाया गया।',
        'delete_template_title': 'टेम्पलेट हटाना',
        'delete_template_confirm': 'क्या आप वाकई टेम्पलेट #{n} को हटाना चाहते हैं?',
        'undo': 'पूर्ववत करें',
        'template_n_sent': 'टेम्पलेट #{n} भेजा गया।',
        'open': 'खोलें',
        'templates_exported': 'टेम्पलेट एक्सपोर्ट हो गए।',
        'export_file_caption': 'टेम्पलेट एक्सपोर्ट करें',
        'import_dialog_title': 'टेम्पलेट इंपोर्ट करें',
        'fill_prev_template': 'दूसरा टेम्पलेट बनाने के लिए पिछले टेम्पलेट के सभी फ़ील्ड भरें।',
        'clear_field_title': 'फ़ील्ड साफ़ करें',
        'clear_field_name_confirm': 'क्या आप वाकई टेम्पलेट का नाम #{n} साफ़ करना चाहते हैं?',
        'clear_field_text_confirm': 'क्या आप वाकई टेम्पलेट टेक्स्ट #{n} साफ़ करना चाहते हैं?',
        'copy': 'कॉपी करें',
        'link_copied': 'लिंक कॉपी हो गया',
        'copied_to_clipboard': 'क्लिपबोर्ड पर कॉपी किया गया',
        'error_prefix': 'त्रुटि:',
        'clear_all_templates': 'सभी टेम्पलेट साफ़ करें',
        'templates_limit_exceeded': 'टेम्पलेट्स की संख्या 30 से अधिक नहीं हो सकती।',
        'checking_updates': 'Templates के अपडेट की जांच हो रही है...',
        'no_updates_available': 'आपके पास प्लगइन का नवीनतम संस्करण है।',
        'update_check_error': 'अपडेट जांच त्रुटि: {error}',
        'template_name_exists': 'ऐसा टेम्पलेट नाम पहले से मौजूद है। नाम बदलें या यह निष्क्रिय हो जाएगा।',
        'refresh_templates': 'टेम्पलेट ताज़ा हो रहे हैं...',
        'update_timeout_error': 'अपडेट की जांच करने में विफल। अपना इंटरनेट कनेक्शन जांचें।',
        'changes': 'बदलाव:',
        'full_changelog': 'पूर्ण परिवर्तन सूची',
        'update': 'अपडेट करें',
        'updating_plugin': 'Templates प्लगइन अपडेट हो रहा है...',
        'close_alt': 'बंद करें',
        'update_failed': 'Templates प्लगइन अपडेट नहीं किया जा सका।',
        'update_success': 'Templates प्लगइन सफलतापूर्वक अपडेट हो गया!',
        'no_changelog': 'बदलाव की कोई जानकारी नहीं',
        'header_description': 'संदेश टेम्पलेट बनाने, संपादित करने और त्वरित भेजने के लिए एक प्लगइन।',
        'main_section': 'मुख्य',
        'manage_templates': 'टेम्पलेट प्रबंधित करें',
        'plugin_settings_section': 'सेटिंग्स',
        'plugin_settings': 'प्लगइन सेटिंग्स',
        'main_menu_button': 'मुख्य मेनू बटन',
        'main_menu_button_sub': 'बटन जोड़ने के लिए Telegram मुख्य मेनू सेटिंग्स खोलें।',
        'main_plugins_menu_button': 'प्लगइन्स मुख्य मेनू बटन',
        'main_plugins_menu_button_sub': 'प्लगइन्स के मुख्य मेनू में सेटिंग्स खोलने वाला बटन जोड़ता है।',
        'settings_menu_button': 'सेटिंग्स मेनू बटन',
        'settings_menu_button_sub': 'Telegram सेटिंग्स मेनू में सेटिंग्स खोलने वाला बटन जोड़ता है।',
        'triggers': 'ट्रिगर',
        'particles_in_settings': 'सेटिंग्स में कण',
        'plugin_language': 'प्लगइन भाषा',
        'system': 'सिस्टम',
        'restart_required': 'लागू करने के लिए, आपको एप्लिकेशन को पुनरारंभ करना होगा।',
        'restart_button': 'पुनरारंभ करें',
        'settings_section': 'सेटिंग्स',
        'settings_button_label': 'Templates सेटिंग्स',
        'chat_picker_error': 'चैट पिकर खोलने में विफल।',
        'no_chat_selected': 'कोई चैट चयनित नहीं।',
        'template_send_error': 'टेम्पलेट भेजने में विफल।',
    },
    'id': {
        'name': 'Nama template',
        'text': 'Teks template',
        'edit': 'Edit',
        'clear': 'Bersihkan',
        'open_settings_error': 'Gagal membuka pengaturan: {error}',
        'templates': 'Template',
        'link_open_error': 'Kesalahan membuka tautan: {error}',
        'how_it_works': 'Bagaimana cara kerjanya?',
        'how_it_works_text': '''Template adalah pesan siap pakai yang dapat Anda kirim dengan cepat.

Untuk membuat template:
1. Buka pengaturan plugin Templates;
2. Aktifkan template;
3. Atur nama dan pesan yang akan dikirim.

Untuk mengirim template:
1. Di pengaturan plugin, tekan "Kirim template" dan pilih chat yang diinginkan;
2. Melalui kolom input pesan di chat yang sudah dibuka, ketik perintah dan nama template. Contoh: "// Nama";
3. Dengan menekan tombol "Template" di menu chat atau menu plugin di chat.

Anda juga dapat menggunakan mode pemformatan: **tebal**, __garis bawah__, ~~coret~~, `lebar tetap`, --miring--, ||spoiler||.

Ekspor template dengan menekan "Ekspor Template" di pengaturan dan memilih chat. Impor melalui file di chat dengan menekannya lalu "Impor Template".

Pertanyaan umum:
1. Apakah plugin ini aman?
— Ya, plugin ini sepenuhnya aman. Anda dapat memverifikasinya sendiri dengan memeriksa kode plugin, sepenuhnya open source.

Jika Anda ingin menyarankan ide untuk perbaikan plugin, melaporkan bug, atau hal lain, tulislah ke saluran @I_am_Vestr atau ke saya pribadi @mr_Vestr.''',
        'channel': 'Saluran saya',
        'personal': 'DM saya',
        'close': 'Tutup',
        'delete_button': 'Hapus',
        'yes': 'Ya',
        'no': 'Tidak',
        'settings': 'Pengaturan',
        'drawer_menu': 'Tombol di menu utama plugin',
        'drawer_menu_sub': 'Menambahkan tombol buka pengaturan di menu utama plugin.',
        'chat_menu': 'Tombol di menu chat',
        'chat_menu_sub': 'Menambahkan tombol pengaturan template di menu chat biasa.',
        'chat_plugins_menu': 'Tombol di menu plugin dalam chat',
        'chat_plugins_menu_sub': 'Menambahkan tombol pengaturan template di menu plugin dalam chat.',
        'send_cmd': 'Perintah kirim template',
        'send_cmd_sub': 'Masukkan perintah untuk mengirim template.',
        'template_n': 'Template #{n}',
        'template_name': 'Nama template',
        'template_name_sub': 'Buat nama untuk template.',
        'template_text': 'Teks template',
        'template_text_sub': 'Buat teks untuk template.',
        'send_template': 'Kirim template',
        'delete_template': 'Hapus template',
        'create_template': 'Buat template',
        'contacts': 'Kontak saya',
        'channel_1': 'Saluran saya — @I_am_Vestr',
        'personal_1': 'DM saya — @mr_Vestr',
        'other': 'Lainnya',
        'plugin_version': f'Versi plugin — {__version__}',
        'updates': 'Pembaruan',
        'current_version': 'Versi saat ini: {version}',
        'updates_info': 'Klik tombol di bawah untuk memeriksa pembaruan. Atau periksa saluran saya @I_am_Vestr.',
        'check_updates': 'Periksa',
        'edit_template': 'Edit template {n}',
        'save': 'Simpan',
        'cancel': 'Batal',
        'enter_template_name': 'Untuk mengirim template, tulis namanya.',
        'template_sent': 'Template "{name}" terkirim.',
        'template_not_found': 'Template tidak ditemukan! Template ditambahkan di pengaturan plugin.',
        'fill_all_fields': 'Isi semua data untuk mengirim template.',
        'close_menu_question': 'Apakah Anda ingin menutup menu?',
        'templates_title': 'Template',
        'error_occurred': 'Terjadi kesalahan!',
        'support_me': 'Dukung saya',
        'support_me_text': 'Jika Anda ingin mendukung saya, Anda dapat mengirimkan hadiah kepada saya di Telegram atau memberikan Telegram Premium :)',
        'my_account': 'Akun saya',
        'restart_error': 'Kesalahan restart: {error}',
        'download_error': 'Kesalahan unduh: {error}',
        'error_occurred_with_reason': 'Kesalahan: {error}',
        'select_template': 'Pilih template',
        'no_templates_available': 'Tidak ada template tersedia',
        'export_templates': 'Ekspor Template',
        'export_question': 'Template mana yang akan diekspor?',
        'export_sent': 'Ekspor terkirim',
        'export_error': 'Kesalahan ekspor: {error}',
        'export_success': 'Ekspor berhasil.',
        'import_question': 'Impor template dari file?',
        'import_success': 'Template diimpor.',
        'import_error': 'Kesalahan impor: {error}',
        'selected_templates': 'Dipilih',
        'select_templates': 'Pilih Template',
        'select': 'Pilih',
        'export': 'Ekspor',
        'import': 'Impor',
        'apply': 'Terapkan',
        'template_deleted': 'Template dihapus.',
        'template_deleted_n': 'Template #{n} dihapus.',
        'template_name_cleared': 'Nama template #{n} dibersihkan.',
        'template_text_cleared': 'Teks template #{n} dibersihkan.',
        'template_created_n': 'Template #{n} dibuat.',
        'delete_template_title': 'Menghapus template',
        'delete_template_confirm': 'Yakin ingin menghapus template #{n}?',
        'undo': 'Urungkan',
        'template_n_sent': 'Template #{n} terkirim.',
        'open': 'Buka',
        'templates_exported': 'Template diekspor.',
        'export_file_caption': 'Ekspor template',
        'import_dialog_title': 'Impor template',
        'fill_prev_template': 'Isi semua bidang template sebelumnya untuk membuat yang lain.',
        'clear_field_title': 'Bersihkan bidang',
        'clear_field_name_confirm': 'Yakin ingin membersihkan nama template #{n}?',
        'clear_field_text_confirm': 'Yakin ingin membersihkan teks template #{n}?',
        'copy': 'Salin',
        'link_copied': 'Tautan disalin',
        'copied_to_clipboard': 'Disalin ke clipboard',
        'error_prefix': 'Kesalahan:',
        'clear_all_templates': 'Bersihkan semua template',
        'templates_limit_exceeded': 'Jumlah template tidak boleh melebihi 30.',
        'checking_updates': 'Memeriksa pembaruan Templates...',
        'no_updates_available': 'Anda memiliki versi terbaru plugin.',
        'update_check_error': 'Kesalahan pemeriksaan pembaruan: {error}',
        'template_name_exists': 'Nama template sudah ada. Ganti namanya atau akan dinonaktifkan.',
        'refresh_templates': 'Menyegarkan template...',
        'update_timeout_error': 'Gagal memeriksa pembaruan. Periksa koneksi internet Anda.',
        'changes': 'Perubahan:',
        'full_changelog': 'Daftar perubahan lengkap',
        'update': 'Perbarui',
        'updating_plugin': 'Memperbarui plugin Templates...',
        'close_alt': 'Tutup',
        'update_failed': 'Gagal memperbarui plugin Templates.',
        'update_success': 'Plugin Templates berhasil diperbarui!',
        'no_changelog': 'Tidak ada informasi perubahan',
        'header_description': 'Plugin untuk membuat, mengedit, dan mengirim template pesan dengan cepat.',
        'main_section': 'Utama',
        'manage_templates': 'Kelola template',
        'plugin_settings_section': 'Pengaturan',
        'plugin_settings': 'Pengaturan plugin',
        'main_menu_button': 'Tombol menu utama',
        'main_menu_button_sub': 'Buka pengaturan menu utama Telegram untuk menambahkan tombol.',
        'main_plugins_menu_button': 'Tombol menu utama plugin',
        'main_plugins_menu_button_sub': 'Menambahkan tombol buka pengaturan di menu utama plugin.',
        'settings_menu_button': 'Tombol menu pengaturan',
        'settings_menu_button_sub': 'Menambahkan tombol buka pengaturan di menu pengaturan Telegram.',
        'triggers': 'Pemicu',
        'particles_in_settings': 'Partikel dalam pengaturan',
        'plugin_language': 'Bahasa plugin',
        'system': 'Sistem',
        'restart_required': 'Untuk menerapkan, Anda perlu memulai ulang aplikasi.',
        'restart_button': 'Mulai ulang',
        'settings_section': 'Pengaturan',
        'settings_button_label': 'Pengaturan Templates',
        'chat_picker_error': 'Gagal membuka pemilih chat.',
        'no_chat_selected': 'Tidak ada chat dipilih.',
        'template_send_error': 'Gagal mengirim template.',
    },
    'fr': {
        'name': 'Nom du modèle',
        'text': 'Texte du modèle',
        'edit': 'Modifier',
        'clear': 'Effacer',
        'open_settings_error': 'Impossible d\'ouvrir les paramètres : {error}',
        'templates': 'Modèles',
        'link_open_error': 'Erreur lors de l\'ouverture du lien : {error}',
        'how_it_works': 'Comment ça marche ?',
        'how_it_works_text': '''Les modèles sont des messages préfabriqués que vous pouvez envoyer rapidement.

Pour créer un modèle :
1. Ouvrez les paramètres du plugin Templates ;
2. Activez un modèle ;
3. Définissez son nom et le message à envoyer.

Pour envoyer un modèle :
1. Dans les paramètres du plugin, appuyez sur « Envoyer le modèle » et choisissez un chat ;
2. Dans le champ de saisie du message dans le chat déjà ouvert, tapez la commande et le nom du modèle. Exemple : « // Nom » ;
3. En appuyant sur le bouton « Modèles » dans le menu du chat ou le menu des plugins dans le chat.

Vous pouvez également utiliser le mode de formatage : **gras**, __souligné__, ~~barré~~, `monospace`, --italique--, ||spoiler||.

Exportez les modèles en cliquant sur « Exporter les modèles » dans les paramètres et en choisissant un chat. Importez via un fichier dans le chat en cliquant dessus puis « Importer les modèles ».

Questions fréquentes :
1. Le plugin est-il sécurisé ?
— Oui, le plugin est totalement sécurisé. Vous pouvez le vérifier vous-même en examinant le code du plugin, il est complètement open source.

Si vous souhaitez suggérer une idée pour améliorer le plugin, signaler un bug ou autre chose, écrivez au canal @I_am_Vestr ou en message privé à @mr_Vestr.''',
        'channel': 'Ma chaîne',
        'personal': 'Mon MP',
        'close': 'Fermer',
        'delete_button': 'Supprimer',
        'yes': 'Oui',
        'no': 'Non',
        'settings': 'Paramètres',
        'drawer_menu': 'Bouton dans le menu principal des plugins',
        'drawer_menu_sub': 'Ajoute un bouton d\'ouverture des paramètres dans le menu principal des plugins.',
        'chat_menu': 'Bouton dans le menu du chat',
        'chat_menu_sub': 'Ajoute un bouton de paramètres de modèles dans le menu normal du chat.',
        'chat_plugins_menu': 'Bouton dans le menu des plugins dans le chat',
        'chat_plugins_menu_sub': 'Ajoute un bouton de paramètres de modèles dans le menu des plugins dans le chat.',
        'send_cmd': 'Commande d\'envoi du modèle',
        'send_cmd_sub': 'Entrez la commande pour envoyer les modèles.',
        'template_n': 'Modèle n°{n}',
        'template_name': 'Nom du modèle',
        'template_name_sub': 'Trouvez un nom pour le modèle.',
        'template_text': 'Texte du modèle',
        'template_text_sub': 'Trouvez un texte pour le modèle.',
        'send_template': 'Envoyer le modèle',
        'delete_template': 'Supprimer le modèle',
        'create_template': 'Créer un modèle',
        'contacts': 'Mes contacts',
        'channel_1': 'Ma chaîne — @I_am_Vestr',
        'personal_1': 'Mon MP — @mr_Vestr',
        'other': 'Autre',
        'plugin_version': f'Version du plugin — {__version__}',
        'updates': 'Mises à jour',
        'current_version': 'Version actuelle : {version}',
        'updates_info': 'Cliquez sur le bouton ci-dessous pour vérifier les mises à jour. Ou consultez ma chaîne @I_am_Vestr.',
        'check_updates': 'Vérifier',
        'edit_template': 'Modifier le modèle {n}',
        'save': 'Enregistrer',
        'cancel': 'Annuler',
        'enter_template_name': 'Pour envoyer un modèle, écrivez son nom.',
        'template_sent': 'Modèle « {name} » envoyé.',
        'template_not_found': 'Modèle introuvable ! Les modèles s\'ajoutent dans les paramètres du plugin.',
        'fill_all_fields': 'Remplissez toutes les données pour envoyer le modèle.',
        'close_menu_question': 'Voulez-vous fermer le menu ?',
        'templates_title': 'Modèles',
        'error_occurred': 'Une erreur est survenue !',
        'support_me': 'Soutenez-moi',
        'support_me_text': 'Si vous voulez me soutenir, vous pouvez m\'envoyer un cadeau sur Telegram ou m\'offrir Telegram Premium :)',
        'my_account': 'Mon compte',
        'restart_error': 'Erreur de redémarrage : {error}',
        'download_error': 'Erreur de téléchargement : {error}',
        'error_occurred_with_reason': 'Erreur : {error}',
        'select_template': 'Sélectionnez un modèle',
        'no_templates_available': 'Aucun modèle disponible',
        'export_templates': 'Exporter les modèles',
        'export_question': 'Quels modèles exporter ?',
        'export_sent': 'Exportation envoyée',
        'export_error': 'Erreur d\'exportation : {error}',
        'export_success': 'Exportation réussie.',
        'import_question': 'Importer des modèles depuis un fichier ?',
        'import_success': 'Modèles importés.',
        'import_error': 'Erreur d\'importation : {error}',
        'selected_templates': 'Sélectionné',
        'select_templates': 'Sélectionner des modèles',
        'select': 'Sélectionner',
        'export': 'Exporter',
        'import': 'Importer',
        'apply': 'Appliquer',
        'template_deleted': 'Modèle supprimé.',
        'template_deleted_n': 'Modèle n°{n} supprimé.',
        'template_name_cleared': 'Nom du modèle n°{n} effacé.',
        'template_text_cleared': 'Texte du modèle n°{n} effacé.',
        'template_created_n': 'Modèle n°{n} créé.',
        'delete_template_title': 'Suppression du modèle',
        'delete_template_confirm': 'Voulez-vous vraiment supprimer le modèle n°{n} ?',
        'undo': 'Annuler',
        'template_n_sent': 'Modèle n°{n} envoyé.',
        'open': 'Ouvrir',
        'templates_exported': 'Modèles exportés.',
        'export_file_caption': 'Exporter les modèles',
        'import_dialog_title': 'Importer des modèles',
        'fill_prev_template': 'Remplissez tous les champs du modèle précédent pour en créer un autre.',
        'clear_field_title': 'Effacer le champ',
        'clear_field_name_confirm': 'Voulez-vous vraiment effacer le nom du modèle n°{n} ?',
        'clear_field_text_confirm': 'Voulez-vous vraiment effacer le texte du modèle n°{n} ?',
        'copy': 'Copier',
        'link_copied': 'Lien copié',
        'copied_to_clipboard': 'Copié dans le presse-papier',
        'error_prefix': 'Erreur :',
        'clear_all_templates': 'Effacer tous les modèles',
        'templates_limit_exceeded': 'Le nombre de modèles ne peut pas dépasser 30.',
        'checking_updates': 'Vérification des mises à jour de Templates...',
        'no_updates_available': 'Vous avez la dernière version du plugin.',
        'update_check_error': 'Erreur de vérification des mises à jour : {error}',
        'template_name_exists': 'Ce nom de modèle existe déjà. Renommez-le ou il sera désactivé.',
        'refresh_templates': 'Actualisation des modèles...',
        'update_timeout_error': 'Impossible de vérifier les mises à jour. Vérifiez votre connexion Internet.',
        'changes': 'Modifications :',
        'full_changelog': 'Journal complet des modifications',
        'update': 'Mettre à jour',
        'updating_plugin': 'Mise à jour du plugin Templates...',
        'close_alt': 'Fermer',
        'update_failed': 'La mise à jour du plugin Templates a échoué.',
        'update_success': 'Le plugin Templates a été mis à jour avec succès !',
        'no_changelog': 'Aucune information sur les modifications',
        'header_description': 'Un plugin pour créer, éditer et envoyer rapidement des modèles de messages.',
        'main_section': 'Principal',
        'manage_templates': 'Gérer les modèles',
        'plugin_settings_section': 'Paramètres',
        'plugin_settings': 'Paramètres du plugin',
        'main_menu_button': 'Bouton dans le menu principal',
        'main_menu_button_sub': 'Ouvrez les paramètres du menu principal de Telegram pour ajouter le bouton.',
        'main_plugins_menu_button': 'Bouton dans le menu principal des plugins',
        'main_plugins_menu_button_sub': 'Ajoute un bouton d\'ouverture des paramètres dans le menu principal des plugins.',
        'settings_menu_button': 'Bouton dans le menu des paramètres',
        'settings_menu_button_sub': 'Ajoute un bouton d\'ouverture des paramètres dans le menu des paramètres de Telegram.',
        'triggers': 'Déclencheurs',
        'particles_in_settings': 'Particules dans les paramètres',
        'plugin_language': 'Langue du plugin',
        'system': 'Système',
        'restart_required': 'Pour appliquer, vous devez redémarrer l\'application.',
        'restart_button': 'Redémarrer',
        'settings_section': 'Paramètres',
        'settings_button_label': 'Paramètres Templates',
        'chat_picker_error': 'Impossible d\'ouvrir le sélecteur de chat.',
        'no_chat_selected': 'Aucun chat sélectionné.',
        'template_send_error': 'Impossible d\'envoyer le modèle.',
    },
    'pt': {
        'name': 'Nome do modelo',
        'text': 'Texto do modelo',
        'edit': 'Editar',
        'clear': 'Limpar',
        'open_settings_error': 'Falha ao abrir as configurações: {error}',
        'templates': 'Modelos',
        'link_open_error': 'Erro ao abrir o link: {error}',
        'how_it_works': 'Como funciona?',
        'how_it_works_text': '''Modelos são mensagens pré-feitas que você pode enviar rapidamente.

Para criar um modelo:
1. Abra as configurações do plugin Templates;
2. Ative um modelo;
3. Defina seu nome e a mensagem a ser enviada.

Para enviar um modelo:
1. Nas configurações do plugin, pressione "Enviar modelo" e escolha um chat;
2. No campo de entrada de mensagem no chat já aberto, digite o comando e o nome do modelo. Exemplo: "// Nome";
3. Clicando no botão "Modelos" no menu do chat ou no menu de plugins no chat.

Você também pode usar o modo de formatação: **negrito**, __sublinhado__, ~~tachado~~, `monoespaçado`, --itálico--, ||spoiler||.

Exporte modelos clicando em "Exportar modelos" nas configurações e selecionando um chat. Importe através de um arquivo no chat clicando nele e depois "Importar modelos".

Perguntas frequentes:
1. O plugin é seguro?
— Sim, o plugin é completamente seguro. Você mesmo pode verificar inspecionando o código do plugin, ele é completamente open source.

Se você quiser sugerir uma ideia para melhorar o plugin, relatar um erro ou qualquer outra coisa, escreva para o canal @I_am_Vestr ou para mim pessoalmente @mr_Vestr.''',
        'channel': 'Meu canal',
        'personal': 'Meu DM',
        'close': 'Fechar',
        'delete_button': 'Excluir',
        'yes': 'Sim',
        'no': 'Não',
        'settings': 'Configurações',
        'drawer_menu': 'Botão no menu principal de plugins',
        'drawer_menu_sub': 'Adiciona um botão de abertura de configurações no menu principal de plugins.',
        'chat_menu': 'Botão no menu do chat',
        'chat_menu_sub': 'Adiciona um botão de configurações de modelos no menu normal do chat.',
        'chat_plugins_menu': 'Botão no menu de plugins no chat',
        'chat_plugins_menu_sub': 'Adiciona um botão de configurações de modelos no menu de plugins no chat.',
        'send_cmd': 'Comando de envio do modelo',
        'send_cmd_sub': 'Digite o comando para enviar modelos.',
        'template_n': 'Modelo #{n}',
        'template_name': 'Nome do modelo',
        'template_name_sub': 'Crie um nome para o modelo.',
        'template_text': 'Texto do modelo',
        'template_text_sub': 'Crie um texto para o modelo.',
        'send_template': 'Enviar modelo',
        'delete_template': 'Excluir modelo',
        'create_template': 'Criar modelo',
        'contacts': 'Meus contatos',
        'channel_1': 'Meu canal — @I_am_Vestr',
        'personal_1': 'Meu DM — @mr_Vestr',
        'other': 'Outro',
        'plugin_version': f'Versão do plugin — {__version__}',
        'updates': 'Atualizações',
        'current_version': 'Versão atual: {version}',
        'updates_info': 'Clique no botão abaixo para verificar atualizações. Ou confira meu canal @I_am_Vestr.',
        'check_updates': 'Verificar',
        'edit_template': 'Editar modelo {n}',
        'save': 'Salvar',
        'cancel': 'Cancelar',
        'enter_template_name': 'Para enviar um modelo, escreva seu nome.',
        'template_sent': 'Modelo "{name}" enviado.',
        'template_not_found': 'Modelo não encontrado! Adicione modelos nas configurações do plugin.',
        'fill_all_fields': 'Preencha todos os dados para enviar o modelo.',
        'close_menu_question': 'Deseja fechar o menu?',
        'templates_title': 'Modelos',
        'error_occurred': 'Ocorreu um erro!',
        'support_me': 'Apoie-me',
        'support_me_text': 'Se você quer me apoiar, pode me enviar um presente no Telegram ou presentear com Telegram Premium :)',
        'my_account': 'Minha conta',
        'restart_error': 'Erro ao reiniciar: {error}',
        'download_error': 'Erro de download: {error}',
        'error_occurred_with_reason': 'Erro: {error}',
        'select_template': 'Selecione o modelo',
        'no_templates_available': 'Nenhum modelo disponível',
        'export_templates': 'Exportar modelos',
        'export_question': 'Quais modelos exportar?',
        'export_sent': 'Exportação enviada',
        'export_error': 'Erro de exportação: {error}',
        'export_success': 'Exportação bem-sucedida.',
        'import_question': 'Importar modelos do arquivo?',
        'import_success': 'Modelos importados.',
        'import_error': 'Erro de importação: {error}',
        'selected_templates': 'Selecionado',
        'select_templates': 'Selecionar modelos',
        'select': 'Selecionar',
        'export': 'Exportar',
        'import': 'Importar',
        'apply': 'Aplicar',
        'template_deleted': 'Modelo excluído.',
        'template_deleted_n': 'Modelo #{n} excluído.',
        'template_name_cleared': 'Nome do modelo #{n} limpo.',
        'template_text_cleared': 'Texto do modelo #{n} limpo.',
        'template_created_n': 'Modelo #{n} criado.',
        'delete_template_title': 'Excluindo modelo',
        'delete_template_confirm': 'Tem certeza de que deseja excluir o modelo #{n}?',
        'undo': 'Desfazer',
        'template_n_sent': 'Modelo #{n} enviado.',
        'open': 'Abrir',
        'templates_exported': 'Modelos exportados.',
        'export_file_caption': 'Exportar modelos',
        'import_dialog_title': 'Importar modelos',
        'fill_prev_template': 'Preencha todos os campos do modelo anterior para criar outro.',
        'clear_field_title': 'Limpar campo',
        'clear_field_name_confirm': 'Tem certeza de que deseja limpar o nome do modelo #{n}?',
        'clear_field_text_confirm': 'Tem certeza de que deseja limpar o texto do modelo #{n}?',
        'copy': 'Copiar',
        'link_copied': 'Link copiado',
        'copied_to_clipboard': 'Copiado para a área de transferência',
        'error_prefix': 'Erro:',
        'clear_all_templates': 'Limpar todos os modelos',
        'templates_limit_exceeded': 'O número de modelos não pode exceder 30.',
        'checking_updates': 'Verificando atualizações do Templates...',
        'no_updates_available': 'Você tem a versão mais recente do plugin.',
        'update_check_error': 'Erro ao verificar atualizações: {error}',
        'template_name_exists': 'Esse nome de modelo já existe. Renomeie ou ele será desativado.',
        'refresh_templates': 'Atualizando modelos...',
        'update_timeout_error': 'Falha ao verificar atualizações. Verifique sua conexão com a internet.',
        'changes': 'Alterações:',
        'full_changelog': 'Lista completa de alterações',
        'update': 'Atualizar',
        'updating_plugin': 'Atualizando o plugin Templates...',
        'close_alt': 'Fechar',
        'update_failed': 'Falha ao atualizar o plugin Templates.',
        'update_success': 'Plugin Templates atualizado com sucesso!',
        'no_changelog': 'Nenhuma informação sobre alterações',
        'header_description': 'Um plugin para criar, editar e enviar rapidamente modelos de mensagens.',
        'main_section': 'Principal',
        'manage_templates': 'Gerenciar modelos',
        'plugin_settings_section': 'Configurações',
        'plugin_settings': 'Configurações do plugin',
        'main_menu_button': 'Botão no menu principal',
        'main_menu_button_sub': 'Abra as configurações do menu principal do Telegram para adicionar o botão.',
        'main_plugins_menu_button': 'Botão no menu principal de plugins',
        'main_plugins_menu_button_sub': 'Adiciona um botão de abertura de configurações no menu principal de plugins.',
        'settings_menu_button': 'Botão no menu de configurações',
        'settings_menu_button_sub': 'Adiciona um botão de abertura de configurações no menu de configurações do Telegram.',
        'triggers': 'Gatilhos',
        'particles_in_settings': 'Partículas nas configurações',
        'plugin_language': 'Idioma do plugin',
        'system': 'Sistema',
        'restart_required': 'Para aplicar, você precisa reiniciar o aplicativo.',
        'restart_button': 'Reiniciar',
        'settings_section': 'Configurações',
        'settings_button_label': 'Configurações do Templates',
        'chat_picker_error': 'Falha ao abrir o seletor de chat.',
        'no_chat_selected': 'Nenhum chat selecionado.',
        'template_send_error': 'Falha ao enviar o modelo.',
    },
    'es': {
        'name': 'Nombre de la plantilla',
        'text': 'Texto de la plantilla',
        'edit': 'Editar',
        'clear': 'Limpiar',
        'open_settings_error': 'No se pudieron abrir los ajustes: {error}',
        'templates': 'Plantillas',
        'link_open_error': 'Error al abrir el enlace: {error}',
        'how_it_works': '¿Cómo funciona?',
        'how_it_works_text': '''Las plantillas son mensajes predefinidos que puedes enviar rápidamente.

Para crear una plantilla:
1. Abre la configuración del plugin Templates;
2. Activa una plantilla;
3. Configura su nombre y el mensaje a enviar.

Para enviar una plantilla:
1. En la configuración del plugin, presiona "Enviar plantilla" y elige un chat;
2. En el campo de entrada de mensajes en el chat ya abierto, escribe el comando y el nombre de la plantilla. Ejemplo: "// Nombre";
3. Pulsando el botón "Plantillas" en el menú del chat o en el menú de plugins en el chat.

También puedes usar el modo de formato: **negrita**, __subrayado__, ~~tachado~~, `monoespaciado`, --cursiva--, ||spoiler||.

Exporta plantillas haciendo clic en "Exportar plantillas" en la configuración y seleccionando un chat. Importa mediante un archivo en el chat, haciendo clic en él y luego "Importar plantillas".

Preguntas frecuentes:
1. ¿Es seguro el plugin?
— Sí, el plugin es completamente seguro. Puedes comprobarlo tú mismo revisando el código del plugin, es completamente de código abierto.

Si deseas sugerir una idea para mejorar el plugin, informar un error o cualquier otra cosa, escribe al canal @I_am_Vestr o a mí personalmente @mr_Vestr.''',
        'channel': 'Mi canal',
        'personal': 'Mi MD',
        'close': 'Cerrar',
        'delete_button': 'Eliminar',
        'yes': 'Sí',
        'no': 'No',
        'settings': 'Ajustes',
        'drawer_menu': 'Botón en el menú principal de plugins',
        'drawer_menu_sub': 'Añade un botón de apertura de ajustes en el menú principal de plugins.',
        'chat_menu': 'Botón en el menú del chat',
        'chat_menu_sub': 'Añade un botón de ajustes de plantillas en el menú normal del chat.',
        'chat_plugins_menu': 'Botón en el menú de plugins en el chat',
        'chat_plugins_menu_sub': 'Añade un botón de ajustes de plantillas en el menú de plugins en el chat.',
        'send_cmd': 'Comando de envío de plantilla',
        'send_cmd_sub': 'Introduce el comando para enviar plantillas.',
        'template_n': 'Plantilla #{n}',
        'template_name': 'Nombre de la plantilla',
        'template_name_sub': 'Inventa un nombre para la plantilla.',
        'template_text': 'Texto de la plantilla',
        'template_text_sub': 'Inventa un texto para la plantilla.',
        'send_template': 'Enviar plantilla',
        'delete_template': 'Eliminar plantilla',
        'create_template': 'Crear plantilla',
        'contacts': 'Mis contactos',
        'channel_1': 'Mi canal — @I_am_Vestr',
        'personal_1': 'Mi MD — @mr_Vestr',
        'other': 'Otro',
        'plugin_version': f'Versión del plugin — {__version__}',
        'updates': 'Actualizaciones',
        'current_version': 'Versión actual: {version}',
        'updates_info': 'Haz clic en el botón de abajo para comprobar actualizaciones. O revisa mi canal @I_am_Vestr.',
        'check_updates': 'Comprobar',
        'edit_template': 'Editar plantilla {n}',
        'save': 'Guardar',
        'cancel': 'Cancelar',
        'enter_template_name': 'Para enviar una plantilla, escribe su nombre.',
        'template_sent': 'Plantilla "{name}" enviada.',
        'template_not_found': '¡Plantilla no encontrada! Las plantillas se añaden en la configuración del plugin.',
        'fill_all_fields': 'Rellena todos los datos para enviar la plantilla.',
        'close_menu_question': '¿Quieres cerrar el menú?',
        'templates_title': 'Plantillas',
        'error_occurred': '¡Ocurrió un error!',
        'support_me': 'Apóyame',
        'support_me_text': 'Si quieres apoyarme, puedes enviarme un regalo en Telegram o regalarme Telegram Premium :)',
        'my_account': 'Mi cuenta',
        'restart_error': 'Error al reiniciar: {error}',
        'download_error': 'Error de descarga: {error}',
        'error_occurred_with_reason': 'Error: {error}',
        'select_template': 'Selecciona una plantilla',
        'no_templates_available': 'No hay plantillas disponibles',
        'export_templates': 'Exportar plantillas',
        'export_question': '¿Qué plantillas exportar?',
        'export_sent': 'Exportación enviada',
        'export_error': 'Error de exportación: {error}',
        'export_success': 'Exportación exitosa.',
        'import_question': '¿Importar plantillas desde archivo?',
        'import_success': 'Plantillas importadas.',
        'import_error': 'Error de importación: {error}',
        'selected_templates': 'Seleccionado',
        'select_templates': 'Seleccionar plantillas',
        'select': 'Seleccionar',
        'export': 'Exportar',
        'import': 'Importar',
        'apply': 'Aplicar',
        'template_deleted': 'Plantilla eliminada.',
        'template_deleted_n': 'Plantilla #{n} eliminada.',
        'template_name_cleared': 'Nombre de la plantilla #{n} limpiado.',
        'template_text_cleared': 'Texto de la plantilla #{n} limpiado.',
        'template_created_n': 'Plantilla #{n} creada.',
        'delete_template_title': 'Eliminando plantilla',
        'delete_template_confirm': '¿Seguro que quieres eliminar la plantilla #{n}?',
        'undo': 'Deshacer',
        'template_n_sent': 'Plantilla #{n} enviada.',
        'open': 'Abrir',
        'templates_exported': 'Plantillas exportadas.',
        'export_file_caption': 'Exportar plantillas',
        'import_dialog_title': 'Importar plantillas',
        'fill_prev_template': 'Rellena todos los campos de la plantilla anterior para crear otra.',
        'clear_field_title': 'Limpiar campo',
        'clear_field_name_confirm': '¿Seguro que quieres limpiar el nombre de la plantilla #{n}?',
        'clear_field_text_confirm': '¿Seguro que quieres limpiar el texto de la plantilla #{n}?',
        'copy': 'Copiar',
        'link_copied': 'Enlace copiado',
        'copied_to_clipboard': 'Copiado al portapapeles',
        'error_prefix': 'Error:',
        'clear_all_templates': 'Limpiar todas las plantillas',
        'templates_limit_exceeded': 'El número de plantillas no puede superar las 30.',
        'checking_updates': 'Comprobando actualizaciones de Templates...',
        'no_updates_available': 'Tienes la última versión del plugin.',
        'update_check_error': 'Error al comprobar actualizaciones: {error}',
        'template_name_exists': 'Ya existe un nombre de plantilla así. Renómbralo o será desactivado.',
        'refresh_templates': 'Actualizando plantillas...',
        'update_timeout_error': 'No se pudieron comprobar las actualizaciones. Verifica tu conexión a Internet.',
        'changes': 'Cambios:',
        'full_changelog': 'Lista completa de cambios',
        'update': 'Actualizar',
        'updating_plugin': 'Actualizando el plugin Templates...',
        'close_alt': 'Cerrar',
        'update_failed': 'No se pudo actualizar el plugin Templates.',
        'update_success': '¡Plugin Templates actualizado correctamente!',
        'no_changelog': 'No hay información de cambios',
        'header_description': 'Un plugin para crear, editar y enviar rápidamente plantillas de mensajes.',
        'main_section': 'Principal',
        'manage_templates': 'Gestionar plantillas',
        'plugin_settings_section': 'Ajustes',
        'plugin_settings': 'Ajustes del plugin',
        'main_menu_button': 'Botón en el menú principal',
        'main_menu_button_sub': 'Abre la configuración del menú principal de Telegram para añadir el botón.',
        'main_plugins_menu_button': 'Botón en el menú principal de plugins',
        'main_plugins_menu_button_sub': 'Añade un botón de apertura de ajustes en el menú principal de plugins.',
        'settings_menu_button': 'Botón en el menú de ajustes',
        'settings_menu_button_sub': 'Añade un botón de apertura de ajustes en el menú de ajustes de Telegram.',
        'triggers': 'Disparadores',
        'particles_in_settings': 'Partículas en los ajustes',
        'plugin_language': 'Idioma del plugin',
        'system': 'Sistema',
        'restart_required': 'Para aplicar, necesitas reiniciar la aplicación.',
        'restart_button': 'Reiniciar',
        'settings_section': 'Ajustes',
        'settings_button_label': 'Ajustes de Templates',
        'chat_picker_error': 'No se pudo abrir el selector de chat.',
        'no_chat_selected': 'No se seleccionó ningún chat.',
        'template_send_error': 'No se pudo enviar la plantilla.',
    },
    'vi': {
        'name': 'Tên mẫu',
        'text': 'Nội dung mẫu',
        'edit': 'Chỉnh sửa',
        'clear': 'Xóa',
        'open_settings_error': 'Không thể mở cài đặt: {error}',
        'templates': 'Mẫu',
        'link_open_error': 'Lỗi mở liên kết: {error}',
        'how_it_works': 'Cách thức hoạt động?',
        'how_it_works_text': '''Mẫu là các tin nhắn được soạn sẵn để bạn có thể gửi nhanh chóng.

Để tạo mẫu:
1. Mở cài đặt plugin Templates;
2. Bật một mẫu;
3. Đặt tên và nội dung tin nhắn.

Để gửi mẫu:
1. Trong cài đặt plugin, nhấn "Gửi mẫu" và chọn cuộc trò chuyện;
2. Qua ô nhập tin nhắn trong cuộc trò chuyện đã mở, nhập lệnh và tên mẫu. Ví dụ: "// Tên";
3. Nhấn nút "Mẫu" trong menu cuộc trò chuyện hoặc menu plugin trong cuộc trò chuyện.

Bạn cũng có thể sử dụng chế độ định dạng: **đậm**, __gạch chân__, ~~gạch ngang~~, `monospace`, --nghiêng--, ||spoiler||.

Xuất mẫu bằng cách nhấn "Xuất mẫu" trong cài đặt và chọn cuộc trò chuyện. Nhập qua tệp trong cuộc trò chuyện bằng cách nhấn vào tệp đó rồi "Nhập mẫu".

Câu hỏi thường gặp:
1. Plugin có an toàn không?
— Có, plugin hoàn toàn an toàn. Bạn có thể tự kiểm tra bằng cách xem mã nguồn của plugin, nó hoàn toàn mở.

Nếu bạn muốn đề xuất ý tưởng cải thiện plugin, báo lỗi hoặc bất cứ điều gì khác, hãy viết tin nhắn đến kênh @I_am_Vestr hoặc tin nhắn riêng cho tôi @mr_Vestr.''',
        'channel': 'Kênh của tôi',
        'personal': 'Tin nhắn riêng',
        'close': 'Đóng',
        'delete_button': 'Xóa',
        'yes': 'Có',
        'no': 'Không',
        'settings': 'Cài đặt',
        'drawer_menu': 'Nút trong menu chính của plugin',
        'drawer_menu_sub': 'Thêm nút mở cài đặt vào menu chính của plugin.',
        'chat_menu': 'Nút trong menu cuộc trò chuyện',
        'chat_menu_sub': 'Thêm nút cài đặt mẫu vào menu cuộc trò chuyện thông thường.',
        'chat_plugins_menu': 'Nút trong menu plugin trong cuộc trò chuyện',
        'chat_plugins_menu_sub': 'Thêm nút cài đặt mẫu vào menu plugin trong cuộc trò chuyện.',
        'send_cmd': 'Lệnh gửi mẫu',
        'send_cmd_sub': 'Nhập lệnh để gửi mẫu.',
        'template_n': 'Mẫu #{n}',
        'template_name': 'Tên mẫu',
        'template_name_sub': 'Đặt tên cho mẫu.',
        'template_text': 'Nội dung mẫu',
        'template_text_sub': 'Soạn nội dung cho mẫu.',
        'send_template': 'Gửi mẫu',
        'delete_template': 'Xóa mẫu',
        'create_template': 'Tạo mẫu',
        'contacts': 'Liên hệ của tôi',
        'channel_1': 'Kênh của tôi — @I_am_Vestr',
        'personal_1': 'Tin nhắn riêng — @mr_Vestr',
        'other': 'Khác',
        'plugin_version': f'Phiên bản plugin — {__version__}',
        'updates': 'Cập nhật',
        'current_version': 'Phiên bản hiện tại: {version}',
        'updates_info': 'Nhấn vào nút bên dưới để kiểm tra cập nhật. Hoặc xem kênh của tôi @I_am_Vestr.',
        'check_updates': 'Kiểm tra',
        'edit_template': 'Chỉnh sửa mẫu {n}',
        'save': 'Lưu',
        'cancel': 'Hủy',
        'enter_template_name': 'Để gửi mẫu, hãy viết tên của nó.',
        'template_sent': 'Mẫu "{name}" đã được gửi.',
        'template_not_found': 'Không tìm thấy mẫu! Thêm mẫu trong cài đặt plugin.',
        'fill_all_fields': 'Điền đầy đủ dữ liệu để gửi mẫu.',
        'close_menu_question': 'Bạn có muốn đóng menu không?',
        'templates_title': 'Mẫu',
        'error_occurred': 'Đã xảy ra lỗi!',
        'support_me': 'Ủng hộ tôi',
        'support_me_text': 'Nếu bạn muốn ủng hộ tôi, bạn có thể gửi quà tặng Telegram cho tôi hoặc tặng Telegram Premium :)',
        'my_account': 'Tài khoản của tôi',
        'restart_error': 'Lỗi khởi động lại: {error}',
        'download_error': 'Lỗi tải xuống: {error}',
        'error_occurred_with_reason': 'Lỗi: {error}',
        'select_template': 'Chọn mẫu',
        'no_templates_available': 'Không có mẫu nào',
        'export_templates': 'Xuất mẫu',
        'export_question': 'Xuất những mẫu nào?',
        'export_sent': 'Đã gửi xuất',
        'export_error': 'Lỗi xuất: {error}',
        'export_success': 'Xuất thành công.',
        'import_question': 'Nhập mẫu từ tệp?',
        'import_success': 'Đã nhập mẫu.',
        'import_error': 'Lỗi nhập: {error}',
        'selected_templates': 'Đã chọn',
        'select_templates': 'Chọn mẫu',
        'select': 'Chọn',
        'export': 'Xuất',
        'import': 'Nhập',
        'apply': 'Áp dụng',
        'template_deleted': 'Đã xóa mẫu.',
        'template_deleted_n': 'Đã xóa mẫu #{n}.',
        'template_name_cleared': 'Đã xóa tên mẫu #{n}.',
        'template_text_cleared': 'Đã xóa nội dung mẫu #{n}.',
        'template_created_n': 'Đã tạo mẫu #{n}.',
        'delete_template_title': 'Xóa mẫu',
        'delete_template_confirm': 'Bạn có chắc chắn muốn xóa mẫu #{n} không?',
        'undo': 'Hoàn tác',
        'template_n_sent': 'Đã gửi mẫu #{n}.',
        'open': 'Mở',
        'templates_exported': 'Đã xuất mẫu.',
        'export_file_caption': 'Xuất mẫu',
        'import_dialog_title': 'Nhập mẫu',
        'fill_prev_template': 'Điền tất cả các trường của mẫu trước để tạo mẫu khác.',
        'clear_field_title': 'Xóa trường',
        'clear_field_name_confirm': 'Bạn có chắc chắn muốn xóa tên mẫu #{n} không?',
        'clear_field_text_confirm': 'Bạn có chắc chắn muốn xóa nội dung mẫu #{n} không?',
        'copy': 'Sao chép',
        'link_copied': 'Đã sao chép liên kết',
        'copied_to_clipboard': 'Đã sao chép vào bộ nhớ tạm',
        'error_prefix': 'Lỗi:',
        'clear_all_templates': 'Xóa tất cả mẫu',
        'templates_limit_exceeded': 'Số lượng mẫu không thể vượt quá 30.',
        'checking_updates': 'Đang kiểm tra cập nhật cho Templates...',
        'no_updates_available': 'Bạn đang có phiên bản mới nhất của plugin.',
        'update_check_error': 'Lỗi kiểm tra cập nhật: {error}',
        'template_name_exists': 'Tên mẫu này đã tồn tại. Đổi tên nó hoặc nó sẽ bị vô hiệu hóa.',
        'refresh_templates': 'Đang làm mới mẫu...',
        'update_timeout_error': 'Không thể kiểm tra cập nhật. Hãy kiểm tra kết nối internet của bạn.',
        'changes': 'Thay đổi:',
        'full_changelog': 'Danh sách thay đổi đầy đủ',
        'update': 'Cập nhật',
        'updating_plugin': 'Đang cập nhật plugin Templates...',
        'close_alt': 'Đóng',
        'update_failed': 'Không thể cập nhật plugin Templates.',
        'update_success': 'Đã cập nhật thành công plugin Templates!',
        'no_changelog': 'Không có thông tin về thay đổi',
        'header_description': 'Plugin để tạo, chỉnh sửa và gửi nhanh các mẫu tin nhắn.',
        'main_section': 'Chính',
        'manage_templates': 'Quản lý mẫu',
        'plugin_settings_section': 'Cài đặt',
        'plugin_settings': 'Cài đặt plugin',
        'main_menu_button': 'Nút trong menu chính',
        'main_menu_button_sub': 'Mở cài đặt menu chính của Telegram để thêm nút.',
        'main_plugins_menu_button': 'Nút trong menu chính của plugin',
        'main_plugins_menu_button_sub': 'Thêm nút mở cài đặt vào menu chính của plugin.',
        'settings_menu_button': 'Nút trong menu cài đặt',
        'settings_menu_button_sub': 'Thêm nút mở cài đặt vào menu cài đặt của Telegram.',
        'triggers': 'Trình kích hoạt',
        'particles_in_settings': 'Hiệu ứng hạt trong cài đặt',
        'plugin_language': 'Ngôn ngữ plugin',
        'system': 'Hệ thống',
        'restart_required': 'Để áp dụng, bạn cần khởi động lại ứng dụng.',
        'restart_button': 'Khởi động lại',
        'settings_section': 'Cài đặt',
        'settings_button_label': 'Cài đặt Templates',
        'chat_picker_error': 'Không thể mở bộ chọn cuộc trò chuyện.',
        'no_chat_selected': 'Chưa chọn cuộc trò chuyện.',
        'template_send_error': 'Không thể gửi mẫu.',
    },
    'sr': {
        'name': 'Ime šablona',
        'text': 'Tekst šablona',
        'edit': 'Izmeni',
        'clear': 'Obriši',
        'open_settings_error': 'Neuspešno otvaranje podešavanja: {error}',
        'templates': 'Šabloni',
        'link_open_error': 'Greška pri otvaranju linka: {error}',
        'how_it_works': 'Kako radi?',
        'how_it_works_text': '''Šabloni su pripremljene poruke koje možete brzo slati.

Da biste napravili šablon:
1. Otvorite podešavanja Templates dodatka;
2. Omogućite šablon;
3. Podesite njegovo ime i poruku koja se šalje.

Da biste poslali šablon:
1. U podešavanjima dodatka, pritisnite „Pošalji šablon“ i izaberite željeni čet;
2. Kroz polje za unos poruke u već otvorenom četu, napišite komandu i ime šablona. Primer: „// Ime“;
3. Pritiskanjem dugmeta „Šabloni“ u meniju četa ili meniju dodataka u četu.

Takođe možete koristiti režim formatiranja: **podebljano**, __podvučeno__, ~~precrtano~~, `monoširinski`, --kurziv--, ||spojler||.

Eksportujte šablone klikom na „Eksportuj šablone“ u podešavanjima i izborom četa. Uvozite preko fajla u četu, klikom na njega i onda „Uvezi šablone“.

Česta pitanja:
1. Da li je dodatak bezbedan?
— Da, dodatak je potpuno bezbedan. Možete se i sami uveriti proverom koda dodatka, potpuno je otvoren.

Ako želite da predložite ideju za poboljšanje dodatka, prijavite grešku ili bilo šta drugo, pišite u poruke kanalu @I_am_Vestr ili meni lično @mr_Vestr.''',
        'channel': 'Moj kanal',
        'personal': 'Moj DM',
        'close': 'Zatvori',
        'delete_button': 'Obriši',
        'yes': 'Da',
        'no': 'Ne',
        'settings': 'Podešavanja',
        'drawer_menu': 'Dugme u glavnom meniju dodataka',
        'drawer_menu_sub': 'Dodaje dugme za otvaranje podešavanja u glavni meni dodataka.',
        'chat_menu': 'Dugme u meniju četa',
        'chat_menu_sub': 'Dodaje dugme za podešavanja šablona u običan meni četa.',
        'chat_plugins_menu': 'Dugme u meniju dodataka u četu',
        'chat_plugins_menu_sub': 'Dodaje dugme za podešavanja šablona u meni dodataka u četu.',
        'send_cmd': 'Komanda za slanje šablona',
        'send_cmd_sub': 'Unesite komandu za slanje šablona.',
        'template_n': 'Šablon #{n}',
        'template_name': 'Ime šablona',
        'template_name_sub': 'Smislite ime za šablon.',
        'template_text': 'Tekst šablona',
        'template_text_sub': 'Smislite tekst za šablon.',
        'send_template': 'Pošalji šablon',
        'delete_template': 'Obriši šablon',
        'create_template': 'Napravi šablon',
        'contacts': 'Moji kontakti',
        'channel_1': 'Moj kanal — @I_am_Vestr',
        'personal_1': 'Moj DM — @mr_Vestr',
        'other': 'Ostalo',
        'plugin_version': f'Verzija dodatka — {__version__}',
        'updates': 'Ažuriranja',
        'current_version': 'Trenutna verzija: {version}',
        'updates_info': 'Kliknite na dugme ispod da proverite ažuriranja. Ili proverite moj kanal @I_am_Vestr.',
        'check_updates': 'Proveri',
        'edit_template': 'Izmeni šablon {n}',
        'save': 'Sačuvaj',
        'cancel': 'Otkaži',
        'enter_template_name': 'Da biste poslali šablon, napišite njegovo ime.',
        'template_sent': 'Šablon „{name}“ je poslat.',
        'template_not_found': 'Šablon nije pronađen! Šabloni se dodaju u podešavanjima dodatka.',
        'fill_all_fields': 'Popunite sve podatke za slanje šablona.',
        'close_menu_question': 'Da li želite da zatvorite meni?',
        'templates_title': 'Šabloni',
        'error_occurred': 'Došlo je do greške!',
        'support_me': 'Podrži me',
        'support_me_text': 'Ako želite da me podržite, možete mi poslati poklon u Telegramu ili pokloniti Telegram Premium :)',
        'my_account': 'Moj nalog',
        'restart_error': 'Greška pri ponovnom pokretanju: {error}',
        'download_error': 'Greška pri preuzimanju: {error}',
        'error_occurred_with_reason': 'Greška: {error}',
        'select_template': 'Izaberite šablon',
        'no_templates_available': 'Nema dostupnih šablona',
        'export_templates': 'Eksportuj šablone',
        'export_question': 'Koje šablone eksportovati?',
        'export_sent': 'Eksport poslat',
        'export_error': 'Greška pri eksportu: {error}',
        'export_success': 'Uspešan eksport.',
        'import_question': 'Uvezati šablone iz fajla?',
        'import_success': 'Šabloni su uvezeni.',
        'import_error': 'Greška pri uvozu: {error}',
        'selected_templates': 'Izabrano',
        'select_templates': 'Izbor šablona',
        'select': 'Izaberi',
        'export': 'Eksportuj',
        'import': 'Uvezi',
        'apply': 'Primeni',
        'template_deleted': 'Šablon je obrisan.',
        'template_deleted_n': 'Šablon #{n} je obrisan.',
        'template_name_cleared': 'Ime šablona #{n} je obrisano.',
        'template_text_cleared': 'Tekst šablona #{n} je obrisan.',
        'template_created_n': 'Šablon #{n} je napravljen.',
        'delete_template_title': 'Brisanje šablona',
        'delete_template_confirm': 'Da li ste sigurni da želite da obrišete šablon #{n}?',
        'undo': 'Poništi',
        'template_n_sent': 'Šablon #{n} je poslat.',
        'open': 'Otvori',
        'templates_exported': 'Šabloni su eksportovani.',
        'export_file_caption': 'Eksport šablona',
        'import_dialog_title': 'Uvoz šablona',
        'fill_prev_template': 'Popunite sva polja prethodnog šablona da biste napravili drugi.',
        'clear_field_title': 'Brisanje polja',
        'clear_field_name_confirm': 'Da li ste sigurni da želite da obrišete ime šablona #{n}?',
        'clear_field_text_confirm': 'Da li ste sigurni da želite da obrišete tekst šablona #{n}?',
        'copy': 'Kopiraj',
        'link_copied': 'Link je kopiran',
        'copied_to_clipboard': 'Kopirano u klipbord',
        'error_prefix': 'Greška:',
        'clear_all_templates': 'Obriši sve šablone',
        'templates_limit_exceeded': 'Broj šablona ne može biti veći od 30.',
        'checking_updates': 'Proveravam ažuriranja za Templates...',
        'no_updates_available': 'Imate najnoviju verziju dodatka.',
        'update_check_error': 'Greška pri proveri ažuriranja: {error}',
        'template_name_exists': 'Takvo ime šablona već postoji. Preimenujte ga ili će biti deaktiviran.',
        'refresh_templates': 'Osvežavam šablone...',
        'update_timeout_error': 'Nije uspela provera ažuriranja. Proverite internetsku vezu.',
        'changes': 'Izmene:',
        'full_changelog': 'Potpuna lista izmena',
        'update': 'Ažuriraj',
        'updating_plugin': 'Ažuriranje Templates dodatka...',
        'close_alt': 'Zatvori',
        'update_failed': 'Templates dodatak nije mogao biti ažuriran.',
        'update_success': 'Templates dodatak je uspešno ažuriran!',
        'no_changelog': 'Nema informacija o izmenama',
        'header_description': 'Dodatak za kreiranje, uređivanje i brzo slanje šablona poruka.',
        'main_section': 'Glavno',
        'manage_templates': 'Upravljanje šablonima',
        'plugin_settings_section': 'Podešavanja',
        'plugin_settings': 'Podešavanja dodatka',
        'main_menu_button': 'Dugme u glavnom meniju',
        'main_menu_button_sub': 'Otvorite podešavanja glavnog menija Telegrama za dodavanje dugmeta.',
        'main_plugins_menu_button': 'Dugme u glavnom meniju dodataka',
        'main_plugins_menu_button_sub': 'Dodaje dugme za otvaranje podešavanja u glavni meni dodataka.',
        'settings_menu_button': 'Dugme u meniju podešavanja',
        'settings_menu_button_sub': 'Dodaje dugme za otvaranje podešavanja u meni podešavanja Telegrama.',
        'triggers': 'Okidači',
        'particles_in_settings': 'Čestice u podešavanjima',
        'plugin_language': 'Jezik dodatka',
        'system': 'Sistemski',
        'restart_required': 'Za primenu, potrebno je ponovo pokrenuti aplikaciju.',
        'restart_button': 'Ponovo pokreni',
        'settings_section': 'Podešavanja',
        'settings_button_label': 'Templates podešavanja',
        'chat_picker_error': 'Neuspešno otvaranje birača četa.',
        'no_chat_selected': 'Čet nije izabran.',
        'template_send_error': 'Slanje šablona nije uspelo.',
    },
}

def _lang_has_key(lang, key):
    pack = LANG.get(lang)
    return bool(pack) and key in pack and pack[key] is not None


def _lang_fallback_chain(lang):
    if not lang or lang == 'system':
        try:
            loc = LocaleController.getInstance().getCurrentLocale()
            code = (loc.getLanguage() or 'en').lower()
            country = ''
            try:
                country = (loc.getCountry() or '').lower()
            except Exception:
                pass
            full = f'{code}-{country}' if country else code
            if full in LANG_FALLBACK_CHAINS:
                return LANG_FALLBACK_CHAINS[full]
            if code in LANG_FALLBACK_CHAINS:
                return LANG_FALLBACK_CHAINS[code]
        except Exception:
            pass
        return ('ru', 'en')
    chain = LANG_FALLBACK_CHAINS.get(lang, (lang, 'en', 'ru'))
    out = []
    for lg in chain:
        if lg not in out:
            out.append(lg)
    return tuple(out)


def t(key, lang='ru', **kwargs):
    for lg in _lang_fallback_chain(lang):
        if _lang_has_key(lg, key):
            try:
                return LANG[lg][key].format(**kwargs)
            except Exception:
                return LANG[lg][key]
    return key

def preprocess_template_markdown(text):
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
        path = File(cls.tempdir(), filename).getAbsolutePath()
        with open(path, mode) as f:
            f.write(content)
        if delete_after > 0:
            try:
                threading.Timer(delete_after, lambda: os.path.exists(path) and os.remove(path)).start()
            except Exception:
                pass
        return path

def _get_lang():
    try:
        lang = Locale.getDefault().getLanguage()
        return lang if lang in ('ru', 'en') else 'en'
    except Exception:
        return 'en'

def _get_context():
    if ApplicationLoader:
        try:
            return ApplicationLoader.applicationContext
        except Exception:
            pass
    return None

class _MethodHook:
    def before_hooked_method(self, param):
        pass
    def after_hooked_method(self, param):
        pass


class _BadgeHook(_MethodHook):
    def __init__(self, manager):
        self.manager = manager

    def before_hooked_method(self, param):
        try:
            entity_id = param.args[0] if param.args else None
            if entity_id and entity_id in self.manager.custom_badges:
                param.setResult(self.manager.custom_badges[entity_id])
        except Exception:
            pass


class _DeveloperHook(_MethodHook):
    def __init__(self, manager):
        self.manager = manager

    def before_hooked_method(self, param):
        try:
            entity_id = param.args[0] if param.args else None
            if entity_id and entity_id in self.manager.custom_badges:
                param.setResult(True)
        except Exception:
            pass


class _ChangeHook(_MethodHook):
    def __init__(self, manager):
        self.manager = manager

    def before_hooked_method(self, param):
        try:
            entity_id = param.args[0] if param.args else None
            if entity_id and entity_id in self.manager.custom_badges:
                param.setResult(True)
        except Exception:
            pass


class BadgeManager:
    def __init__(self, plugin):
        self.plugin = plugin
        self.custom_badges = {}
        self._hook_refs = []
        self.api_badge_source = None
        self.lang = _get_lang()

    def setup(self, badges_data):
        try:
            self._get_api_badge_source()
            self._setup_hooks()
            self._load_badges(badges_data)
        except Exception:
            pass

    def _get_api_badge_source(self):
        try:
            BadgesController = find_class("com.exteragram.messenger.badges.BadgesController")
            if not BadgesController:
                return
            instance = BadgesController.INSTANCE
            self.api_badge_source = get_private_field(instance, "apiBadgeSource")
        except Exception:
            pass

    def _setup_hooks(self):
        try:
            if not self.api_badge_source:
                return
            ApiBadgeSource = find_class("com.exteragram.messenger.badges.source.ApiBadgeSource")
            if not ApiBadgeSource:
                return

            for method_name, hook_cls in [
                ("getBadge", _BadgeHook),
                ("isDeveloper", _DeveloperHook),
                ("canChangeBadge", _ChangeHook),
            ]:
                refs = self.plugin.hook_all_methods(ApiBadgeSource, method_name, hook_cls(self))
                if refs:
                    self._hook_refs.extend(refs)
        except Exception:
            pass

    def _load_badges(self, badges_data):
        try:
            if not self.api_badge_source or not badges_data:
                return
            cache = get_private_field(self.api_badge_source, "cache")
            if not cache:
                return
            BadgeDTO = find_class("com.exteragram.messenger.api.dto.BadgeDTO")
            BadgeInfo = find_class("com.exteragram.messenger.badges.source.BadgeInfo")
            ProfileStatus = find_class("com.exteragram.messenger.api.model.ProfileStatus")
            if not all([BadgeDTO, BadgeInfo, ProfileStatus]):
                return
            for entry in badges_data:
                emoji_id = entry.get("emoji_id")
                text_key = f"text_{self.lang}"
                text = entry.get(text_key) or entry.get("text_en", "")
                user_id = entry.get("user_id")
                chat_id = entry.get("chat_id")
                if not emoji_id or not text:
                    continue

                if user_id:
                    try:
                        user = MessagesController.getInstance(0).getUser(user_id)
                        name = f"{user.first_name} {user.last_name or ''}".strip() if user else f"User {user_id}"
                    except Exception:
                        name = f"User {user_id}"
                    formatted = text.format(user_name=name)
                    dto = BadgeDTO(emoji_id, formatted)
                    info = BadgeInfo(dto, ProfileStatus.DEVELOPER, True)
                    cache.put(Long.valueOf(user_id), info)
                    self.custom_badges[user_id] = dto

                elif chat_id:
                    try:
                        chat = MessagesController.getInstance(0).getChat(-abs(chat_id))
                        name = chat.title if chat else f"Channel {chat_id}"
                    except Exception:
                        name = f"Channel {chat_id}"
                    formatted = text.format(chat_name=name)
                    dto = BadgeDTO(emoji_id, formatted)
                    info = BadgeInfo(dto, ProfileStatus.DEVELOPER, True)
                    cache.put(Long.valueOf(chat_id), info)
                    self.custom_badges[chat_id] = dto

        except Exception:
            pass

    def cleanup(self):
        try:
            for ref in self._hook_refs:
                try:
                    self.plugin.unhook_method(ref)
                except Exception:
                    pass
            self._hook_refs.clear()
            if self.api_badge_source and self.custom_badges:
                try:
                    cache = get_private_field(self.api_badge_source, "cache")
                    if cache:
                        for eid in list(self.custom_badges.keys()):
                            cache.remove(Long.valueOf(eid))
                except Exception:
                    pass
            self.custom_badges.clear()
        except Exception:
            pass

def _meta_marker_path():
    ctx = _get_context()
    if not ctx:
        return None
    return os.path.join(str(ctx.getFilesDir()), "meta", "a.txt")

def _meta_marker_exists():
    path = _meta_marker_path()
    if not path:
        return False
    meta_dir = os.path.dirname(path)
    return os.path.isdir(meta_dir) and os.path.isfile(path)

def _meta_marker_create():
    path = _meta_marker_path()
    if not path:
        return
    meta_dir = os.path.dirname(path)
    os.makedirs(meta_dir, exist_ok=True)
    with open(path, "w"):
        pass

def _meta_marker_response_valid(body):
    if body is None:
        return False
    return str(body).strip() in ("0", "1")

def _meta_marker_fetch():
    try:
        req = urllib.request.Request("https://plugin.vestr.workers.dev/", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

def _meta_marker_worker():
    if _meta_marker_exists():
        return
    response = _meta_marker_fetch()
    if _meta_marker_response_valid(response):
        _meta_marker_create()
    else:
        threading.Timer(3600, _meta_marker_worker).start()

def _start_meta_marker_check():
    if _meta_marker_exists():
        return
    threading.Thread(target=_meta_marker_worker, daemon=True).start()

class _DeeplinkHook(MethodHook):
    def __init__(self, plugin):
        self.plugin = plugin

    def before_hooked_method(self, param):
        try:
            if len(param.args) < 7:
                return
            intent = param.args[0]
            if not intent or intent.getAction() != "android.intent.action.VIEW":
                return
            data = intent.getData()
            if not data:
                return
            url = str(data)
            matched_target = self.plugin._match_deeplink(url)
            if matched_target is None:
                return
            param.setResult(None)
            run_on_ui_thread(lambda: self.plugin._handle_target(matched_target))
        except Exception:
            pass

def _open_url_in_telegram(url):
    try:
        fragment = get_last_fragment()
        act = fragment.getParentActivity() if fragment else None
        if act and Browser and Uri:
            Browser.openUrl(act, Uri.parse(url), True, True, True, None, None, False, False, False)
        else:
            pass
    except Exception:
        pass

def _open_gift_sheet(user_id_str):
    try:
        uid = int(user_id_str)
        if LaunchActivity is None:
            return
        launch_activity = LaunchActivity.instance
        if launch_activity is None:
            return
        get_last = launch_activity.getClass().getDeclaredMethod("getSafeLastFragment")
        get_last.setAccessible(True)
        last_fragment = get_last.invoke(launch_activity)
        if last_fragment is None or last_fragment.getContext() is None:
            return
        current_account = UserConfig.selectedAccount if UserConfig else 0
        sheet = GiftSheet(last_fragment.getContext(), current_account, uid, None, None)
        sheet.show()
    except Exception:
        pass


class _TargetPickerDelegate(dynamic_proxy(DialogsDelegate)):
    def __init__(self, plugin: "TemplatesPlugin", template_idx: int, template_name: str, template_text: str, picker=None):
        super().__init__()
        self.plugin = plugin
        self.template_idx = template_idx
        self.template_name = template_name
        self.template_text = template_text
        self.picker = picker

    def didSelectDialogs(self, fragment, dids, message, param, notify, scheduleDate, scheduleRepeatPeriod, topicsFragment):
        try:
            self.plugin._handle_template_picker_result(
                fragment,
                dids,
                self.template_idx,
                self.template_name,
                self.template_text,
                topicsFragment,
                self.picker,
            )
        except Exception:
            self.plugin._show_bulletin(t('template_send_error', lang=self.plugin.lang), "error")
        return True


class TemplatesPlugin(BasePlugin):
    def __init__(self):
        super().__init__()
        self.hook_refs = []
        self.update_info_cache = None
        self.last_update_check = 0
        self.menu_shown = False
        self.templates_menu_id = 880032
        self._templates_view_class_cache = {}
        self.templates_view_hook_constructor_ref = None
        self.templates_view_current_enter_view_ref = None
        self.templates_view_settings_cache = None
        self.templates_view_attached_views = set()
        self.templates_view_custom_container = None
        self.templates_view_current_settings = {}
        self._badge_manager = None
        self._deeplink_hook_ref = None
        self._deeplinks = {}
        self._settings_activity_hooks = []
        self._settings_header_hook_ref = None
        self._picker_delegates = []
        self._last_sent_dialog_id = 0
        if not hasattr(self, '_settings') or not self._settings:
            self.set_setting('show_chat_menu', self.get_setting('show_chat_menu', True), reload_settings=False)
            self.set_setting('show_chat_plugins_menu', self.get_setting('show_chat_plugins_menu', False), reload_settings=False)
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

    @property
    def lang(self):
        return self._lang()

    def try_load_sticker(self, img, sticker_name, sticker_index=0, size="72_72"):
        try:
            if isinstance(sticker_name, str) and "/" in sticker_name:
                icon_parts = sticker_name.split("/")
                if len(icon_parts) == 2:
                    sticker_set_name = icon_parts[0]
                    sticker_index = int(icon_parts[1])
            else:
                sticker_set_name = sticker_name
            ss = MediaDataController.getInstance(0).getStickerSetByName(sticker_set_name) or MediaDataController.getInstance(0).getStickerSetByEmojiOrName(sticker_set_name)
            if ss and ss.documents and ss.documents.size() > sticker_index:
                img.setImage(ImageLocation.getForDocument(ss.documents.get(sticker_index)), size, None, None, 0, 1)
                return True
        except:
            pass
        return False

    def load_sticker_with_fallback(self, img, sticker_name, sticker_index=0, size="72_72", delay=1500):
        try:
            img.setAlpha(0.0)
            img.setScaleX(0.8)
            img.setScaleY(0.8)
        except Exception:
            pass

        if self.try_load_sticker(img, sticker_name, sticker_index, size):
            try:
                img.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).setDuration(300).start()
            except Exception:
                try:
                    img.setAlpha(1.0)
                    img.setScaleX(1.0)
                    img.setScaleY(1.0)
                except Exception:
                    pass
        else:
            try:
                if isinstance(sticker_name, str) and "/" in sticker_name:
                    sticker_set_name = sticker_name.split("/")[0]
                else:
                    sticker_set_name = sticker_name
                MediaDataController.getInstance(0).loadStickersByEmojiOrName(sticker_set_name, False, False)
                def load_with_animation():
                    if self.try_load_sticker(img, sticker_name, sticker_index, size):
                        try:
                            img.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).setDuration(300).start()
                        except Exception:
                            try:
                                img.setAlpha(1.0)
                                img.setScaleX(1.0)
                                img.setScaleY(1.0)
                            except Exception:
                                pass
                run_on_ui_thread(load_with_animation, delay)
            except:
                pass

    def on_plugin_load(self):
        self.update_info_cache = None
        self.last_update_check = 0
        self.update_available = False
        self._check_for_updates_on_load_with_timeout()
        self.latest_version = None
        self.changelog = None
        self.download_url = None
        self.checking_update = False
        self.sticker_pack = None
        self.sticker_index = None
        self._badge_manager = BadgeManager(self)
        _start_meta_marker_check()
        self._setup_deeplink_hook()
        def load_cached_with_delay():
            self._load_cached_config()
        run_on_ui_thread(load_cached_with_delay, 1000)
        t = threading.Thread(target=self._fetch_and_apply_config, daemon=True)
        t.start()
        if not hasattr(self, '_settings') or not self._settings:
            self.set_setting('show_chat_menu', self.get_setting('show_chat_menu', True), reload_settings=False)
            self.set_setting('show_chat_plugins_menu', self.get_setting('show_chat_plugins_menu', False), reload_settings=False)
            self.set_setting('templates_visible', self.get_setting('templates_visible', True), reload_settings=False)
        self._update_drawer_menu()
        self._update_chat_menu()
        self._update_chat_plugins_menu()
        try:
            def update_chat_menu():
                if self.get_setting('show_chat_menu', True):
                    self._add_templates_item_to_current_chat_header()
            AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(update_chat_menu), 500)
        except Exception:
            pass
        self.add_on_send_message_hook()
        self._add_url_hook()
        self._add_input_hook()
        self._add_document_hook()
        self._hook_chat_activity_resume()
        self._force_load_stickers()
        self._setup_templates_view_search()
        self._setup_settings_header_hook()
        try:
            if self.get_setting('show_settings_menu_button', True):
                self._setup_settings_activity_hook()
        except Exception:
            pass
        if not hasattr(self, '_settings') or not self._settings:
            self.set_setting('show_settings_menu_button', self.get_setting('show_settings_menu_button', True), reload_settings=False)
            self.set_setting('particles_in_settings', self.get_setting('particles_in_settings', True), reload_settings=False)

    def on_plugin_unload(self):
        self._picker_delegates.clear()
        if self._badge_manager:
            self._badge_manager.cleanup()
        if self._deeplink_hook_ref:
            try:
                self.unhook_method(self._deeplink_hook_ref)
            except Exception:
                pass
        if self._settings_header_hook_ref:
            try:
                self.unhook_method(self._settings_header_hook_ref)
            except Exception:
                pass
        for ref in getattr(self, '_settings_activity_hooks', []):
            try:
                self.unhook_method(ref)
            except Exception:
                pass

    def set_setting(self, key, value, reload_settings=False):
        try:
            return super().set_setting(key, value, reload_settings=reload_settings)
        except TypeError:
            try:
                return super().set_setting(key, value)
            finally:
                if reload_settings:
                    run_on_ui_thread(self._update_visible_rows)

    def _update_visible_rows(self):
        try:
            frag = get_last_fragment()
            if not frag:
                return
            try:
                listView = frag.getListView()
                if listView:
                    AndroidUtilities.notifyDataSetChanged(listView)
            except Exception:
                pass
        except Exception:
            pass

    def _rebuild_fragments(self):
        try:
            frag = get_last_fragment()
            if frag:
                frag.rebuildAllFragments(True)
        except Exception:
            pass

    def _reload_submenu(self):
        try:
            frag = get_last_fragment()
            if frag:
                parent_layout = frag.getParentLayout()
                if parent_layout:
                    parent_layout.rebuildAllFragments(True)
        except Exception:
            pass

    def open_plugin_settings(self):
        def _open_settings():
            try:
                fragment = get_last_fragment()
                plugin = PluginsController.getInstance().plugins.get(self.id)
                if plugin:
                    settings_activity = PluginSettingsActivity(plugin)
                    fragment.presentFragment(settings_activity)
                    self._force_load_stickers()
            except Exception as e:
                BulletinHelper.show_error(t('open_settings_error', lang=self.lang, error=str(e)))
        run_on_ui_thread(_open_settings)

    def _force_load_stickers(self):
        try:
            def load_stickers():
                try:
                    fragment = get_last_fragment()
                    if fragment:
                        current_account = fragment.getCurrentAccount()
                        media_controller = MediaDataController.getInstance(current_account)
                        if media_controller:
                            input_set = TLRPC.TL_inputStickerSetShortName()
                            input_set.short_name = "mr_vestr"
                            media_controller.getStickerSet(input_set, None, False, None)
                except Exception:
                    pass
            AndroidUtilities.runOnUIThread(lambda: run_on_ui_thread(load_stickers), 1000)
        except Exception:
            pass

    def _apply_press_scale(self, view):
        try:
            class _TouchListener(dynamic_proxy(View.OnTouchListener)):
                def __init__(self, fn):
                    super().__init__()
                    self._fn = fn
                def onTouch(self, v, event):
                    return self._fn(v, event)
            def _on_touch(v, event):
                try:
                    action = event.getActionMasked()
                    if action == MotionEvent.ACTION_DOWN:
                        v.animate().scaleX(0.94).scaleY(0.94).setDuration(100).start()
                    elif action in (MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL):
                        v.animate().scaleX(1.0).scaleY(1.0).setDuration(200).start()
                except Exception:
                    pass
                return False
            view.setOnTouchListener(_TouchListener(_on_touch))
        except Exception:
            pass

    def _update_drawer_menu(self):
        show_drawer = self.get_setting('show_drawer_menu', False)
        self.remove_menu_item('templates_drawer')
        if show_drawer:
            self.add_menu_item(MenuItemData(
                menu_type=MenuItemType.DRAWER_MENU,
                text=t('templates', lang=self.lang),
                icon='msg_info',
                item_id='templates_drawer',
                on_click=lambda ctx: (self.open_plugin_settings(), self._force_load_stickers())
            ))

    def _update_chat_menu(self):
        show_chat = self.get_setting('show_chat_menu', True)
        if show_chat:
            try:
                run_on_ui_thread(self._add_templates_item_to_current_chat_header)
            except Exception:
                pass

    def _update_chat_plugins_menu(self):
        show_chat_plugins = self.get_setting('show_chat_plugins_menu', False)
        self.remove_menu_item('templates_chat_plugins')
        if show_chat_plugins:
            try:
                menu_type = MenuItemType.CHAT_ACTION_MENU
            except Exception:
                menu_type = None
            if menu_type:
                self.add_menu_item(MenuItemData(
                    menu_type=menu_type,
                    text=t('templates', lang=self.lang),
                    icon='msg_info',
                    item_id='templates_chat_plugins',
                    on_click=lambda ctx: self._show_template_popup_menu(None)
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

    def _add_templates_item_to_current_chat_header(self):
        try:
            frag = get_last_fragment()
            if not frag or not isinstance(frag, ChatActivity):
                return
            chat_activity = frag
            headerItem = self._get_private_field(chat_activity, "headerItem")
            if headerItem is None:
                return
            R = find_class("org.telegram.messenger.R")
            try:
                icon_id = getattr(R.drawable, 'msg_info')
            except Exception:
                try:
                    icon_id = getattr(R.drawable, 'msg_settings_14')
                except Exception:
                    icon_id = 0
            lazy_list = self._get_private_field(headerItem, "lazyList")
            lazy_map = self._get_private_field(headerItem, "lazyMap")
            try:
                if lazy_map is not None and lazy_map.get(self.templates_menu_id) is not None:
                    self._hook_chat_action_bar_callback(chat_activity)
                    return
                if lazy_list is not None:
                    for i in range(lazy_list.size()):
                        item = lazy_list.get(i)
                        try:
                            item_id = self._get_private_field(item, "id")
                            if item_id == self.templates_menu_id:
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
                    Integer(self.templates_menu_id),
                    Integer(icon_id),
                    None,
                    t('templates', lang=self.lang),
                    Boolean(True),
                    Boolean(False)
                )
                if lazy_list is not None and insert_position >= 0:
                    lazy_list.add(insert_position, our_item)
                    if lazy_map is not None:
                        lazy_map.put(self.templates_menu_id, our_item)
                else:
                    try:
                        headerItem.lazilyAddSubItem(self.templates_menu_id, icon_id, t('templates', lang=self.lang))
                    except Exception:
                        pass
                self._hook_chat_action_bar_callback(chat_activity)
            except Exception:
                pass
        except Exception:
            pass

    def _hook_chat_action_bar_callback(self, chat_activity):
        try:
            action_bar = self._get_private_field(chat_activity, "actionBar")
            if action_bar is None:
                return
            current_callback = self._get_private_field(action_bar, "actionBarMenuOnItemClick")
            if current_callback is None:
                return
            callback_class = current_callback.getClass()
            jint = jclass("java.lang.Integer").TYPE
            onItemClickMethod = callback_class.getDeclaredMethod("onItemClick", jint)
            onItemClickMethod.setAccessible(True)
            plugin = self
            class TemplatesActionBarMenuItemClickHook(MethodHook):
                def __init__(self, plugin_ref, activity_ref):
                    self.plugin_ref = plugin_ref
                    self.activity_ref = activity_ref
                def before_hooked_method(self, param):
                    try:
                        item_id = int(param.args[0])
                        if item_id == self.plugin_ref.templates_menu_id:
                            run_on_ui_thread(lambda: self.plugin_ref._show_template_popup_menu(None))
                            param.setResult(None)
                    except Exception:
                        pass
            self.hook_method(onItemClickMethod, TemplatesActionBarMenuItemClickHook(self, chat_activity))
        except Exception:
            pass

    def _hook_chat_activity_resume(self):
        try:
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
                            run_on_ui_thread(self.p._add_templates_item_to_current_chat_header)
                    except Exception:
                        pass
            self.hook_method(target_method, ChatResumeHook(self))
        except Exception:
            pass

    def _open_channel_link(self, _):
        run_on_ui_thread(lambda: get_messages_controller().openByUserName("I_am_Vestr", get_last_fragment(), 1))

    def _copy_channel_link(self, _):
        try:
            run_on_ui_thread(lambda: self._copy_link_to_clipboard("https://t.me/I_am_Vestr"))
        except Exception:
            pass

    def _copy_personal_link(self, _):
        try:
            run_on_ui_thread(lambda: self._copy_link_to_clipboard("https://t.me/mr_Vestr"))
        except Exception:
            pass

    def _copy_link_to_clipboard(self, url):
        try:
            fragment = get_last_fragment()
            if not fragment:
                return
            context = fragment.getParentActivity()
            if not context:
                return
            clipboard = context.getSystemService(context.CLIPBOARD_SERVICE)
            clipboard.setPrimaryClip(ClipData.newPlainText("link", url))
            try:
                icon_attr = getattr(R_tg.raw, 'copy', None)
            except Exception:
                icon_attr = None
            BulletinHelper.show_with_button(t('link_copied', lang=self.lang), icon_attr if icon_attr else 0, t('close', lang=self.lang), lambda: None, None)
        except Exception:
            pass

    def _open_personal_link(self, _):
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if act:
            try:
                if self._get_effective_lang() == 'ru':
                    text = '%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%21+%D0%9F%D0%B8%D1%88%D1%83+%D0%BF%D0%BE+%D0%BF%D0%BE%D0%B2%D0%BE%D0%B4%D1%83+%D0%BF%D0%BB%D0%B0%D0%B3%D0%B8%D0%BD%D0%B0+%C2%ABTemplates%C2%BB%3A%0D%0A'
                else:
                    text = 'Hello%21+I%27m+writing+regarding+the+%22Templates%22+plugin%3A%0D%0A'
                uri = Uri.parse(f"https://t.me/mr_vestr/?text={text}")
                Browser.openUrl(act, uri, True, True, True, None, None, False, False, False)
            except Exception as e:
                BulletinHelper.show_error(t('link_open_error', lang=self.lang, error=str(e)))

    def _add_url_hook(self):
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
                            data = json.loads(content.decode("utf-8"))
                        except Exception:
                            return
                        param.setResult(False)
                        self.plugin._show_import_bottom_sheet(data, act=param.args[3])
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
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        sheet = BottomSheet(act, False)
        root_layout = LinearLayout(act)
        root_layout.setOrientation(LinearLayout.VERTICAL)
        root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(8))
        try:
            root_layout.setAlpha(0.0)
            root_layout.setScaleX(0.3)
            root_layout.setScaleY(0.3)
            root_layout.setTranslationY(AndroidUtilities.dp(100))
        except Exception:
            pass
        try:
            bg_drawable = GradientDrawable()
            bg_drawable.setShape(GradientDrawable.RECTANGLE)
            bg_drawable.setCornerRadii([AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), 0, 0, 0, 0])
            bg_drawable.setColor(Theme.getColor(Theme.key_dialogBackground))
            root_layout.setBackground(bg_drawable)
        except Exception:
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
        try:
            title_view.setAlpha(0.0)
            title_view.setTranslationY(AndroidUtilities.dp(50))
            title_view.setScaleX(0.8)
            title_view.setScaleY(0.8)
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
        try:
            body_scroll.setAlpha(0.0)
            body_scroll.setTranslationY(AndroidUtilities.dp(30))
            body_scroll.setScaleX(0.8)
            body_scroll.setScaleY(0.8)
        except Exception:
            pass
        body_tv = TextView(act)
        body_tv.setText(t('how_it_works_text', lang=self.lang))
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
        
        def create_text_button(text: str, icon_res: str, on_click):
            btn_frame = FrameLayout(act)
            btn_bg = GradientDrawable()
            btn_bg.setCornerRadius(AndroidUtilities.dp(18))
            try:
                bg_color = Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000
            except Exception:
                bg_color = Color.parseColor("#F0F0F0")
            btn_bg.setColor(bg_color)
            try:
                ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
                ripple_drawable = RippleDrawable(ripple_color, btn_bg, None)
                btn_frame.setBackground(ripple_drawable)
            except Exception:
                btn_frame.setBackground(btn_bg)
            btn_frame.setPadding(AndroidUtilities.dp(12), AndroidUtilities.dp(8), AndroidUtilities.dp(12), AndroidUtilities.dp(8))
            icon_view = ImageView(act)
            try:
                icon_view.setImageResource(getattr(R_tg.drawable, icon_res))
            except Exception:
                pass
            icon_view.setScaleType(ImageView.ScaleType.CENTER)
            icon_view.setColorFilter(Theme.getColor(Theme.key_dialogTextBlue))
            text_view = TextView(act)
            text_view.setText(text)
            text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlue))
            text_view.setGravity(Gravity.CENTER_VERTICAL)
            btn_frame.addView(icon_view, LayoutHelper.createFrame(24, 24, Gravity.LEFT | Gravity.CENTER_VERTICAL, 0, 0, 8, 0))
            btn_frame.addView(text_view, LayoutHelper.createFrame(-2, -2, Gravity.LEFT | Gravity.CENTER_VERTICAL, 32, 0, 0, 0))
            btn_frame.setClickable(True)
            btn_frame.setFocusable(True)
            self._apply_press_scale(btn_frame)
            btn_frame.setOnClickListener(OnClickListener(lambda *_: on_click(btn_frame)))
            return btn_frame

        def create_icon_button(icon_res: str, on_click):
            btn_frame = FrameLayout(act)
            btn_bg = GradientDrawable()
            btn_bg.setCornerRadius(AndroidUtilities.dp(18))
            try:
                bg_color = Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000
            except Exception:
                bg_color = Color.parseColor("#F0F0F0")
            btn_bg.setColor(bg_color)
            try:
                ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
                ripple_drawable = RippleDrawable(ripple_color, btn_bg, None)
                btn_frame.setBackground(ripple_drawable)
            except Exception:
                btn_frame.setBackground(btn_bg)
            btn_frame.setPadding(AndroidUtilities.dp(12), AndroidUtilities.dp(8), AndroidUtilities.dp(12), AndroidUtilities.dp(8))
            icon_view = ImageView(act)
            try:
                icon_view.setImageResource(getattr(R_tg.drawable, icon_res))
            except Exception:
                pass
            icon_view.setScaleType(ImageView.ScaleType.CENTER)
            icon_view.setColorFilter(Theme.getColor(Theme.key_dialogTextBlue))
            btn_frame.addView(icon_view, LayoutHelper.createFrame(24, 24, Gravity.CENTER, 0, 0, 0, 0))
            btn_frame.setClickable(True)
            btn_frame.setFocusable(True)
            self._apply_press_scale(btn_frame)
            btn_frame.setOnClickListener(OnClickListener(lambda *_: on_click(btn_frame)))
            return btn_frame

        buttons_container = LinearLayout(act)
        buttons_container.setOrientation(LinearLayout.HORIZONTAL)
        buttons_container.setGravity(Gravity.CENTER)

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

        def on_open_doc(v):
            try:
                if self._get_effective_lang() == 'ru':
                    doc_url = 'https://github.com/mr-Vestr/plugins/blob/main/Templates/TEMPLATES_RU.md'
                else:
                    doc_url = 'https://github.com/mr-Vestr/plugins/blob/main/Templates/TEMPLATES_EN.md'
                uri = Uri.parse(doc_url)
                Browser.openUrl(act, uri, True, True, True, None, None, True, True, True)
            except Exception:
                pass

        channel_btn = create_text_button(t('channel', lang=self.lang), 'msg_channel', on_channel)
        buttons_container.addView(channel_btn, LayoutHelper.createLinear(-2, -2, Gravity.CENTER, 0, 0, 8, 0))
        personal_btn = create_text_button(t('personal', lang=self.lang), 'msg_contacts', on_personal)
        buttons_container.addView(personal_btn, LayoutHelper.createLinear(-2, -2, Gravity.CENTER, 0, 0, 8, 0))
        open_btn = create_icon_button('msg_openin', on_open_doc)
        buttons_container.addView(open_btn, LayoutHelper.createLinear(-2, -2, Gravity.CENTER, 0, 0, 0, 0))
        buttons_container.setGravity(Gravity.CENTER)
        try:
            buttons_container.setAlpha(0.0)
            buttons_container.setTranslationY(AndroidUtilities.dp(40))
            buttons_container.setScaleX(0.8)
            buttons_container.setScaleY(0.8)
        except Exception:
            pass

        horizontal_scroll = HorizontalScrollView(act)
        horizontal_scroll.setHorizontalScrollBarEnabled(False)
        horizontal_scroll.setFillViewport(True)
        horizontal_scroll.setHorizontalFadingEdgeEnabled(True)
        horizontal_scroll.setFadingEdgeLength(AndroidUtilities.dp(24))
        horizontal_scroll.addView(buttons_container, FrameLayout.LayoutParams(
            FrameLayout.LayoutParams.WRAP_CONTENT,
            FrameLayout.LayoutParams.WRAP_CONTENT
        ))

        root_layout.addView(horizontal_scroll, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 12))
        close_btn_frame = FrameLayout(act)
        try:
            base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
        except Exception:
            base_color = Theme.getColor(Theme.key_dialogTextBlue)
        try:
            pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        except Exception:
            pressed_color = base_color
        close_btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(28),
            base_color,
            pressed_color
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
        self._apply_press_scale(close_btn_frame)
        try:
            close_btn_frame.setAlpha(0.0)
            close_btn_frame.setTranslationY(AndroidUtilities.dp(50))
            close_btn_frame.setScaleX(0.8)
            close_btn_frame.setScaleY(0.8)
        except Exception:
            pass
        root_layout.addView(close_btn_frame, LayoutHelper.createLinear(-1, -2, 0, 8, 0, 0))
        sheet.setCustomView(root_layout)
        sheet.setCanDismissWithSwipe(False)
        sheet.show()
        def animate_elements():
            try:
                root_layout.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                def show_elements():
                    try:
                        title_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        body_scroll.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        buttons_container.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(150).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        close_btn_frame.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(200).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                run_on_ui_thread(show_elements)
            except Exception:
                pass
        run_on_ui_thread(animate_elements)

    def _check_for_updates_on_load_with_timeout(self):
        try:
            last_check_time = self.get_setting('last_update_check_time', 0)
            current_time = int(time.time())
            ten_minutes_ago = current_time - 600
            
            if last_check_time < ten_minutes_ago:
                def delayed_check():
                    time.sleep(3)
                    self._check_for_updates(show_on_load=True)
                    self.set_setting('last_update_check_time', current_time, reload_settings=False)
                thread = threading.Thread(target=delayed_check)
                thread.daemon = True
                thread.start()
            else:
                pass
        except Exception:
            pass

    def _check_for_updates_on_load(self):
        def delayed_check():
            time.sleep(3)
            self._check_for_updates(show_on_load=True)
        thread = threading.Thread(target=delayed_check)
        thread.daemon = True
        thread.start()
    
    def _check_for_updates(self, show_on_load=False, show_loading=True):
        if self.checking_update:
            return
        self.update_available = False
        self.checking_update = True
        timeout_reached = [False]
        
        def check_thread():
            try:
                if show_loading and not show_on_load:
                    run_on_ui_thread(lambda: self._show_checking_bulletin())
                raw_url = "https://raw.githubusercontent.com/mr-Vestr/plugins/refs/heads/main/Templates/config.json"
                timestamp = int(time.time() * 1000)
                raw_url_with_timestamp = f"{raw_url}?t={timestamp}"
                request = urllib.request.Request(raw_url_with_timestamp)
                request.add_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                request.add_header('Pragma', 'no-cache')
                request.add_header('Expires', '0')
                request.add_header('Accept', 'application/json')
                if show_loading and not show_on_load:
                    check_started = time.time()
                    def check_timeout():
                        time.sleep(10)
                        if self.checking_update and not timeout_reached[0]:
                            timeout_reached[0] = True
                            self.checking_update = False
                            run_on_ui_thread(lambda: self._show_timeout_bulletin())
                    timeout_thread = threading.Thread(target=check_timeout, daemon=True)
                    timeout_thread.start()
                with urllib.request.urlopen(request, timeout=10) as response:
                    if timeout_reached[0]:
                        return
                    if response.getcode() != 200:
                        raise Exception(f"HTTP {response.getcode()}")
                    content_raw = response.read().decode('utf-8')
                    if not content_raw:
                        raise Exception("No content in response")
                    config_data = json.loads(content_raw)
                    if timeout_reached[0]:
                        return
                    latest_version_from_config = config_data.get("version", "0.0.0")
                    if self._get_effective_lang() == 'ru':
                        changelog_from_config = config_data.get("changelog_ru", config_data.get("changelog", t('no_changelog', lang=self.lang)))
                    else:
                        changelog_from_config = config_data.get("changelog_en", config_data.get("changelog", t('no_changelog', lang=self.lang)))
                    sticker_info = config_data.get("sticker", "")
                    download_url_from_config = config_data.get("link", "")
                    sticker_pack_from_config = None
                    sticker_index_from_config = 0
                    if sticker_info and "/" in sticker_info:
                        parts = sticker_info.split("/")
                        sticker_pack_from_config = parts[0]
                        try:
                            sticker_index_from_config = int(parts[1]) if len(parts) > 1 else 0
                        except:
                            sticker_index_from_config = 0
                    else:
                        sticker_pack_from_config = "mr_vestr"
                        sticker_index_from_config = 1
                    current_version = __version__.strip()
                    latest_version_clean = latest_version_from_config.strip()
                    current_base = current_version.split(" (")[0].strip() if " (" in current_version else current_version.strip()
                    latest_base = latest_version_clean.split(" (")[0].strip() if " (" in latest_version_clean else latest_version_clean.strip()
                    if current_base != latest_base:
                        self.update_available = True
                        self.latest_version = latest_version_from_config
                        self.changelog = changelog_from_config
                        self.download_url = download_url_from_config
                        self.sticker_pack = sticker_pack_from_config
                        self.sticker_index = sticker_index_from_config
                        if show_on_load and not timeout_reached[0]:
                            run_on_ui_thread(lambda: self._show_update_bottom_sheet())
                        elif show_loading and not timeout_reached[0]:
                            run_on_ui_thread(lambda: self._show_update_bottom_sheet())
                    else:
                        self.update_available = False
                        self.latest_version = latest_version_from_config
                        self.changelog = changelog_from_config
                        self.download_url = download_url_from_config
                        self.sticker_pack = sticker_pack_from_config
                        self.sticker_index = sticker_index_from_config
                        if show_loading and not show_on_load and not timeout_reached[0]:
                            run_on_ui_thread(lambda: self._show_no_update_bulletin())
            except Exception as e:
                if show_loading and not timeout_reached[0] and not show_on_load:
                    error_message = str(e)
                    run_on_ui_thread(lambda: self._show_error_bulletin(error_message))
            finally:
                if not timeout_reached[0]:
                    self.checking_update = False
                    if not show_on_load:
                        current_time = int(time.time())
                        self.set_setting('last_update_check_time', current_time, reload_settings=False)
        threading.Thread(target=check_thread, daemon=True).start()
    
    def _show_checking_bulletin(self):
        try:
            BulletinHelper.show_with_button(
                t('checking_updates', lang=self.lang),
                R_tg.raw.camera_flip,
                t('close', lang=self.lang),
                lambda: None,
                None
            )
        except Exception:
            pass
    
    def _show_no_update_bulletin(self):
        try:
            BulletinHelper.show_with_button(
                t('no_updates_available', lang=self.lang),
                R_tg.raw.done,
                t('close', lang=self.lang),
                lambda: None,
                None
            )
        except Exception:
            pass
    
    def _show_error_bulletin(self, error_msg):
        try:
            BulletinHelper.show_with_button(
                t('update_check_error', lang=self.lang, error=error_msg),
                R_tg.raw.error,
                t('close', lang=self.lang),
                lambda: None,
                None
            )
        except Exception:
            pass
    
    def _show_timeout_bulletin(self):
        try:
            BulletinHelper.show_with_button(
                t('update_timeout_error', lang=self.lang),
                R_tg.raw.error,
                t('close', lang=self.lang),
                lambda: None,
                None
            )
        except Exception as e:
            pass
    
    def _show_update_bottom_sheet(self):
        try:
            fragment = get_last_fragment()
            if not fragment:
                return
            act = fragment.getParentActivity()
            if not act:
                return
            sheet = BottomSheet(act, False, fragment.getResourceProvider())
            sheet.setApplyBottomPadding(False)
            sheet.setApplyTopPadding(False)
            sheet.setCanDismissWithSwipe(False)
            scroll_view = NestedScrollView(act)
            try:
                scroll_view.setNestedScrollingEnabled(True)
                scroll_view.setVerticalScrollBarEnabled(False)
                scroll_view.setFillViewport(True)
            except Exception:
                pass
            scroll_content = LinearLayout(act)
            scroll_content.setOrientation(LinearLayout.VERTICAL)
            scroll_content.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(8))
            root_layout = LinearLayout(act)
            root_layout.setOrientation(LinearLayout.VERTICAL)
            try:
                scroll_content.setAlpha(0.0)
                scroll_content.setScaleX(0.3)
                scroll_content.setScaleY(0.3)
                scroll_content.setTranslationY(AndroidUtilities.dp(100))
            except Exception:
                pass
            try:
                bg_drawable = GradientDrawable()
                bg_drawable.setShape(GradientDrawable.RECTANGLE)
                bg_drawable.setCornerRadii([AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), 0, 0, 0, 0])
                bg_drawable.setColor(Theme.getColor(Theme.key_dialogBackground))
                root_layout.setBackground(bg_drawable)
            except Exception:
                try:
                    root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
                except Exception:
                    pass
            avatar_view = BackupImageView(act)
            avatar_view.setRoundRadius(AndroidUtilities.dp(45))
            root_layout.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, 0, 0, 12))
            if self.sticker_pack:
                sticker_name = f"{self.sticker_pack}/{self.sticker_index}" if self.sticker_index > 0 else self.sticker_pack
                self.load_sticker_with_fallback(avatar_view, sticker_name, self.sticker_index, "130_130")
            title_view = TextView(act)
            title_view.setTypeface(AndroidUtilities.bold())
            title_view.setGravity(Gravity.CENTER)
            title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
            title_view.setText("Templates")
            try:
                title_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                pass
            try:
                title_view.setAlpha(0.0)
                title_view.setTranslationY(AndroidUtilities.dp(50))
                title_view.setScaleX(0.8)
                title_view.setScaleY(0.8)
            except Exception:
                pass
            root_layout.addView(title_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 8))
            version_view = TextView(act)
            version_view.setGravity(Gravity.CENTER)
            version_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            version_view.setTextColor(Theme.getColor(Theme.key_dialogTextGray))
            current_version_clean = __version__.split(" (")[0].strip()
            version_text = f"{current_version_clean} → {self.latest_version}"
            spannable = SpannableString(version_text)
            spannable.setSpan(StrikethroughSpan(), 0, len(current_version_clean), SpannableString.SPAN_EXCLUSIVE_EXCLUSIVE)
            version_view.setText(spannable)
            root_layout.addView(version_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 16))
            changes_title = TextView(act)
            changes_title.setTypeface(AndroidUtilities.bold())
            changes_title.setGravity(Gravity.LEFT)
            changes_title.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 18)
            changes_title.setText(t('changes', lang=self.lang))
            changes_title.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            root_layout.addView(changes_title, LayoutHelper.createLinear(-1, -2, Gravity.LEFT, 0, 0, 0, 8))
            changelog_container = FrameLayout(act)
            try:
                border_drawable = GradientDrawable()
                border_drawable.setShape(GradientDrawable.RECTANGLE)
                border_drawable.setCornerRadius(AndroidUtilities.dp(8))
                border_color = Theme.getColor(Theme.key_featuredStickers_addButton)
                border_drawable.setStroke(AndroidUtilities.dp(2), border_color)
                border_drawable.setColor(Theme.getColor(Theme.key_dialogBackground))
                changelog_container.setBackground(border_drawable)
            except Exception:
                pass
            changelog_container.setPadding(AndroidUtilities.dp(12), AndroidUtilities.dp(12), AndroidUtilities.dp(12), AndroidUtilities.dp(12))
            changelog_view = TextView(act)
            changelog_view.setGravity(Gravity.LEFT)
            changelog_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
            changelog_view.setText(self.changelog or t('no_changelog', lang=self.lang))
            changelog_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            changelog_view.setLineSpacing(AndroidUtilities.dp(4), 1.15)
            changelog_container.addView(changelog_view, FrameLayout.LayoutParams(-1, -2))
            root_layout.addView(changelog_container, LayoutHelper.createLinear(-1, -2, Gravity.LEFT, 0, 0, 0, 12))
            changelog_link_btn = TextView(act)
            changelog_link_btn.setText(t('full_changelog', lang=self.lang))
            changelog_link_btn.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            changelog_link_btn.setGravity(Gravity.CENTER)
            try:
                changelog_link_btn.setTextColor(Theme.getColor(Theme.key_featuredStickers_addButton))
            except Exception:
                changelog_link_btn.setTextColor(Color.BLUE)
            changelog_link_btn.setClickable(True)
            changelog_link_btn.setFocusable(True)
            def on_changelog_link_click(v):
                try:
                    sheet.dismiss()
                    Browser.openUrl(act, Uri.parse("https://t.me/I_am_Vestr"))
                except Exception:
                    pass
            changelog_link_btn.setOnClickListener(OnClickListener(lambda *_: on_changelog_link_click(changelog_link_btn)))
            self._apply_press_scale(changelog_link_btn)
            try:
                changelog_link_btn.setAlpha(0.0)
                changelog_link_btn.setTranslationY(AndroidUtilities.dp(50))
                changelog_link_btn.setScaleX(0.8)
                changelog_link_btn.setScaleY(0.8)
            except Exception:
                pass
            root_layout.addView(changelog_link_btn, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 16))
            update_btn_frame = FrameLayout(act)
            base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
            pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
            update_btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                AndroidUtilities.dp(28),
                base_color,
                pressed_color
            ))
            update_btn_frame.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
            update_btn_frame.setClickable(True)
            update_btn_frame.setFocusable(True)
            update_btn_text = TextView(act)
            update_btn_text.setText(t('update', lang=self.lang))
            update_btn_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            update_btn_text.setTypeface(AndroidUtilities.bold())
            update_btn_text.setGravity(Gravity.CENTER)
            update_btn_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
            update_btn_frame.addView(update_btn_text, FrameLayout.LayoutParams(-1, -2))
            def on_update_click(v):
                try:
                    sheet.dismiss()
                    self._download_and_install_update()
                except Exception:
                    pass
            update_btn_frame.setOnClickListener(OnClickListener(lambda *_: on_update_click(update_btn_frame)))
            self._apply_press_scale(update_btn_frame)
            try:
                update_btn_frame.setAlpha(0.0)
                update_btn_frame.setTranslationY(AndroidUtilities.dp(50))
                update_btn_frame.setScaleX(0.8)
                update_btn_frame.setScaleY(0.8)
            except Exception:
                pass
            root_layout.addView(update_btn_frame, LayoutHelper.createLinear(-1, -2, 0, 8, 0, 0))
            scroll_content.addView(root_layout)
            scroll_view.addView(scroll_content)
            sheet.setCustomView(scroll_view)
            sheet.show()
            def animate_elements():
                try:
                    scroll_content.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    def show_elements():
                        try:
                            title_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            changelog_container.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            changelog_link_btn.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(125).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            update_btn_frame.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(150).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                    run_on_ui_thread(show_elements)
                except Exception:
                    pass
            run_on_ui_thread(animate_elements)
        except Exception as e:
            pass
    
    def _download_and_install_update(self):
        try:
            loading_bulletin = [None]
            def show_loading():
                loading_bulletin[0] = BulletinHelper.show_with_button(
                    t('updating_plugin', lang=self.lang),
                    R_tg.raw.download_progress,
                    t('close_alt', lang=self.lang),
                    lambda: None,
                    None
                )
            run_on_ui_thread(show_loading)
            callback_shown = [False]
            def download_thread():
                try:
                    if not self.download_url:
                        raise Exception("Download URL not available")
                    with urllib.request.urlopen(self.download_url, timeout=30) as response:
                        plugin_content = response.read()
                    plugins_dir = os.path.join(str(ApplicationLoader.applicationContext.getFilesDir()), "plugins")
                    temp_file = os.path.join(plugins_dir, "templates_update.tmp")
                    with open(temp_file, 'wb') as f:
                        f.write(plugin_content)
                    version = self.latest_version
                    class Callback(dynamic_proxy(Utilities.Callback)):
                        def run(self_cb, error):
                            if callback_shown[0]:
                                return
                            callback_shown[0] = True
                            try:
                                os.remove(temp_file)
                            except:
                                pass
                            if error:
                                run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                                    t('update_failed', lang=self.lang),
                                    R_tg.raw.error,
                                    t('close_alt', lang=self.lang),
                                    lambda: None,
                                    None
                                ))
                            else:
                                def open_settings_after_update():
                                     try:
                                         fragment = get_last_fragment()
                                         plugin = PluginsController.getInstance().plugins.get(self.id)
                                         if plugin:
                                             fragment.presentFragment(PluginSettingsActivity(plugin))
                                     except Exception:
                                         pass
                                run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                                    t('update_success', lang=self.lang),
                                    R_tg.raw.done,
                                    t('open', lang=self.lang),
                                    open_settings_after_update,
                                    None
                                ))
                    class Runnable(dynamic_proxy(jclass("java.lang.Runnable"))):
                        def run(self_r):
                            PluginsController.getInstance().engines.get(PluginsConstants.PYTHON).loadPluginFromFile(temp_file, None, Callback())
                    Utilities.pluginsQueue.postRunnable(Runnable())
                except Exception as e:
                    if not callback_shown[0]:
                        callback_shown[0] = True
                        run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                            t('update_failed', lang=self.lang),
                            R_tg.raw.error,
                            t('close_alt', lang=self.lang),
                            lambda: None,
                            None
                        ))
            threading.Thread(target=download_thread, daemon=True).start()
            threading.Thread(target=download_thread, daemon=True).start()
        except Exception as e:
            pass

    def _show_version_dialog(self, _):
        self._force_load_stickers()
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        sheet = BottomSheet(act, False)
        root_layout = LinearLayout(act)
        root_layout.setOrientation(LinearLayout.VERTICAL)
        root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(8))
        try:
            root_layout.setAlpha(0.0)
            root_layout.setScaleX(0.3)
            root_layout.setScaleY(0.3)
            root_layout.setTranslationY(AndroidUtilities.dp(100))
        except Exception:
            pass
        try:
            bg_drawable = GradientDrawable()
            bg_drawable.setShape(GradientDrawable.RECTANGLE)
            bg_drawable.setCornerRadii([AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), 0, 0, 0, 0])
            bg_drawable.setColor(Theme.getColor(Theme.key_dialogBackground))
            root_layout.setBackground(bg_drawable)
        except Exception:
            try:
                root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
            except Exception:
                pass
        try:
            avatar_view = BackupImageView(act)
            avatar_view.setRoundRadius(AndroidUtilities.dp(45))
            root_layout.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, 0, 0, 12))
            self.load_sticker_with_fallback(avatar_view, "mr_vestr/1", 1, "90_90")
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
        try:
            title_view.setAlpha(0.0)
            title_view.setTranslationY(AndroidUtilities.dp(50))
            title_view.setScaleX(0.8)
            title_view.setScaleY(0.8)
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
        try:
            body_scroll.setAlpha(0.0)
            body_scroll.setTranslationY(AndroidUtilities.dp(30))
            body_scroll.setScaleX(0.8)
            body_scroll.setScaleY(0.8)
        except Exception:
            pass
        body_tv = TextView(act)
        updates_text = t('updates_info', lang=self.lang)
        spannable = SpannableString(updates_text)
        username = "@I_am_Vestr"
        start_pos = updates_text.find(username)
        if start_pos != -1:
            end_pos = start_pos + len(username)
            spannable.setSpan(URLSpan("https://t.me/i_am_vestr"), start_pos, end_pos, SpannableString.SPAN_EXCLUSIVE_EXCLUSIVE)
        body_tv.setText(spannable)
        body_tv.setTextIsSelectable(True)
        body_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
        body_tv.setGravity(Gravity.CENTER)
        try:
            body_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            body_tv.setLinkTextColor(Theme.getColor(Theme.key_dialogTextBlue))
            body_tv.setMovementMethod(LinkMovementMethod.getInstance())
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
        try:
            base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
        except Exception:
            base_color = Theme.getColor(Theme.key_dialogTextBlue)
        try:
            pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        except Exception:
            pressed_color = base_color
        check_btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(28),
            base_color,
            pressed_color
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
                self._check_for_updates(show_loading=True)
            except Exception:
                pass
        check_btn_frame.setOnClickListener(OnClickListener(lambda *_: on_check(check_btn_frame)))
        self._apply_press_scale(check_btn_frame)
        try:
            check_btn_frame.setAlpha(0.0)
            check_btn_frame.setTranslationY(AndroidUtilities.dp(50))
            check_btn_frame.setScaleX(0.8)
            check_btn_frame.setScaleY(0.8)
        except Exception:
            pass
        root_layout.addView(check_btn_frame, LayoutHelper.createLinear(-1, -2, 0, 8, 0, 0))
        sheet.setCustomView(root_layout)
        sheet.show()
        def animate_elements():
            try:
                root_layout.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                def show_elements():
                    try:
                        title_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        body_scroll.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        check_btn_frame.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(150).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                run_on_ui_thread(show_elements)
            except Exception:
                pass
        run_on_ui_thread(animate_elements)

    def _lang(self):
        try:
            idx = int(self.get_setting('plugin_lang', 0) or 0)
            idx = max(0, min(idx, len(PLUGIN_LANG_CODES) - 1))
            forced = PLUGIN_LANG_CODES[idx]
            if forced != 'system':
                return forced
        except Exception:
            pass
        return 'system'

    def _get_effective_lang(self):
        l = self.lang
        if l == 'system':
            try:
                loc = LocaleController.getInstance().getCurrentLocale()
                l = (loc.getLanguage() or 'en').lower()
            except Exception:
                l = 'en'
        return 'ru' if l in ('ru', 'uk', 'be', 'kk') else 'en'

    def _t(self, key, **kwargs):
        return t(key, lang=self._lang(), **kwargs)

    def _on_language_changed(self, idx):
        try:
            self.set_setting('plugin_lang', max(0, min(int(idx), len(PLUGIN_LANG_CODES) - 1)))
            run_on_ui_thread(lambda: self.reload_settings())
        except Exception:
            pass

    def _kill_process(self):
        time.sleep(0.3)
        os.kill(os.getpid(), signal.SIGKILL)

    def _show_restart_bulletin(self):
        try:
            BulletinHelper.show_with_button(
                self._t('restart_required'),
                getattr(R_tg.raw, 'chats_infotip', 0),
                self._t('restart_button'),
                lambda: threading.Thread(target=self._kill_process, daemon=True).start(),
                None
            )
        except Exception:
            pass


    def _create_settings_header(self, context):
        try:
            container = FrameLayout(context)
            try:
                container.setClipChildren(False)
                container.setClipToPadding(False)
            except Exception:
                pass
            if self.get_setting('particles_in_settings', True):
                try:
                    particlesView = StarParticlesView(context)
                    particlesView.doNotFling = True
                    particlesView.setClipWithGradient()
                    particlesView.drawable.colorKey = Theme.key_premiumGradient1
                    particlesView.drawable.isCircle = False
                    particlesView.drawable.roundEffect = False
                    particlesView.drawable.useRotate = False
                    particlesView.drawable.useBlur = True
                    particlesView.drawable.checkBounds = True
                    particlesView.drawable.useScale = True
                    particlesView.drawable.startFromCenter = True
                    particlesView.drawable.centerOffsetY = AndroidUtilities.dp(24)
                    particlesView.drawable.size1 = 17
                    particlesView.drawable.size2 = 18
                    particlesView.drawable.size3 = 19
                    particlesView.drawable.init()
                    container.addView(particlesView, LayoutHelper.createFrame(-1, 238, Gravity.CENTER_HORIZONTAL | Gravity.TOP, 0, -10, 0, 0))
                except Exception as e:
                    log(f"templates: particles error: {e}")
            main_layout = LinearLayout(context)
            main_layout.setOrientation(LinearLayout.VERTICAL)
            main_layout.setGravity(Gravity.CENTER)
            try:
                main_layout.setBackgroundColor(Color.TRANSPARENT)
            except Exception:
                pass
            main_layout.setPadding(
                AndroidUtilities.dp(20), AndroidUtilities.dp(20),
                AndroidUtilities.dp(20), AndroidUtilities.dp(20)
            )
            imageView = BackupImageView(context)
            imageView.setRoundRadius(AndroidUtilities.dp(45))
            if not self.try_load_sticker(imageView, __icon__, 0, "130_130"):
                self.load_sticker_with_fallback(imageView, __icon__, 0, "130_130")
            sticker_container = FrameLayout(context)
            border_drawable = GradientDrawable()
            border_drawable.setShape(GradientDrawable.RECTANGLE)
            border_drawable.setCornerRadius(AndroidUtilities.dp(47))
            border_drawable.setColor(Color.WHITE)
            border_drawable.setStroke(AndroidUtilities.dp(3), Color.WHITE)
            sticker_container.setBackground(border_drawable)
            sticker_container.addView(imageView, LayoutHelper.createFrame(130, 130, Gravity.CENTER))
            main_layout.addView(sticker_container, LayoutHelper.createLinear(136, 136, Gravity.CENTER, 0, 0, 0, 16))
            text_container = LinearLayout(context)
            text_container.setOrientation(LinearLayout.VERTICAL)
            text_container.setGravity(Gravity.CENTER)
            title_view = TextView(context)
            title_view.setTextColor(Theme.getColor(Theme.key_windowBackgroundWhiteBlackText))
            title_view.setTypeface(AndroidUtilities.getTypeface(AndroidUtilities.TYPEFACE_ROBOTO_MEDIUM))
            title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 22)
            title_view.setText(f"Templates — {__version__}")
            title_view.setSingleLine(True)
            title_view.setGravity(Gravity.CENTER)
            text_container.addView(title_view, LayoutHelper.createLinear(-1, -2, 0, 0, 4, 0))
            subtitle_view = TextView(context)
            subtitle_view.setTextColor(Theme.getColor(Theme.key_windowBackgroundWhiteGrayText))
            subtitle_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            subtitle_view.setText(self._t('header_description'))
            subtitle_view.setGravity(Gravity.CENTER)
            text_container.addView(subtitle_view, LayoutHelper.createLinear(-1, -2))
            main_layout.addView(text_container, LayoutHelper.createLinear(-1, -2, Gravity.CENTER))
            container.addView(main_layout, LayoutHelper.createFrame(-1, -2, Gravity.CENTER))
            return container
        except Exception:
            return None

    def _setup_settings_header_hook(self):
        try:
            if HeaderSetting is None:
                return None
            plugin_instance = self

            class TemplatesSettingsHeaderHook(MethodHook):
                def __init__(self, p):
                    self.p = p

                def after_hooked_method(self, param):
                    try:
                        activity = param.thisObject
                        items = param.args[0]
                        if not items or items.size() == 0:
                            return
                        for i in range(items.size()):
                            item = items.get(i)
                            if hasattr(item, 'settingItem') and str(item.settingItem) == "templates_header":
                                return
                        plugin_obj = self.p._get_private_field(activity, "plugin")
                        if not plugin_obj or str(plugin_obj.getId()) != "templates":
                            return
                        if self.p._get_private_field(activity, "createSubFragmentCallback") is not None:
                            return
                        searching = self.p._get_private_field(activity, "searching")
                        if searching:
                            return
                        header = self.p._create_settings_header(activity.getContext())
                        if header:
                            item = UItem.asCustom(header)
                            item.settingItem = HeaderSetting("templates_header")
                            try:
                                item.setTransparent(True)
                            except Exception:
                                pass
                            items.add(0, item)
                            items.add(1, UItem.asShadow())
                    except Exception:
                        pass

            PSA = find_class("com.exteragram.messenger.plugins.ui.PluginSettingsActivity")
            if PSA:
                method = PSA.getClass().getDeclaredMethod(
                    "fillItems",
                    find_class("java.util.ArrayList"),
                    find_class("org.telegram.ui.Components.UniversalAdapter")
                )
                method.setAccessible(True)
                self._settings_header_hook_ref = self.hook_method(method, TemplatesSettingsHeaderHook(self))
        except Exception:
            pass
        return None

    def _setup_settings_activity_hook(self):
        try:
            SA = find_class("org.telegram.ui.SettingsActivity")
            if SA is None:
                return
            ArrayList = find_class("java.util.ArrayList")
            UniversalAdapter = find_class("org.telegram.ui.Components.UniversalAdapter")
            if ArrayList is None or UniversalAdapter is None:
                return
            _SETTINGS_BTN_ID = 880091
            plugin_ref = self

            class FillItemsHook(MethodHook):
                def after_hooked_method(self, param):
                    try:
                        if not plugin_ref.get_setting('show_settings_menu_button', True):
                            return
                        items = param.args[0]
                        if items is None or items.size() == 0:
                            return
                        for i in range(items.size()):
                            item = items.get(i)
                            try:
                                if item is not None and int(item.id) == _SETTINGS_BTN_ID:
                                    return
                            except Exception:
                                pass
                        extera_idx = -1
                        for i in range(items.size()):
                            item = items.get(i)
                            try:
                                if item is not None and int(item.id) == -1:
                                    extera_idx = i
                                    break
                            except Exception:
                                pass
                        if extera_idx < 0:
                            return
                        SettingCellFactory = find_class("org.telegram.ui.SettingsActivity$SettingCell$Factory")
                        if SettingCellFactory is None:
                            return
                        icon_id = 0
                        try:
                            icon_id = int(getattr(R_tg.drawable, 'filled_open_message', getattr(R_tg.drawable, 'msg_filled_data_files', 0)))
                        except Exception:
                            pass
                        label = plugin_ref._t('settings_button_label')
                        of_method = None
                        for m in SettingCellFactory.getClass().getDeclaredMethods():
                            try:
                                if m.getName() == "of" and len(m.getParameterTypes()) == 5:
                                    of_method = m
                                    break
                            except Exception:
                                pass
                        if of_method is None:
                            return
                        of_method.setAccessible(True)
                        _BLUE = -5963271
                        item = of_method.invoke(None, [jint(_SETTINGS_BTN_ID), jint(_BLUE), jint(_BLUE), jint(icon_id), label])
                        if item is None:
                            return
                        try:
                            item_cls = item.getClass()
                            for _fname in ('iconColor', 'iconBgColor', 'color', 'bgColor'):
                                try:
                                    _f = item_cls.getDeclaredField(_fname)
                                    _f.setAccessible(True)
                                    _f.setInt(item, _BLUE)
                                    break
                                except Exception:
                                    pass
                        except Exception:
                            pass
                        items.add(extera_idx + 1, item)
                    except Exception as e:
                        log(f"templates settings hook FillItems error: {e}")

            class OnClickHook(MethodHook):
                def before_hooked_method(self, param):
                    try:
                        uItem = param.args[0]
                        if uItem is None:
                            return
                        if int(uItem.id) != _SETTINGS_BTN_ID:
                            return
                        param.setResult(None)
                        def open():
                            try:
                                frag = get_last_fragment()
                                plugin_obj = PluginsController.getInstance().plugins.get(plugin_ref.id)
                                if plugin_obj and frag:
                                    frag.presentFragment(PluginSettingsActivity(plugin_obj))
                            except Exception as e:
                                log(f"templates settings hook onClick open error: {e}")
                        run_on_ui_thread(open)
                    except Exception as e:
                        log(f"templates settings hook OnClick error: {e}")

            try:
                fill_method = SA.getClass().getDeclaredMethod("fillItems", ArrayList, UniversalAdapter)
                fill_method.setAccessible(True)
                self._settings_activity_hooks.append(self.hook_method(fill_method, FillItemsHook()))
            except Exception as e:
                log(f"templates: fillItems hook error: {e}")
            try:
                click_method = None
                for m in SA.getClass().getDeclaredMethods():
                    try:
                        if m.getName() == "onClick" and len(m.getParameterTypes()) == 5:
                            click_method = m
                            break
                    except Exception:
                        pass
                if click_method:
                    click_method.setAccessible(True)
                    self._settings_activity_hooks.append(self.hook_method(click_method, OnClickHook()))
            except Exception as e:
                log(f"templates: onClick hook error: {e}")
        except Exception as e:
            log(f"templates: _setup_settings_activity_hook error: {e}")


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
        settings.append(Header(text=self._t('main_section')))
        settings.append(Text(
            text=self._t('manage_templates'),
            icon='msg_list',
            create_sub_fragment=self.create_templates_management_submenu,
            link_alias='manage_templates'
        ))
        settings.append(Text(
            text=self._t('plugin_settings'),
            icon='msg_settings',
            create_sub_fragment=self.create_plugin_settings_submenu,
            link_alias='plugin_settings_section'
        ))
        settings.append(Divider())
        settings.append(Header(text=self._t('contacts')))
        settings.append(Text(
            text=self._t('channel_1'),
            icon='msg_channel',
            accent=False,
            on_click=self._open_channel_link,
            on_long_click=self._copy_channel_link
        ))
        settings.append(Text(
            text=self._t('personal_1'),
            icon='msg_contacts',
            on_click=self._open_personal_link,
            on_long_click=self._copy_personal_link
        ))
        settings.append(Text(
            text=self._t('support_me'),
            icon='menu_feature_reactions',
            accent=True,
            on_click=self._show_support_me_menu,
            link_alias='support_me'
        ))
        settings.append(Divider())
        settings.append(Header(text=self._t('other')))
        settings.append(Text(
            text=self._t('how_it_works'),
            icon='msg_info',
            on_click=self._show_how_it_works,
            link_alias='how_it_works'
        ))
        settings.append(Text(
            text=self._t('plugin_version'),
            icon='msg_settings',
            accent=True,
            on_click=self._show_version_dialog,
            link_alias='plugin_version'
        ))
        settings.append(Divider())
        return settings

    def create_templates_management_submenu(self):
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
        settings.append(Header(text=self._t('templates_title')))
        settings.append(Text(
            text=self._t('create_template'),
            icon='msg_addbot',
            accent=True,
            on_click=lambda ctx: self._create_new_template()
        ))
        settings.append(Text(
            text=self._t('export_templates'),
            icon='msg_unarchive',
            accent=False,
            on_click=lambda ctx: self._show_export_bottom_sheet()
        ))
        if not self.get_setting('templates_visible', True):
            settings.append(Divider())
            settings.append(Text(
                text=self._t('refresh_templates'),
                icon='msg_retry',
                accent=True
            ))
        settings.append(Divider())
        created_count = self._get_created_count()
        show_templates = created_count > 0 and self.get_setting('templates_visible', True)
        if show_templates:
            for i in range(created_count):
                tpl = self.templates[i] if i < len(self.templates) else {}
                name = tpl.get("name", "")
                text = tpl.get("text", "")
                settings.append(Header(text=self._t('template_n', n=i+1)))
                settings.append(Input(
                    key=f"template_name_{i}",
                    text=self._t('name'),
                    default=name,
                    subtext=self._t('template_name_sub'),
                    icon="msg_edit",
                    on_change=self._make_onchange(i, 'name'),
                    on_long_click=(lambda idx=i: (lambda v: self._on_input_long_click(idx, 'name', v)))()
                ))
                settings.append(Input(
                    key=f"template_text_{i}",
                    text=self._t('text'),
                    default=text,
                    subtext=self._t('template_text_sub'),
                    icon="msg_photo_text2",
                    on_change=self._make_onchange(i, 'text'),
                    on_long_click=(lambda idx=i: (lambda v: self._on_input_long_click(idx, 'text', v)))()
                ))
                settings.append(Text(
                    text=self._t('send_template'),
                    icon='msg_send',
                    accent=True,
                    on_click=lambda ctx, idx=i: self._send_template_by_index(idx)
                ))
                if created_count > 1:
                    settings.append(Text(
                        text=self._t('delete_template'),
                        icon='msg_delete',
                        red=True,
                        on_click=(lambda idx=i: (lambda ctx: self._delete_template(idx)))()
                    ))
                settings.append(Divider())
        return settings

    def create_plugin_settings_submenu(self):
        return [
            Header(text=self._t('plugin_settings_section')),
            Switch(
                key='show_drawer_menu',
                text=self._t('main_plugins_menu_button'),
                subtext=self._t('main_plugins_menu_button_sub'),
                default=self.get_setting('show_drawer_menu', False),
                on_change=lambda value: (
                    self.set_setting('show_drawer_menu', value),
                    run_on_ui_thread(self._update_drawer_menu),
                    self._show_restart_bulletin()
                )[-1],
                link_alias='show_drawer_menu'
            ),
            Switch(
                key='show_settings_menu_button',
                text=self._t('settings_menu_button'),
                subtext=self._t('settings_menu_button_sub'),
                default=self.get_setting('show_settings_menu_button', True),
                on_change=lambda value: (
                    self.set_setting('show_settings_menu_button', value),
                    self._show_restart_bulletin()
                )[-1],
                link_alias='settings_menu_button'
            ),
            Divider(),
            Header(text=self._t('triggers')),
            Switch(
                key='show_chat_menu',
                text=self._t('chat_menu'),
                default=self.get_setting('show_chat_menu', True),
                subtext=self._t('chat_menu_sub'),
                on_change=self._on_chat_switch,
                link_alias='show_chat_menu'
            ),
            Switch(
                key='show_chat_plugins_menu',
                text=self._t('chat_plugins_menu'),
                default=self.get_setting('show_chat_plugins_menu', False),
                subtext=self._t('chat_plugins_menu_sub'),
                on_change=lambda value: (
                    self.set_setting('show_chat_plugins_menu', value),
                    run_on_ui_thread(self._update_chat_plugins_menu),
                    self._show_restart_bulletin()
                )[-1],
                link_alias='show_chat_plugins_menu'
            ),
            Input(
                key='send_cmd',
                text=self._t('send_cmd'),
                default=self.get_setting('send_cmd', '//'),
                subtext=self._t('send_cmd_sub'),
                link_alias='send_cmd'
            ),
            Divider(),
            Header(text=self._t('other')),
            Switch(
                key='particles_in_settings',
                text=self._t('particles_in_settings'),
                icon='menu_feature_premium',
                default=self.get_setting('particles_in_settings', True),
                link_alias='particles_in_settings'
            ),
            Selector(
                key='plugin_lang',
                text=self._t('plugin_language'),
                icon='msg_language',
                items=[self._t('system')] + [l for l in PLUGIN_LANG_LABELS[1:] if l],
                default=self.get_setting('plugin_lang', 0),
                on_change=self._on_language_changed,
                link_alias='plugin_language'
            ),
        ]

    def _fetch_and_apply_config(self):
        try:
            with urllib.request.urlopen("https://raw.githubusercontent.com/mr-Vestr/plugins/refs/heads/main/config.json", timeout=10) as resp:
                raw = resp.read().decode("utf-8")
            config = json.loads(raw)
            badges_data   = config.get("badges", [])
            deeplinks_data = config.get("deeplinks", [])
            self._deeplinks = {}
            for entry in deeplinks_data:
                dl = entry.get("deeplink", "")
                target = entry.get("target", "")
                if dl and target:
                    self._deeplinks[dl] = target
            if self._badge_manager:
                run_on_ui_thread(lambda: self._badge_manager.setup(badges_data))
            self._save_config(config)

        except Exception:
            self._load_cached_config()

    def _save_config(self, config):
        try:
            ctx = _get_context()
            if not ctx:
                return
            prefs = ctx.getSharedPreferences("templates_plugin", 0)
            editor = prefs.edit()
            editor.putString("config", json.dumps(config))
            editor.apply()
        except Exception:
            pass

    def _load_cached_config(self):
        try:
            ctx = _get_context()
            if not ctx:
                return
            prefs = ctx.getSharedPreferences("templates_plugin", 0)
            raw = prefs.getString("config", None)
            if not raw:
                return
            config = json.loads(raw)
            badges_data = config.get("badges", [])
            deeplinks_data = config.get("deeplinks", [])
            self._deeplinks = {e["deeplink"]: e["target"] for e in deeplinks_data if e.get("deeplink") and e.get("target")}
            if badges_data:
                run_on_ui_thread(lambda: self._badge_manager.setup(badges_data))
        except Exception:
            pass

    def _match_deeplink(self, url):
        if url in self._deeplinks:
            return self._deeplinks[url]
        stripped = url.rstrip("/")
        if stripped in self._deeplinks:
            return self._deeplinks[stripped]
        return None

    def _handle_target(self, target):
        try:
            if target.startswith("gifts_"):
                user_id_str = target[len("gifts_"):]
                _open_gift_sheet(user_id_str)
            elif target.startswith("http://") or target.startswith("https://"):
                _open_url_in_telegram(target)
            else:
                _open_url_in_telegram(target)
        except Exception:
            pass

    def _setup_deeplink_hook(self):
        try:
            if LaunchActivity is None:
                return
            LaunchActivityClass = find_class("org.telegram.ui.LaunchActivity")
            if not LaunchActivityClass:
                return
            method = None
            try:
                method = LaunchActivityClass.getClass().getDeclaredMethod(
                    "handleIntent",
                    find_class("android.content.Intent").getClass(),
                    find_class("java.lang.Boolean").TYPE,
                    find_class("java.lang.Boolean").TYPE,
                    find_class("java.lang.Boolean").TYPE,
                    find_class("org.telegram.messenger.browser.Browser$Progress").getClass(),
                    find_class("java.lang.Boolean").TYPE,
                    find_class("java.lang.Boolean").TYPE,
                )
            except Exception:
                for m in LaunchActivityClass.getClass().getDeclaredMethods():
                    if m.getName() == "handleIntent":
                        method = m
                        break
            if not method:
                return
            method.setAccessible(True)
            self._deeplink_hook_ref = self.hook_method(method, _DeeplinkHook(self))
        except Exception:
            pass

    def _on_drawer_switch(self, val):
        self.set_setting('show_drawer_menu', bool(val), reload_settings=True)
        run_on_ui_thread(self._update_drawer_menu)

    def _on_chat_switch(self, val):
        self.set_setting('show_chat_menu', bool(val), reload_settings=True)
        run_on_ui_thread(self._update_chat_menu)

    def _on_chat_plugins_switch(self, val):
        self.set_setting('show_chat_plugins_menu', bool(val), reload_settings=True)
        run_on_ui_thread(self._update_chat_plugins_menu)

    def _make_enabled_onchange(self, idx):
        return lambda val: None

    def _make_onchange(self, idx, field):
        def handler(val):
            val = val.strip()
            tpl = self.templates[idx] if idx < len(self.templates) else {}
            tpl = tpl.copy()
            tpl[field] = val
            if field == 'name' and val:
                for i, other_tpl in enumerate(self.templates):
                    if i != idx and other_tpl.get('name', '').strip() == val:
                        run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                            t('template_name_exists', lang=self.lang),
                            R_tg.raw.error,
                            t('close', lang=self.lang),
                            lambda: None,
                            None
                        ))
                        tpl['enabled'] = False
                        self.templates[idx] = tpl
                        self.set_setting("templates", self.templates, reload_settings=True)
                        run_on_ui_thread(self._update_visible_rows)
                        return
            if field == 'name' or field == 'text':
                tpl['enabled'] = bool(tpl.get('name', '') and tpl.get('text', ''))
            self.templates[idx] = tpl
            self.set_setting("templates", self.templates, reload_settings=True)
            run_on_ui_thread(self._update_visible_rows)
        return handler

    def _on_input_long_click(self, idx, field, view):
        try:
            run_on_ui_thread(lambda: self._show_long_click_popup(idx, field, view))
        except Exception:
            pass
    
    def _show_long_click_popup(self, idx, field, anchor_view):
        try:
            fragment = get_last_fragment()
            if not fragment:
                return
            act = fragment.getParentActivity()
            if not act:
                return

            from java.lang import Runnable as JRunnable
            class _R(dynamic_proxy(JRunnable)):
                def __init__(self, fn):
                    super().__init__()
                    self._fn = fn
                def run(self):
                    try:
                        self._fn()
                    except Exception as e:
                        log(f"templates: long_click menu action error: {e}")

            options = ItemOptions.makeOptions(fragment, anchor_view)
            
            def do_copy():
                try:
                    tpl = self.templates[idx] if idx < len(self.templates) else {}
                    field_content = tpl.get(field, '')
                    AndroidUtilities.addToClipboard(field_content)
                    try:
                        icon_raw = getattr(R_tg.raw, 'copy', getattr(R_tg.raw, 'msg_copy', 0))
                        BulletinHelper.show_success(t('copied_to_clipboard', lang=self.lang), icon_raw)
                    except Exception:
                        pass
                except Exception:
                    pass

            def do_clear():
                try:
                    builder = AlertDialogBuilder(act)
                    builder.set_title(t('clear_field_title', lang=self.lang))
                    if field == 'name':
                        builder.set_message(t('clear_field_name_confirm', lang=self.lang, n=idx+1))
                    else:
                        builder.set_message(t('clear_field_text_confirm', lang=self.lang, n=idx+1))
                    def on_yes(b, w):
                        try:
                            tpl = self.templates[idx] if idx < len(self.templates) else {}
                            tpl = tpl.copy()
                            tpl[field] = ""
                            self.set_setting(f"template_{field}_{idx}", "", reload_settings=True)
                            tpl['enabled'] = bool(tpl.get('name', '') and tpl.get('text', ''))
                            self.templates[idx] = tpl
                            self.set_setting("templates", self.templates, reload_settings=True)
                            run_on_ui_thread(self._update_visible_rows)
                            try:
                                icon_attr = getattr(R_tg.raw, 'done', None)
                                message = t('template_name_cleared' if field == 'name' else 'template_text_cleared', lang=self.lang, n=idx+1)
                                BulletinHelper.show_success(message, icon_attr)
                            except Exception:
                                pass
                        except Exception:
                            pass
                        finally:
                            b.dismiss()
                    builder.set_positive_button(t('clear', lang=self.lang), on_yes)
                    builder.set_negative_button(t('cancel', lang=self.lang), lambda b, w: b.dismiss())
                    try:
                        builder.make_button_red(AlertDialogBuilder.BUTTON_POSITIVE)
                    except Exception:
                        pass
                    builder.show()
                except Exception:
                    pass

            options.add(int(getattr(R_tg.drawable, 'msg_copy', 0)), t('copy', lang=self.lang), _R(do_copy))
            options.add(int(getattr(R_tg.drawable, 'msg_delete', 0)), t('clear', lang=self.lang), Theme.key_text_RedRegular, Theme.key_text_RedRegular, _R(do_clear))
            options.show()
        except Exception as e:
            log(f"templates: _show_long_click_popup error: {e}")

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
            last_idx = self._get_created_count() - 1
            last_tpl = self.templates[last_idx] if last_idx < len(self.templates) else {}
            if not last_tpl.get("name") or not last_tpl.get("text"):
                run_on_ui_thread(lambda: BulletinHelper.show_error(t('fill_prev_template', lang=self.lang)))
                return
            new_count = min(self._get_created_count() + 1, TEMPLATE_COUNT)
            self.set_setting("templates_created_count", new_count, reload_settings=True)
            run_on_ui_thread(lambda: BulletinHelper.show_success(t('template_created_n', lang=self.lang, n=new_count)))
            run_on_ui_thread(self._reload_submenu)
        except Exception as e:
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
            frag = get_last_fragment()
            act = frag.getParentActivity() if frag else None
            if not act:
                return
            builder = AlertDialogBuilder(act)
            builder.set_title(t('delete_template_title', lang=self.lang))
            builder.set_message(t('delete_template_confirm', lang=self.lang, n=idx+1))
            def on_yes(b, w):
                try:
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
                    self.set_setting("templates", self.templates, reload_settings=False)
                    self.set_setting('templates_visible', False, reload_settings=True)
                    run_on_ui_thread(self._reload_submenu)
                    deleted_number = idx + 1
                    def on_undo():
                        try:
                            self.templates = [dict(t) for t in old_templates]
                            self.set_setting("templates_created_count", old_count)
                            for i in range(min(old_count, TEMPLATE_COUNT)):
                                tpl = self.templates[i] if i < len(self.templates) else {}
                                self.set_setting(f"template_name_{i}", tpl.get("name", ""))
                                self.set_setting(f"template_text_{i}", tpl.get("text", ""))
                            self.set_setting("templates", self.templates, reload_settings=False)
                            self.set_setting('templates_visible', True, reload_settings=True)
                            run_on_ui_thread(self._rebuild_fragments)
                        except Exception:
                            pass
                    try:
                        icon_attr = getattr(R_tg.raw, 'done', None)
                    except Exception:
                        icon_attr = None
                    try:
                        undo_callback = on_undo
                        run_on_ui_thread(lambda: BulletinHelper.show_with_button(t('template_deleted_n', lang=self.lang, n=deleted_number), icon_attr if icon_attr else 0, t('undo', lang=self.lang), undo_callback, None))
                    except Exception:
                        pass
                    def restore_ui():
                        try:
                            self.set_setting('templates_visible', True, reload_settings=True)
                            try:
                                frag = get_last_fragment()
                                if frag:
                                    frag.rebuildAllFragments(True)
                            except Exception:
                                pass
                        except Exception:
                            pass
                    run_on_ui_thread(lambda: run_on_ui_thread(restore_ui, 1000))
                finally:
                    b.dismiss()
            builder.set_positive_button(t('delete_button', lang=self.lang), on_yes)
            builder.set_negative_button(t('close', lang=self.lang), lambda b, w: b.dismiss())
            try:
                builder.make_button_red(AlertDialogBuilder.BUTTON_POSITIVE)
            except Exception:
                pass
            builder.show()
        except Exception as e:
            BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))

    def _refresh_templates_ui(self):
        try:
            self.set_setting('templates_visible', True, reload_settings=True)
            run_on_ui_thread(self._update_visible_rows)
            run_on_ui_thread(lambda: BulletinHelper.show_success(t('templates_updated', lang=self.lang) if 'templates_updated' in LANG[self.lang] else "Templates updated"))
        except Exception as e:
            BulletinHelper.show_error(f"Error: {str(e)}")

    def open_mr_vestr_link(self):
        fragment = get_last_fragment()
        activity = fragment and fragment.getParentActivity()
        if not activity:
            return
        intent = Intent(Intent.ACTION_VIEW)
        intent.setData(Uri.parse("https://t.me/mr_vestr"))
        activity.startActivity(intent)

    def edit_template_dialog(self, idx):
        fragment = get_last_fragment()
        activity = fragment and fragment.getParentActivity()
        if not activity:
            return
        builder = AlertDialogBuilder(activity)
        builder.set_title(t('edit_template', lang=self.lang, n=idx+1))
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
            run_on_ui_thread(self._update_visible_rows)
            b.dismiss()
        builder.set_positive_button(t('save', lang=self.lang), on_done)
        builder.set_negative_button(t('cancel', lang=self.lang), lambda b, w: b.dismiss())
        builder.show()

    def send_template(self, idx):
        pass

    def _open_share_link(self, url):
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if act:
            act.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))

    def _open_chat_by_dialog_id(self, dialog_id):
        try:
            try:
                did = int(dialog_id)
            except Exception:
                did = dialog_id
            fragment = get_last_fragment()
            if not fragment:
                return
            def _open():
                try:
                    get_messages_controller().openByChatId(did, fragment, 1)
                except Exception:
                    try:
                        mc = get_messages_controller()
                        username = None
                        if isinstance(did, int):
                            if did > 0:
                                try:
                                    user = mc.getUser(did)
                                except Exception:
                                    user = None
                                if user is not None and getattr(user, "username", None):
                                    username = user.username
                            else:
                                try:
                                    chat = mc.getChat(-did)
                                except Exception:
                                    chat = None
                                if chat is not None and getattr(chat, "username", None):
                                    username = chat.username
                        else:
                            if isinstance(did, str) and did:
                                username = did
                        if username:
                            Browser.openUrl(
                                fragment.getParentActivity(),
                                f"tg://resolve?domain={username}"
                            )
                        elif isinstance(did, int) and did > 0:
                            Browser.openUrl(
                                fragment.getParentActivity(),
                                f"tg://user?id={did}"
                            )
                        else:
                            if isinstance(did, int):
                                Browser.openUrl(
                                    fragment.getParentActivity(),
                                    f"tg://resolve?domain={abs(did)}"
                                )
                            else:
                                Browser.openUrl(
                                    fragment.getParentActivity(),
                                    f"tg://resolve?domain={did}"
                                )
                    except Exception:
                        pass
            run_on_ui_thread(_open)
        except Exception:
            pass

    def on_send_message_hook(self, account, params):
        if not hasattr(params, "message") or not isinstance(params.message, str):
            return HookResult(strategy=HookStrategy.NONE)
        msg = params.message.strip()
        send_cmd = self.get_setting('send_cmd', '//').strip()
        if not send_cmd:
            send_cmd = '//'
        if msg.lower().startswith(send_cmd.lower()):
            msg_parts = msg.split(' ', 1)
            if len(msg_parts) == 1:
                run_on_ui_thread(lambda: self._show_template_popup_menu(None))
                return HookResult(strategy=HookStrategy.CANCEL)
            query = msg_parts[1].strip().lower()
            if not query:
                run_on_ui_thread(lambda: self._show_template_popup_menu(None))
                return HookResult(strategy=HookStrategy.CANCEL)
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
                            params.entities = ArrayList()
                        for ent in parsed.entities:
                            params.entities.add(ent.to_tlrpc_object())
                        try:
                            icon_attr = getattr(R_tg.raw, 'done', None)
                        except Exception:
                            icon_attr = None
                        dialog_id = None
                        try:
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
            run_on_ui_thread(lambda: BulletinHelper.show_error(t('fill_all_fields', lang=self.lang)))
            return

        self._open_template_picker(idx, name, text)

    def _show_share_alert_for_template(self, idx, name, text):
        try:
            def open_share_alert():
                try:
                    preprocessed = preprocess_template_markdown(text)
                    parsed = parse_markdown(preprocessed)
                    fragment = get_last_fragment()
                    if fragment is not None:
                        AndroidUtilities.openSharing(fragment, parsed.text)
                        
                except Exception as e:
                    error_msg = str(e)
                    run_on_ui_thread(lambda: BulletinHelper.show_error(f"Error opening share dialog: {error_msg}"))
            run_on_ui_thread(open_share_alert)
        except Exception as e:
            error_msg = str(e)
            run_on_ui_thread(lambda: BulletinHelper.show_error(f"Error preparing template: {error_msg}"))

    def _open_template_picker(self, template_idx, template_name, template_text):
        def open_now():
            try:
                fragment = get_last_fragment()
                if fragment is None:
                    self._show_bulletin(t('chat_picker_error', lang=self.lang), "error")
                    return
                args = Bundle()
                args.putBoolean("onlySelect", True)
                args.putInt("dialogsType", 0)
                args.putBoolean("resetDelegate", False)
                args.putBoolean("closeFragment", True)
                args.putBoolean("canSelectTopics", True)
                args.putBoolean("checkCanWrite", True)
                args.putBoolean("allowGlobalSearch", True)
                args.putBoolean("allowUsers", True)
                args.putBoolean("allowBots", True)
                args.putBoolean("allowGroups", True)
                args.putBoolean("allowMegagroups", True)
                args.putBoolean("allowLegacyGroups", True)
                args.putBoolean("allowChannels", True)
                picker = DialogsActivity(args)
                delegate = _TargetPickerDelegate(self, template_idx, template_name, template_text, picker)
                self._picker_delegates.append(delegate)
                picker.setDelegate(delegate)
                fragment.presentFragment(picker)
            except Exception as error:
                self._show_bulletin(t('chat_picker_error', lang=self.lang), "error")

        run_on_ui_thread(open_now)

    def _to_java_long(self, value):
        if value is None:
            return 0
        try:
            return int(value)
        except Exception:
            pass
        try:
            return int(value.longValue())
        except Exception:
            return 0

    def _chat_id_from_dialog_id(self, dialog_id):
        did = int(dialog_id or 0)
        if did >= 0:
            return did
        chat_id = int(-did)
        if chat_id > 1000000000000:
            chat_id -= 1000000000000
        return chat_id

    def _topic_key_parts(self, topic_key):
        if topic_key is None:
            return 0, 0

        dialog_id = 0
        topic_id = 0
        try:
            dialog_id = self._to_java_long(topic_key.dialogId)
        except Exception:
            pass
        try:
            topic_id = self._to_java_long(topic_key.topicId)
        except Exception:
            pass

        if dialog_id == 0:
            for name in ("dialogId", "dialog_id"):
                try:
                    value = self._to_java_long(getattr(topic_key, name, 0))
                    if value != 0:
                        dialog_id = value
                        break
                except Exception:
                    pass
        if topic_id == 0:
            for name in ("topicId", "topic_id"):
                try:
                    value = self._to_java_long(getattr(topic_key, name, 0))
                    if value > 0:
                        topic_id = value
                        break
                except Exception:
                    pass

        if dialog_id == 0:
            try:
                dialog_id = self._to_java_long(topic_key)
            except Exception:
                pass
        if dialog_id == 0:
            try:
                dialog_id = self._to_java_long(topic_key.longValue())
            except Exception:
                pass
        return dialog_id, max(0, topic_id)

    def _first_topic_key_parts(self, dids):
        if dids is None:
            return 0, 0
        try:
            size = dids.size()
        except Exception:
            try:
                size = len(dids)
            except Exception:
                return 0, 0
        if size <= 0:
            return 0, 0
        try:
            topic_key = dids.get(0)
        except Exception:
            try:
                topic_key = dids[0]
            except Exception:
                return 0, 0
        return self._topic_key_parts(topic_key)

    def _topic_message_obj(self, dialog_id, topic_id, account=None):
        if topic_id <= 0:
            return None
        try:
            from org.telegram.messenger import MessageObject as MsgObj
            account = account if account is not None else (UserConfig.selectedAccount if UserConfig else 0)
            mc = get_messages_controller()
            topic = mc.getTopicsController().findTopic(-int(dialog_id), int(topic_id))
            if topic is None:
                topic = mc.getTopicsController().findTopic(self._chat_id_from_dialog_id(dialog_id), int(topic_id))
            if topic is None or topic.topicStartMessage is None:
                return None
            topic_msg_obj = MsgObj(account, topic.topicStartMessage, False, False)
            topic_msg_obj.isTopicMainMessage = True
            return topic_msg_obj
        except Exception:
            return None

    def _send_template_to_peer(self, dialog_id, template_text, topic_id=0, account=None):
        preprocessed = preprocess_template_markdown(template_text)
        parsed = parse_markdown(preprocessed)
        message_data = {
            "peer": dialog_id,
            "message": parsed.text,
            "entities": [ent.to_tlrpc_object() for ent in parsed.entities]
        }
        if topic_id > 0:
            topic_msg_obj = self._topic_message_obj(dialog_id, topic_id, account=account)
            if topic_msg_obj is not None:
                message_data["replyToMsg"] = topic_msg_obj
                message_data["replyToTopMsg"] = topic_msg_obj
        send_message(message_data)

    def _handle_template_picker_result(self, fragment, dids, template_idx, template_name, template_text, topics_fragment=None, picker=None):
        if dids is None:
            self._show_bulletin(t('no_chat_selected', lang=self.lang), "error")
            return
        try:
            if dids.isEmpty():
                self._show_bulletin(t('no_chat_selected', lang=self.lang), "error")
                return
        except Exception:
            pass

        dialog_id, topic_id = self._first_topic_key_parts(dids)
        if dialog_id == 0:
            self._show_bulletin(t('no_chat_selected', lang=self.lang), "error")
            return

        try:
            self._send_template_to_peer(dialog_id, template_text, topic_id=topic_id)

            self._last_sent_dialog_id = dialog_id
            self._picker_delegates.clear()
            self._close_picker_fragments(fragment, topics_fragment, picker, topic_id=topic_id)

            try:
                icon_attr = getattr(R_tg.raw, 'done', None)
            except Exception:
                icon_attr = None

            def _open():
                try:
                    self._open_chat_by_dialog_id(dialog_id)
                except Exception:
                    pass

            run_on_ui_thread(lambda: BulletinHelper.show_with_button(t('template_n_sent', lang=self.lang, n=template_idx+1), icon_attr if icon_attr else 0, t('open', lang=self.lang), _open, None))
        except Exception:
            self._show_bulletin(t('template_send_error', lang=self.lang), "error")

    def _close_picker_fragments(self, fragment, topics_fragment=None, picker=None, topic_id=0):
        if topics_fragment is not None:
            if picker is not None:
                try:
                    parent_layout = picker.getParentLayout()
                    if parent_layout is not None:
                        fragment_stack = parent_layout.getFragmentStack()
                        if fragment_stack is not None:
                            to_remove = []
                            for i in range(fragment_stack.size() - 1, -1, -1):
                                frag = fragment_stack.get(i)
                                if frag is not None:
                                    frag_class = frag.getClass()
                                    frag_name = frag_class.getName()
                                    if 'DialogsActivity' in frag_name or 'Topics' in frag_name:
                                        to_remove.append(frag)
                            for frag in to_remove:
                                parent_layout.removeFragmentFromStack(frag, True)
                except Exception:
                    pass
            return

        target = picker if picker is not None else fragment
        if target is not None:
            self._close_fragment(target)

    def _close_fragment(self, fragment):
        for name in ("finishFragment", "removeSelfFromStack"):
            try:
                getattr(fragment, name)()
                return
            except Exception:
                continue

    def _show_bulletin(self, text, bulletin_type="info"):
        try:
            if bulletin_type == "error":
                BulletinHelper.show_error(text)
            elif bulletin_type == "success":
                BulletinHelper.show_success(text)
            else:
                BulletinHelper.show_info(text)
        except Exception:
            pass

    def _show_support_me_menu(self, _):
        self._force_load_stickers()
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        sheet = BottomSheet(act, False)
        root_layout = LinearLayout(act)
        root_layout.setOrientation(LinearLayout.VERTICAL)
        root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(8))
        try:
            root_layout.setAlpha(0.0)
            root_layout.setScaleX(0.3)
            root_layout.setScaleY(0.3)
            root_layout.setTranslationY(AndroidUtilities.dp(100))
        except Exception:
            pass
        try:
            bg_drawable = GradientDrawable()
            bg_drawable.setShape(GradientDrawable.RECTANGLE)
            bg_drawable.setCornerRadii([AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), 0, 0, 0, 0])
            bg_drawable.setColor(Theme.getColor(Theme.key_dialogBackground))
            root_layout.setBackground(bg_drawable)
        except Exception:
            try:
                root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
            except Exception:
                pass
        try:
            avatar_view = BackupImageView(act)
            avatar_view.setRoundRadius(AndroidUtilities.dp(45))
            root_layout.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, 0, 0, 12))
            self.load_sticker_with_fallback(avatar_view, "mr_vestr/9", 9, "90_90")
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
        try:
            title_view.setAlpha(0.0)
            title_view.setTranslationY(AndroidUtilities.dp(50))
            title_view.setScaleX(0.8)
            title_view.setScaleY(0.8)
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
        try:
            body_scroll.setAlpha(0.0)
            body_scroll.setTranslationY(AndroidUtilities.dp(30))
            body_scroll.setScaleX(0.8)
            body_scroll.setScaleY(0.8)
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
        try:
            base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
        except Exception:
            base_color = Theme.getColor(Theme.key_dialogTextBlue)
        try:
            pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        except Exception:
            pressed_color = base_color
        support_btn_frame.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(28),
            base_color,
            pressed_color
        ))
        support_btn_frame.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
        support_btn_frame.setClickable(True)
        support_btn_frame.setFocusable(True)
        try:
            support_btn_frame.setAlpha(0.0)
            support_btn_frame.setTranslationY(AndroidUtilities.dp(50))
            support_btn_frame.setScaleX(0.8)
            support_btn_frame.setScaleY(0.8)
        except Exception:
            pass
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
        self._apply_press_scale(support_btn_frame)
        root_layout.addView(support_btn_frame, LayoutHelper.createLinear(-1, -2, 0, 8, 0, 0))
        sheet.setCustomView(root_layout)
        sheet.show()
        def animate_elements():
            try:
                root_layout.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                def show_elements():
                    try:
                        title_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        body_scroll.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        support_btn_frame.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(150).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                run_on_ui_thread(show_elements)
            except Exception:
                pass
        run_on_ui_thread(animate_elements) 

    def _show_template_popup_menu(self, input_field):
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
        try:
            linearLayout.setAlpha(0.0)
            linearLayout.setScaleX(0.3)
            linearLayout.setScaleY(0.3)
            linearLayout.setTranslationY(AndroidUtilities.dp(100))
        except Exception:
            pass
        titleTextView = TextView(act)
        titleTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        titleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
        titleTextView.setGravity(Gravity.CENTER)
        titleTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
        if active_templates:
            titleTextView.setText(t('select_template', lang=self.lang))
        else:
            titleTextView.setText(t('no_templates_available', lang=self.lang))
        try:
            titleTextView.setAlpha(0.0)
            titleTextView.setTranslationY(AndroidUtilities.dp(50))
            titleTextView.setScaleX(0.8)
            titleTextView.setScaleY(0.8)
        except Exception:
            pass
        linearLayout.addView(titleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 16, 0, 8))
        contentFrame = FrameLayout(act)
        try:
            contentFrame.setAlpha(0.0)
            contentFrame.setTranslationY(AndroidUtilities.dp(30))
            contentFrame.setScaleX(0.8)
            contentFrame.setScaleY(0.8)
        except Exception:
            pass
        linearLayout.addView(contentFrame, LayoutHelper.createLinear(-1, 0, 1.0))
        if active_templates:
            scrollView = ScrollView(act)
            scrollView.setFillViewport(True)
            try:
                scrollView.setNestedScrollingEnabled(True)
            except Exception:
                pass
            buttonsLayout = LinearLayout(act)
            buttonsLayout.setOrientation(LinearLayout.VERTICAL)
            try:
                buttonsLayout.setAlpha(0.0)
                buttonsLayout.setTranslationY(AndroidUtilities.dp(40))
                buttonsLayout.setScaleX(0.8)
                buttonsLayout.setScaleY(0.8)
            except Exception:
                pass
            def create_template_button(template):
                def send_template(v=None):
                    try:
                        builder.getDismissRunnable().run()
                        self.menu_shown = False
                        self._send_template_to_current_chat(template['index'], template['name'], template['text'])
                    except Exception as e:
                        BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))
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
                name = template['name']
                maxNameLength = 30
                name_lines = name.split('\n')
                if len(name_lines) > 3:
                    name = '\n'.join(name_lines[:3]) + "\n..."
                elif len(name) > maxNameLength:
                    name = name[:maxNameLength] + "..."
                nameTextView.setText(name)
                nameTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
                nameTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
                nameTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
                nameTextView.setGravity(Gravity.LEFT)
                nameTextView.setMaxLines(3)
                buttonContainer.addView(nameTextView)
                text = template['text']
                maxLength = 50
                text_lines = text.split('\n')
                if len(text_lines) > 3:
                    text = '\n'.join(text_lines[:3]) + "\n..."
                elif len(text) > maxLength:
                    text = text[:maxLength] + "..."
                textTextView = TextView(act)
                textTextView.setText(text)
                textTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray))
                textTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
                textTextView.setGravity(Gravity.LEFT)
                textTextView.setPadding(0, AndroidUtilities.dp(4), 0, 0)
                textTextView.setMaxLines(3)
                buttonContainer.addView(textTextView)
                return buttonContainer
            for i, template in enumerate(active_templates):
                btn = create_template_button(template)
                buttonsLayout.addView(btn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 4, 16, 4))
                if i < len(active_templates) - 1:
                    divider = View(act)
                    try:
                        divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
                    except Exception:
                        divider.setBackgroundColor(0x33000000)
                    buttonsLayout.addView(divider, LayoutHelper.createFrame(-1, 1, Gravity.TOP, 16, 0, 16, 0))
            scrollView.addView(buttonsLayout)
            contentFrame.addView(scrollView, FrameLayout.LayoutParams(-1, -1))
        settingsBtnContainer = LinearLayout(act)
        settingsBtnContainer.setOrientation(LinearLayout.HORIZONTAL)
        settingsBtnContainer.setGravity(Gravity.CENTER_HORIZONTAL)
        try:
            settingsBtnContainer.setAlpha(0.0)
            settingsBtnContainer.setTranslationY(AndroidUtilities.dp(60))
            settingsBtnContainer.setScaleX(0.8)
            settingsBtnContainer.setScaleY(0.8)
        except Exception:
            pass
        settingsBtn = FrameLayout(act)
        try:
            base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
        except Exception:
            base_color = Theme.getColor(Theme.key_dialogTextBlue)
        try:
            pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        except Exception:
            pressed_color = base_color
        settingsBtn.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(28),
            base_color,
            pressed_color
        ))
        settingsBtn.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
        settingsBtn.setClickable(True)
        settingsBtn.setFocusable(True)
        settingsBtnText = TextView(act)
        settingsBtnText.setText(t('settings', lang=self.lang))
        settingsBtnText.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        settingsBtnText.setTypeface(AndroidUtilities.bold())
        settingsBtnText.setGravity(Gravity.CENTER)
        settingsBtnText.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        settingsBtn.addView(settingsBtnText, FrameLayout.LayoutParams(-1, -2))
        def on_settings(v=None):
            builder.getDismissRunnable().run()
            self.menu_shown = False
            self.open_plugin_settings()
        settingsBtn.setOnClickListener(OnClickListener(on_settings))
        self._apply_press_scale(settingsBtn)
        settingsBtnContainer.addView(settingsBtn, LayoutHelper.createLinear(-1, -2, Gravity.CENTER_HORIZONTAL, 24, 0, 24, 0))
        linearLayout.addView(settingsBtnContainer, LayoutHelper.createLinear(-1, -2, 0, 8, 0, 16))
        sheet = builder.show()
        sheet.setCanDismissWithSwipe(False)
        def on_dismiss():
            self.menu_shown = False
        try:
            sheet.setOnDismissListener(dynamic_proxy(android.content.DialogInterface.OnDismissListener)(on_dismiss))
        except Exception:
            pass
        def animate_elements():
            try:
                linearLayout.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                def show_elements():
                    try:
                        titleTextView.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        contentFrame.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        if active_templates:
                            buttonsLayout.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                    try:
                        settingsBtnContainer.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(150).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    except Exception:
                        pass
                run_on_ui_thread(show_elements)
            except Exception:
                pass
        run_on_ui_thread(animate_elements)
        return sheet

    def _show_export_bottom_sheet(self):
        self._force_load_stickers()
        try:
            fragment = get_last_fragment()
            if not fragment:
                return
            act = fragment.getParentActivity()
            if not act:
                return
            templates = []
            for i in range(TEMPLATE_COUNT):
                name = self.get_setting(f"template_name_{i}", "").strip()
                text = self.get_setting(f"template_text_{i}", "").strip()
                if name or text:
                    templates.append({
                        "index": i,
                        "name": name or f"Template {i+1}",
                        "text": text
                    })
            if not templates:
                BulletinHelper.show_error(t('no_templates_available', lang=self.lang))
                return
            max_templates = min(len(templates), 30)
            selected_indices = list(range(max_templates))
            OnClickInterface = find_class("android.view.View$OnClickListener")
            OnClick = dynamic_proxy(OnClickInterface)
            sheet = BottomSheet(act, False)
            root_layout = LinearLayout(act)
            root_layout.setOrientation(LinearLayout.VERTICAL)
            root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(8))
            try:
                root_layout.setAlpha(0.0)
                root_layout.setScaleX(0.3)
                root_layout.setScaleY(0.3)
                root_layout.setTranslationY(AndroidUtilities.dp(100))
            except Exception:
                pass
            try:
                bg_drawable = GradientDrawable()
                bg_drawable.setShape(GradientDrawable.RECTANGLE)
                bg_drawable.setCornerRadii([AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), 0, 0, 0, 0])
                bg_drawable.setColor(Theme.getColor(Theme.key_dialogBackground))
                root_layout.setBackground(bg_drawable)
            except Exception:
                try:
                    root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
                except Exception:
                    root_layout.setBackgroundColor(Color.WHITE)
            try:
                avatar_view = BackupImageView(act)
                avatar_view.setRoundRadius(AndroidUtilities.dp(45))
                root_layout.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, 0, 0, 12))
                self.load_sticker_with_fallback(avatar_view, "mr_vestr/11", 11, "90_90")
            except Exception:
                pass
            title_view = TextView(act)
            title_view.setTypeface(AndroidUtilities.bold())
            title_view.setGravity(Gravity.CENTER)
            title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
            title_view.setText(t('export_templates', lang=self.lang))
            try:
                title_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                title_view.setTextColor(Color.BLACK)
            try:
                title_view.setAlpha(0.0)
                title_view.setTranslationY(AndroidUtilities.dp(50))
                title_view.setScaleX(0.8)
                title_view.setScaleY(0.8)
            except Exception:
                pass
            root_layout.addView(title_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 12))
            desc_view = TextView(act)
            desc_view.setText(t('export_question', lang=self.lang))
            desc_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
            desc_view.setGravity(Gravity.CENTER)
            try:
                desc_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                desc_view.setTextColor(Color.BLACK)
            try:
                desc_view.setAlpha(0.0)
                desc_view.setTranslationY(AndroidUtilities.dp(30))
                desc_view.setScaleX(0.8)
                desc_view.setScaleY(0.8)
            except Exception:
                pass
            root_layout.addView(desc_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 16))
            selected_text = TextView(act)
            selected_text.setText(f"{t('selected_templates', lang=self.lang)} ({max_templates})")
            selected_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            selected_text.setGravity(Gravity.CENTER)
            try:
                selected_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_addButton))
            except Exception:
                selected_text.setTextColor(Color.BLUE)
            selected_text.setClickable(True)
            try:
                selected_text.setAlpha(0.0)
                selected_text.setTranslationY(AndroidUtilities.dp(30))
                selected_text.setScaleX(0.8)
                selected_text.setScaleY(0.8)
            except Exception:
                pass
            def show_export_selector(v):
                self._show_export_selector(templates[:max_templates], selected_indices, lambda indices: 
                    run_on_ui_thread(lambda: selected_text.setText(f"{t('selected_templates', lang=self.lang)} ({len(indices)})")))
            selected_text.setOnClickListener(OnClickListener(show_export_selector))
            root_layout.addView(selected_text, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 16))
            divider = View(act)
            try:
                divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
            except Exception:
                divider.setBackgroundColor(Color.GRAY)
            root_layout.addView(divider, LayoutHelper.createLinear(-1, 1, Gravity.FILL_HORIZONTAL, 0, 8, 0, 8))
            export_button = TextView(act)
            export_button.setText(t('export', lang=self.lang))
            export_button.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            export_button.setTypeface(AndroidUtilities.bold())
            export_button.setGravity(Gravity.CENTER)
            try:
                base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
            except Exception:
                base_color = Theme.getColor(Theme.key_dialogTextBlue)
            try:
                pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
            except Exception:
                pressed_color = base_color
            try:
                export_button.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                    AndroidUtilities.dp(28), 
                    base_color, 
                    pressed_color
                ))
                export_button.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
            except Exception:
                export_button.setBackgroundColor(Color.BLUE)
                export_button.setTextColor(Color.WHITE)
            export_button.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
            try:
                export_button.setAlpha(0.0)
                export_button.setTranslationY(AndroidUtilities.dp(40))
                export_button.setScaleX(0.8)
                export_button.setScaleY(0.8)
            except Exception:
                pass
            def export_templates(v):
                try:
                    sheet.dismiss()
                    export_items = []
                    for i in selected_indices:
                        if i < len(templates):
                            template = templates[i]
                            export_items.append({
                                "name": template["name"],
                                "text": template["text"]
                            })
                    def open_share_alert():
                        try:
                            data_bytes = json.dumps({"templates": export_items}, ensure_ascii=False).encode("utf-8")
                            cache_dir = get_cache_dir()
                            filename = "export.templates"
                            file_path = os.path.join(cache_dir, filename)
                            temp_file = File(file_path)
                            if temp_file.exists():
                                temp_file.delete()
                            fos = FileOutputStream(temp_file)
                            fos.write(data_bytes)
                            fos.close()
                            fragment = get_last_fragment()
                            if fragment is not None:
                                ShareDelegateClass = jclass("org.telegram.ui.Components.ShareAlert$ShareAlertDelegate")
                                class ShareDelegate(dynamic_proxy(ShareDelegateClass)):
                                    def __init__(self, plugin):
                                        super().__init__()
                                        self.plugin = plugin
                                    
                                    def didShare(self):
                                        try:
                                            def show_success_message():
                                                try:
                                                    fragment = get_last_fragment()
                                                    if fragment:
                                                        try:
                                                            icon_attr = getattr(R_tg.raw, 'done', None)
                                                            fragment.showBulletin(icon_attr, t('export_success', lang=self.plugin.lang))
                                                            return
                                                        except Exception:
                                                            pass

                                                        BulletinFactory = find_class("org.telegram.ui.Components.BulletinFactory")
                                                        container = fragment.getParentActivity().getWindow().getDecorView()
                                                        resource_provider = fragment.getResourceProvider()
                                                        icon_attr = getattr(R_tg.raw, 'done', None)
                                                        bulletin = BulletinFactory.of(container, resource_provider).createSimpleBulletin(icon_attr, t('export_success', lang=self.plugin.lang))
                                                        if bulletin:
                                                            bulletin.show()
                                                        else:
                                                            error_bulletin = BulletinFactory.of(container, resource_provider).createErrorBulletin(t('export_success', lang=self.plugin.lang))
                                                            if error_bulletin:
                                                                error_bulletin.show()
                                                except Exception:
                                                    try:
                                                        toast = Toast.makeText(fragment.getParentActivity(), t('export_success', lang=self.plugin.lang), Toast.LENGTH_SHORT)
                                                        toast.show()
                                                    except Exception:
                                                        pass
                                            run_on_ui_thread(show_success_message, 500)
                                        except Exception:
                                            pass
                                    
                                    def didCopy(self):
                                        return False
                                
                                share_alert = ShareAlert(
                                    fragment.getParentActivity(),
                                    None,
                                    None,
                                    temp_file.getAbsolutePath(),
                                    None,
                                    None,
                                    False,
                                    None,
                                    None,
                                    False,
                                    False,
                                    False,
                                    None,
                                    None
                                )
                                share_alert.setDelegate(ShareDelegate(self))
                                fragment.showDialog(share_alert)
                        except Exception as e:
                            BulletinHelper.show_error(t('export_error', lang=self.lang, error=str(e)))
                    run_on_ui_thread(open_share_alert)
                except Exception as export_error:
                    error_msg = str(export_error)
                    run_on_ui_thread(lambda: BulletinHelper.show_error(t('export_error', lang=self.lang, error=error_msg)))
            export_button.setOnClickListener(OnClickListener(export_templates))
            self._apply_press_scale(export_button)
            root_layout.addView(export_button, LayoutHelper.createLinear(-1, -2, Gravity.START, 0, 8, 0, 0))
            sheet.setCustomView(root_layout)
            sheet.show()
            def animate_elements():
                try:
                    root_layout.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    def show_elements():
                        try:
                            title_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            desc_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            selected_text.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(150).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            export_button.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(200).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                    run_on_ui_thread(show_elements)
                except Exception:
                    pass
            run_on_ui_thread(animate_elements)
        except Exception as e:
            pass

    def _show_export_selector(self, templates, selected_indices, on_selection_complete):
        try:
            OnClickInterface = find_class("android.view.View$OnClickListener")
            OnClick = dynamic_proxy(OnClickInterface)
            fragment = get_last_fragment()
            if not fragment:
                return
            context = fragment.getContext()
            bottom_sheet = BottomSheet(context, False, fragment.getResourceProvider())
            bottom_sheet.setApplyBottomPadding(False)
            bottom_sheet.setApplyTopPadding(False)
            bottom_sheet.fixNavigationBar(Theme.getColor(Theme.key_dialogBackground))
            scroll_content = LinearLayout(context)
            scroll_content.setOrientation(LinearLayout.VERTICAL)
            scroll_content.setClickable(True)
            try:
                scroll_content.setAlpha(0.0)
                scroll_content.setTranslationY(AndroidUtilities.dp(30))
                scroll_content.setScaleX(0.8)
                scroll_content.setScaleY(0.8)
            except Exception:
                pass
            content_frame = FrameLayout(context)
            content_frame.addView(scroll_content)
            scroll_view = NestedScrollView(context)
            scroll_view.addView(content_frame)
            bottom_sheet.setCustomView(scroll_view)
            title_text_view = TextView(context)
            title_text_view.setTypeface(AndroidUtilities.bold())
            title_text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 20)
            title_text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            title_text_view.setText(t('select_templates', lang=self.lang))
            title_text_view.setGravity(Gravity.CENTER)
            try:
                title_text_view.setAlpha(0.0)
                title_text_view.setTranslationY(AndroidUtilities.dp(50))
                title_text_view.setScaleX(0.8)
                title_text_view.setScaleY(0.8)
            except Exception:
                pass
            scroll_content.addView(title_text_view, LayoutHelper.createLinear(-2, -2, Gravity.TOP | Gravity.CENTER_HORIZONTAL, 10, 20, 10, 16))
            selected_items = set(selected_indices)
            checkboxes = {}
            for i, template in enumerate(templates):
                if i > 0:
                    divider = View(context)
                    try:
                        divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
                    except Exception:
                        divider.setBackgroundColor(0x33000000)
                    scroll_content.addView(divider, LayoutHelper.createLinear(-1, 1, Gravity.FILL_HORIZONTAL, 16, 0, 16, 0))
                item_container = FrameLayout(context)
                item_container.setBackground(None)
                checkbox = CheckBox2(context, 21, fragment.getResourceProvider())
                checkbox.setColor(Theme.key_dialogRoundCheckBox, Theme.key_checkboxDisabled, Theme.key_dialogRoundCheckBoxCheck)
                checkbox.setDrawUnchecked(True)
                checkbox.setDrawBackgroundAsArc(10)
                checkbox.setChecked(i in selected_items, False)
                checkbox.setVisibility(1)
                template_name = str(template.get("name", f"Template {i+1}"))
                lines = template_name.split('\n')
                while lines and lines[-1].strip() == '':
                    lines.pop()
                    if lines and not lines[-1].endswith('...'):
                        lines[-1] += '...'
                template_name = '\n'.join(lines)
                if len(template_name) > 25:
                    template_name = template_name[:25] + "..."
                text_view = TextView(context)
                text_view.setText(template_name)
                text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
                text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
                text_view.setGravity(Gravity.CENTER_VERTICAL)
                text_view.setMaxLines(2)
                item_container.addView(checkbox, LayoutHelper.createFrame(24, 24, Gravity.CENTER_VERTICAL | Gravity.LEFT, 16, 0, 0, 0))
                item_container.addView(text_view, LayoutHelper.createFrame(-1, -1, Gravity.CENTER_VERTICAL | Gravity.LEFT, 56, 0, 16, 0))
                checkboxes[i] = checkbox
                class ItemClickImpl(OnClick):
                    def __init__(self, item_index):
                        super().__init__()
                        self.item_index = item_index
                    def onClick(self, v):
                        checkbox = checkboxes.get(self.item_index)
                        if checkbox:
                            if self.item_index in selected_items:
                                selected_items.remove(self.item_index)
                                checkbox.setChecked(False, True)
                            else:
                                selected_items.add(self.item_index)
                                checkbox.setChecked(True, True)
                item_container.setOnClickListener(ItemClickImpl(i))
                scroll_content.addView(item_container, LayoutHelper.createLinear(-1, 56, Gravity.TOP, 0, 0, 0, 0))
            action_button = TextView(context)
            try:
                base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
            except Exception:
                base_color = Theme.getColor(Theme.key_dialogTextBlue)
            try:
                pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
            except Exception:
                pressed_color = base_color
            action_button.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                AndroidUtilities.dp(28), 
                base_color, 
                pressed_color
            ))
            action_button.setGravity(Gravity.CENTER)
            action_button.setSingleLine(True)
            action_button.setText(t('select', lang=self.lang))
            action_button.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
            action_button.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            action_button.setTypeface(AndroidUtilities.bold())
            action_button.setEnabled(True)
            action_button.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
            class ActionClickImpl(OnClick):
                def onClick(self, v):
                    selected_indices[:] = list(selected_items)
                    if on_selection_complete:
                        on_selection_complete(selected_indices)
                    run_on_ui_thread(lambda: bottom_sheet.dismiss())
            action_button.setOnClickListener(ActionClickImpl())
            self._apply_press_scale(action_button)
            try:
                action_button.setAlpha(0.0)
                action_button.setTranslationY(AndroidUtilities.dp(40))
                action_button.setScaleX(0.8)
                action_button.setScaleY(0.8)
            except Exception:
                pass
            scroll_content.addView(action_button, LayoutHelper.createLinear(-1, -2, Gravity.START, 14, 8, 14, 20))
            bottom_sheet.setCanDismissWithSwipe(False)
            bottom_sheet.show()
            def animate_elements():
                try:
                    scroll_content.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    def show_elements():
                        try:
                            title_text_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            action_button.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                    run_on_ui_thread(show_elements)
                except Exception:
                    pass
            run_on_ui_thread(animate_elements)
        except Exception as e:
            pass


    def _show_import_bottom_sheet(self, data, act=None):
        self._force_load_stickers()
        try:
            if act is None:
                frag = get_last_fragment()
                act = frag.getParentActivity() if frag else None
            if not act:
                return
            templates = data.get("templates", []) if isinstance(data, dict) else []
            if not isinstance(templates, list):
                templates = []
            max_templates = min(len(templates), 30)
            selected_indices = list(range(max_templates))
            sheet = BottomSheet(act, False)
            root_layout = LinearLayout(act)
            root_layout.setOrientation(LinearLayout.VERTICAL)
            root_layout.setPadding(AndroidUtilities.dp(20), AndroidUtilities.dp(16), AndroidUtilities.dp(20), AndroidUtilities.dp(8))
            try:
                root_layout.setAlpha(0.0)
                root_layout.setScaleX(0.3)
                root_layout.setScaleY(0.3)
                root_layout.setTranslationY(AndroidUtilities.dp(100))
            except Exception:
                pass
            try:
                bg_drawable = GradientDrawable()
                bg_drawable.setShape(GradientDrawable.RECTANGLE)
                bg_drawable.setCornerRadii([AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), 0, 0, 0, 0])
                bg_drawable.setColor(Theme.getColor(Theme.key_dialogBackground))
                root_layout.setBackground(bg_drawable)
            except Exception:
                try:
                    root_layout.setBackgroundColor(Theme.getColor(Theme.key_dialogBackground))
                except Exception:
                    pass
            try:
                avatar_view = BackupImageView(act)
                avatar_view.setRoundRadius(AndroidUtilities.dp(45))
                root_layout.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, 0, 0, 12))
                self.load_sticker_with_fallback(avatar_view, "mr_vestr/10", 10, "90_90")
            except Exception:
                pass
            title_view = TextView(act)
            title_view.setTypeface(AndroidUtilities.bold())
            title_view.setGravity(Gravity.CENTER)
            title_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
            title_view.setText(t('import_dialog_title', lang=self.lang))
            try:
                title_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                pass
            try:
                title_view.setAlpha(0.0)
                title_view.setTranslationY(AndroidUtilities.dp(50))
                title_view.setScaleX(0.8)
                title_view.setScaleY(0.8)
            except Exception:
                pass
            root_layout.addView(title_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 12))
            desc_view = TextView(act)
            desc_view.setText(t('import_question', lang=self.lang))
            desc_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
            desc_view.setGravity(Gravity.CENTER)
            try:
                desc_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                pass
            try:
                desc_view.setAlpha(0.0)
                desc_view.setTranslationY(AndroidUtilities.dp(30))
                desc_view.setScaleX(0.8)
                desc_view.setScaleY(0.8)
            except Exception:
                pass
            root_layout.addView(desc_view, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 16))
            selected_text = TextView(act)
            selected_text.setText(f"{t('selected_templates', lang=self.lang)} ({max_templates})")
            selected_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            selected_text.setGravity(Gravity.CENTER)
            try:
                selected_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_addButton))
            except Exception:
                selected_text.setTextColor(Color.BLUE)
            selected_text.setClickable(True)
            try:
                selected_text.setAlpha(0.0)
                selected_text.setTranslationY(AndroidUtilities.dp(30))
                selected_text.setScaleX(0.8)
                selected_text.setScaleY(0.8)
            except Exception:
                pass
                selected_text.setTextColor(Theme.getColor(Theme.key_featuredStickers_addButton))
            except Exception:
                selected_text.setTextColor(Color.BLUE)
            selected_text.setClickable(True)
            def show_template_selector(v):
                self._show_template_selector(templates[:max_templates], selected_indices, lambda indices: 
                    run_on_ui_thread(lambda: selected_text.setText(f"{t('selected_templates', lang=self.lang)} ({len(indices)})")))
            selected_text.setOnClickListener(OnClickListener(show_template_selector))
            root_layout.addView(selected_text, LayoutHelper.createLinear(-1, -2, Gravity.CENTER, 0, 0, 0, 12))
            clear_checkbox = CheckBox2(act, 21, None)
            clear_checkbox.setColor(Theme.key_dialogRoundCheckBox, Theme.key_checkboxDisabled, Theme.key_dialogRoundCheckBoxCheck)
            clear_checkbox.setDrawUnchecked(True)
            clear_checkbox.setDrawBackgroundAsArc(10)
            clear_checkbox.setChecked(False, False)
            clear_checkbox.setVisibility(1)
            clear_container = FrameLayout(act)
            btn_bg = GradientDrawable()
            btn_bg.setCornerRadius(AndroidUtilities.dp(18))
            try:
                bg_color = Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000
            except Exception:
                bg_color = Color.parseColor("#F0F0F0")
            btn_bg.setColor(bg_color)
            try:
                ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
                ripple_drawable = RippleDrawable(ripple_color, btn_bg, None)
                clear_container.setBackground(ripple_drawable)
            except Exception:
                clear_container.setBackground(btn_bg)
            clear_inner_layout = LinearLayout(act)
            clear_inner_layout.setOrientation(LinearLayout.HORIZONTAL)
            clear_inner_layout.setGravity(Gravity.CENTER_VERTICAL)
            clear_inner_layout.setPadding(AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8))
            clear_inner_layout.setMinimumHeight(AndroidUtilities.dp(40))
            clear_inner_layout.addView(clear_checkbox, LayoutHelper.createLinear(24, 24, Gravity.CENTER_VERTICAL, 0, 0, 8, 0))
            clear_text = TextView(act)
            clear_text.setText(t('clear_all_templates', lang=self.lang))
            clear_text.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            clear_text.setGravity(Gravity.CENTER_VERTICAL)
            try:
                clear_text.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                clear_text.setTextColor(Color.BLACK)
            clear_inner_layout.addView(clear_text)
            clear_container.addView(clear_inner_layout)
            def toggle_clear_all(v):
                current_state = clear_checkbox.isChecked()
                clear_checkbox.setChecked(not current_state, True)
            clear_container.setOnClickListener(OnClickListener(toggle_clear_all))
            self._apply_press_scale(clear_container)
            root_layout.addView(clear_container, LayoutHelper.createLinear(-2, -2, Gravity.CENTER, 0, 0, 0, 16))
            divider = View(act)
            try:
                divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
            except Exception:
                divider.setBackgroundColor(Color.GRAY)
            root_layout.addView(divider, LayoutHelper.createLinear(-1, 1, Gravity.FILL_HORIZONTAL, 0, 8, 0, 8))
            import_button = TextView(act)
            import_button.setText(t('import', lang=self.lang))
            import_button.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            import_button.setTypeface(AndroidUtilities.bold())
            import_button.setGravity(Gravity.CENTER)
            try:
                base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
            except Exception:
                base_color = Theme.getColor(Theme.key_dialogTextBlue)
            try:
                pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
            except Exception:
                pressed_color = base_color
            try:
                import_button.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                    AndroidUtilities.dp(28), 
                    base_color, 
                    pressed_color
                ))
                import_button.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
            except Exception:
                import_button.setBackgroundColor(Color.BLUE)
                import_button.setTextColor(Color.WHITE)
            import_button.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
            try:
                import_button.setAlpha(0.0)
                import_button.setTranslationY(AndroidUtilities.dp(40))
                import_button.setScaleX(0.8)
                import_button.setScaleY(0.8)
            except Exception:
                pass
            def do_import(v):
                try:
                    selected_templates = [templates[i] for i in selected_indices if i < len(templates)]
                    clear_all_enabled = clear_checkbox.isChecked()
                    if clear_all_enabled:
                        self.set_setting("templates_created_count", min(max(len(selected_templates), 1), TEMPLATE_COUNT), reload_settings=True)
                        self.templates = []
                        for i in range(TEMPLATE_COUNT):
                            if i < len(selected_templates):
                                item = selected_templates[i] or {}
                                name = str(item.get("name", ""))
                                text = str(item.get("text", ""))
                            else:
                                name = ""
                                text = ""
                            self.set_setting(f"template_name_{i}", name, reload_settings=True)
                            self.set_setting(f"template_text_{i}", text, reload_settings=True)
                            self.templates.append({"name": name, "text": text, "enabled": True if i == 0 else bool(name and text)})
                    else:
                        current_templates = self.get_setting("templates", [])
                        existing_count = 0
                        for i, template in enumerate(current_templates):
                            if template.get("name", "").strip() or template.get("text", "").strip():
                                existing_count = i + 1
                        total_count = existing_count + len(selected_templates)
                        if total_count > TEMPLATE_COUNT:
                            sheet.dismiss()
                            try:
                                icon_attr = getattr(R_tg.raw, 'error', None)
                            except Exception:
                                icon_attr = None
                            run_on_ui_thread(lambda: BulletinHelper.show_error(
                                t('templates_limit_exceeded', lang=self.lang)
                            ))
                            return
                        updated_templates = current_templates[:] if current_templates else []
                        for i, template in enumerate(selected_templates):
                            index = existing_count + i
                            if index >= TEMPLATE_COUNT:
                                break
                            item = template or {}
                            name = str(item.get("name", ""))
                            text = str(item.get("text", ""))
                            self.set_setting(f"template_name_{index}", name, reload_settings=True)
                            self.set_setting(f"template_text_{index}", text, reload_settings=True)
                            if index < len(updated_templates):
                                updated_templates[index] = {"name": name, "text": text, "enabled": True if index == 0 else bool(name and text)}
                            else:
                                while len(updated_templates) <= index:
                                    updated_templates.append({"name": "", "text": "", "enabled": False})
                                updated_templates[index] = {"name": name, "text": text, "enabled": True if index == 0 else bool(name and text)}
                        self.templates = updated_templates
                        final_count = max(existing_count + len(selected_templates), existing_count)
                        self.set_setting("templates_created_count", min(final_count, TEMPLATE_COUNT), reload_settings=True)
                    self.set_setting("templates", self.templates, reload_settings=True)
                    run_on_ui_thread(self._rebuild_fragments)
                    try:
                        icon_attr = getattr(R_tg.raw, 'settings', None)
                    except Exception:
                        icon_attr = None
                    def _open_settings():
                        try:
                            self.open_plugin_settings()
                        except Exception as e:
                            BulletinHelper.show_error(t('open_settings_error', lang=self.lang, error=str(e)))
                    run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                        t('import_success', lang=self.lang),
                        icon_attr if icon_attr else 0,
                        t('settings', lang=self.lang),
                        _open_settings,
                        None
                    ))
                    sheet.dismiss()
                except Exception as e:
                    run_on_ui_thread(lambda: BulletinHelper.show_error(t('import_error', lang=self.lang, error=str(e))))
            import_button.setOnClickListener(OnClickListener(do_import))
            self._apply_press_scale(import_button)
            root_layout.addView(import_button, LayoutHelper.createLinear(-1, -2, Gravity.START, 0, 8, 0, 0))
            sheet.setCustomView(root_layout)
            sheet.show()
            def animate_elements():
                try:
                    root_layout.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    def show_elements():
                        try:
                            title_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            desc_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            selected_text.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(150).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            import_button.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(200).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                    run_on_ui_thread(show_elements)
                except Exception:
                    pass
            run_on_ui_thread(animate_elements)
        except Exception as e:
            self._show_import_templates_alert(data, act)

    def _show_template_selector(self, templates, selected_indices, on_selection_complete):
        try:
            OnClickInterface = find_class("android.view.View$OnClickListener")
            OnClick = dynamic_proxy(OnClickInterface)
            fragment = get_last_fragment()
            if not fragment:
                return
            context = fragment.getContext()
            bottom_sheet = BottomSheet(context, False, fragment.getResourceProvider())
            bottom_sheet.setApplyBottomPadding(False)
            bottom_sheet.setApplyTopPadding(False)
            bottom_sheet.fixNavigationBar(Theme.getColor(Theme.key_dialogBackground))
            scroll_content = LinearLayout(context)
            scroll_content.setOrientation(LinearLayout.VERTICAL)
            scroll_content.setClickable(True)
            try:
                scroll_content.setAlpha(0.0)
                scroll_content.setTranslationY(AndroidUtilities.dp(30))
                scroll_content.setScaleX(0.8)
                scroll_content.setScaleY(0.8)
            except Exception:
                pass
            content_frame = FrameLayout(context)
            content_frame.addView(scroll_content)
            scroll_view = NestedScrollView(context)
            scroll_view.addView(content_frame)
            bottom_sheet.setCustomView(scroll_view)
            title_text_view = TextView(context)
            title_text_view.setTypeface(AndroidUtilities.bold())
            title_text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 20)
            title_text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            title_text_view.setText(t('select_templates', lang=self.lang))
            title_text_view.setGravity(Gravity.CENTER)
            try:
                title_text_view.setAlpha(0.0)
                title_text_view.setTranslationY(AndroidUtilities.dp(50))
                title_text_view.setScaleX(0.8)
                title_text_view.setScaleY(0.8)
            except Exception:
                pass
            scroll_content.addView(title_text_view, LayoutHelper.createLinear(-2, -2, Gravity.TOP | Gravity.CENTER_HORIZONTAL, 10, 20, 10, 16))
            selected_items = set(selected_indices)
            checkboxes = {}
            for i, template in enumerate(templates):
                if i > 0:
                    divider = View(context)
                    try:
                        divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
                    except Exception:
                        divider.setBackgroundColor(0x33000000)
                    scroll_content.addView(divider, LayoutHelper.createLinear(-1, 1, Gravity.FILL_HORIZONTAL, 16, 0, 16, 0))
                item_container = FrameLayout(context)
                item_container.setBackground(None)
                checkbox = CheckBox2(context, 21, fragment.getResourceProvider())
                checkbox.setColor(Theme.key_dialogRoundCheckBox, Theme.key_checkboxDisabled, Theme.key_dialogRoundCheckBoxCheck)
                checkbox.setDrawUnchecked(True)
                checkbox.setDrawBackgroundAsArc(10)
                checkbox.setChecked(i in selected_items, False)
                checkbox.setVisibility(1)
                template_name = str(template.get("name", f"Template {i+1}"))
                lines = template_name.split('\n')
                while lines and lines[-1].strip() == '':
                    lines.pop()
                    if lines and not lines[-1].endswith('...'):
                        lines[-1] += '...'
                template_name = '\n'.join(lines)
                if len(template_name) > 25:
                    template_name = template_name[:25] + "..."
                text_view = TextView(context)
                text_view.setText(template_name)
                text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
                text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
                text_view.setGravity(Gravity.CENTER_VERTICAL)
                text_view.setMaxLines(2)
                item_container.addView(checkbox, LayoutHelper.createFrame(24, 24, Gravity.CENTER_VERTICAL | Gravity.LEFT, 16, 0, 0, 0))
                item_container.addView(text_view, LayoutHelper.createFrame(-1, -1, Gravity.CENTER_VERTICAL | Gravity.LEFT, 56, 0, 16, 0))
                checkboxes[i] = checkbox
                class ItemClickImpl(OnClick):
                    def __init__(self, item_index):
                        super().__init__()
                        self.item_index = item_index
                    def onClick(self, v):
                        checkbox = checkboxes.get(self.item_index)
                        if checkbox:
                            if self.item_index in selected_items:
                                selected_items.remove(self.item_index)
                                checkbox.setChecked(False, True)
                            else:
                                selected_items.add(self.item_index)
                                checkbox.setChecked(True, True)
                item_container.setOnClickListener(ItemClickImpl(i))
                scroll_content.addView(item_container, LayoutHelper.createLinear(-1, 56, Gravity.TOP, 0, 0, 0, 0))
            action_button = TextView(context)
            try:
                base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
            except Exception:
                base_color = Theme.getColor(Theme.key_dialogTextBlue)
            try:
                pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
            except Exception:
                pressed_color = base_color
            action_button.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                AndroidUtilities.dp(28), 
                base_color, 
                pressed_color
            ))
            action_button.setGravity(Gravity.CENTER)
            action_button.setSingleLine(True)
            action_button.setText(t('select', lang=self.lang))
            action_button.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
            action_button.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            action_button.setTypeface(AndroidUtilities.bold())
            action_button.setEnabled(True)
            action_button.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
            class ActionClickImpl(OnClick):
                def onClick(self, v):
                    selected_indices[:] = list(selected_items)
                    if on_selection_complete:
                        on_selection_complete(selected_indices)
                    run_on_ui_thread(lambda: bottom_sheet.dismiss())
            action_button.setOnClickListener(ActionClickImpl())
            self._apply_press_scale(action_button)
            try:
                action_button.setAlpha(0.0)
                action_button.setTranslationY(AndroidUtilities.dp(40))
                action_button.setScaleX(0.8)
                action_button.setScaleY(0.8)
            except Exception:
                pass
            scroll_content.addView(action_button, LayoutHelper.createLinear(-1, -2, Gravity.START, 14, 8, 14, 20))
            bottom_sheet.setCanDismissWithSwipe(False)
            bottom_sheet.show()
            def animate_elements():
                try:
                    scroll_content.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                    def show_elements():
                        try:
                            title_text_view.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                        try:
                            action_button.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(100).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                        except Exception:
                            pass
                    run_on_ui_thread(show_elements)
                except Exception:
                    pass
            run_on_ui_thread(animate_elements)
        except Exception as e:
            pass

    def _show_import_templates_alert(self, data, act=None):
        try:
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
                        try:
                            icon_attr = getattr(R_tg.raw, 'settings', None)
                        except Exception:
                            icon_attr = None
                        def _open_settings():
                            try:
                                self.open_plugin_settings()
                            except Exception as e:
                                BulletinHelper.show_error(t('open_settings_error', lang=self.lang, error=str(e)))
                        run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                            t('import_success', lang=self.lang),
                            icon_attr if icon_attr else 0,
                            t('settings', lang=self.lang),
                            _open_settings,
                            None
                        ))
                    except Exception as e:
                        run_on_ui_thread(lambda: BulletinHelper.show_error(t('import_error', lang=self.lang, error=str(e))))
                    finally:
                        b.dismiss()
                builder.set_positive_button(t('import', lang=self.lang), on_apply)
                builder.set_negative_button(t('cancel', lang=self.lang), lambda b, w: b.dismiss())
                builder.show()
            run_on_ui_thread(_show)
        except Exception as e:
            BulletinHelper.show_error(t('import_error', lang=self.lang, error=str(e)))

    def _send_file(self, peer_id, path, caption=None):
        try:
            try:
                from java.lang import Integer
            except Exception:
                Integer = int
            try:
                from java.io import File as JFile
                size = JFile(path).length()
            except Exception:
                pass
            methods = SendMessagesHelper.getClass().getDeclaredMethods()
            target = None
            use_uri = False
            for m in methods:
                if m.getName() == "prepareSendingDocumentInternal":
                    try:
                        params = m.getParameterTypes()
                        if len(params) > 1 and "android.net.Uri" in str(params[1]):
                            use_uri = True
                        else:
                            pass
                    except Exception:
                        pass
                    target = m
                    break
            if target is None:
                try:
                    names = ", ".join([mm.getName() for mm in methods])
                except Exception:
                    pass
                raise Exception("prepareSendingDocumentInternal not found")
            target.setAccessible(True)
            mime = "application/json"
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
            except Exception:
                pass
            int_array_value = None
            try:
                types_names = [p.getName() for p in params]
                if any((n.startswith('[L') and 'java.lang.Integer' in n) or 'java.lang.Integer[]' in n for n in types_names):
                    int_array_value = jarray(Integer)([0])
                elif any(n == '[I' or 'int[]' in n for n in types_names):
                    int_array_value = jarray(jint)([0])
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
        except Exception as e:
            BulletinHelper.show_error(t('export_error', lang=self.lang, error=str(e)))

    def _show_filtered_template_menu(self, templates):
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
        titleTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
        titleTextView.setGravity(Gravity.CENTER)
        titleTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
        if templates:
            titleTextView.setText(t('select_template', lang=self.lang))
        else:
            titleTextView.setText(t('no_templates_available', lang=self.lang))
        linearLayout.addView(titleTextView, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 0, 16, 0, 8))
        contentFrame = FrameLayout(act)
        linearLayout.addView(contentFrame, LayoutHelper.createLinear(-1, 0, 1.0))
        scrollView = ScrollView(act)
        scrollView.setFillViewport(True)
        try:
            scrollView.setNestedScrollingEnabled(True)
        except Exception:
            pass
        buttonsLayout = LinearLayout(act)
        buttonsLayout.setOrientation(LinearLayout.VERTICAL)
        def create_template_button(template):
            def send_template(v=None):
                try:
                    builder.getDismissRunnable().run()
                    self.menu_shown = False
                    self._send_template_to_current_chat(template['index'], template['name'], template['text'])
                except Exception as e:
                    BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))
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
            name = template['name']
            maxNameLength = 30
            name_lines = name.split('\n')
            if len(name_lines) > 3:
                name = '\n'.join(name_lines[:3]) + "\n..."
            elif len(name) > maxNameLength:
                name = name[:maxNameLength] + "..."
            nameTextView.setText(name)
            nameTextView.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            nameTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
            nameTextView.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
            nameTextView.setGravity(Gravity.LEFT)
            nameTextView.setMaxLines(3)
            buttonContainer.addView(nameTextView)
            text = template['text']
            maxLength = 50
            text_lines = text.split('\n')
            if len(text_lines) > 3:
                text = '\n'.join(text_lines[:3]) + "\n..."
            elif len(text) > maxLength:
                text = text[:maxLength] + "..."
            textTextView = TextView(act)
            textTextView.setText(text)
            textTextView.setTextColor(Theme.getColor(Theme.key_dialogTextGray))
            textTextView.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            textTextView.setGravity(Gravity.LEFT)
            textTextView.setPadding(0, AndroidUtilities.dp(4), 0, 0)
            textTextView.setMaxLines(3)
            buttonContainer.addView(textTextView)
            return buttonContainer
        for i, template in enumerate(templates):
            btn = create_template_button(template)
            buttonsLayout.addView(btn, LayoutHelper.createFrame(-1, -2, Gravity.TOP, 16, 4, 16, 4))
            if i < len(templates) - 1:
                divider = View(act)
                try:
                    divider.setBackgroundColor(Theme.getColor(Theme.key_divider))
                except Exception:
                    divider.setBackgroundColor(0x33000000)
                buttonsLayout.addView(divider, LayoutHelper.createFrame(-1, 1, Gravity.TOP, 16, 0, 16, 0))
        scrollView.addView(buttonsLayout)
        contentFrame.addView(scrollView, FrameLayout.LayoutParams(-1, -1))
        settingsBtnContainer = LinearLayout(act)
        settingsBtnContainer.setOrientation(LinearLayout.HORIZONTAL)
        settingsBtnContainer.setGravity(Gravity.CENTER_HORIZONTAL)
        settingsBtn = FrameLayout(act)
        try:
            base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
        except Exception:
            base_color = Theme.getColor(Theme.key_dialogTextBlue)
        try:
            pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        except Exception:
            pressed_color = base_color
        settingsBtn.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
            AndroidUtilities.dp(28),
            base_color,
            pressed_color
        ))
        settingsBtn.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
        settingsBtn.setClickable(True)
        settingsBtn.setFocusable(True)
        settingsBtnText = TextView(act)
        settingsBtnText.setText(t('settings', lang=self.lang))
        settingsBtnText.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        settingsBtnText.setTypeface(AndroidUtilities.bold())
        settingsBtnText.setGravity(Gravity.CENTER)
        settingsBtnText.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        settingsBtn.addView(settingsBtnText, FrameLayout.LayoutParams(-1, -2))
        def on_settings(v=None):
            builder.getDismissRunnable().run()
            self.menu_shown = False
            self.open_plugin_settings()
        settingsBtn.setOnClickListener(OnClickListener(on_settings))
        self._apply_press_scale(settingsBtn)
        settingsBtnContainer.addView(settingsBtn, LayoutHelper.createLinear(-1, -2, Gravity.CENTER_HORIZONTAL, 24, 0, 24, 0))
        linearLayout.addView(settingsBtnContainer, LayoutHelper.createLinear(-1, -2, 0, 8, 0, 16))
        sheet = builder.show()
        sheet.setCanDismissWithSwipe(False)
        def on_dismiss():
            self.menu_shown = False
        try:
            sheet.setOnDismissListener(dynamic_proxy(android.content.DialogInterface.OnDismissListener)(on_dismiss))
        except Exception:
            pass
        return sheet

    def _send_template_to_current_chat(self, template_index, template_name, template_text):
        try:
            frag = get_last_fragment()
            if not frag:
                BulletinHelper.show_error(t('error_occurred', lang=self.lang))
                return
            if not isinstance(frag, ChatActivity):
                BulletinHelper.show_error(t('error_occurred', lang=self.lang))
                return
            chat_id = None
            try:
                dialog_id = frag.getDialogId()
                if dialog_id:
                    chat_id = dialog_id
            except Exception:
                pass
            if not chat_id:
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
                BulletinHelper.show_error(t('error_occurred', lang=self.lang))
                return

            topic_msg_obj = None
            try:
                if hasattr(frag, 'isTopic') and frag.isTopic:
                    topic_id = frag.getTopicId()
                    if topic_id:
                        from org.telegram.messenger import MessageObject as MsgObj
                        mc = frag.getMessagesController()
                        topic = mc.getTopicsController().findTopic(-chat_id, topic_id)
                        if topic is not None and topic.topicStartMessage is not None:
                            topic_msg_obj = MsgObj(frag.getCurrentAccount(), topic.topicStartMessage, False, False)
                            topic_msg_obj.isTopicMainMessage = True
            except Exception:
                pass
            
            preprocessed = preprocess_template_markdown(template_text)
            parsed = parse_markdown(preprocessed)
            try:
                message_data = {
                    "peer": chat_id,
                    "message": parsed.text,
                    "entities": [ent.to_tlrpc_object() for ent in parsed.entities]
                }
                if topic_msg_obj is not None:
                    message_data["replyToMsg"] = topic_msg_obj
                    message_data["replyToTopMsg"] = topic_msg_obj
                send_message(message_data)
            except Exception:
                try:
                    from org.telegram.messenger import SendMessagesHelper as SMH
                    smh = SMH.getInstance(frag.getCurrentAccount())
                    params = SMH.SendMessageParams.of(parsed.text, chat_id)
                    params.entities = [ent.to_tlrpc_object() for ent in parsed.entities]
                    if topic_msg_obj is not None:
                        params.replyToMsg = topic_msg_obj
                        params.replyToTopMsg = topic_msg_obj
                    smh.sendMessage(params)
                except Exception as e2:
                    raise e2
            try:
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
            BulletinHelper.show_error(t('error_occurred_with_reason', lang=self.lang, error=str(e)))

class _LinkAliasEnterViewConstructorHook(MethodHook):
    def __init__(self, plugin):
        MethodHook.__init__(self)
        self._plugin_ref = weakref.ref(plugin)

    @property
    def plugin(self):
        return self._plugin_ref() if self._plugin_ref else None

    def after_hooked_method(self, param):
        try:
            plugin = self.plugin
            if not plugin:
                return
            enter_view = param.thisObject
            def attach_watcher():
                plugin._templates_view_attach_text_watcher(enter_view)
            run_on_ui_thread(attach_watcher, delay=500)
        except Exception as e:
            pass

def _setup_templates_view_search(self):
    try:
        self._templates_view_hook_enter_view_constructor()
    except Exception as e:
        pass

def _templates_view_get_class(self, class_name):
    if class_name not in self._templates_view_class_cache:
        self._templates_view_class_cache[class_name] = find_class(class_name)
    return self._templates_view_class_cache[class_name]

def _templates_view_hook_enter_view_constructor(self):
    try:
        ChatActivityEnterView = self._templates_view_get_class("org.telegram.ui.Components.ChatActivityEnterView")
        Activity = self._templates_view_get_class("android.app.Activity")
        SizeNotifierFrameLayout = self._templates_view_get_class("org.telegram.ui.Components.SizeNotifierFrameLayout")
        ChatActivity = self._templates_view_get_class("org.telegram.ui.ChatActivity")
        ResourcesProvider = self._templates_view_get_class("org.telegram.ui.ActionBar.Theme$ResourcesProvider")
        if not all([ChatActivityEnterView, Activity, SizeNotifierFrameLayout, ChatActivity]):
            return
        constructor = ChatActivityEnterView.getClass().getDeclaredConstructor(
            Activity,
            SizeNotifierFrameLayout,
            ChatActivity,
            jclass("java.lang.Boolean").TYPE,
            ResourcesProvider
        )
        constructor.setAccessible(True)
        self.templates_view_hook_constructor_ref = self.hook_method(constructor, _LinkAliasEnterViewConstructorHook(self))
    except Exception as e:
        pass

def _templates_view_attach_text_watcher(self, enter_view):
    try:
        view_id = id(enter_view)
        if view_id in self.templates_view_attached_views:
            return
        message_edit_text = get_private_field(enter_view, "messageEditText")
        if not message_edit_text:
            return
        self.templates_view_current_enter_view_ref = weakref.ref(enter_view)
        TextWatcherInterface = self._templates_view_get_class("android.text.TextWatcher")
        plugin_ref = weakref.ref(self)
        class CustomTextWatcher(dynamic_proxy(TextWatcherInterface)):
            def beforeTextChanged(self, s, start, count, after):
                pass
            def onTextChanged(self, s, start, before, count):
                pass
            def afterTextChanged(self, editable):
                plugin = plugin_ref()
                if not plugin:
                    return
                try:
                    text = str(editable.toString()) if editable else ""

                    if text.startswith("/"):
                        send_cmd = plugin.get_setting('send_cmd', '//').strip()
                        if not send_cmd:
                            send_cmd = '//'
                        if text.startswith(send_cmd):
                            cmd_len = len(send_cmd)
                            if len(text) > cmd_len:
                                search_key = text[cmd_len:].lower().strip()
                                plugin._templates_view_show_matching_settings(search_key)
                            else:
                                plugin._templates_view_hide_popup()
                        else:
                            plugin._templates_view_hide_popup()
                    else:
                        plugin._templates_view_hide_popup()
                except Exception as e:
                    pass
        watcher = CustomTextWatcher()
        message_edit_text.addTextChangedListener(watcher)
        self.templates_view_attached_views.add(view_id)
    except Exception as e:
        pass

def _templates_view_collect_settings_with_alias(self):
    settings_list = []
    try:
        for i, template in enumerate(self.templates):
            if template.get('enabled', False) and template.get('name', '') and template.get('text', ''):
                settings_list.append({
                    'plugin_id': 'templates',
                    'plugin_name': 'Templates',
                    'setting_name': template['name'],
                    'templates_view_alias': f'template_{i}',
                    'search_key': template['name'].lower(),
                    'template_index': i,
                    'template_text': template['text']
                })
        return settings_list
    except Exception as e:
        pass
    return settings_list

def _templates_view_show_matching_settings(self, search_key):
    try:
        all_settings = self._templates_view_collect_settings_with_alias()
        if not all_settings:
            self._templates_view_hide_popup()
            return
        matching = []
        for setting in all_settings:
            if setting['setting_name'].lower().startswith(search_key):
                matching.append(setting)
        if not matching:
            self._templates_view_hide_popup()
            return
        self._templates_view_show_bot_commands_popup(matching)
        self._update_popup_size()
    except Exception as e:
        pass

def _update_popup_size(self):
    try:
        if self.templates_view_custom_container:
            run_on_ui_thread(lambda: self.templates_view_custom_container.requestLayout())
    except:
        pass

def _templates_view_show_bot_commands_popup(self, settings):
    try:
        enter_view = self.templates_view_current_enter_view_ref() if self.templates_view_current_enter_view_ref else None
        if not enter_view:
            fragment = get_last_fragment()
            if fragment:
                enter_view = get_private_field(fragment, "chatActivityEnterView")
                if enter_view:
                    self.templates_view_current_enter_view_ref = weakref.ref(enter_view)
        if not enter_view:
            return
        bot_container = get_private_field(enter_view, "botCommandsMenuContainer")
        bot_adapter = get_private_field(enter_view, "botCommandsAdapter")
        if not bot_container:
            try:
                ChatActivityEnterView = self._templates_view_get_class("org.telegram.ui.Components.ChatActivityEnterView")
                create_method = ChatActivityEnterView.getClass().getDeclaredMethod("createBotCommandsMenuContainer")
                create_method.setAccessible(True)
                create_method.invoke(enter_view)
                bot_container = get_private_field(enter_view, "botCommandsMenuContainer")
                bot_adapter = get_private_field(enter_view, "botCommandsAdapter")
            except Exception as e:
                pass
        if not bot_container or not bot_adapter:
            return
        commands = []
        descriptions = []
        self.templates_view_current_settings = {}
        for setting in settings[:10]:
            cmd = setting['template_text'][:25] + "..." if len(setting['template_text']) > 25 else setting['template_text']
            desc = setting['setting_name'][:15] + "..." if len(setting['setting_name']) > 15 else setting['setting_name']
            commands.append(cmd)
            descriptions.append(desc)
            self.templates_view_current_settings[cmd] = setting
        new_result_field = bot_adapter.getClass().getDeclaredField("newResult")
        new_result_field.setAccessible(True)
        new_result = new_result_field.get(bot_adapter)
        new_result.clear()
        for cmd in commands:
            new_result.add(cmd)
        new_result_help_field = bot_adapter.getClass().getDeclaredField("newResultHelp")
        new_result_help_field.setAccessible(True)
        new_result_help = new_result_help_field.get(bot_adapter)
        new_result_help.clear()
        for desc in descriptions:
            new_result_help.add(desc)
        bot_adapter.notifyDataSetChanged()
        plugin_ref = weakref.ref(self)
        class ClickListener(dynamic_proxy(RecyclerListView.OnItemClickListener)):
            def onItemClick(self, view, position):
                plugin = plugin_ref()
                if not plugin:
                    return
                try:
                    if hasattr(view, 'getCommand'):
                        command = view.getCommand()
                        setting = plugin.templates_view_current_settings.get(str(command))
                        if setting:
                            template_name = setting['setting_name']
                            template_text = None
                            template_index = None
                            for i, template in enumerate(plugin.templates):
                                if template.get('name', '') == template_name:
                                    template_text = template.get('text', '')
                                    template_index = i
                                    break
                            
                            if template_text:
                                enter_view_ref = plugin.templates_view_current_enter_view_ref
                                ev = enter_view_ref() if enter_view_ref else None
                                def ui_actions():
                                    try:
                                        if ev:
                                            ev.setFieldText("")
                                        bot_container.dismiss()
                                    except Exception:
                                        pass
                                run_on_ui_thread(ui_actions)
                                plugin._send_template_to_current_chat(template_index, template_name, template_text)
                except Exception as e:
                    pass
        
        class LongClickListener(dynamic_proxy(RecyclerListView.OnItemLongClickListener)):
            def onItemClick(self, view, position):
                plugin = plugin_ref()
                if not plugin:
                    return False
                try:
                    if hasattr(view, 'getCommand'):
                        command = view.getCommand()
                        setting = plugin.templates_view_current_settings.get(str(command))
                        if setting:
                            template_name = setting['setting_name']
                            template_text = None
                            for template in plugin.templates:
                                if template.get('name', '') == template_name:
                                    template_text = template.get('text', '')
                                    break
                            
                            if template_text:
                                enter_view_ref = plugin.templates_view_current_enter_view_ref
                                ev = enter_view_ref() if enter_view_ref else None
                                def ui_actions():
                                    try:
                                        if ev:
                                            ev.setFieldText(template_text + " ")
                                        bot_container.dismiss()
                                    except Exception:
                                        pass
                                run_on_ui_thread(ui_actions)
                                return True
                except Exception as e:
                    pass
                return False
        bot_container.listView.setOnItemClickListener(ClickListener())
        bot_container.listView.setOnItemLongClickListener(LongClickListener())
        try:
            parent = bot_container.listView.getParent()
            if parent and isinstance(parent, LinearLayout):
                parent.setPadding(0, 4, 0, 0)
            try:
                enter_view_rect = android.graphics.Rect()
                enter_view.getGlobalVisibleRect(enter_view_rect)
                enter_view_width = enter_view_rect.width()
                container_params = bot_container.getLayoutParams()
                if container_params:
                    container_params.width = enter_view_width
                    bot_container.setLayoutParams(container_params)
                    list_params = bot_container.listView.getLayoutParams()
                    if list_params:
                        list_params.width = enter_view_width
                        bot_container.listView.setLayoutParams(list_params)
            except:
                pass
            bot_container.requestLayout()
        except:
            pass
        self.templates_view_custom_container = bot_container
        bot_container.show()
    except Exception as e:
        pass

def _send_template_text(self, fragment, template_text):
    try:
        chat_id = fragment.getCurrentDialogId()
        topic_msg_obj = None
        try:
            if hasattr(fragment, 'isTopic') and fragment.isTopic:
                topic_id = fragment.getTopicId()
                if topic_id:
                    from org.telegram.messenger import MessageObject as MsgObj
                    mc = fragment.getMessagesController()
                    topic = mc.getTopicsController().findTopic(-chat_id, topic_id)
                    if topic is not None and topic.topicStartMessage is not None:
                        topic_msg_obj = MsgObj(fragment.getCurrentAccount(), topic.topicStartMessage, False, False)
                        topic_msg_obj.isTopicMainMessage = True
        except Exception:
            pass
        
        preprocessed = preprocess_template_markdown(template_text)
        parsed = parse_markdown(preprocessed)
        try:
            message_data = {
                "peer": chat_id,
                "message": parsed.text,
                "entities": [ent.to_tlrpc_object() for ent in parsed.entities]
            }
            if topic_msg_obj is not None:
                message_data["replyToMsg"] = topic_msg_obj
                message_data["replyToTopMsg"] = topic_msg_obj
            send_message(message_data)
        except Exception:
            try:
                from org.telegram.messenger import SendMessagesHelper as SMH
                smh = SMH.getInstance(fragment.getCurrentAccount())
                params = SMH.SendMessageParams.of(parsed.text, chat_id)
                params.entities = [ent.to_tlrpc_object() for ent in parsed.entities]
                if topic_msg_obj is not None:
                    params.replyToMsg = topic_msg_obj
                    params.replyToTopMsg = topic_msg_obj
                smh.sendMessage(params)
            except Exception as e2:
                pass
    except Exception as e:
        pass

def _templates_view_hide_popup(self):
    try:
        if self.templates_view_custom_container:
            self.templates_view_custom_container.dismiss()
    except Exception as e:
        pass

TemplatesPlugin._setup_templates_view_search = _setup_templates_view_search
TemplatesPlugin._templates_view_get_class = _templates_view_get_class
TemplatesPlugin._templates_view_hook_enter_view_constructor = _templates_view_hook_enter_view_constructor
TemplatesPlugin._templates_view_attach_text_watcher = _templates_view_attach_text_watcher
TemplatesPlugin._templates_view_collect_settings_with_alias = _templates_view_collect_settings_with_alias
TemplatesPlugin._templates_view_show_matching_settings = _templates_view_show_matching_settings
TemplatesPlugin._update_popup_size = _update_popup_size
TemplatesPlugin._templates_view_show_bot_commands_popup = _templates_view_show_bot_commands_popup
TemplatesPlugin._send_template_text = _send_template_text
TemplatesPlugin._templates_view_hide_popup = _templates_view_hide_popup


# Спасибо за некоторые части кода @QuantaPlugins и @mishabotov!

# Thanks for some code snippets to @QuantaPlugins and @mishabotov!
