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

import os, re, json, threading, time, weakref, signal
from base_plugin import BasePlugin, MenuItemData, MenuItemType, HookResult, HookStrategy, MethodHook
from ui.settings import Divider, Header, Input, Switch, Text, Selector
from client_utils import get_last_fragment, get_messages_controller, send_message, get_account_instance
from hook_utils import find_class, get_private_field
from markdown_utils import parse_markdown
from android.os import Bundle
from java import dynamic_proxy, static_proxy, jclass, jarray, jint, jlong
from ui.bulletin import BulletinHelper
from org.telegram.messenger import ApplicationLoader, Utilities, MediaDataController, ImageLocation, LocaleController, SendMessagesHelper, UserConfig, FileLoader
from android.view import View, MotionEvent, Gravity
from org.telegram.messenger import AndroidUtilities, R
from com.exteragram.messenger.plugins import PluginsController
from com.exteragram.messenger.plugins.ui import PluginSettingsActivity
from org.telegram.tgnet import TLRPC
from java.lang import Runnable
from base_plugin import MethodHook
from org.telegram.ui import ChatActivity, LaunchActivity, DialogsActivity
from org.telegram.ui.Components.Premium import StarParticlesView
from org.telegram.ui.Components import ShareAlert
from org.telegram.messenger.browser import Browser
from android.net import Uri
from android.content import Intent, DialogInterface
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
from android.util import TypedValue, Base64
from android.graphics import Color, PorterDuff
from androidx.core.content import ContextCompat
from android_utils import OnClickListener, run_on_ui_thread, log
from android.text import SpannableString, SpannableStringBuilder
from android.text.style import StrikethroughSpan, URLSpan
from androidx.core.widget import NestedScrollView
from file_utils import get_cache_dir
from java.io import File, FileOutputStream, FileInputStream, ByteArrayOutputStream
from android.text.method import LinkMovementMethod
from java.lang import Long
from java.util import Locale
from org.telegram.messenger import MessagesController, MessageObject


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
__description__ = "Плагин для создания, редактирования и быстрой отправки шаблонов сообщений.\n\nThe plugin for creating, editing, and quickly sending message templates."
__author__ = "@mr_Vestr"
__version__ = "5.0"
__min_version__ = "12.10.6"
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


TEMPLATE_COUNT = 100

LANG = {
    'ru': {
        'name': 'Имя шаблона',
        'text': 'Текст шаблона',
        'edit': 'Изменить',
        'clear': 'Очистить',
        'open_settings_error': 'Не удалось открыть настройки: {error}',
        'templates': 'Шаблоны',
        'embed_files': 'Вложенные файлы',
        'templates_updated': 'Шаблоны обновлены',
        'templates_count': 'Шаблонов: {n}',
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
        'link_preview': 'Предпросмотр ссылки',
        'link_preview_sub': 'Показывать превью ссылок при отправке шаблона. Выключите, чтобы отправить ссылку без превью в сообщении.',
        'create_template': 'Создать шаблон',
        'contacts': 'Мои контакты',
        'channel_1': 'Мой канал — @I_am_Vestr',
        'personal_1': 'Моя личка — @mr_Vestr',
        'other': 'Другое',
        'plugin_version': f'Версия плагина — {__version__}',
        'current_version': 'Текущая версия: {version}',
        'updates_info': 'Нажмите на кнопку ниже, чтобы открыть пост с плагином в моём канале @I_am_Vestr.',
        'check_updates': 'Проверить',
        'badge_meta_chat': '**Meta Plugins Chat** — официальный чат **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — официальный канал **Vestr**.',
        'badge_vestr_user': '**Vestr** — ведущий разработчик **Packit** и основатель **Meta Plugins**.',
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
        'export_question': 'Какие шаблоны экспортировать?',
        'export_sent': 'Экспорт отправлен',
        'export_preparing': 'Готовим экспорт файлов…',
        'export_error': 'Ошибка экспорта: {error}',
        'export_success': 'Успешный экспорт.',
        'import_question': 'Импортировать шаблоны из файла?',
        'import_success': 'Шаблоны импортированы.',
        'import_error': 'Ошибка импорта: {error}',
        'selected_templates': 'Выбрано',
        'select_all': 'Выбрать все',
        'select_templates': 'Выбор шаблонов',
        'select': 'Выбрать',
        'export': 'Экспортировать',
        'import': 'Импортировать',
        'apply': 'Применить',
        'template_deleted': 'Шаблон удалён.',
        'template_deleted_n': 'Удалён шаблон №{n}.',
        'template_name_cleared': 'Очищено имя шаблона №{n}.',
        'template_text_cleared': 'Очищен текст шаблона №{n}.',
        'rich_editor_open': 'Расширенный редактор',
        'rich_editor_opening': 'Открываю расширенный редактор...',
        'rich_editor_busy': 'Расширенный редактор уже открыт.',
        'rich_editor_unavailable': 'Расширенный редактор недоступен. Нужна более новая версия Telegram.',
        'rich_editor_missing_classes': 'Расширенный редактор не найден в этой сборке. Подробности в логе плагина:',
        'rich_editor_no_host': 'Не удалось открыть чат для расширенного редактора.',
        'rich_editor_present_failed': 'Не удалось показать расширенный редактор. Подробности в логе плагина.',
        'rich_editor_premium': 'Расширенный редактор доступен только с Telegram Premium.',
        'template_saved_rich': 'Шаблон №{n} сохранён с расширенным форматированием.',
        'template_saved_plain': 'Шаблон №{n} сохранён.',
        'no_premium_send': 'На аккаунте нет Telegram Premium. Сообщение может быть не отправлено.',
        'rich_editor_settings_section': 'Расширенный редактор',
        'rich_exit_confirm': 'Предупреждение при выходе',
        'rich_exit_confirm_sub': 'При выходе из расширенного редактора кнопкой «Назад» или жестом показывать меню: сохранить изменения или выйти без сохранения.',
        'rich_premium_unlock': 'Разблокировать премиум функции',
        'rich_premium_unlock_sub': 'Снимает ограничения Telegram Premium в расширенном редакторе — только для создания шаблонов. Отправить сообщение без Telegram Premium нельзя.',
        'exit_back_title': 'Выход назад',
        'exit_back_message': 'Что нужно сделать?',
        'exit_leave': 'Выйти',
        'rich_send_error': 'Не удалось отправить шаблон с расширенным форматированием.',
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
        'templates_limit_exceeded': 'Количество шаблонов не может превышать 100 шт.',
        'template_name_exists': 'Такое имя шаблона уже есть. Переименуйте или он будет деактивирован.',
        'refresh_templates': 'Обновление шаблонов...',
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
        'template_sent_n': 'Шаблон отправлен в {n} чатов.',
        'template_send_n_question': 'Отправить шаблон в {n} чатов?',
        'select_chats_done': 'Готово',
        'select_chats_hint': 'Для выбора нескольких чатов, удерживайте чат',
        'channel_promo_title': '🙂 Привет! У меня есть канал!',
        'channel_promo_text': 'Буду рад, если подпишешься на мой канал. Мои плагины бесплатные, а подписка — хорошая поддержка для меня :)',
        'send_action': 'Отправить',
    },
    'en': {
        'name': 'Template name',
        'text': 'Template text',
        'edit': 'Edit',
        'clear': 'Clear',
        'open_settings_error': 'Failed to open settings: {error}',
        'templates': 'Templates',
        'embed_files': 'Embedded files',
        'templates_updated': 'Templates updated',
        'templates_count': 'Templates: {n}',
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
        'link_preview': 'Link preview',
        'link_preview_sub': 'Show link previews when sending the template. Turn it off to send links without a preview in the message.',
        'create_template': 'Create template',
        'contacts': 'My contacts',
        'channel_1': 'My channel — @I_am_Vestr',
        'personal_1': 'My DM — @mr_Vestr',
        'other': 'Other',
        'plugin_version': f'Plugin version — {__version__}',
        'current_version': 'Current version: {version}',
        'updates_info': 'Tap the button below to open the plugin post on my channel @I_am_Vestr.',
        'check_updates': 'Check updates',
        'badge_meta_chat': '**Meta Plugins Chat** — official **Meta Plugins** chat.',
        'badge_meta_channel': '**Meta Plugins** — official **Vestr** channel.',
        'badge_vestr_user': '**Vestr** is the official lead developer of **Packit** and founder of **Meta Plugins**.',
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
        'export_preparing': 'Preparing export files…',
        'export_error': 'Export error: {error}',
        'export_success': 'Export successful.',
        'import_question': 'Import templates from file?',
        'import_success': 'Templates imported.',
        'import_error': 'Import error: {error}',
        'selected_templates': 'Selected',
        'select_all': 'Select all',
        'select_templates': 'Select Templates',
        'select': 'Select',
        'export': 'Export',
        'import': 'Import',
        'apply': 'Apply',
        'template_deleted': 'Template deleted.',
        'template_deleted_n': 'Template #{n} deleted.',
        'template_name_cleared': 'Template name #{n} cleared.',
        'template_text_cleared': 'Template text #{n} cleared.',
        'rich_editor_open': 'Rich editor',
        'rich_editor_opening': 'Opening the rich editor...',
        'rich_editor_busy': 'The rich editor is already open.',
        'rich_editor_unavailable': 'The rich editor is unavailable. A newer version of Telegram is required.',
        'rich_editor_missing_classes': 'The rich editor was not found in this build. See the plugin log for details:',
        'rich_editor_no_host': 'Could not open a chat for the rich editor.',
        'rich_editor_present_failed': 'Could not display the rich editor. See the plugin log for details.',
        'rich_editor_premium': 'The rich editor is available with Telegram Premium only.',
        'template_saved_rich': 'Template #{n} saved with rich formatting.',
        'template_saved_plain': 'Template #{n} saved.',
        'no_premium_send': 'This account has no Telegram Premium. The message may not be sent.',
        'rich_editor_settings_section': 'Rich editor',
        'rich_exit_confirm': 'Exit warning',
        'rich_exit_confirm_sub': 'Show a menu when leaving the rich editor with the back button or gesture: save changes or exit without saving.',
        'rich_premium_unlock': 'Unlock premium features',
        'rich_premium_unlock_sub': 'Removes Telegram Premium limits in the rich editor — for creating templates only. Sending without Telegram Premium is still not possible.',
        'exit_back_title': 'Going back',
        'exit_back_message': 'What should be done?',
        'exit_leave': 'Exit',
        'rich_send_error': 'Failed to send the template with rich formatting.',
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
        'templates_limit_exceeded': 'The number of templates cannot exceed 100.',
        'template_name_exists': 'Template name already exists. Rename it or it will be deactivated.',
        'refresh_templates': 'Refresh templates...',
        'header_description': 'The plugin for creating, editing, and quickly sending message templates.',
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
        'template_sent_n': 'Template sent to {n} chats.',
        'template_send_n_question': 'Send template to {n} chats?',
        'select_chats_done': 'Done',
        'select_chats_hint': 'To select several chats, long-press a chat',
        'channel_promo_title': '🙂 Hi! I have a channel!',
        'channel_promo_text': 'I\'d be glad if you subscribed to my channel. My plugins are free, and a subscription is a great support for me :)',
        'send_action': 'Send',
    },
    'he': {
        'name': 'שם התבנית',
        'text': 'טקסט התבנית',
        'edit': 'ערוך',
        'clear': 'נקה',
        'open_settings_error': 'לא ניתן לפתוח את ההגדרות: {error}',
        'templates': 'תבניות',
        'embed_files': 'קבצים מצורפים',
        'templates_updated': 'התבניות עודכנו',
        'link_preview': 'תצוגה מקדימה של קישור',
        'link_preview_sub': 'הצגת תצוגה מקדימה של קישורים בעת שליחת התבנית. כבה אפשרות זו כדי לשלוח קישורים בלי תצוגה מקדימה בהודעה.',
        'templates_count': 'תבניות: {n}',
        'template_saved_plain': 'התבנית מס׳ {n} נשמרה.',
        'template_saved_rich': 'התבנית מס׳ {n} נשמרה עם עיצוב מלא.',
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
        'exit_back_message': 'מה לעשות?',
        'exit_back_title': 'יציאה לאחור',
        'exit_leave': 'יציאה',
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
        'current_version': 'גרסה נוכחית: {version}',
        'updates_info': 'הקישו על הכפתור למטה כדי לפתוח את פוסט התוסף בערוץ שלי @I_am_Vestr.',
        'check_updates': 'בדוק',
        'badge_meta_chat': '**Meta Plugins Chat** — הצ׳אט הרשמי של **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — הערוץ הרשמי של **Vestr**.',
        'badge_vestr_user': '**Vestr** — המפתח הראשי של **Packit** ומייסד **Meta Plugins**.',
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
        'rich_editor_busy': 'עורך העיצוב המלא כבר פתוח.',
        'rich_editor_missing_classes': 'עורך העיצוב המלא לא נמצא בגרסה הזו. פרטים ביומן של התוסף:',
        'rich_editor_no_host': 'לא הצלחנו לפתוח צ׳אט עבור עורך העיצוב המלא.',
        'rich_editor_open': 'עורך עיצוב מלא',
        'rich_editor_opening': 'פותח את עורך העיצוב המלא...',
        'rich_editor_premium': 'עורך העיצוב המלא זמין רק עם Telegram Premium.',
        'rich_editor_present_failed': 'לא הצלחנו להציג את עורך העיצוב המלא. פרטים ביומן של התוסף.',
        'rich_editor_settings_section': 'עורך עיצוב מלא',
        'rich_editor_unavailable': 'עורך העיצוב המלא אינו זמין. נדרשת גרסה חדשה יותר של Telegram.',
        'rich_exit_confirm': 'אזהרה בעת היציאה',
        'rich_exit_confirm_sub': 'הצגת תפריט בעת יציאה מעורך העיצוב המלא עם כפתור החזרה או מחווה: שמירת השינויים או יציאה בלי לשמור.',
        'rich_premium_unlock': 'שחרור אפשרויות פרימיום',
        'rich_premium_unlock_sub': 'הסרת הגבלות Telegram Premium בעורך העיצוב המלא — ליצירת תבניות בלבד. לא ניתן לשלוח הודעה בלי Telegram Premium.',
        'rich_send_error': 'שליחת התבנית עם עיצוב מלא נכשלה.',
        'support_me': 'תמוך בי',
        'support_me_text': 'אם ברצונך לתמוך בי, תוכל לשלוח לי מתנה בטלגרם או לתת לי טלגרם פרמיום :)',
        'my_account': 'החשבון שלי',
        'restart_error': 'שגיאת הפעלה מחדש: {error}',
        'download_error': 'שגיאת הורדה: {error}',
        'error_occurred_with_reason': 'שגיאה: {error}',
        'select_template': 'בחר תבנית',
        'no_templates_available': 'אין תבניות זמינות',
        'no_premium_send': 'לחשבון זה אין Telegram Premium. ייתכן שההודעה לא תישלח.',
        'export_templates': 'ייצא תבניות',
        'export_question': 'אילו תבניות לייצא?',
        'export_sent': 'ייצוא נשלח',
        'export_error': 'שגיאת ייצוא: {error}',
        'export_preparing': 'מכין קבצי ייצוא…',
        'export_success': 'ייצוא הצליח.',
        'import_question': 'לייבא תבניות מקובץ?',
        'import_success': 'תבניות יובאו.',
        'import_error': 'שגיאת ייבוא: {error}',
        'selected_templates': 'נבחרו',
        'select_all': 'בחר הכול',
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
        'templates_limit_exceeded': 'מספר התבניות לא יכול לעלות על 100.',
        'template_name_exists': 'שם תבנית כזה כבר קיים. שנה את השם או שהיא תושבת.',
        'refresh_templates': 'רענון תבניות...',
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
        'template_sent_n': 'התבנית נשלחה ל-{n} צ׳אטים.',
        'template_send_n_question': 'לשלוח את התבנית ל-{n} צ׳אטים?',
        'select_chats_done': 'סיום',
        'select_chats_hint': 'כדי לבחור כמה צ׳אטים, לחץ לחיצה ארוכה על צ׳אט',
        'channel_promo_title': '🙂 היי! יש לי ערוץ!',
        'channel_promo_text': 'אני אשמח אם תירשם לערוץ שלי. התוספים שלי בחינם, ומנוי זו תמיכה טובה בשבילי :)',
        'send_action': 'שליחה',
    },
    'ar': {
        'name': 'اسم القالب',
        'text': 'نص القالب',
        'edit': 'تحرير',
        'clear': 'مسح',
        'open_settings_error': 'فشل فتح الإعدادات: {error}',
        'templates': 'القوالب',
        'embed_files': 'الملفات المرفقة',
        'templates_updated': 'تم تحديث القوالب',
        'link_preview': 'معاينة الرابط',
        'link_preview_sub': 'إظهار معاينة الروابط عند إرسال القالب. أوقف هذا الخيار لإرسال الروابط دون معاينة داخل الرسالة.',
        'templates_count': 'القوالب: {n}',
        'template_saved_plain': 'تم حفظ القالب رقم {n}.',
        'template_saved_rich': 'تم حفظ القالب رقم {n} بتنسيق متقدم.',
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
        'exit_back_message': 'ماذا يجب أن نفعل؟',
        'exit_back_title': 'الرجوع للخلف',
        'exit_leave': 'خروج',
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
        'current_version': 'الإصدار الحالي: {version}',
        'updates_info': 'اضغط على الزر أدناه لفتح منشور الإضافة في قناتي @I_am_Vestr.',
        'check_updates': 'تحقق',
        'badge_meta_chat': '**Meta Plugins Chat** — دردشة **Meta Plugins** الرسمية.',
        'badge_meta_channel': '**Meta Plugins** — قناة **Vestr** الرسمية.',
        'badge_vestr_user': '**Vestr** هو المطور الرئيسي لـ **Packit** ومؤسس **Meta Plugins**.',
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
        'rich_editor_busy': 'المحرر المتقدم مفتوح بالفعل.',
        'rich_editor_missing_classes': 'لم يتم العثور على المحرر المتقدم في هذه النسخة. التفاصيل في سجل المضافة:',
        'rich_editor_no_host': 'تعذّر فتح محادثة للمحرر المتقدم.',
        'rich_editor_open': 'المحرر المتقدم',
        'rich_editor_opening': 'جارٍ فتح المحرر المتقدم...',
        'rich_editor_premium': 'المحرر المتقدم متاح فقط مع Telegram Premium.',
        'rich_editor_present_failed': 'تعذّر عرض المحرر المتقدم. التفاصيل في سجل المضافة.',
        'rich_editor_settings_section': 'المحرر المتقدم',
        'rich_editor_unavailable': 'المحرر المتقدم غير متاح. يلزم إصدار أحدث من Telegram.',
        'rich_exit_confirm': 'تحذير عند الخروج',
        'rich_exit_confirm_sub': 'إظهار قائمة عند مغادرة المحرر المتقدم بزر الرجوع أو بالإيماءة: حفظ التغييرات أو الخروج دون حفظ.',
        'rich_premium_unlock': 'فتح ميزات Premium',
        'rich_premium_unlock_sub': 'يزيل قيود Telegram Premium في المحرر المتقدم — لإنشاء القوالب فقط. لا يمكن إرسال الرسائل بدون Telegram Premium.',
        'rich_send_error': 'فشل إرسال القالب بتنسيق متقدم.',
        'support_me': 'ادعمني',
        'support_me_text': 'إذا كنت تريد دعمي، يمكنك إرسال هدية لي في Telegram أو إهدائي Telegram Premium :)',
        'my_account': 'حسابي',
        'restart_error': 'خطأ في إعادة التشغيل: {error}',
        'download_error': 'خطأ في التحميل: {error}',
        'error_occurred_with_reason': 'خطأ: {error}',
        'select_template': 'اختر قالبًا',
        'no_templates_available': 'لا توجد قوالب متاحة',
        'no_premium_send': 'لا يوجد Telegram Premium في هذا الحساب. قد لا يتم إرسال الرسالة.',
        'export_templates': 'تصدير القوالب',
        'export_question': 'أي القوالب تريد تصديرها؟',
        'export_sent': 'تم إرسال التصدير',
        'export_error': 'خطأ في التصدير: {error}',
        'export_preparing': 'جارٍ تجهيز ملفات التصدير…',
        'export_success': 'تم التصدير بنجاح.',
        'import_question': 'استيراد القوالب من ملف؟',
        'import_success': 'تم استيراد القوالب.',
        'import_error': 'خطأ في الاستيراد: {error}',
        'selected_templates': 'تم التحديد',
        'select_all': 'تحديد الكل',
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
        'templates_limit_exceeded': 'لا يمكن أن يتجاوز عدد القوالب 100 قالبًا.',
        'template_name_exists': 'اسم القالب موجود بالفعل. أعد تسميته أو سيتم إلغاء تنشيطه.',
        'refresh_templates': 'تحديث القوالب...',
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
        'template_sent_n': 'تم إرسال القالب إلى {n} محادثات.',
        'template_send_n_question': 'إرسال القالب إلى {n} محادثات؟',
        'select_chats_done': 'تم',
        'select_chats_hint': 'لتحديد عدة محادثات، اضغط مطولاً على محادثة',
        'channel_promo_title': '🙂 مرحبًا! لدي قناة!',
        'channel_promo_text': 'يسعدني أن تشترك في قناتي. إضافاتي مجانية، والاشتراك دعم رائع لي :)',
        'send_action': 'إرسال',
    },
    'fa': {
        'name': 'نام قالب',
        'text': 'متن قالب',
        'edit': 'ویرایش',
        'clear': 'پاک کردن',
        'open_settings_error': 'باز کردن تنظیمات انجام نشد: {error}',
        'templates': 'قالب‌ها',
        'embed_files': 'فایل\u200cهای پیوست',
        'templates_updated': 'قالب\u200cها به\u200cروزرسانی شد',
        'link_preview': 'پیش\u200cنمایش پیوند',
        'link_preview_sub': 'نمایش پیش\u200cنمایش پیوندها هنگام ارسال قالب. برای ارسال پیوند بدون پیش\u200cنمایش در پیام، این گزینه را خاموش کنید.',
        'templates_count': 'قالب\u200cها: {n}',
        'template_saved_plain': 'قالب شماره {n} ذخیره شد.',
        'template_saved_rich': 'قالب شماره {n} با قالب\u200cبندی پیشرفته ذخیره شد.',
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
        'exit_back_message': 'چه کاری باید انجام شود؟',
        'exit_back_title': 'بازگشت',
        'exit_leave': 'خروج',
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
        'current_version': 'نسخه فعلی: {version}',
        'updates_info': 'برای باز کردن پست افزونه روی دکمه زیر بزنید، در کانال من @I_am_Vestr.',
        'check_updates': 'بررسی',
        'badge_meta_chat': '**Meta Plugins Chat** — چت رسمی **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — کانال رسمی **Vestr**.',
        'badge_vestr_user': '**Vestr** توسعه‌دهنده اصلی **Packit** و بنیان‌گذار **Meta Plugins** است.',
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
        'rich_editor_busy': 'ویرایشگر پیشرفته از قبل باز است.',
        'rich_editor_missing_classes': 'ویرایشگر پیشرفته در این نسخه یافت نشد. جزئیات در گزارش افزونه:',
        'rich_editor_no_host': 'امکان باز کردن گفتگو برای ویرایشگر پیشرفته نبود.',
        'rich_editor_open': 'ویرایشگر پیشرفته',
        'rich_editor_opening': 'در حال باز کردن ویرایشگر پیشرفته...',
        'rich_editor_premium': 'ویرایشگر پیشرفته تنها با Telegram Premium در دسترس است.',
        'rich_editor_present_failed': 'نمایش ویرایشگر پیشرفته ممکن نشد. جزئیات در گزارش افزونه.',
        'rich_editor_settings_section': 'ویرایشگر پیشرفته',
        'rich_editor_unavailable': 'ویرایشگر پیشرفته در دسترس نیست. نسخه تازه\u200cتری از Telegram لازم است.',
        'rich_exit_confirm': 'هشدار هنگام خروج',
        'rich_exit_confirm_sub': 'هنگام خروج از ویرایشگر پیشرفته با دکمه بازگشت یا حرکت، منویی نمایش داده شود: ذخیره تغییرات یا خروج بدون ذخیره.',
        'rich_premium_unlock': 'باز کردن قابلیت\u200cهای پریمیوم',
        'rich_premium_unlock_sub': 'محدودیت\u200cهای Telegram Premium را در ویرایشگر پیشرفته برمی\u200cدارد — فقط برای ساخت قالب\u200cها. ارسال پیام بدون Telegram Premium ممکن نیست.',
        'rich_send_error': 'ارسال قالب با قالب\u200cبندی پیشرفته ناموفق بود.',
        'support_me': 'از من حمایت کنید',
        'support_me_text': 'اگر می‌خواهید از من حمایت کنید، می‌توانید یک هدیه در تلگرام برای من بفرستید یا تلگرام پریمیوم هدیه دهید :)',
        'my_account': 'حساب من',
        'restart_error': 'خطا در راه‌اندازی مجدد: {error}',
        'download_error': 'خطا در دانلود: {error}',
        'error_occurred_with_reason': 'خطا: {error}',
        'select_template': 'انتخاب قالب',
        'no_templates_available': 'قالبی در دسترس نیست',
        'no_premium_send': 'این حساب Telegram Premium ندارد. ممکن است پیام ارسال نشود.',
        'export_templates': 'خروجی گرفتن از قالب‌ها',
        'export_question': 'کدام قالب‌ها خروجی گرفته شوند؟',
        'export_sent': 'خروجی ارسال شد',
        'export_error': 'خطا در خروجی: {error}',
        'export_preparing': 'در حال آماده\u200cسازی فایل\u200cهای خروجی…',
        'export_success': 'خروجی با موفقیت انجام شد.',
        'import_question': 'ورودی گرفتن قالب‌ها از فایل؟',
        'import_success': 'قالب‌ها ورودی گرفته شدند.',
        'import_error': 'خطا در ورودی: {error}',
        'selected_templates': 'انتخاب شده',
        'select_all': 'انتخاب همه',
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
        'templates_limit_exceeded': 'تعداد قالب‌ها نمی‌تواند از ۱۰۰ عدد بیشتر شود.',
        'template_name_exists': 'چنین نام قالبی از قبل وجود دارد. تغییر نام دهید یا غیرفعال خواهد شد.',
        'refresh_templates': 'بازسازی قالب‌ها...',
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
        'template_sent_n': 'قالب به {n} چت ارسال شد.',
        'template_send_n_question': 'قالب به {n} چت ارسال شود؟',
        'select_chats_done': 'انجام',
        'select_chats_hint': 'برای انتخاب چند چت، روی چت نگه دارید',
        'channel_promo_title': '🙂 سلام! من یک کانال دارم!',
        'channel_promo_text': 'خوشحال می‌شوم اگر در کانال من عضو شوید. افزونه‌های من رایگان هستند و اشتراک، حمایت خوبی برای من است :)',
        'send_action': 'ارسال',
    },
    'de': {
        'name': 'Vorlagenname',
        'text': 'Vorlagentext',
        'edit': 'Bearbeiten',
        'clear': 'Löschen',
        'open_settings_error': 'Einstellungen konnten nicht geöffnet werden: {error}',
        'templates': 'Vorlagen',
        'embed_files': 'Angehängte Dateien',
        'templates_updated': 'Vorlagen aktualisiert',
        'link_preview': 'Link-Vorschau',
        'link_preview_sub': 'Linkvorschauen beim Senden der Vorlage anzeigen. Ausschalten, um Links ohne Vorschau in der Nachricht zu senden.',
        'templates_count': 'Vorlagen: {n}',
        'template_saved_plain': 'Vorlage Nr. {n} gespeichert.',
        'template_saved_rich': 'Vorlage Nr. {n} mit Rich-Formatierung gespeichert.',
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
        'exit_back_message': 'Was soll getan werden?',
        'exit_back_title': 'Zurückgehen',
        'exit_leave': 'Beenden',
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
        'current_version': 'Aktuelle Version: {version}',
        'updates_info': 'Tippen Sie auf die Schaltfläche unten, um den Beitrag zum Plugin auf meinem Kanal @I_am_Vestr zu öffnen.',
        'check_updates': 'Prüfen',
        'badge_meta_chat': '**Meta Plugins Chat** — offizieller Chat von **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — offizieller Kanal von **Vestr**.',
        'badge_vestr_user': '**Vestr** ist der leitende Entwickler von **Packit** und Gründer von **Meta Plugins**.',
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
        'rich_editor_busy': 'Der Rich-Editor ist bereits geöffnet.',
        'rich_editor_missing_classes': 'Der Rich-Editor wurde in diesem Build nicht gefunden. Details im Plugin-Log:',
        'rich_editor_no_host': 'Der Chat für den Rich-Editor konnte nicht geöffnet werden.',
        'rich_editor_open': 'Rich-Editor',
        'rich_editor_opening': 'Rich-Editor wird geöffnet…',
        'rich_editor_premium': 'Der Rich-Editor ist nur mit Telegram Premium verfügbar.',
        'rich_editor_present_failed': 'Der Rich-Editor konnte nicht angezeigt werden. Details im Plugin-Log.',
        'rich_editor_settings_section': 'Rich-Editor',
        'rich_editor_unavailable': 'Der Rich-Editor ist nicht verfügbar. Eine neuere Version von Telegram ist erforderlich.',
        'rich_exit_confirm': 'Warnung beim Beenden',
        'rich_exit_confirm_sub': 'Beim Verlassen des Rich-Editors mit der Zurück-Taste oder Geste ein Menü anzeigen: Änderungen speichern oder ohne Speichern beenden.',
        'rich_premium_unlock': 'Premium-Funktionen freischalten',
        'rich_premium_unlock_sub': 'Hebt die Telegram-Premium-Einschränkungen im Rich-Editor auf — nur zum Erstellen von Vorlagen. Senden ohne Telegram Premium bleibt nicht möglich.',
        'rich_send_error': 'Die Vorlage konnte nicht mit Rich-Formatierung gesendet werden.',
        'support_me': 'Unterstütze mich',
        'support_me_text': 'Wenn du mich unterstützen möchtest, kannst du mir ein Geschenk in Telegram senden oder mir Telegram Premium schenken :)',
        'my_account': 'Mein Konto',
        'restart_error': 'Neustartfehler: {error}',
        'download_error': 'Downloadfehler: {error}',
        'error_occurred_with_reason': 'Fehler: {error}',
        'select_template': 'Vorlage auswählen',
        'no_templates_available': 'Keine Vorlagen verfügbar',
        'no_premium_send': 'Dieses Konto hat kein Telegram Premium. Die Nachricht wird möglicherweise nicht gesendet.',
        'export_templates': 'Vorlagen exportieren',
        'export_question': 'Welche Vorlagen sollen exportiert werden?',
        'export_sent': 'Export gesendet',
        'export_error': 'Exportfehler: {error}',
        'export_preparing': 'Exportdateien werden vorbereitet…',
        'export_success': 'Export erfolgreich.',
        'import_question': 'Vorlagen aus Datei importieren?',
        'import_success': 'Vorlagen importiert.',
        'import_error': 'Importfehler: {error}',
        'selected_templates': 'Ausgewählt',
        'select_all': 'Alle auswählen',
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
        'templates_limit_exceeded': 'Die Anzahl der Vorlagen darf 100 nicht überschreiten.',
        'template_name_exists': 'Ein Vorlagenname mit diesem Namen existiert bereits. Benennen Sie ihn um, sonst wird er deaktiviert.',
        'refresh_templates': 'Vorlagen werden aktualisiert...',
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
        'template_sent_n': 'Vorlage an {n} Chats gesendet.',
        'template_send_n_question': 'Vorlage an {n} Chats senden?',
        'select_chats_done': 'Fertig',
        'select_chats_hint': 'Zum Auswählen mehrerer Chats einen Chat gedrückt halten',
        'channel_promo_title': '🙂 Hallo! Ich habe einen Kanal!',
        'channel_promo_text': 'Ich würde mich freuen, wenn du meinen Kanal abonnierst. Meine Plugins sind kostenlos, und ein Abo ist eine gute Unterstützung für mich :)',
        'send_action': 'Senden',
    },
    'ja': {
        'name': 'テンプレート名',
        'text': 'テンプレートテキスト',
        'edit': '編集',
        'clear': 'クリア',
        'open_settings_error': '設定を開けませんでした: {error}',
        'templates': 'テンプレート',
        'embed_files': '添付ファイル',
        'templates_updated': 'テンプレートを更新しました',
        'link_preview': 'リンクプレビュー',
        'link_preview_sub': 'テンプレート送信時にリンクプレビューを表示します。オフにすると、メッセージ内にプレビューなしでリンクを送信します。',
        'templates_count': 'テンプレート: {n}',
        'template_saved_plain': 'テンプレート {n} を保存しました。',
        'template_saved_rich': 'テンプレート {n} をリッチ書式で保存しました。',
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
        'exit_back_message': 'どうしますか？',
        'exit_back_title': '戻る操作',
        'exit_leave': '終了',
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
        'current_version': '現在のバージョン: {version}',
        'updates_info': '下のボタンをタップすると、私のチャンネル @I_am_Vestr でプラグインの投稿が開きます。',
        'check_updates': '確認',
        'badge_meta_chat': '**Meta Plugins Chat** — **Meta Plugins**の公式チャットです。',
        'badge_meta_channel': '**Meta Plugins** — **Vestr**の公式チャンネルです。',
        'badge_vestr_user': '**Vestr**は**Packit**のリード開発者であり、**Meta Plugins**の創設者です。',
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
        'rich_editor_busy': 'リッチエディタはすでに開いています。',
        'rich_editor_missing_classes': 'このビルドではリッチエディタが見つかりませんでした。詳細はプラグインのログを確認してください：',
        'rich_editor_no_host': 'リッチエディタ用のチャットを開けませんでした。',
        'rich_editor_open': 'リッチエディタ',
        'rich_editor_opening': 'リッチエディタを開いています...',
        'rich_editor_premium': 'リッチエディタは Telegram Premium のみ利用できます。',
        'rich_editor_present_failed': 'リッチエディタを表示できませんでした。詳細はプラグインのログを確認してください。',
        'rich_editor_settings_section': 'リッチエディタ',
        'rich_editor_unavailable': 'リッチエディタは利用できません。新しいバージョンの Telegram が必要です。',
        'rich_exit_confirm': '終了時の警告',
        'rich_exit_confirm_sub': '戻るボタンまたはジェスチャでリッチエディタを離れるときにメニューを表示します：変更を保存するか、保存せずに終了します。',
        'rich_premium_unlock': 'プレミアム機能を解放',
        'rich_premium_unlock_sub': 'リッチエディタ内の Telegram Premium の制限を解除します — テンプレートの作成専用です。Telegram Premium なしでの送信はできません。',
        'rich_send_error': 'リッチ書式でテンプレートを送信できませんでした。',
        'support_me': 'サポートする',
        'support_me_text': 'もし私をサポートしたいなら、Telegramでギフトを送るか、Telegram Premiumをギフトしてください :)',
        'my_account': '私のアカウント',
        'restart_error': '再起動エラー: {error}',
        'download_error': 'ダウンロードエラー: {error}',
        'error_occurred_with_reason': 'エラー: {error}',
        'select_template': 'テンプレートを選択',
        'no_templates_available': '利用可能なテンプレートはありません',
        'no_premium_send': 'このアカウントには Telegram Premium がありません。メッセージが送信されない可能性があります。',
        'export_templates': 'テンプレートをエクスポート',
        'export_question': 'どのテンプレートをエクスポートしますか？',
        'export_sent': 'エクスポートを送信しました',
        'export_error': 'エクスポートエラー: {error}',
        'export_preparing': 'エクスポートファイルを準備しています…',
        'export_success': 'エクスポート成功。',
        'import_question': 'ファイルからテンプレートをインポートしますか？',
        'import_success': 'テンプレートをインポートしました。',
        'import_error': 'インポートエラー: {error}',
        'selected_templates': '選択済み',
        'select_all': 'すべて選択',
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
        'templates_limit_exceeded': 'テンプレートの数は100個を超えることはできません。',
        'template_name_exists': 'このテンプレート名は既に存在します。名前を変更するか、非アクティブになります。',
        'refresh_templates': 'テンプレートを更新しています...',
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
        'template_sent_n': 'テンプレートを {n} 件のチャットに送信しました。',
        'template_send_n_question': 'テンプレートを {n} 件のチャットに送信しますか？',
        'select_chats_done': '完了',
        'select_chats_hint': '複数のチャットを選ぶにはチャットを長押ししてください',
        'channel_promo_title': '🙂 こんにちは！私にはチャンネルがあります！',
        'channel_promo_text': 'チャンネルへの登録をよろしくお願いします。私のプラグインは無料で、登録は私にとって良いサポートになります :)',
        'send_action': '送信',
    },
    'tr': {
        'name': 'Şablon adı',
        'text': 'Şablon metni',
        'edit': 'Düzenle',
        'clear': 'Temizle',
        'open_settings_error': 'Ayarlar açılamadı: {error}',
        'templates': 'Şablonlar',
        'embed_files': 'Gömülü dosyalar',
        'templates_updated': 'Şablonlar güncellendi',
        'link_preview': 'Bağlantı önizlemesi',
        'link_preview_sub': 'Şablon gönderilirken bağlantı önizlemelerini göster. Bağlantıları mesajda önizlemesiz göndermek için kapat.',
        'templates_count': 'Şablonlar: {n}',
        'template_saved_plain': 'Şablon #{n} kaydedildi.',
        'template_saved_rich': 'Şablon #{n} zengin biçimlendirmeyle kaydedildi.',
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
        'exit_back_message': 'Ne yapılacak?',
        'exit_back_title': 'Geri dönüş',
        'exit_leave': 'Çık',
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
        'current_version': 'Mevcut sürüm: {version}',
        'updates_info': 'Eklenti gönderisini kanalım @I_am_Vestr üzerinde açmak için aşağıdaki düğmeye dokunun.',
        'check_updates': 'Kontrol et',
        'badge_meta_chat': '**Meta Plugins Chat** — resmi **Meta Plugins** sohbeti.',
        'badge_meta_channel': '**Meta Plugins** — resmi **Vestr** kanalı.',
        'badge_vestr_user': '**Vestr**, **Packit**in baş geliştiricisi ve **Meta Plugins**in kurucusudur.',
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
        'rich_editor_busy': 'Zengin düzenleyici zaten açık.',
        'rich_editor_missing_classes': 'Zengin düzenleyici bu sürümde bulunamadı. Ayrıntılar eklenti günlüğünde:',
        'rich_editor_no_host': 'Zengin düzenleyici için sohbet açılamadı.',
        'rich_editor_open': 'Zengin düzenleyici',
        'rich_editor_opening': 'Zengin düzenleyici açılıyor...',
        'rich_editor_premium': 'Zengin düzenleyici yalnızca Telegram Premium ile kullanılabilir.',
        'rich_editor_present_failed': 'Zengin düzenleyici gösterilemedi. Ayrıntılar eklenti günlüğünde.',
        'rich_editor_settings_section': 'Zengin düzenleyici',
        'rich_editor_unavailable': 'Zengin düzenleyici kullanılamıyor. Telegram’un daha yeni bir sürümü gerekiyor.',
        'rich_exit_confirm': 'Çıkış uyarısı',
        'rich_exit_confirm_sub': 'Zengin düzenleyiciden geri tuşuyla veya hareketle çıkarken bir menü göster: değişiklikleri kaydet veya kaydetmeden çık.',
        'rich_premium_unlock': 'Premium özellikleri aç',
        'rich_premium_unlock_sub': 'Zengin düzenleyicideki Telegram Premium kısıtlamalarını kaldırır — yalnızca şablon oluşturmak için. Telegram Premium olmadan mesaj gönderilemez.',
        'rich_send_error': 'Zengin biçimlendirmeli şablon gönderilemedi.',
        'support_me': 'Beni destekle',
        'support_me_text': 'Beni desteklemek isterseniz, Telegram\'da bana hediye gönderebilir veya Telegram Premium hediye edebilirsiniz :)',
        'my_account': 'Hesabım',
        'restart_error': 'Yeniden başlatma hatası: {error}',
        'download_error': 'İndirme hatası: {error}',
        'error_occurred_with_reason': 'Hata: {error}',
        'select_template': 'Şablon seç',
        'no_templates_available': 'Kullanılabilir şablon yok',
        'no_premium_send': 'Bu hesapta Telegram Premium yok. Mesaj gönderilmeyebilir.',
        'export_templates': 'Şablonları dışa aktar',
        'export_question': 'Hangi şablonlar dışa aktarılsın?',
        'export_sent': 'Dışa aktarma gönderildi',
        'export_error': 'Dışa aktarma hatası: {error}',
        'export_preparing': 'Dışa aktarma dosyaları hazırlanıyor…',
        'export_success': 'Dışa aktarma başarılı.',
        'import_question': 'Dosyadan şablonları içe aktar?',
        'import_success': 'Şablonlar içe aktarıldı.',
        'import_error': 'İçe aktarma hatası: {error}',
        'selected_templates': 'Seçildi',
        'select_all': 'Tümünü seç',
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
        'templates_limit_exceeded': 'Şablon sayısı 100\'ü geçemez.',
        'template_name_exists': 'Bu şablon adı zaten mevcut. Yeniden adlandırın veya devre dışı kalacaktır.',
        'refresh_templates': 'Şablonlar yenileniyor...',
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
        'template_sent_n': 'Şablon {n} sohbete gönderildi.',
        'template_send_n_question': 'Şablon {n} sohbete gönderilsin mi?',
        'select_chats_done': 'Tamam',
        'select_chats_hint': 'Birden fazla sohbet seçmek için sohbeti basılı tutun',
        'channel_promo_title': '🙂 Merhaba! Bir kanalım var!',
        'channel_promo_text': 'Kanalıma abone olursan sevinirim. Eklentilerim ücretsiz, abonelik benim için güzel bir destek olur :)',
        'send_action': 'Gönder',
    },
    'zh': {
        'name': '模板名称',
        'text': '模板文本',
        'edit': '编辑',
        'clear': '清除',
        'open_settings_error': '无法打开设置：{error}',
        'templates': '模板',
        'embed_files': '嵌入的文件',
        'templates_updated': '模板已更新',
        'link_preview': '链接预览',
        'link_preview_sub': '发送模板时显示链接预览。关闭后将以不附带预览的方式发送链接。',
        'templates_count': '模板：{n}',
        'template_saved_plain': '模板 #{n} 已保存。',
        'template_saved_rich': '模板 #{n} 已以富文本格式保存。',
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
        'exit_back_message': '要做什么？',
        'exit_back_title': '返回',
        'exit_leave': '退出',
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
        'current_version': '当前版本：{version}',
        'updates_info': '点击下面的按钮，在我的频道 @I_am_Vestr 中打开插件帖文。',
        'check_updates': '检查',
        'badge_meta_chat': '**Meta Plugins Chat**——**Meta Plugins** 的官方群聊。',
        'badge_meta_channel': '**Meta Plugins**——**Vestr** 的官方频道。',
        'badge_vestr_user': '**Vestr** 是 **Packit** 的首席开发者，也是 **Meta Plugins** 的创始人。',
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
        'rich_editor_busy': '富文本编辑器已打开。',
        'rich_editor_missing_classes': '此版本中未找到富文本编辑器。详情请查看插件日志：',
        'rich_editor_no_host': '无法为富文本编辑器打开聊天。',
        'rich_editor_open': '富文本编辑器',
        'rich_editor_opening': '正在打开富文本编辑器…',
        'rich_editor_premium': '富文本编辑器仅在 Telegram Premium 下可用。',
        'rich_editor_present_failed': '无法显示富文本编辑器。详情请查看插件日志。',
        'rich_editor_settings_section': '富文本编辑器',
        'rich_editor_unavailable': '富文本编辑器不可用，需要更新版本的 Telegram。',
        'rich_exit_confirm': '退出前警告',
        'rich_exit_confirm_sub': '使用返回键或返回手势离开富文本编辑器时显示菜单：保存更改或不保存直接退出。',
        'rich_premium_unlock': '解锁高级功能',
        'rich_premium_unlock_sub': '解除富文本编辑器中的 Telegram Premium 限制 — 仅用于创建模板。没有 Telegram Premium 仍无法发送消息。',
        'rich_send_error': '无法发送带富文本格式的模板。',
        'support_me': '支持我',
        'support_me_text': '如果你想支持我，你可以在Telegram上给我发送礼物或赠送Telegram Premium :)',
        'my_account': '我的账户',
        'restart_error': '重启错误：{error}',
        'download_error': '下载错误：{error}',
        'error_occurred_with_reason': '错误：{error}',
        'select_template': '选择模板',
        'no_templates_available': '没有可用的模板',
        'no_premium_send': '此账号没有 Telegram Premium，消息可能无法发送。',
        'export_templates': '导出模板',
        'export_question': '要导出哪些模板？',
        'export_sent': '导出已发送',
        'export_error': '导出错误：{error}',
        'export_preparing': '正在准备导出文件…',
        'export_success': '导出成功。',
        'import_question': '从文件导入模板？',
        'import_success': '模板已导入。',
        'import_error': '导入错误：{error}',
        'selected_templates': '已选择',
        'select_all': '全选',
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
        'templates_limit_exceeded': '模板数量不能超过100个。',
        'template_name_exists': '该模板名称已存在。请重命名，否则将被停用。',
        'refresh_templates': '正在刷新模板...',
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
        'template_sent_n': '模板已发送到 {n} 个聊天。',
        'template_send_n_question': '将模板发送到 {n} 个聊天？',
        'select_chats_done': '完成',
        'select_chats_hint': '要选择多个聊天，请长按聊天',
        'channel_promo_title': '🙂 你好！我有一个频道！',
        'channel_promo_text': '欢迎订阅我的频道。我的插件是免费的，而订阅是对我的很好支持 :)',
        'send_action': '发送',
    },
    'hi': {
        'name': 'टेम्पलेट का नाम',
        'text': 'टेम्पलेट टेक्स्ट',
        'edit': 'संपादित करें',
        'clear': 'साफ़ करें',
        'open_settings_error': 'सेटिंग्स खोलने में विफल: {error}',
        'templates': 'टेम्पलेट',
        'embed_files': 'संलग्न फ़ाइलें',
        'templates_updated': 'टेम्पलेट अपडेट किए गए',
        'link_preview': 'लिंक प्रीव्यू',
        'link_preview_sub': 'टेम्पलेट भेजते समय लिंक प्रीव्यू दिखाएँ। बंद करें ताकि लिंक संदेश में प्रीव्यू के बिना भेजे जाएँ।',
        'templates_count': 'टेम्पलेट: {n}',
        'template_saved_plain': 'टेम्पलेट #{n} सहेजा गया।',
        'template_saved_rich': 'टेम्पलेट #{n} रिच फ़ॉर्मेटिंग के साथ सहेजा गया।',
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
        'exit_back_message': 'क्या करना है?',
        'exit_back_title': 'वापस जाना',
        'exit_leave': 'बाहर निकलें',
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
        'current_version': 'वर्तमान संस्करण: {version}',
        'updates_info': 'नीचे दिए गए बटन पर टैप करें ताकि मेरे चैनल @I_am_Vestr पर प्लगइन की पोस्ट खुले।',
        'check_updates': 'जांचें',
        'badge_meta_chat': '**Meta Plugins Chat** — **Meta Plugins** का आधिकारिक चैट।',
        'badge_meta_channel': '**Meta Plugins** — **Vestr** का आधिकारिक चैनल।',
        'badge_vestr_user': '**Vestr** — **Packit** के मुख्य डेवलपर और **Meta Plugins** के संस्थापक।',
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
        'rich_editor_busy': 'रिच एडिटर पहले से खुला है।',
        'rich_editor_missing_classes': 'इस बिल्ड में रिच एडिटर नहीं मिला। विवरण प्लगइन लॉग में हैं:',
        'rich_editor_no_host': 'रिच एडिटर के लिए चैट नहीं खोली जा सकी।',
        'rich_editor_open': 'रिच एडिटर',
        'rich_editor_opening': 'रिच एडिटर खोला जा रहा है...',
        'rich_editor_premium': 'रिच एडिटर केवल Telegram Premium के साथ उपलब्ध है।',
        'rich_editor_present_failed': 'रिच एडिटर नहीं दिखाया जा सका। विवरण प्लगइन लॉग में हैं।',
        'rich_editor_settings_section': 'रिच एडिटर',
        'rich_editor_unavailable': 'रिच एडिटर उपलब्ध नहीं है। Telegram का नया संस्करण आवश्यक है।',
        'rich_exit_confirm': 'बाहर जाने पर चेतावनी',
        'rich_exit_confirm_sub': 'रिच एडिटर से बैक बटन या जेस्चर से बाहर जाते समय मेनू दिखाएँ: बदलाव सहेजें या बिना सहेजे बाहर निकलें।',
        'rich_premium_unlock': 'प्रीमियम सुविधाएँ अनलॉक करें',
        'rich_premium_unlock_sub': 'रिच एडिटर में Telegram Premium की सीमाएँ हटाता है — केवल टेम्पलेट बनाने के लिए। Telegram Premium के बिना संदेश भेजना संभव नहीं है।',
        'rich_send_error': 'रिच फ़ॉर्मेटिंग वाला टेम्पलेट नहीं भेजा जा सका।',
        'support_me': 'मेरा समर्थन करें',
        'support_me_text': 'यदि आप मेरा समर्थन करना चाहते हैं, तो आप मुझे टेलीग्राम पर उपहार भेज सकते हैं या टेलीग्राम प्रीमियम उपहार दे सकते हैं :)',
        'my_account': 'मेरा खाता',
        'restart_error': 'पुनरारंभ त्रुटि: {error}',
        'download_error': 'डाउनलोड त्रुटि: {error}',
        'error_occurred_with_reason': 'त्रुटि: {error}',
        'select_template': 'टेम्पलेट चुनें',
        'no_templates_available': 'कोई टेम्पलेट उपलब्ध नहीं',
        'no_premium_send': 'इस खाते में Telegram Premium नहीं है। संदेश नहीं भेजा जा सकता है।',
        'export_templates': 'टेम्पलेट एक्सपोर्ट करें',
        'export_question': 'कौन से टेम्पलेट एक्सपोर्ट करें?',
        'export_sent': 'एक्सपोर्ट भेजा गया',
        'export_error': 'एक्सपोर्ट त्रुटि: {error}',
        'export_preparing': 'एक्सपोर्ट फ़ाइलें तैयार हो रही हैं…',
        'export_success': 'एक्सपोर्ट सफल।',
        'import_question': 'फ़ाइल से टेम्पलेट इंपोर्ट करें?',
        'import_success': 'टेम्पलेट इंपोर्ट हो गए।',
        'import_error': 'इंपोर्ट त्रुटि: {error}',
        'selected_templates': 'चयनित',
        'select_all': 'सभी चुनें',
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
        'templates_limit_exceeded': 'टेम्पलेट्स की संख्या 100 से अधिक नहीं हो सकती।',
        'template_name_exists': 'ऐसा टेम्पलेट नाम पहले से मौजूद है। नाम बदलें या यह निष्क्रिय हो जाएगा।',
        'refresh_templates': 'टेम्पलेट ताज़ा हो रहे हैं...',
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
        'template_sent_n': 'टेम्पलेट {n} चैट में भेजा गया।',
        'template_send_n_question': 'टेम्पलेट {n} चैट में भेजें?',
        'select_chats_done': 'हो गया',
        'select_chats_hint': 'कई चैट चुनने के लिए चैट को देर तक दबाए रखें',
        'channel_promo_title': '🙂 नमस्ते! मेरे पास एक चैनल है!',
        'channel_promo_text': 'आप मेरे चैनल को सब्सक्राइब करें तो मुझे खुशी होगी। मेरे प्लगइन मुफ़्त हैं, और सब्सक्रिप्शन मेरे लिए अच्छा सपोर्ट है :)',
        'send_action': 'भेजें',
    },
    'id': {
        'name': 'Nama template',
        'text': 'Teks template',
        'edit': 'Edit',
        'clear': 'Bersihkan',
        'open_settings_error': 'Gagal membuka pengaturan: {error}',
        'templates': 'Template',
        'embed_files': 'File terlampir',
        'templates_updated': 'Template diperbarui',
        'link_preview': 'Pratinjau tautan',
        'link_preview_sub': 'Tampilkan pratinjau tautan saat mengirim template. Matikan untuk mengirim tautan tanpa pratinjau di pesan.',
        'templates_count': 'Template: {n}',
        'template_saved_plain': 'Template #{n} disimpan.',
        'template_saved_rich': 'Template #{n} disimpan dengan format kaya.',
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
        'exit_back_message': 'Apa yang harus dilakukan?',
        'exit_back_title': 'Kembali',
        'exit_leave': 'Keluar',
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
        'current_version': 'Versi saat ini: {version}',
        'updates_info': 'Ketuk tombol di bawah untuk membuka postingan plugin di saluran saya @I_am_Vestr.',
        'check_updates': 'Periksa',
        'badge_meta_chat': '**Meta Plugins Chat** — obrolan resmi **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — kanal resmi **Vestr**.',
        'badge_vestr_user': '**Vestr** adalah pengembang utama **Packit** dan pendiri **Meta Plugins**.',
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
        'rich_editor_busy': 'Editor kaya sudah terbuka.',
        'rich_editor_missing_classes': 'Editor kaya tidak ditemukan pada build ini. Lihat detail di log plugin:',
        'rich_editor_no_host': 'Tidak dapat membuka obrolan untuk editor kaya.',
        'rich_editor_open': 'Editor kaya',
        'rich_editor_opening': 'Membuka editor kaya...',
        'rich_editor_premium': 'Editor kaya hanya tersedia dengan Telegram Premium.',
        'rich_editor_present_failed': 'Tidak dapat menampilkan editor kaya. Lihat detail di log plugin.',
        'rich_editor_settings_section': 'Editor kaya',
        'rich_editor_unavailable': 'Editor kaya tidak tersedia. Diperlukan versi Telegram yang lebih baru.',
        'rich_exit_confirm': 'Peringatan saat keluar',
        'rich_exit_confirm_sub': 'Tampilkan menu saat keluar dari editor kaya dengan tombol kembali atau gestur: simpan perubahan atau keluar tanpa menyimpan.',
        'rich_premium_unlock': 'Buka fitur premium',
        'rich_premium_unlock_sub': 'Menghapus batasan Telegram Premium di editor kaya — hanya untuk membuat template. Mengirim pesan tanpa Telegram Premium tetap tidak dimungkinkan.',
        'rich_send_error': 'Gagal mengirim template dengan format kaya.',
        'support_me': 'Dukung saya',
        'support_me_text': 'Jika Anda ingin mendukung saya, Anda dapat mengirimkan hadiah kepada saya di Telegram atau memberikan Telegram Premium :)',
        'my_account': 'Akun saya',
        'restart_error': 'Kesalahan restart: {error}',
        'download_error': 'Kesalahan unduh: {error}',
        'error_occurred_with_reason': 'Kesalahan: {error}',
        'select_template': 'Pilih template',
        'no_templates_available': 'Tidak ada template tersedia',
        'no_premium_send': 'Akun ini tidak memiliki Telegram Premium. Pesan mungkin tidak terkirim.',
        'export_templates': 'Ekspor Template',
        'export_question': 'Template mana yang akan diekspor?',
        'export_sent': 'Ekspor terkirim',
        'export_error': 'Kesalahan ekspor: {error}',
        'export_preparing': 'Menyiapkan berkas ekspor…',
        'export_success': 'Ekspor berhasil.',
        'import_question': 'Impor template dari file?',
        'import_success': 'Template diimpor.',
        'import_error': 'Kesalahan impor: {error}',
        'selected_templates': 'Dipilih',
        'select_all': 'Pilih semua',
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
        'templates_limit_exceeded': 'Jumlah template tidak boleh melebihi 100.',
        'template_name_exists': 'Nama template sudah ada. Ganti namanya atau akan dinonaktifkan.',
        'refresh_templates': 'Menyegarkan template...',
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
        'template_sent_n': 'Template dikirim ke {n} obrolan.',
        'template_send_n_question': 'Kirim template ke {n} obrolan?',
        'select_chats_done': 'Selesai',
        'select_chats_hint': 'Untuk memilih beberapa obrolan, tekan lama obrolan',
        'channel_promo_title': '🙂 Halo! Saya punya kanal!',
        'channel_promo_text': 'Saya senang jika kamu berlangganan kanal saya. Plugin saya gratis, dan langganan adalah dukungan yang bagus bagi saya :)',
        'send_action': 'Kirim',
    },
    'fr': {
        'name': 'Nom du modèle',
        'text': 'Texte du modèle',
        'edit': 'Modifier',
        'clear': 'Effacer',
        'open_settings_error': 'Impossible d\'ouvrir les paramètres : {error}',
        'templates': 'Modèles',
        'embed_files': 'Fichiers joints',
        'templates_updated': 'Modèles mis à jour',
        'link_preview': 'Aperçu des liens',
        'link_preview_sub': 'Afficher l’aperçu des liens lors de l’envoi du modèle. Désactivez-le pour envoyer les liens sans aperçu dans le message.',
        'templates_count': 'Modèles : {n}',
        'template_saved_plain': 'Modèle n° {n} enregistré.',
        'template_saved_rich': 'Modèle n° {n} enregistré avec la mise en forme enrichie.',
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
        'exit_back_message': 'Que faut-il faire ?',
        'exit_back_title': 'Retour en arrière',
        'exit_leave': 'Quitter',
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
        'current_version': 'Version actuelle : {version}',
        'updates_info': 'Touchez le bouton ci-dessous pour ouvrir la publication du plugin sur ma chaîne @I_am_Vestr.',
        'check_updates': 'Vérifier',
        'badge_meta_chat': '**Meta Plugins Chat** — chat officiel de **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — chaîne officielle de **Vestr**.',
        'badge_vestr_user': '**Vestr** est le développeur principal de **Packit** et le fondateur de **Meta Plugins**.',
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
        'rich_editor_busy': 'L’éditeur enrichi est déjà ouvert.',
        'rich_editor_missing_classes': 'L’éditeur enrichi est introuvable dans cette version. Détails dans le journal du plugin :',
        'rich_editor_no_host': 'Impossible d’ouvrir une discussion pour l’éditeur enrichi.',
        'rich_editor_open': 'Éditeur enrichi',
        'rich_editor_opening': 'Ouverture de l’éditeur enrichi…',
        'rich_editor_premium': 'L’éditeur enrichi est uniquement disponible avec Telegram Premium.',
        'rich_editor_present_failed': 'Impossible d’afficher l’éditeur enrichi. Détails dans le journal du plugin.',
        'rich_editor_settings_section': 'Éditeur enrichi',
        'rich_editor_unavailable': 'L’éditeur enrichi est indisponible. Une version plus récente de Telegram est requise.',
        'rich_exit_confirm': 'Avertissement à la sortie',
        'rich_exit_confirm_sub': 'Afficher un menu lors de la sortie de l’éditeur enrichi via le bouton retour ou le geste : enregistrer les modifications ou quitter sans enregistrer.',
        'rich_premium_unlock': 'Débloquer les fonctions premium',
        'rich_premium_unlock_sub': 'Supprime les limites Telegram Premium dans l’éditeur enrichi — uniquement pour créer des modèles. L’envoi sans Telegram Premium reste impossible.',
        'rich_send_error': 'Échec de l’envoi du modèle avec la mise en forme enrichie.',
        'support_me': 'Soutenez-moi',
        'support_me_text': 'Si vous voulez me soutenir, vous pouvez m\'envoyer un cadeau sur Telegram ou m\'offrir Telegram Premium :)',
        'my_account': 'Mon compte',
        'restart_error': 'Erreur de redémarrage : {error}',
        'download_error': 'Erreur de téléchargement : {error}',
        'error_occurred_with_reason': 'Erreur : {error}',
        'select_template': 'Sélectionnez un modèle',
        'no_templates_available': 'Aucun modèle disponible',
        'no_premium_send': 'Ce compte n’a pas Telegram Premium. Le message risque de ne pas être envoyé.',
        'export_templates': 'Exporter les modèles',
        'export_question': 'Quels modèles exporter ?',
        'export_sent': 'Exportation envoyée',
        'export_error': 'Erreur d\'exportation : {error}',
        'export_preparing': 'Préparation des fichiers d’export…',
        'export_success': 'Exportation réussie.',
        'import_question': 'Importer des modèles depuis un fichier ?',
        'import_success': 'Modèles importés.',
        'import_error': 'Erreur d\'importation : {error}',
        'selected_templates': 'Sélectionné',
        'select_all': 'Tout sélectionner',
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
        'templates_limit_exceeded': 'Le nombre de modèles ne peut pas dépasser 100.',
        'template_name_exists': 'Ce nom de modèle existe déjà. Renommez-le ou il sera désactivé.',
        'refresh_templates': 'Actualisation des modèles...',
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
        'template_sent_n': 'Modèle envoyé à {n} discussions.',
        'template_send_n_question': 'Envoyer le modèle à {n} discussions ?',
        'select_chats_done': 'Terminé',
        'select_chats_hint': 'Pour sélectionner plusieurs discussions, appuyez longuement sur une discussion',
        'channel_promo_title': '🙂 Salut ! J\'ai une chaîne !',
        'channel_promo_text': 'Je serais ravi que tu t\'abonnes à ma chaîne. Mes plugins sont gratuits, et un abonnement est un bon soutien pour moi :)',
        'send_action': 'Envoyer',
    },
    'pt': {
        'name': 'Nome do modelo',
        'text': 'Texto do modelo',
        'edit': 'Editar',
        'clear': 'Limpar',
        'open_settings_error': 'Falha ao abrir as configurações: {error}',
        'templates': 'Modelos',
        'embed_files': 'Ficheiros anexados',
        'templates_updated': 'Modelos atualizados',
        'link_preview': 'Pré-visualização de ligação',
        'link_preview_sub': 'Mostrar a pré-visualização das ligações ao enviar o modelo. Desative para enviar ligações sem pré-visualização na mensagem.',
        'templates_count': 'Modelos: {n}',
        'template_saved_plain': 'Modelo n.º {n} guardado.',
        'template_saved_rich': 'Modelo n.º {n} guardado com formatação avançada.',
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
        'exit_back_message': 'O que deve ser feito?',
        'exit_back_title': 'Voltar',
        'exit_leave': 'Sair',
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
        'current_version': 'Versão atual: {version}',
        'updates_info': 'Toque no botão abaixo para abrir a publicação do plugin no meu canal @I_am_Vestr.',
        'check_updates': 'Verificar',
        'badge_meta_chat': '**Meta Plugins Chat** — chat oficial do **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — canal oficial do **Vestr**.',
        'badge_vestr_user': '**Vestr** é o desenvolvedor principal do **Packit** e fundador do **Meta Plugins**.',
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
        'rich_editor_busy': 'O editor avançado já está aberto.',
        'rich_editor_missing_classes': 'O editor avançado não foi encontrado nesta versão. Detalhes no registo do plugin:',
        'rich_editor_no_host': 'Não foi possível abrir uma conversa para o editor avançado.',
        'rich_editor_open': 'Editor avançado',
        'rich_editor_opening': 'A abrir o editor avançado…',
        'rich_editor_premium': 'O editor avançado só está disponível com Telegram Premium.',
        'rich_editor_present_failed': 'Não foi possível mostrar o editor avançado. Detalhes no registo do plugin.',
        'rich_editor_settings_section': 'Editor avançado',
        'rich_editor_unavailable': 'O editor avançado não está disponível. É necessária uma versão mais recente do Telegram.',
        'rich_exit_confirm': 'Aviso ao sair',
        'rich_exit_confirm_sub': 'Mostrar um menu ao sair do editor avançado com o botão voltar ou o gesto: guardar as alterações ou sair sem guardar.',
        'rich_premium_unlock': 'Desbloquear funcionalidades premium',
        'rich_premium_unlock_sub': 'Remove os limites do Telegram Premium no editor avançado — apenas para criar modelos. Continua a não ser possível enviar mensagens sem Telegram Premium.',
        'rich_send_error': 'Falha ao enviar o modelo com formatação avançada.',
        'support_me': 'Apoie-me',
        'support_me_text': 'Se você quer me apoiar, pode me enviar um presente no Telegram ou presentear com Telegram Premium :)',
        'my_account': 'Minha conta',
        'restart_error': 'Erro ao reiniciar: {error}',
        'download_error': 'Erro de download: {error}',
        'error_occurred_with_reason': 'Erro: {error}',
        'select_template': 'Selecione o modelo',
        'no_templates_available': 'Nenhum modelo disponível',
        'no_premium_send': 'Esta conta não tem Telegram Premium. A mensagem pode não ser enviada.',
        'export_templates': 'Exportar modelos',
        'export_question': 'Quais modelos exportar?',
        'export_sent': 'Exportação enviada',
        'export_error': 'Erro de exportação: {error}',
        'export_preparing': 'A preparar os ficheiros de exportação…',
        'export_success': 'Exportação bem-sucedida.',
        'import_question': 'Importar modelos do arquivo?',
        'import_success': 'Modelos importados.',
        'import_error': 'Erro de importação: {error}',
        'selected_templates': 'Selecionado',
        'select_all': 'Selecionar todos',
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
        'templates_limit_exceeded': 'O número de modelos não pode exceder 100.',
        'template_name_exists': 'Esse nome de modelo já existe. Renomeie ou ele será desativado.',
        'refresh_templates': 'Atualizando modelos...',
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
        'template_sent_n': 'Modelo enviado para {n} conversas.',
        'template_send_n_question': 'Enviar modelo para {n} conversas?',
        'select_chats_done': 'Concluído',
        'select_chats_hint': 'Para selecionar várias conversas, mantenha pressionado',
        'channel_promo_title': '🙂 Olá! Eu tenho um canal!',
        'channel_promo_text': 'Fico feliz se você se inscrever no meu canal. Meus plugins são gratuitos, e uma inscrição é um ótimo apoio para mim :)',
        'send_action': 'Enviar',
    },
    'es': {
        'name': 'Nombre de la plantilla',
        'text': 'Texto de la plantilla',
        'edit': 'Editar',
        'clear': 'Limpiar',
        'open_settings_error': 'No se pudieron abrir los ajustes: {error}',
        'templates': 'Plantillas',
        'embed_files': 'Archivos adjuntos',
        'templates_updated': 'Plantillas actualizadas',
        'link_preview': 'Vista previa del enlace',
        'link_preview_sub': 'Mostrar la vista previa de los enlaces al enviar la plantilla. Desactívalo para enviar enlaces sin vista previa en el mensaje.',
        'templates_count': 'Plantillas: {n}',
        'template_saved_plain': 'Plantilla n.º {n} guardada.',
        'template_saved_rich': 'Plantilla n.º {n} guardada con formato avanzado.',
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
        'exit_back_message': '¿Qué hay que hacer?',
        'exit_back_title': 'Volver atrás',
        'exit_leave': 'Salir',
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
        'current_version': 'Versión actual: {version}',
        'updates_info': 'Toca el botón de abajo para abrir la publicación del plugin en mi canal @I_am_Vestr.',
        'check_updates': 'Comprobar',
        'badge_meta_chat': '**Meta Plugins Chat** — chat oficial de **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — canal oficial de **Vestr**.',
        'badge_vestr_user': '**Vestr** es el desarrollador principal de **Packit** y fundador de **Meta Plugins**.',
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
        'rich_editor_busy': 'El editor avanzado ya está abierto.',
        'rich_editor_missing_classes': 'El editor avanzado no se encontró en esta compilación. Detalles en el registro del plugin:',
        'rich_editor_no_host': 'No se pudo abrir un chat para el editor avanzado.',
        'rich_editor_open': 'Editor avanzado',
        'rich_editor_opening': 'Abriendo el editor avanzado…',
        'rich_editor_premium': 'El editor avanzado solo está disponible con Telegram Premium.',
        'rich_editor_present_failed': 'No se pudo mostrar el editor avanzado. Detalles en el registro del plugin.',
        'rich_editor_settings_section': 'Editor avanzado',
        'rich_editor_unavailable': 'El editor avanzado no está disponible. Se necesita una versión más reciente de Telegram.',
        'rich_exit_confirm': 'Aviso al salir',
        'rich_exit_confirm_sub': 'Mostrar un menú al salir del editor avanzado con el botón atrás o el gesto: guardar los cambios o salir sin guardar.',
        'rich_premium_unlock': 'Desbloquear funciones premium',
        'rich_premium_unlock_sub': 'Elimina las limitaciones de Telegram Premium en el editor avanzado: solo para crear plantillas. Seguirá sin poder enviar mensajes sin Telegram Premium.',
        'rich_send_error': 'No se pudo enviar la plantilla con formato avanzado.',
        'support_me': 'Apóyame',
        'support_me_text': 'Si quieres apoyarme, puedes enviarme un regalo en Telegram o regalarme Telegram Premium :)',
        'my_account': 'Mi cuenta',
        'restart_error': 'Error al reiniciar: {error}',
        'download_error': 'Error de descarga: {error}',
        'error_occurred_with_reason': 'Error: {error}',
        'select_template': 'Selecciona una plantilla',
        'no_templates_available': 'No hay plantillas disponibles',
        'no_premium_send': 'Esta cuenta no tiene Telegram Premium. Puede que el mensaje no se envíe.',
        'export_templates': 'Exportar plantillas',
        'export_question': '¿Qué plantillas exportar?',
        'export_sent': 'Exportación enviada',
        'export_error': 'Error de exportación: {error}',
        'export_preparing': 'Preparando los archivos de exportación…',
        'export_success': 'Exportación exitosa.',
        'import_question': '¿Importar plantillas desde archivo?',
        'import_success': 'Plantillas importadas.',
        'import_error': 'Error de importación: {error}',
        'selected_templates': 'Seleccionado',
        'select_all': 'Seleccionar todo',
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
        'templates_limit_exceeded': 'El número de plantillas no puede superar las 100.',
        'template_name_exists': 'Ya existe un nombre de plantilla así. Renómbralo o será desactivado.',
        'refresh_templates': 'Actualizando plantillas...',
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
        'template_sent_n': 'Plantilla enviada a {n} chats.',
        'template_send_n_question': '¿Enviar la plantilla a {n} chats?',
        'select_chats_done': 'Listo',
        'select_chats_hint': 'Para seleccionar varios chats, mantén pulsado un chat',
        'channel_promo_title': '🙂 ¡Hola! ¡Tengo un canal!',
        'channel_promo_text': 'Me alegraría que te suscribieras a mi canal. Mis plugins son gratuitos, y la suscripción es un buen apoyo para mí :)',
        'send_action': 'Enviar',
    },
    'vi': {
        'name': 'Tên mẫu',
        'text': 'Nội dung mẫu',
        'edit': 'Chỉnh sửa',
        'clear': 'Xóa',
        'open_settings_error': 'Không thể mở cài đặt: {error}',
        'templates': 'Mẫu',
        'embed_files': 'Tệp đính kèm',
        'templates_updated': 'Đã cập nhật mẫu',
        'link_preview': 'Xem trước liên kết',
        'link_preview_sub': 'Hiển thị bản xem trước liên kết khi gửi mẫu. Tắt đi để gửi liên kết không kèm bản xem trước trong tin nhắn.',
        'templates_count': 'Mẫu: {n}',
        'template_saved_plain': 'Đã lưu mẫu số {n}.',
        'template_saved_rich': 'Đã lưu mẫu số {n} với định dạng giàu.',
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
        'exit_back_message': 'Cần làm gì?',
        'exit_back_title': 'Quay lại',
        'exit_leave': 'Thoát',
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
        'current_version': 'Phiên bản hiện tại: {version}',
        'updates_info': 'Nhấn vào nút bên dưới để mở bài đăng về plugin trên kênh của tôi @I_am_Vestr.',
        'check_updates': 'Kiểm tra',
        'badge_meta_chat': '**Meta Plugins Chat** — nhóm chat chính thức của **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — kênh chính thức của **Vestr**.',
        'badge_vestr_user': '**Vestr** là nhà phát triển chính của **Packit** và là người sáng lập **Meta Plugins**.',
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
        'rich_editor_busy': 'Trình soạn thảo giàu đã mở.',
        'rich_editor_missing_classes': 'Không tìm thấy trình soạn thảo giàu trong bản dựng này. Chi tiết trong nhật ký plugin:',
        'rich_editor_no_host': 'Không thể mở cuộc trò chuyện cho trình soạn thảo giàu.',
        'rich_editor_open': 'Trình soạn thảo giàu',
        'rich_editor_opening': 'Đang mở trình soạn thảo giàu...',
        'rich_editor_premium': 'Trình soạn thảo giàu chỉ khả dụng với Telegram Premium.',
        'rich_editor_present_failed': 'Không thể hiển thị trình soạn thảo giàu. Chi tiết trong nhật ký plugin.',
        'rich_editor_settings_section': 'Trình soạn thảo giàu',
        'rich_editor_unavailable': 'Trình soạn thảo giàu không khả dụng. Cần phiên bản Telegram mới hơn.',
        'rich_exit_confirm': 'Cảnh báo khi thoát',
        'rich_exit_confirm_sub': 'Hiện menu khi thoát trình soạn thảo giàu bằng nút quay lại hoặc cử chỉ: lưu thay đổi hoặc thoát mà không lưu.',
        'rich_premium_unlock': 'Mở khóa tính năng cao cấp',
        'rich_premium_unlock_sub': 'Gỡ bỏ giới hạn Telegram Premium trong trình soạn thảo giàu — chỉ dùng để tạo mẫu. Vẫn không thể gửi tin nhắn khi không có Telegram Premium.',
        'rich_send_error': 'Không thể gửi mẫu với định dạng giàu.',
        'support_me': 'Ủng hộ tôi',
        'support_me_text': 'Nếu bạn muốn ủng hộ tôi, bạn có thể gửi quà tặng Telegram cho tôi hoặc tặng Telegram Premium :)',
        'my_account': 'Tài khoản của tôi',
        'restart_error': 'Lỗi khởi động lại: {error}',
        'download_error': 'Lỗi tải xuống: {error}',
        'error_occurred_with_reason': 'Lỗi: {error}',
        'select_template': 'Chọn mẫu',
        'no_templates_available': 'Không có mẫu nào',
        'no_premium_send': 'Tài khoản này không có Telegram Premium. Tin nhắn có thể không được gửi.',
        'export_templates': 'Xuất mẫu',
        'export_question': 'Xuất những mẫu nào?',
        'export_sent': 'Đã gửi xuất',
        'export_error': 'Lỗi xuất: {error}',
        'export_preparing': 'Đang chuẩn bị tệp xuất…',
        'export_success': 'Xuất thành công.',
        'import_question': 'Nhập mẫu từ tệp?',
        'import_success': 'Đã nhập mẫu.',
        'import_error': 'Lỗi nhập: {error}',
        'selected_templates': 'Đã chọn',
        'select_all': 'Chọn tất cả',
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
        'templates_limit_exceeded': 'Số lượng mẫu không thể vượt quá 100.',
        'template_name_exists': 'Tên mẫu này đã tồn tại. Đổi tên nó hoặc nó sẽ bị vô hiệu hóa.',
        'refresh_templates': 'Đang làm mới mẫu...',
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
        'template_sent_n': 'Đã gửi mẫu tới {n} cuộc trò chuyện.',
        'template_send_n_question': 'Gửi mẫu tới {n} cuộc trò chuyện?',
        'select_chats_done': 'Xong',
        'select_chats_hint': 'Để chọn nhiều cuộc trò chuyện, nhấn giữ cuộc trò chuyện',
        'channel_promo_title': '🙂 Chào bạn! Mình có một kênh!',
        'channel_promo_text': 'Mình sẽ rất vui nếu bạn đăng ký kênh của mình. Các plugin của mình đều miễn phí, và việc đăng ký là một sự ủng hộ tốt dành cho mình :)',
        'send_action': 'Gửi',
    },
    'sr': {
        'name': 'Ime šablona',
        'text': 'Tekst šablona',
        'edit': 'Izmeni',
        'clear': 'Obriši',
        'open_settings_error': 'Neuspešno otvaranje podešavanja: {error}',
        'templates': 'Šabloni',
        'embed_files': 'Приложене датотеке',
        'templates_updated': 'Шаблони су ажурирани',
        'link_preview': 'Преглед линкова',
        'link_preview_sub': 'Приказуј преглед линкова при слању шаблона. Искључите да би линкови били послати без прегледа у поруци.',
        'templates_count': 'Шаблона: {n}',
        'template_saved_plain': 'Шаблон бр. {n} је сачуван.',
        'template_saved_rich': 'Шаблон бр. {n} је сачуван са богатим форматирањем.',
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
        'exit_back_message': 'Шта треба урадити?',
        'exit_back_title': 'Повратак назад',
        'exit_leave': 'Излаз',
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
        'current_version': 'Trenutna verzija: {version}',
        'updates_info': 'Кликните на дугме испод да бисте отворили пост о додатку на мом каналу @I_am_Vestr.',
        'check_updates': 'Proveri',
        'badge_meta_chat': '**Meta Plugins Chat** — званични ћаскавица **Meta Plugins**.',
        'badge_meta_channel': '**Meta Plugins** — званични канал **Vestr**.',
        'badge_vestr_user': '**Vestr** — главни програмер **Packit**-a и оснивач **Meta Plugins**-a.',
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
        'rich_editor_busy': 'Богати уређивач је већ отворен.',
        'rich_editor_missing_classes': 'Богати уређивач није пронађен у овој верзији. Детаљи у дневнику додатка:',
        'rich_editor_no_host': 'Није могуће отворити разговор за богати уређивач.',
        'rich_editor_open': 'Богати уређивач',
        'rich_editor_opening': 'Отварам богати уређивач...',
        'rich_editor_premium': 'Богати уређивач је доступан само са Telegram Premium.',
        'rich_editor_present_failed': 'Није могуће приказати богати уређивач. Детаљи у дневнику додатка.',
        'rich_editor_settings_section': 'Богати уређивач',
        'rich_editor_unavailable': 'Богати уређивач није доступан. Потребна је новија верзија Telegram-а.',
        'rich_exit_confirm': 'Упозорење при изласку',
        'rich_exit_confirm_sub': 'При изласку из богатог уређивача дугмеом „Назад“ или покретом прикажи мени: сачувај измене или изази без чувања.',
        'rich_premium_unlock': 'Откључај премијум функције',
        'rich_premium_unlock_sub': 'Уклања Telegram Premium ограничења у богатом уређивачу — само за прављење шаблона. Слање без Telegram Premium и даље није могуће.',
        'rich_send_error': 'Није могуће послати шаблон са богатим форматирањем.',
        'support_me': 'Podrži me',
        'support_me_text': 'Ako želite da me podržite, možete mi poslati poklon u Telegramu ili pokloniti Telegram Premium :)',
        'my_account': 'Moj nalog',
        'restart_error': 'Greška pri ponovnom pokretanju: {error}',
        'download_error': 'Greška pri preuzimanju: {error}',
        'error_occurred_with_reason': 'Greška: {error}',
        'select_template': 'Izaberite šablon',
        'no_templates_available': 'Nema dostupnih šablona',
        'no_premium_send': 'Овај налог нема Telegram Premium. Порука можда неће бити послата.',
        'export_templates': 'Eksportuj šablone',
        'export_question': 'Koje šablone eksportovati?',
        'export_sent': 'Eksport poslat',
        'export_error': 'Greška pri eksportu: {error}',
        'export_preparing': 'Припремају се датотеке за извоз…',
        'export_success': 'Uspešan eksport.',
        'import_question': 'Uvezati šablone iz fajla?',
        'import_success': 'Šabloni su uvezeni.',
        'import_error': 'Greška pri uvozu: {error}',
        'selected_templates': 'Izabrano',
        'select_all': 'Izaberi sve',
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
        'templates_limit_exceeded': 'Broj šablona ne može biti veći od 100.',
        'template_name_exists': 'Takvo ime šablona već postoji. Preimenujte ga ili će biti deaktiviran.',
        'refresh_templates': 'Osvežavam šablone...',
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
        'template_sent_n': 'Šablon poslat u {n} četa.',
        'template_send_n_question': 'Poslati šablon u {n} četa?',
        'select_chats_done': 'Gotovo',
        'select_chats_hint': 'Za izbor više četova pritisnite i držite čet',
        'channel_promo_title': '🙂 Здраво! Имам канал!',
        'channel_promo_text': 'Био би срећан ако се претплатиш на мој канал. Моји плагини су бесплатни, а претплата је добра подршка за мене :)',
        'send_action': 'Pošalji',
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


RICH_CLASS_CACHE = {}
RICH_CLASS_ERRORS = {}
RICH_HOOK_STATE = {
    "prepareSendingArticle": False,
    "sendConvertedRichAsSimple": False,
    "richEditorAvailable": False,
    "richEditorAllowed": False,
    "draftSuppressed": False,
}
RICH_PAYLOAD_VERSION = 3
RICH_EDITOR_SESSION_TTL = 1800
RICH_SKIP_FIELDS = frozenset((
    "first", "bottom", "level", "quoteLevels", "mid", "groupId",
    "thumb", "thumbObject", "cachedWidth", "cachedHeight",
    "parentRichText", "bitmap", "tried",
))
RICH_SKIP_MEDIA_FIELDS = frozenset(("photos", "documents"))
RICH_MEDIA_BLOCKS = (
    "pageBlockPhoto",
    "pageBlockVideo",
    "pageBlockAudio",
    "pageBlockDocument",
    "pageBlockMap",
)
RICH_MEDIA_CHUNK = 48 * 1024
RICH_MEDIA_DOWNLOAD_MIN_TIMEOUT = 30
RICH_MEDIA_DOWNLOAD_MAX_TIMEOUT = 300
RICH_MEDIA_DOWNLOAD_POLL = 0.2
PICKER_PAD_H = 35
PICKER_BUTTON_PAD_H = 12
PICKER_BUTTON_TOP_PAD = 18
PICKER_TOKEN_KEY = "templates_picker_token"
PICKER_HINT_LIMIT = 3
STICKER_TAG = "templates_sticker_view"
CHANNEL_PROMO_URL = "https://t.me/I_am_Vestr"
CHANNEL_PROMO_USERNAME = "I_am_Vestr"
CHANNEL_PROMO_EMOJI_ID = 5420090561086398517
CHANNEL_PROMO_EMOJI_CHAR = "\U0001F642"
RICH_REQUIRED_CLASSES = (
    "org.telegram.ui.iv.RichEditor",
    "org.telegram.ui.iv.RichEditorListView",
    "org.telegram.ui.iv.RichHtml",
    "org.telegram.ui.iv.RichMessageConvert",
    "org.telegram.ui.iv.RichMessageButtonUsers",
    "org.telegram.tgnet.tl.TL_iv$RichMessage",
    "org.telegram.ui.Components.MarkdownParser",
    "org.telegram.messenger.AccountInstance",
)


def _rich_forget_classes():
    RICH_CLASS_CACHE.clear()
    RICH_CLASS_ERRORS.clear()


def _rich_class_via_context(name):
    try:
        from java.lang import Class
        context = ApplicationLoader.applicationContext
        if context is None:
            return None
        loader = context.getClassLoader()
        if loader is None:
            return None
        return Class.forName(name, False, loader)
    except Exception as e:
        RICH_CLASS_ERRORS.setdefault(name, []).append(f"context: {type(e).__name__}: {e}")
        return None


def _rich_class(name):
    if name in RICH_CLASS_CACHE:
        return RICH_CLASS_CACHE[name]
    if name in RICH_CLASS_ERRORS:
        return None
    errors = []
    cls = None
    try:
        cls = find_class(name)
    except Exception as e:
        errors.append(f"find_class: {type(e).__name__}: {e}")
    if cls is None:
        try:
            cls = jclass(name)
        except Exception as e:
            errors.append(f"jclass: {type(e).__name__}: {e}")
    if cls is None:
        try:
            cls = jclass(name, True)
        except Exception as e:
            errors.append(f"jclass+init: {type(e).__name__}: {e}")
    if cls is None:
        cls = _rich_class_via_context(name)
    if cls is None:
        RICH_CLASS_ERRORS[name] = errors or ["not found"]
        return None
    RICH_CLASS_CACHE[name] = cls
    return cls


def rich_self_dialog_id(account):
    try:
        user = UserConfig.getInstance(int(account)).getCurrentUser()
        if user is not None:
            return int(user.id)
    except Exception as e:
        pass
    try:
        user = MessagesController.getInstance(int(account)).getUser(jlong(0))
        if user is not None:
            return int(user.id)
    except Exception as e:
        pass
    return 0


def rich_editor_supported():
    return _rich_class("org.telegram.ui.iv.RichEditor") is not None


def rich_editor_status(account=0):
    _rich_forget_classes()
    missing = [name for name in RICH_REQUIRED_CLASSES if _rich_class(name) is None]
    if missing:
        return "missing_classes", missing
    try:
        controller = MessagesController.getInstance(int(account))
        if hasattr(controller, "richEditorAvailable") and not controller.richEditorAvailable():
            return "disabled_by_config", None
    except Exception as e:
        pass
    try:
        allowed = MessagesController.getInstance(int(account)).richEditorAllowed()
        premium = bool(UserConfig.getInstance(int(account)).isPremium())
    except Exception as e:
        pass
    return "ok", None


def _rich_java_name(value):
    try:
        return str(value.getClass().getName())
    except Exception:
        return ""


def _rich_encode(value, skip=()):
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float, str)):
        return value
    java_name = _rich_java_name(value)
    if not java_name:
        return None
    if java_name.startswith("["):
        length = len(value)
        if java_name == "[B":
            return {"__b": [int(value[i]) & 0xFF for i in range(length)]}
        return [_rich_encode(value[i], skip) for i in range(length)]
    if java_name.startswith("java.util.") or java_name.startswith("android.util."):
        items = _java_list(value)
        if not items:
            return None
        return [_rich_encode(item, skip) for item in items]
    return {"n": java_name, "f": _rich_encode_fields(value, skip)}


def _rich_encode_fields(obj, skip=()):
    out = {}
    try:
        from java.lang.reflect import Modifier
        cls = obj.getClass()
        while cls is not None and str(cls.getName()) != "org.telegram.tgnet.TLObject":
            simple = str(cls.getSimpleName())
            for field in cls.getDeclaredFields():
                name = str(field.getName())
                if name in RICH_SKIP_FIELDS or name in skip or name.startswith("this$"):
                    continue
                try:
                    if Modifier.isStatic(int(field.getModifiers())):
                        continue
                    field.setAccessible(True)
                    raw = field.get(obj)
                except Exception:
                    continue
                if raw is None:
                    continue
                encoded = _rich_encode(raw, skip)
                if encoded is not None:
                    out[f"{simple}.{name}"] = encoded
            cls = cls.getSuperclass()
    except Exception as e:
        pass
    return out


def _rich_find_field(obj, key):
    owner, _, name = key.rpartition(".")
    cls = obj.getClass()
    if owner:
        while cls is not None and str(cls.getName()) != "org.telegram.tgnet.TLObject":
            if str(cls.getSimpleName()) == owner:
                for field in cls.getDeclaredFields():
                    if str(field.getName()) == name:
                        field.setAccessible(True)
                        return field
            cls = cls.getSuperclass()
        return None
    cls = obj.getClass()
    while cls is not None and str(cls.getName()) != "org.telegram.tgnet.TLObject":
        for field in cls.getDeclaredFields():
            if str(field.getName()) == name:
                field.setAccessible(True)
                return field
        cls = cls.getSuperclass()
    return None


def _rich_find_field_by_type(obj, name, value):
    value_cls = _rich_java_name(value)
    if not value_cls:
        return None
    cls = obj.getClass()
    while cls is not None and str(cls.getName()) != "org.telegram.tgnet.TLObject":
        for field in cls.getDeclaredFields():
            if str(field.getName()) != name:
                continue
            try:
                field.setAccessible(True)
                if str(field.getType().getName()) == value_cls:
                    return field
            except Exception:
                continue
        cls = cls.getSuperclass()
    return None


def _rich_decode(encoded):
    if encoded is None:
        return None
    if isinstance(encoded, list):
        out = ArrayList()
        for item in encoded:
            decoded = _rich_decode(item)
            if decoded is not None:
                out.add(decoded)
        return out
    if not isinstance(encoded, dict):
        return encoded
    if "__b" in encoded:
        return _rich_byte_array(encoded.get("__b") or [])
    cls = _rich_class(str(encoded.get("n") or ""))
    if cls is None:
        return None
    try:
        obj = cls()
    except Exception as e:
        return None
    for name, value in (encoded.get("f") or {}).items():
        field = _rich_find_field(obj, name)
        if field is None:
            continue
        decoded = _rich_decode(value)
        if decoded is None:
            continue
        applied = False
        try:
            type_name = str(field.getType().getName())
            if type_name == "long":
                decoded = jlong(int(decoded))
            elif type_name == "int":
                decoded = jint(int(decoded))
            elif type_name == "boolean":
                decoded = bool(decoded)
            elif type_name == "short":
                decoded = int(decoded)
            field.set(obj, decoded)
            applied = True
        except Exception:
            applied = False
        if not applied:
            actual = _rich_decode(value)
            alternate = _rich_find_field_by_type(obj, name.rpartition(".")[-1], actual)
            if alternate is not None:
                try:
                    alternate.set(obj, actual)
                    applied = True
                except Exception as e:
                    pass
            if not applied:
                pass
    return obj


def rich_message_to_json(rich):
    if rich is None:
        return ""
    try:
        return json.dumps(_rich_encode(rich, RICH_SKIP_MEDIA_FIELDS), ensure_ascii=False)
    except Exception as e:
        return ""


def rich_message_from_json(raw):
    if not raw:
        return None
    try:
        return _rich_decode(json.loads(raw))
    except Exception as e:
        return None


def _java_list(collection):
    if collection is None:
        return []
    try:
        size = collection.size()
        return [collection.get(i) for i in range(size)]
    except Exception:
        pass
    try:
        out = []
        iterator = collection.iterator()
        while iterator.hasNext():
            out.append(iterator.next())
        return out
    except Exception:
        return []


def _iter_collection(collection):
    return _java_list(collection)


def _java_collection(value):
    if value is None:
        return ArrayList()
    if _rich_java_name(value).startswith("java.util."):
        return value
    out = ArrayList()
    for item in _java_list(value):
        out.add(item)
    return out


def _rich_call(cls_name, method, *args):
    cls = _rich_class(cls_name)
    if cls is None:
        raise RuntimeError(f"{cls_name} is unavailable")
    return getattr(cls, method)(*args)


def _rich_flatten_for_copy(rich):
    cls = _rich_class("org.telegram.ui.iv.RichEditorListView")
    if cls is None or rich is None:
        return None
    try:
        return cls.flattenForCopy(rich)
    except Exception:
        return None


def _rich_new_message(blocks, photos=None, documents=None):
    cls = _rich_class("org.telegram.tgnet.tl.TL_iv$RichMessage")
    if cls is None:
        return None
    try:
        rich = cls()
        for block in _java_list(blocks):
            rich.blocks.add(block)
        for photo in _java_list(photos):
            rich.photos.add(photo)
        for document in _java_list(documents):
            rich.documents.add(document)
        return rich
    except Exception:
        return None


def _rich_find_method(cls_name, method_name, arity):
    cls = _rich_class(cls_name)
    if cls is None:
        raise RuntimeError(f"{cls_name} is unavailable")
    for method in cls.getClass().getDeclaredMethods():
        if method.getName() != method_name:
            continue
        if arity is not None and len(method.getParameterTypes()) != arity:
            continue
        try:
            method.setAccessible(True)
        except Exception:
            pass
        return method
    raise RuntimeError(f"{cls_name}.{method_name} with {arity} args not found")


def _rich_invoke(method, args):
    from java.lang import Object as JObject
    holder = jarray(JObject)([None] * int(len(args)))
    for i in range(len(args)):
        holder[i] = args[i]
    return method.invoke(None, holder)


def rich_rows_to_html(rows):
    if rows is None:
        return ""
    try:
        count = int(rows.size())
    except Exception as e:
        return ""
    if count <= 0:
        return ""
    frm, to, s_off, e_off = jint(0), jint(count - 1), jint(0), jint(2147483647)
    try:
        from java.util import HashMap
        return str(_rich_call("org.telegram.ui.iv.RichHtml", "serialize",
                             rows, frm, to, s_off, e_off, HashMap()))
    except Exception as e:
        pass
    try:
        method = _rich_find_method("org.telegram.ui.iv.RichHtml", "serialize", 5)
        return str(_rich_invoke(method, [rows, frm, to, s_off, e_off]))
    except Exception as e:
        pass
    try:
        from java.util import HashMap
        method = _rich_find_method("org.telegram.ui.iv.RichHtml", "serialize", 6)
        return str(_rich_invoke(method, [rows, frm, to, s_off, e_off, HashMap()]))
    except Exception as e:
        pass
    return ""


def rich_blocks_to_html(blocks):
    if not blocks:
        return ""
    return rich_rows_to_html(_rich_flatten_for_copy(_rich_new_message(blocks)))


def rich_source_to_blocks(source):
    if not source:
        return None
    blocks = ArrayList()
    try:
        _rich_call("org.telegram.ui.Components.MarkdownParser", "parse", source, blocks)
    except Exception:
        return None
    if blocks.isEmpty():
        return None
    return blocks


def rich_blocks_has_media(blocks):
    for block in _java_list(blocks):
        try:
            name = block.getClass().getSimpleName()
            if name in RICH_MEDIA_BLOCKS:
                return True
            nested = getattr(block, "blocks", None)
            if nested is not None and nested.size() and rich_blocks_has_media(nested):
                return True
        except Exception:
            continue
    return False


def rich_blocks_is_extended(blocks):
    if not blocks or blocks.isEmpty():
        return False
    if rich_blocks_has_media(blocks):
        return True
    rows = _rich_flatten_for_copy(_rich_new_message(blocks))
    if rows is None:
        return False
    try:
        return bool(_rich_call("org.telegram.ui.iv.RichMessageConvert", "isLossy", rows))
    except Exception:
        return False


def rich_blocks_to_plain(blocks):
    if not blocks:
        return ""
    try:
        return str(_rich_call("org.telegram.ui.iv.RichMessageConvert", "blocksToCharSequence", blocks))
    except Exception:
        return ""


def rich_rows_to_char_sequence(rows):
    if rows is None:
        return None
    try:
        return _rich_call("org.telegram.ui.iv.RichMessageConvert", "rowsToCharSequence", rows)
    except Exception:
        return None


def rich_blocks_to_char_sequence(blocks):
    if not blocks:
        return None
    try:
        return _rich_call("org.telegram.ui.iv.RichMessageConvert", "blocksToCharSequence", blocks)
    except Exception:
        return None


def rich_rows_to_plain(rows):
    if rows is None:
        return ""
    try:
        return str(_rich_call("org.telegram.ui.iv.RichMessageConvert", "rowsToCharSequence", rows))
    except Exception:
        return ""


def rich_plain_to_entities(text, account):
    try:
        from java.lang import CharSequence as JCharSequence
        holder = jarray(JCharSequence)([text])
        mdc = MediaDataController.getInstance(account)
        return mdc.getEntities(holder, True, False)
    except Exception as e:
        return None


def rich_media_ids(collection):
    out = []
    for index, item in enumerate(_iter_collection(collection)):
        try:
            reference = []
            raw = getattr(item, "file_reference", None)
            if raw is not None:
                size = len(raw)
                for i in range(size):
                    reference.append(int(raw[i]) & 0xFF)
            entry = {
                "id": int(getattr(item, "id", 0)),
                "ah": int(getattr(item, "access_hash", 0)),
                "fr": reference,
            }
            out.append(entry)
        except Exception as e:
            continue
    if not out and collection is not None:
        pass
    return out


def _rich_byte_array(reference):
    if not reference:
        return None
    try:
        from java.lang import Byte
        signed = []
        for value in reference:
            value = int(value) & 0xFF
            signed.append(value - 256 if value > 127 else value)
        return jarray(Byte.TYPE)(signed)
    except Exception as e:
        return None


def rich_media_register(photos, documents):
    try:
        cls = _rich_class("org.telegram.ui.iv.RichMediaClipboard")
        if cls is None:
            return False
        photo_list = _java_collection(photos)
        document_list = _java_collection(documents)
        cls.set(photo_list, document_list)
        return True
    except Exception as e:
        return False


def rich_media_restore(entries, is_document=False):
    out = ArrayList()
    if not entries:
        return out
    clipboard = _rich_class("org.telegram.ui.iv.RichMediaClipboard")
    for entry in entries:
        try:
            ident = int(entry.get("id", 0))
            access_hash = int(entry.get("ah", 0))
        except Exception as e:
            continue
        if not ident:
            continue
        found = None
        if clipboard is not None:
            try:
                found = clipboard.document(ident) if is_document else clipboard.photo(ident)
            except Exception as e:
                found = None
        if found is not None:
            out.add(found)
            continue
        try:
            cls = _rich_class("org.telegram.tgnet.TLRPC$TL_document" if is_document else "org.telegram.tgnet.TLRPC$TL_photo")
            if cls is None:
                continue
            item = cls()
            item.id = jlong(ident)
            item.access_hash = jlong(access_hash)
            reference = entry.get("fr") or []
            item.file_reference = _rich_byte_array(reference)
            out.add(item)
        except Exception as e:
            continue
    return out


def rich_message_attach_media(rich, photos, documents):
    if rich is None:
        return rich
    try:
        photo_list = rich_media_restore(photos or [], False)
        document_list = rich_media_restore(documents or [], True)
        rich.photos = photo_list
        rich.documents = document_list
        rich_media_register(photo_list, document_list)
    except Exception as e:
        pass
    return rich


def rich_media_pack(collection, paths=None, is_document=False):
    out = []
    for item in _iter_collection(collection):
        try:
            encoded = _rich_encode(item)
            if not isinstance(encoded, dict) or not encoded.get("n"):
                continue
            local_path = str(getattr(item, "localPath", None) or "")
            if not local_path and paths:
                kind = "d" if is_document else "p"
                local_path = str(paths.get((kind, int(getattr(item, "id", 0) or 0)), "") or "")
            out.append({"tl": encoded, "path": local_path})
        except Exception as e:
            pass
    return out


def rich_media_decode_entries(entries):
    out = ArrayList()
    if not entries:
        return out
    for entry in entries:
        try:
            encoded = entry.get("tl") if isinstance(entry, dict) else None
            if not isinstance(encoded, dict):
                continue
            obj = _rich_decode(encoded)
            if obj is not None:
                out.add(obj)
        except Exception as e:
            pass
    return out


def rich_media_fill_missing(objects, manifest, is_document):
    try:
        have = set()
        for obj in _iter_collection(objects):
            try:
                have.add(int(getattr(obj, "id", 0) or 0))
            except Exception:
                continue
        missing = []
        for entry in manifest or []:
            try:
                ident = int(entry.get("id", 0))
            except Exception:
                continue
            if ident and ident not in have:
                missing.append(entry)
        if missing:
            for obj in _iter_collection(rich_media_restore(missing, is_document)):
                objects.add(obj)
    except Exception as e:
        pass
    return objects


def _rich_media_loader(account):
    return FileLoader.getInstance(int(account))


def _rich_media_candidates(obj, account, hint_path=None):
    out = []
    if hint_path:
        try:
            out.append(File(str(hint_path)))
        except Exception:
            pass
    try:
        local_path = getattr(obj, "localPath", None)
        if local_path:
            out.append(File(str(local_path)))
    except Exception:
        pass
    loader = None
    try:
        loader = _rich_media_loader(account)
        target = loader.getPathToAttach(obj)
        if target is not None:
            out.append(target)
    except Exception as e:
        pass
    try:
        sizes = getattr(obj, "sizes", None)
        if loader is not None and sizes is not None:
            for size in reversed(_java_list(sizes)):
                try:
                    target = loader.getPathToAttach(size)
                    if target is not None:
                        out.append(target)
                except Exception:
                    continue
    except Exception:
        pass
    return out


def rich_media_local_file(obj, account, hint_path=None):
    for candidate in _rich_media_candidates(obj, account, hint_path):
        try:
            if candidate.exists() and candidate.isFile() and int(candidate.length()) > 0:
                return candidate
        except Exception:
            continue
    return None


def _rich_media_size_hint(obj, is_document):
    try:
        if is_document:
            return int(getattr(obj, "size", 0) or 0)
        sizes = getattr(obj, "sizes", None)
        if sizes is not None:
            for size in reversed(_java_list(sizes)):
                value = int(getattr(size, "size", 0) or 0)
                if value > 0:
                    return value
    except Exception:
        pass
    return 0


def _rich_media_download(obj, account, is_document, target, timeout):
    try:
        loader = _rich_media_loader(account)
        if is_document:
            loader.loadFile(obj, None, jint(1), jint(0))
        else:
            sizes = getattr(obj, "sizes", None)
            size = FileLoader.getClosestPhotoSizeWithSize(sizes, AndroidUtilities.getPhotoSize(True))
            if size is None:
                return None
            location = ImageLocation.getForPhoto(size, obj)
            if location is None:
                return None
            loader.loadFile(location, None, "jpg", jint(1), jint(0))
    except Exception as e:
        return None
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            if target.exists() and int(target.length()) > 0:
                return target
        except Exception:
            pass
        time.sleep(RICH_MEDIA_DOWNLOAD_POLL)
    try:
        pass
    except Exception:
        pass
    return None


def _rich_media_read_base64(target):
    try:
        if int(target.length()) <= 0:
            return None
        stream = FileInputStream(target)
        parts = []
        try:
            buffer = _rich_byte_array([0] * RICH_MEDIA_CHUNK)
            while True:
                count = stream.read(buffer, 0, RICH_MEDIA_CHUNK)
                if count is None or int(count) <= 0:
                    break
                parts.append(str(Base64.encodeToString(buffer, 0, int(count), Base64.NO_WRAP)))
        finally:
            stream.close()
        data = "".join(parts)
        return data
    except Exception as e:
        return None


def rich_media_embed_file(obj, account, hint_path=None, is_document=None, allow_download=True):
    if is_document is None:
        is_document = getattr(obj, "mime_type", None) is not None
    target = rich_media_local_file(obj, account, hint_path)
    if target is None and allow_download:
        download_target = _rich_media_download_target(obj, account)
        if download_target is not None:
            size_hint = _rich_media_size_hint(obj, is_document)
            timeout = RICH_MEDIA_DOWNLOAD_MAX_TIMEOUT
            if size_hint > 0:
                timeout = min(RICH_MEDIA_DOWNLOAD_MAX_TIMEOUT, max(RICH_MEDIA_DOWNLOAD_MIN_TIMEOUT, int(size_hint / (256 * 1024)) * 10))
            target = _rich_media_download(obj, account, is_document, download_target, timeout)
    if target is None:
        return None
    data = _rich_media_read_base64(target)
    if not data:
        return None
    info = {"b64": data, "size": int(target.length()), "name": str(target.getName() or "")}
    try:
        if is_document:
            name = FileLoader.getDocumentFileName(obj)
            if name:
                info["name"] = str(name)
            info["mime"] = str(getattr(obj, "mime_type", "") or "")
        else:
            info["mime"] = "image/jpeg"
    except Exception:
        pass
    return info


def _rich_media_download_target(obj, account):
    try:
        loader = _rich_media_loader(account)
    except Exception as e:
        return None
    try:
        obj.localPath = None
    except Exception:
        pass
    try:
        target = loader.getPathToAttach(obj)
        path = str(target.getPath() or "") if target is not None else ""
        if not path:
            return None
        return target
    except Exception as e:
        return None


def rich_media_write_file(obj, b64, account, is_document=None):
    if not b64:
        return None
    if is_document is None:
        is_document = getattr(obj, "mime_type", None) is not None
    try:
        loader = _rich_media_loader(account)
    except Exception as e:
        return None
    try:
        obj.localPath = None
    except Exception:
        pass
    try:
        target = loader.getPathToAttach(obj)
        path_str = str(target.getPath() or "") if target is not None else ""
    except Exception as e:
        return None
    if not path_str:
        return None
    try:
        data = Base64.decode(str(b64), Base64.DEFAULT)
        parent = target.getParentFile()
        if parent is not None and not parent.exists():
            parent.mkdirs()
        stream = FileOutputStream(target)
        try:
            stream.write(data)
        finally:
            stream.close()
    except Exception as e:
        return None
    if is_document:
        try:
            obj.localPath = path_str
            loader.setLocalPathTo(obj, path_str)
        except Exception as e:
            pass
    else:
        try:
            sizes = getattr(obj, "sizes", None)
            size = FileLoader.getClosestPhotoSizeWithSize(sizes, AndroidUtilities.getPhotoSize(True))
            if size is not None:
                loader.setLocalPathTo(size, path_str)
        except Exception as e:
            pass
    try:
        pass
    except Exception:
        pass
    return path_str


def entities_to_json(entities):
    out = []
    for entity in _iter_collection(entities):
        try:
            item = {
                "c": entity.getClass().getSimpleName(),
                "o": int(entity.offset),
                "l": int(entity.length),
            }
            url = getattr(entity, "url", None)
            if url:
                item["u"] = str(url)
            user_id = getattr(entity, "user_id", None)
            if user_id:
                item["uid"] = int(user_id)
            document_id = getattr(entity, "document_id", None)
            if document_id:
                item["did"] = int(document_id)
            language = getattr(entity, "language", None)
            if language:
                item["lang"] = str(language)
            out.append(item)
        except Exception:
            continue
    return out


def entities_from_json(items):
    out = ArrayList()
    if not items:
        return out
    for item in items:
        try:
            cls = jclass(f"org.telegram.tgnet.TLRPC${item.get('c')}")
            entity = cls()
            entity.offset = jint(int(item.get("o", 0)))
            entity.length = jint(int(item.get("l", 0)))
            if item.get("u"):
                entity.url = str(item["u"])
            if item.get("uid"):
                entity.user_id = jlong(int(item["uid"]))
            if item.get("did"):
                entity.document_id = jlong(int(item["did"]))
            if item.get("lang"):
                entity.language = str(item["lang"])
            out.add(entity)
        except Exception:
            continue
    return out


def normalize_template_text(value):
    return re.sub(r'[ \t]+', ' ', value or "").strip()


def rich_source_roundtrips(source, expected_text):
    blocks = rich_source_to_blocks(source)
    if not blocks:
        return False
    if not expected_text:
        return True
    return normalize_template_text(rich_blocks_to_plain(blocks)) == normalize_template_text(expected_text)


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
                text = None
                text_key = entry.get("text_key")
                if text_key:
                    try:
                        resolved = t(text_key, lang=self.plugin._lang())
                        text = None if resolved == text_key else resolved
                    except Exception:
                        text = None
                if not text:
                    text = entry.get("text_ru") or entry.get("text_en", "")
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

_EMBEDDED_CONFIG = {
    "deeplinks": [
        {"deeplink": "tg://vestr", "target": "https://t.me/mr_Vestr?profile"},
        {"deeplink": "tg://vestr?direct", "target": "https://t.me/mr_Vestr?direct"},
        {"deeplink": "tg://vestr?channel", "target": "https://t.me/i_am_vestr"},
        {"deeplink": "tg://vestr?github", "target": "https://github.com/mr-Vestr"},
        {"deeplink": "tg://vestr?support", "target": "gifts_2037728749"},
    ],
    "badges": [
        {"chat_id": 3682773171, "emoji_id": 5208665577555512622, "text_key": "badge_meta_chat"},
        {"chat_id": 2693931764, "emoji_id": 5208665577555512622, "text_key": "badge_meta_channel"},
        {"user_id": 2037728749, "emoji_id": 5208665577555512622, "text_key": "badge_vestr_user"},
    ],
}

_SAFE_RIPPLE_CLS = None
_SAFE_RIPPLE_LOOKED_UP = False


def _safe_ripple_class():
    global _SAFE_RIPPLE_CLS, _SAFE_RIPPLE_LOOKED_UP
    if not _SAFE_RIPPLE_LOOKED_UP:
        _SAFE_RIPPLE_LOOKED_UP = True
        try:
            _SAFE_RIPPLE_CLS = find_class("org.telegram.ui.Cells.BaseCell$RippleDrawableSafe")
        except Exception:
            _SAFE_RIPPLE_CLS = None
    return _SAFE_RIPPLE_CLS


def _safe_ripple(color_state_list, content, mask):
    cls = _safe_ripple_class()
    if cls is not None:
        try:
            return cls(color_state_list, content, mask)
        except Exception:
            pass
    try:
        return RippleDrawable(color_state_list, content, mask)
    except Exception:
        return content


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
        self.menu_shown = False
        self._header_sticker_loaded = False
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
        self._picker_sessions = {}
        self._picker_token_seq = 0
        self._picker_hooks_ready = False
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

    def _is_sticker_ready(self, img):
        try:
            if img.getBitmap() is not None:
                return True
        except Exception:
            pass
        try:
            if img.getDrawable() is not None:
                return True
        except Exception:
            pass
        try:
            if self._get_private_field(img, "bitmap") is not None:
                return True
        except Exception:
            pass
        try:
            receiver = self._get_private_field(img, "imageReceiver")
            if receiver is not None and receiver.getBitmap() is not None:
                return True
            if receiver is not None and receiver.getDrawable() is not None:
                return True
        except Exception:
            pass
        return False

    def _animate_sticker_in(self, img, animate=True):
        if not animate:
            try:
                img.animate().cancel()
            except Exception:
                pass
            try:
                img.setAlpha(1.0); img.setScaleX(1.0); img.setScaleY(1.0)
                img.setTranslationX(0.0); img.setTranslationY(0.0)
            except Exception:
                pass
            return
        try:
            img.animate().cancel()
            img.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationX(0.0).translationY(0.0).setDuration(300).start()
        except Exception:
            try:
                img.animate().cancel()
                img.setAlpha(1.0); img.setScaleX(1.0); img.setScaleY(1.0)
                img.setTranslationX(0.0); img.setTranslationY(0.0)
            except Exception:
                pass

    def load_sticker_with_fallback(self, img, sticker_name, sticker_index=0, size="72_72", grace=1200, interval=40, max_wait=15000, animate=True):
        try:
            img.animate().cancel()
            img.setAlpha(0.0)
            if animate:
                img.setScaleX(0.8)
                img.setScaleY(0.8)
            else:
                img.setScaleX(1.0)
                img.setScaleY(1.0)
        except Exception:
            pass
        try:
            bound = bool(self.try_load_sticker(img, sticker_name, sticker_index, size))
        except Exception:
            bound = False
        if bound and self._is_sticker_ready(img):
            self._animate_sticker_in(img, animate=False)
            return
        try:
            sname = sticker_name.split("/")[0] if isinstance(sticker_name, str) and "/" in sticker_name else sticker_name
        except Exception:
            sname = sticker_name
        state = {'bound': bound, 'requested': False, 'done': False}

        def step(waited=0, total=0):
            if state['done']:
                return
            if not state['bound']:
                try:
                    if self.try_load_sticker(img, sticker_name, sticker_index, size):
                        state['bound'] = True
                        waited = 0
                except Exception:
                    pass
                if not state['bound'] and not state['requested']:
                    state['requested'] = True
                    try:
                        MediaDataController.getInstance(0).loadStickersByEmojiOrName(sname, False, False)
                    except Exception:
                        pass
            if state['bound'] and self._is_sticker_ready(img):
                state['done'] = True
                self._animate_sticker_in(img, animate and total > 120)
                return
            if total >= max_wait:
                state['done'] = True
                self._animate_sticker_in(img, animate)
                return
            try:
                run_on_ui_thread(lambda: step(waited + interval, total + interval), interval)
            except Exception:
                pass
        try:
            run_on_ui_thread(lambda: step(0, 0), 0)
        except Exception:
            pass

    def on_plugin_load(self):
        self._badge_manager = BadgeManager(self)
        self._setup_deeplink_hook()
        self._apply_embedded_config()
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
        self._rich_capture_index = None
        self._rich_capture_pending = False
        self._rich_editor_ref = None
        self._rich_editor_open = False
        self._rich_editor_opening = False
        self._rich_editor_opened_at = 0
        self._rich_self_sending = False
        for key in RICH_HOOK_STATE:
            RICH_HOOK_STATE[key] = False
        self._add_rich_editor_send_hook()
        self._add_url_hook()
        self._add_input_hook()
        self._add_document_hook()
        self._hook_chat_activity_resume()
        self._force_load_stickers()
        self._setup_templates_view_search()
        self._setup_settings_header_hook()
        self._setup_picker_multi_select_hooks()
        try:
            if not hasattr(self, '_promo_hook_refs'):
                self._promo_hook_refs = []
            if not hasattr(self, '_promo_check_state'):
                self._promo_check_state = None
            if not hasattr(self, '_promo_cell_active'):
                self._promo_cell_active = False
            self._setup_channel_promo_hook()
            if not getattr(self, '_promo_check_started', False):
                self._promo_check_started = True
                threading.Thread(target=self._channel_promo_check, daemon=True).start()
        except Exception:
            pass
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
        for session in list(self._picker_sessions.values()):
            session["confirm"] = None
            session["hint"] = None
        self._picker_sessions.clear()
        self._rich_capture_index = None
        self._rich_capture_pending = False
        self._rich_editor_ref = None
        self._rich_editor_open = False
        self._rich_editor_opening = False
        self._rich_editor_opened_at = 0
        self._rich_self_sending = False
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
        for ref in getattr(self, '_promo_hook_refs', []):
            try:
                self.unhook_method(ref)
            except Exception:
                pass
        self._promo_hook_refs = []
        self._promo_cell_active = False

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
                asSubItemMethod = item_java_class.getDeclaredMethod("asSubItem", Integer.TYPE, Integer.TYPE, jclass("android.graphics.drawable.Drawable"), jclass("java.lang.CharSequence"), Boolean.TYPE, Boolean.TYPE)
                asSubItemMethod.setAccessible(True)
                our_item = asSubItemMethod.invoke(None, Integer(self.templates_menu_id), Integer(icon_id), None, t('templates', lang=self.lang), Boolean(True), Boolean(False))
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
        try:
            frag = get_last_fragment()
            act = frag.getParentActivity() if frag else None
            if act:
                Browser.openUrl(act, "tg://resolve?domain=I_am_Vestr")
                return
        except Exception:
            pass
        try:
            run_on_ui_thread(lambda: get_messages_controller().openByUserName("I_am_Vestr", get_last_fragment(), 1))
        except Exception:
            pass

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
        try:
            PluginsController.getInstance().reloadPlugin(self.id)
        except Exception as e:
            BulletinHelper.show_error(t('restart_error', lang=self.lang, error=str(e)))

    def _show_how_it_works(self, _):
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return

        def on_close(v=None):
            try:
                sheet.dismiss()
            except Exception:
                pass

        def on_channel(v=None):
            try:
                sheet.dismiss()
                self._open_channel_link(None)
            except Exception:
                pass

        def on_personal(v=None):
            try:
                sheet.dismiss()
                self._open_personal_link(None)
            except Exception:
                pass

        def on_open_doc(v=None):
            try:
                if self._get_effective_lang() == 'ru':
                    doc_url = 'https://github.com/mr-Vestr/plugins/blob/main/Templates/TEMPLATES_RU.md'
                else:
                    doc_url = 'https://github.com/mr-Vestr/plugins/blob/main/Templates/TEMPLATES_EN.md'
                uri = Uri.parse(doc_url)
                Browser.openUrl(act, uri, True, True, True, None, None, True, True, True)
            except Exception:
                pass

        sheet, outer, subtitle_tv = self._picker_sheet_container(
            act, frag, t('how_it_works', lang=self.lang), '')
        dark_container, dark_lp = self._picker_body_block(
            act, t('how_it_works_text', lang=self.lang), max_height_dp=380)
        outer.addView(dark_container, dark_lp)
        pills = [
            self._picker_icon_pill(act, 'msg_channel', t('channel', lang=self.lang), on_channel),
            self._picker_icon_pill(act, 'msg_contacts', t('personal', lang=self.lang), on_personal),
            self._picker_icon_pill(act, 'msg_openin', '', on_open_doc),
        ]
        options_wrap, center_options_row = self._picker_options_row(act, pills)
        outer.addView(options_wrap, LayoutHelper.createLinear(-1, -2, PICKER_PAD_H, AndroidUtilities.dp(6), PICKER_PAD_H, AndroidUtilities.dp(2)))
        outer.addView(self._picker_button(act, t('close', lang=self.lang), on_close), LayoutHelper.createLinear(-1, -2, PICKER_BUTTON_PAD_H, PICKER_BUTTON_TOP_PAD, PICKER_BUTTON_PAD_H, 16))
        self._picker_show_animated(sheet, outer)
        try:
            options_wrap.post(center_options_row)
        except Exception:
            pass
        return sheet

    def _show_version_dialog(self, _):
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return

        def on_check(v=None):
            try:
                sheet.dismiss()
            except Exception:
                pass
            try:
                Browser.openUrl(act, "tg://resolve?domain=I_am_Vestr&post=13")
            except Exception:
                try:
                    Browser.openUrl(act, Uri.parse("https://t.me/I_am_Vestr/13"), True, True, True, None, None, False, False, False)
                except Exception:
                    pass

        sheet, outer, subtitle_tv = self._picker_sheet_container(
            act, frag, t('current_version', lang=self.lang, version=__version__), '', ("mr_vestr/1", 1))
        updates_text = t('updates_info', lang=self.lang)
        spannable = SpannableString(updates_text)
        username = "@I_am_Vestr"
        start_pos = updates_text.find(username)
        if start_pos != -1:
            end_pos = start_pos + len(username)
            spannable.setSpan(URLSpan("https://t.me/i_am_vestr"), start_pos, end_pos, SpannableString.SPAN_EXCLUSIVE_EXCLUSIVE)
        dark_container, dark_lp = self._picker_body_block(act, spannable, max_height_dp=300, gravity=Gravity.CENTER, link_color=Theme.key_dialogTextBlue, keep_scroll=False)
        outer.addView(dark_container, dark_lp)
        outer.addView(self._picker_button(act, t('check_updates', lang=self.lang), on_check), LayoutHelper.createLinear(-1, -2, PICKER_BUTTON_PAD_H, PICKER_BUTTON_TOP_PAD, PICKER_BUTTON_PAD_H, 16))
        self._picker_show_animated(sheet, outer)
        return sheet

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
        except Exception:
            pass
        try:
            PluginsController.getInstance().loadPluginSettings(str(self.id))
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
                    pass
            main_layout = LinearLayout(context)
            main_layout.setOrientation(LinearLayout.VERTICAL)
            main_layout.setGravity(Gravity.CENTER)
            try:
                main_layout.setBackgroundColor(Color.TRANSPARENT)
            except Exception:
                pass
            main_layout.setPadding( AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20))
            imageView = BackupImageView(context)
            imageView.setRoundRadius(AndroidUtilities.dp(45))
            header_animate = not getattr(self, '_header_sticker_loaded', False)
            self._header_sticker_loaded = True
            self.load_sticker_with_fallback(imageView, __icon__, 0, "130_130", animate=header_animate)
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
                method = PSA.getClass().getDeclaredMethod( "fillItems", find_class("java.util.ArrayList"), find_class("org.telegram.ui.Components.UniversalAdapter"))
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
                        pass

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
                                pass
                        run_on_ui_thread(open)
                    except Exception as e:
                        pass
            try:
                fill_method = SA.getClass().getDeclaredMethod("fillItems", ArrayList, UniversalAdapter)
                fill_method.setAccessible(True)
                self._settings_activity_hooks.append(self.hook_method(fill_method, FillItemsHook()))
            except Exception as e:
                pass
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
                pass
        except Exception as e:
            pass


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
        self._migrate_legacy_templates()
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
                settings.append(Text(
                    text=self._t('text'),
                    icon="msg_photo_text2",
                    accent=False,
                    on_click=lambda ctx, idx=i: self._open_template_rich_editor(idx),
                    on_long_click=(lambda idx=i: (lambda v: self._on_input_long_click(idx, 'text', v)))()
                ))
                settings.append(Switch(
                    key=f"template_linkpreview_{i}",
                    text=self._t('link_preview'),
                    icon='msg_link2',
                    default=self.get_setting(f"template_linkpreview_{i}", True),
                    link_alias=f"template_linkpreview_{i}"
                ))
                settings.append(Text(
                    text=self._t('send_template'),
                    icon='msg_send',
                    accent=True,
                    on_click=lambda ctx, idx=i: self._send_template_by_index(idx)
                ))
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
            Header(text=self._t('rich_editor_settings_section')),
            Switch(
                key='rich_exit_confirm',
                text=self._t('rich_exit_confirm'),
                subtext=self._t('rich_exit_confirm_sub'),
                default=self.get_setting('rich_exit_confirm', True),
                link_alias='rich_exit_confirm'
            ),
            Switch(
                key='rich_premium_unlock',
                text=self._t('rich_premium_unlock'),
                subtext=self._t('rich_premium_unlock_sub'),
                default=self.get_setting('rich_premium_unlock', True),
                link_alias='rich_premium_unlock'
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
            Text(
                text=self._t('plugin_language'),
                icon='msg_language',
                on_click=self._show_language_sheet,
                link_alias='plugin_language'
            ),
        ]

    def _apply_embedded_config(self):
        try:
            self._deeplinks = {
                e["deeplink"]: e["target"]
                for e in _EMBEDDED_CONFIG.get("deeplinks", [])
                if e.get("deeplink") and e.get("target")
            }
        except Exception:
            pass
        try:
            badges = _EMBEDDED_CONFIG.get("badges", [])
            if self._badge_manager:
                run_on_ui_thread(lambda: self._badge_manager.setup(badges))
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
            if field == 'text':
                self._compile_template_payload(idx, val)
            self.set_setting("templates", self.templates, reload_settings=True)
            run_on_ui_thread(self._update_visible_rows)
        return handler


    def _is_ui_thread(self):
        try:
            from android.os import Looper
            return Looper.myLooper() == Looper.getMainLooper()
        except Exception as e:
            return True

    def _account_number(self):
        try:
            frag = get_last_fragment()
            if frag is not None and hasattr(frag, 'getCurrentAccount'):
                num = int(frag.getCurrentAccount())
                if num >= 0:
                    return num
        except Exception:
            pass
        try:
            account = get_account_instance()
            if account is not None and hasattr(account, 'accountNum'):
                return int(account.accountNum)
        except Exception:
            pass
        return 0

    def _read_rich_setting(self, idx):
        raw = self.get_setting(f"template_rich_{idx}", "")
        if not raw:
            return None
        try:
            data = json.loads(raw)
        except Exception:
            return None
        return data if isinstance(data, dict) else None

    def _write_rich_setting(self, idx, payload):
        try:
            if not payload:
                self.set_setting(f"template_rich_{idx}", "")
                return
            self.set_setting(f"template_rich_{idx}", json.dumps(payload, ensure_ascii=False))
        except Exception:
            pass

    def _compile_template_payload(self, idx, source):
        payload = {
            "text": source or "",
            "src": source or "",
            "entities": [],
            "source": source or "",
            "extended": False,
            "photos": [],
            "documents": [],
            "rich_ok": False,
        }
        if not source or not source.strip():
            if self.get_setting(f"template_rich_{idx}", ""):
                self._write_rich_setting(idx, payload)
            return payload
        try:
            parsed = parse_markdown(preprocess_template_markdown(source))
            payload["text"] = str(parsed.text)
            payload["entities"] = entities_to_json([ent.to_tlrpc_object() for ent in parsed.entities])
        except Exception:
            pass
        if rich_editor_supported():
            try:
                blocks = rich_source_to_blocks(source)
                if blocks:
                    html = rich_blocks_to_html(blocks)
                    plain = rich_blocks_to_plain(blocks)
                    extended = rich_blocks_is_extended(blocks)
                    if html:
                        payload["source"] = html
                        payload["extended"] = extended
                        payload["rich_ok"] = rich_source_roundtrips(html, plain)
                        if extended and plain:
                            payload["text"] = plain
            except Exception:
                pass
        self._write_rich_setting(idx, payload)
        return payload

    def _migrate_legacy_templates(self):
        try:
            if self.get_setting("templates_rich_version", 0) == RICH_PAYLOAD_VERSION:
                return
            changed = 0
            for i in range(self._get_created_count()):
                text = self.get_setting(f"template_text_{i}", "")
                if not text or not text.strip():
                    continue
                payload = self._read_rich_setting(i)
                if payload is not None and not self._payload_is_broken(payload):
                    continue
                self._compile_template_payload(i, text)
                changed += 1
            self.set_setting("templates_rich_version", RICH_PAYLOAD_VERSION)
            self.set_setting("templates_rich_migrated", True)
            if changed:
                run_on_ui_thread(self._update_visible_rows)
        except Exception as e:
            pass

    def _payload_is_broken(self, payload):
        try:
            if payload.get("v") == RICH_PAYLOAD_VERSION:
                return bool(payload.get("extended")) and not payload.get("blob")
            return bool(payload.get("extended")) and not payload.get("source")
        except Exception:
            return True

    def _template_payload(self, idx, source=None):
        if source is None:
            source = self.get_setting(f"template_text_{idx}", "")
        source = str(source or "")
        payload = self._read_rich_setting(idx)
        if payload is not None and self._payload_is_broken(payload):
            payload = None
        if payload is not None and str(payload.get("src") or "").strip() != source.strip():
            if str(payload.get("text") or "").strip() == source.strip():
                payload["src"] = source
                self._write_rich_setting(idx, payload)
            else:
                payload = None
        if payload is None:
            payload = self._compile_template_payload(idx, source)
        return payload or {"v": RICH_PAYLOAD_VERSION, "text": source, "entities": [],
                           "extended": False, "source": source, "blob": "",
                           "photos": [], "documents": [], "rich_ok": False}

    def _payload_text_and_entities(self, payload):
        text = str((payload or {}).get("text") or "")
        return text, entities_from_json((payload or {}).get("entities") or [])

    def _restore_payload_media(self, payload):
        payload = payload if isinstance(payload, dict) else {}
        media = payload.get("media")
        photos = ArrayList()
        documents = ArrayList()
        if isinstance(media, dict):
            photos = rich_media_decode_entries(media.get("photos"))
            documents = rich_media_decode_entries(media.get("documents"))
        photos = rich_media_fill_missing(photos, payload.get("photos") or [], False)
        documents = rich_media_fill_missing(documents, payload.get("documents") or [], True)
        rich_media_register(photos, documents)
        return photos, documents

    def _payload_rich_message(self, payload):
        blob = (payload or {}).get("blob") or ""
        if not blob:
            return None
        rich = rich_message_from_json(blob)
        if rich is None:
            return None
        photos, documents = self._restore_payload_media(payload)
        rich.photos = photos
        rich.documents = documents
        return rich

    def _payload_rich_blocks(self, payload, account=None):
        if not payload or not payload.get("extended"):
            return None, None, None
        rich = self._payload_rich_message(payload)
        if rich is not None:
            return rich.blocks, rich.photos, rich.documents
        source = payload.get("source") or ""
        if not source:
            return None, None, None
        try:
            blocks = rich_source_to_blocks(source)
        except Exception:
            blocks = None
        if not blocks:
            return None, None, None
        photos, documents = self._restore_payload_media(payload)
        return blocks, photos, documents

    def _rich_sending_allowed(self, account):
        try:
            controller = MessagesController.getInstance(int(account))
            if hasattr(controller, "richEditorAllowed") and controller.richEditorAllowed():
                return True
            return bool(UserConfig.getInstance(int(account)).isPremium())
        except Exception as e:
            return True

    def _send_rich_payload(self, account, dialog_id, payload, reply_to=None, reply_to_top=None):
        blocks, photos, documents = self._payload_rich_blocks(payload, account)
        if not blocks:
            return False
        if not self._rich_sending_allowed(account):
            return False

        def _do():
            self._rich_self_sending = True
            try:
                instance_cls = find_class("org.telegram.messenger.AccountInstance")
                helper_cls = find_class("org.telegram.messenger.SendMessagesHelper")
                account_instance = instance_cls.getInstance(int(account))
                helper_cls.prepareSendingArticle(account_instance, blocks, photos, documents, None, False, jlong(int(dialog_id)), reply_to, reply_to_top, True, jint(0), jint(0), None, jlong(0), jlong(0), jlong(0))
            except Exception as e:
                pass
            finally:
                self._rich_self_sending = False

        if not self._is_ui_thread():
            run_on_ui_thread(_do)
            return True
        _do()
        return True

    def _on_input_long_click(self, idx, field, view):
        try:
            run_on_ui_thread(lambda: self._show_long_click_popup(idx, field, view))
        except Exception:
            pass

    def _resolve_long_click_anchor(self, fragment, anchor_view):
        anchor = anchor_view
        try:
            if anchor is not None and not isinstance(anchor, View):
                anchor = None
        except Exception:
            pass
        if anchor is None:
            try:
                anchor = fragment.getListView()
            except Exception:
                anchor = None
        return anchor

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
                        pass

            options = ItemOptions.makeOptions(fragment, self._resolve_long_click_anchor(fragment, anchor_view))
            
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
                            if field == 'text':
                                self.set_setting(f"template_rich_{idx}", "")
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
            pass

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
            old_count = self._get_created_count()
            if old_count > 0:
                last_idx = old_count - 1
                last_tpl = self.templates[last_idx] if last_idx < len(self.templates) else {}
                if not last_tpl.get("name") or not last_tpl.get("text"):
                    run_on_ui_thread(lambda: BulletinHelper.show_error(t('fill_prev_template', lang=self.lang)))
                    return
            new_count = min(old_count + 1, TEMPLATE_COUNT)
            if new_count > old_count:
                new_idx = new_count - 1
                self.set_setting(f"template_name_{new_idx}", "")
                self.set_setting(f"template_text_{new_idx}", "")
                self.set_setting(f"template_rich_{new_idx}", "")
                self.set_setting(f"template_linkpreview_{new_idx}", True)
            if old_count == 0:
                self.set_setting('templates_visible', True, reload_settings=False)
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
        if not isinstance(count, int) or count < 0:
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
                    old_rich = [self.get_setting(f"template_rich_{i}", "") for i in range(TEMPLATE_COUNT)]
                    old_linkpreview = [self.get_setting(f"template_linkpreview_{i}", True) for i in range(TEMPLATE_COUNT)]
                    current_count = self._get_created_count()
                    if current_count <= 1:
                        self.templates[0] = {"name": "", "text": "", "enabled": False}
                        self.set_setting("template_name_0", "")
                        self.set_setting("template_text_0", "")
                        self.set_setting("template_rich_0", "")
                        self.set_setting("template_linkpreview_0", True)
                        self.set_setting("templates_created_count", 0)
                    else:
                        if idx < current_count - 1:
                            for i in range(idx, current_count - 1):
                                self.templates[i] = dict(self.templates[i + 1])
                                self.templates[i]['enabled'] = bool(self.templates[i].get('name', '') and self.templates[i].get('text', ''))
                                self.set_setting(f"template_name_{i}", self.templates[i].get("name", ""))
                                self.set_setting(f"template_text_{i}", self.templates[i].get("text", ""))
                                self.set_setting(f"template_rich_{i}", self.get_setting(f"template_rich_{i + 1}", ""))
                                self.set_setting(f"template_linkpreview_{i}", self.get_setting(f"template_linkpreview_{i + 1}", True))
                        last_created = current_count - 1
                        self.templates[last_created] = {"name": "", "text": "", "enabled": False}
                        self.set_setting(f"template_name_{last_created}", "")
                        self.set_setting(f"template_text_{last_created}", "")
                        self.set_setting(f"template_rich_{last_created}", "")
                        self.set_setting(f"template_linkpreview_{last_created}", True)
                        self.set_setting("templates_created_count", current_count - 1)
                    self.set_setting("templates", self.templates, reload_settings=False)
                    self.set_setting('templates_visible', True, reload_settings=True)
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
                                self.set_setting(f"template_rich_{i}", old_rich[i])
                                self.set_setting(f"template_linkpreview_{i}", old_linkpreview[i])
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

    def _open_main_dialogs(self):
        try:
            frag = get_last_fragment()
            if frag is None:
                return
            if frag.getParentLayout() is None:
                raise AttributeError("no parent layout")
            frag.presentFragment(DialogsActivity(Bundle()))
        except Exception:
            try:
                frag = get_last_fragment()
                act = frag.getParentActivity() if frag else None
                if act is not None and Browser is not None:
                    Browser.openUrl(act, "tg://")
            except Exception:
                pass

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
                            Browser.openUrl(fragment.getParentActivity(), f"tg://resolve?domain={username}")
                        elif isinstance(did, int) and did > 0:
                            Browser.openUrl(fragment.getParentActivity(), f"tg://user?id={did}")
                        else:
                            if isinstance(did, int):
                                Browser.openUrl(fragment.getParentActivity(), f"tg://resolve?domain={abs(did)}")
                            else:
                                Browser.openUrl(fragment.getParentActivity(), f"tg://resolve?domain={did}")
                    except Exception:
                        pass
            run_on_ui_thread(_open)
        except Exception:
            pass


    def _add_rich_editor_send_hook(self):
        plugin = self

        class RichSendHandler(MethodHook):
            def __init__(self):
                MethodHook.__init__(self)

            def before_hooked_method(self, param):
                try:
                    idx = getattr(plugin, "_rich_capture_index", None)
                    if idx is None or not getattr(plugin, "_rich_capture_pending", False):
                        return
                    if getattr(plugin, "_rich_self_sending", False):
                        return
                    if not plugin._rich_editor_session_alive():
                        return
                    args = param.args
                    blocks = args[1]
                    photos = args[2]
                    documents = args[3]
                    captured = ArrayList()
                    for block in _java_list(blocks):
                        captured.add(block)
                    blocks.clear()
                    plugin._rich_capture_pending = False
                    plugin._save_rich_editor_result(idx, captured, photos, documents)
                except Exception as e:
                    try:
                        plugin._rich_capture_pending = False
                    except Exception:
                        pass

        class RichDowngradeHandler(MethodHook):
            def __init__(self):
                MethodHook.__init__(self)

            def before_hooked_method(self, param):
                try:
                    idx = getattr(plugin, "_rich_capture_index", None)
                    if idx is None or not getattr(plugin, "_rich_capture_pending", False):
                        return
                    if not plugin._rich_editor_active():
                        return
                    args = param.args
                    plugin._rich_capture_pending = False
                    plugin._save_downgraded_rich_result(idx, args[0])
                except Exception as e:
                    try:
                        plugin._rich_capture_pending = False
                    except Exception:
                        pass
        try:
            helper_cls = find_class("org.telegram.messenger.SendMessagesHelper")
            if helper_cls:
                for method in helper_cls.getClass().getDeclaredMethods():
                    if method.getName() != "prepareSendingArticle":
                        continue
                    if len(method.getParameterTypes()) != 16:
                        continue
                    self.hook_method(method, RichSendHandler(), 0)
                    RICH_HOOK_STATE["prepareSendingArticle"] = True
                    break
        except Exception as e:
            pass
        try:
            enter_cls = find_class("org.telegram.ui.Components.ChatActivityEnterView")
            if enter_cls:
                for method in enter_cls.getClass().getDeclaredMethods():
                    if method.getName() != "sendConvertedRichAsSimple":
                        continue
                    if len(method.getParameterTypes()) != 4:
                        continue
                    self.hook_method(method, RichDowngradeHandler(), 0)
                    RICH_HOOK_STATE["sendConvertedRichAsSimple"] = True
                    break
        except Exception as e:
            pass
        self._add_premium_bypass_hooks()

    def _add_premium_bypass_hooks(self):
        plugin = self

        class BypassHandler(MethodHook):
            def before_hooked_method(self, param):
                try:
                    if not plugin.get_setting('rich_premium_unlock', True):
                        return
                    if not plugin._rich_editor_active():
                        return
                    param.setResult(True)
                except Exception as e:
                    pass

        class DraftSuppressHandler(MethodHook):
            def before_hooked_method(self, param):
                try:
                    if not plugin._rich_editor_active():
                        return
                    if len(param.args) < 11:
                        return
                    param.setResult(None)
                except Exception as e:
                    pass

        try:
            controller_cls = find_class("org.telegram.messenger.MessagesController")
            for method in controller_cls.getClass().getDeclaredMethods():
                name = method.getName()
                if name not in ("richEditorAvailable", "richEditorAllowed"):
                    continue
                if len(method.getParameterTypes()) != 0:
                    continue
                self.hook_method(method, BypassHandler(), 0)
                RICH_HOOK_STATE[name] = True
        except Exception as e:
            pass

        try:
            mdc_cls = find_class("org.telegram.messenger.MediaDataController")
            for method in mdc_cls.getClass().getDeclaredMethods():
                if method.getName() != "saveDraft":
                    continue
                if len(method.getParameterTypes()) != 11:
                    continue
                self.hook_method(method, DraftSuppressHandler(), 0)
                RICH_HOOK_STATE["draftSuppressed"] = True
                break
        except Exception as e:
            pass

        self._add_rich_editor_lifecycle_hooks()

    def _add_rich_editor_lifecycle_hooks(self):
        plugin = self
        self._add_rich_exit_hooks()

        class EditorDestroyedHandler(MethodHook):
            def after_hooked_method(self, param):
                try:
                    editor = getattr(plugin, "_rich_editor_ref", None)
                    if editor is None:
                        return
                    if not param.thisObject.equals(editor):
                        return
                    plugin._rich_capture_index = None
                    plugin._rich_capture_pending = False
                    plugin._rich_editor_ref = None
                    plugin._rich_editor_open = False
                    plugin._rich_editor_opening = False
                    plugin._rich_editor_opened_at = 0
                except Exception as e:
                    pass
        try:
            editor_cls = _rich_class("org.telegram.ui.iv.RichEditor")
            if editor_cls is None:
                return
            for method in editor_cls.getClass().getDeclaredMethods():
                if method.getName() != "onDestroyView" or len(method.getParameterTypes()) != 0:
                    continue
                self.hook_method(method, EditorDestroyedHandler(), 0)
                return
        except Exception as e:
            pass

    def _add_rich_exit_hooks(self):
        plugin = self

        class RichExitBackHandler(MethodHook):
            def __init__(self, block_value):
                MethodHook.__init__(self)
                self.block_value = block_value

            def before_hooked_method(self, param):
                try:
                    if not plugin._rich_exit_intercept(param.thisObject):
                        return
                    param.setResult(self.block_value)
                    now = time.time()
                    if now - getattr(plugin, "_rich_exit_dialog_at", 0) < 1.0:
                        return
                    plugin._rich_exit_dialog_at = now
                    run_on_ui_thread(plugin._show_rich_exit_dialog)
                except Exception as e:
                    pass

        try:
            editor_cls = _rich_class("org.telegram.ui.iv.RichEditor")
            if editor_cls is None:
                return
            one_arg = []
            zero_arg = []
            for method in editor_cls.getClass().getDeclaredMethods():
                if method.getName() != "onBackPressed":
                    continue
                param_count = len(method.getParameterTypes())
                if param_count == 1:
                    one_arg.append(method)
                elif param_count == 0:
                    zero_arg.append(method)
            targets = one_arg or zero_arg
            if not targets:
                klass = editor_cls.getClass().getSuperclass()
                while klass is not None and klass.getName() != "java.lang.Object" and not targets:
                    for method in klass.getDeclaredMethods():
                        if method.getName() != "onBackPressed":
                            continue
                        param_count = len(method.getParameterTypes())
                        if param_count in (0, 1):
                            targets.append(method)
                    if not targets:
                        klass = klass.getSuperclass()
                if targets:
                    pass
            for method in targets:
                try:
                    returns_boolean = method.getReturnType().getName() == "boolean"
                except Exception:
                    returns_boolean = True
                block_value = False if returns_boolean else None
                self.hook_method(method, RichExitBackHandler(block_value), 0)
            if targets:
                pass
            else:
                pass
        except Exception as e:
            pass

        class RichSlideBlockHandler(MethodHook):
            def before_hooked_method(self, param):
                try:
                    if not plugin._rich_exit_intercept(param.thisObject):
                        return
                    param.setResult(False)
                    now = time.time()
                    if now - getattr(plugin, "_rich_exit_dialog_at", 0) < 1.0:
                        return
                    plugin._rich_exit_dialog_at = now
                    run_on_ui_thread(plugin._show_rich_exit_dialog)
                except Exception as e:
                    pass

        try:
            editor_cls = _rich_class("org.telegram.ui.iv.RichEditor")
            if editor_cls is not None:
                slide_targets = []
                for method in editor_cls.getClass().getDeclaredMethods():
                    if method.getName() == "canBeginSlide" and len(method.getParameterTypes()) == 0:
                        slide_targets.append(method)
                if not slide_targets:
                    klass = editor_cls.getClass().getSuperclass()
                    while klass is not None and klass.getName() != "java.lang.Object" and not slide_targets:
                        for method in klass.getDeclaredMethods():
                            if method.getName() == "canBeginSlide" and len(method.getParameterTypes()) == 0:
                                slide_targets.append(method)
                        if not slide_targets:
                            klass = klass.getSuperclass()
                for method in slide_targets:
                    self.hook_method(method, RichSlideBlockHandler(), 0)
        except Exception as e:
            pass

    def _rich_exit_intercept(self, this_object=None):
        try:
            if not self.get_setting('rich_exit_confirm', True):
                return False
        except Exception:
            pass
        editor = getattr(self, "_rich_editor_ref", None)
        if editor is None or not getattr(self, "_rich_editor_open", False):
            return False
        if this_object is not None:
            try:
                if not this_object.equals(editor):
                    return False
            except Exception:
                if this_object is not editor:
                    return False
        return True

    def _show_rich_exit_dialog(self):
        try:
            if not self._rich_exit_intercept():
                return
            fragment = get_last_fragment()
            activity = fragment and fragment.getParentActivity()
            if not activity:
                return
            editor = getattr(self, "_rich_editor_ref", None)
            plugin = self

            def on_cancel(b, w):
                try:
                    b.dismiss()
                except Exception:
                    pass

            def on_save(b, w):
                try:
                    b.dismiss()
                except Exception:
                    pass
                plugin._rich_exit_save(editor)

            def on_leave(b, w):
                try:
                    b.dismiss()
                except Exception:
                    pass
                plugin._rich_exit_leave(editor)

            builder = AlertDialogBuilder(activity)
            builder.set_title(t('exit_back_title', lang=self.lang))
            builder.set_message(t('exit_back_message', lang=self.lang))
            builder.set_negative_button(t('cancel', lang=self.lang), on_cancel)
            builder.set_positive_button(t('save', lang=self.lang), on_save)
            builder.set_neutral_button(t('exit_leave', lang=self.lang), on_leave)
            red_button = getattr(AlertDialogBuilder, 'BUTTON_NEUTRAL', -3)
            try:
                builder.make_button_red(red_button)
            except Exception as e:
                pass
            builder.show()
        except Exception as e:
            pass

    def _rich_exit_save(self, editor):
        if editor is None:
            return
        try:
            self._rich_editor_opened_at = time.time()
            method = None
            klass = editor.getClass()
            while klass is not None and method is None:
                try:
                    method = klass.getDeclaredMethod("sendMessage")
                except Exception:
                    klass = klass.getSuperclass()
            if method is None:
                raise AttributeError("RichEditor.sendMessage not found")
            method.setAccessible(True)
            method.invoke(editor)
        except Exception as e:
            pass

        def finish_if_open():
            try:
                if self._rich_editor_active():
                    editor.finishFragment()
            except Exception as e:
                pass

        run_on_ui_thread(finish_if_open, 800)

    def _rich_exit_leave(self, editor):
        if editor is None:
            return
        try:
            self._close_fragment(editor)
        except Exception as e:
            pass

    def _rich_editor_default_back(self, editor):
        if editor is None:
            return
        try:
            list_view = _tv_read_field(editor, "listView")
            if list_view is not None and list_view.deselectIfAny():
                return
        except Exception:
            pass
        try:
            self._close_fragment(editor)
        except Exception as e:
            pass

    def _install_rich_exit_button(self, editor, attempt=0):
        try:
            if editor is None:
                return
            button = _tv_read_field(editor, "backButton")
            if button is None:
                raise AttributeError("backButton is None")
            current = None
            try:
                current = button.getOnClickListener()
                if current is not None and 'RichExitClickListener' in str(current.getClass().getName()):
                    return
            except Exception:
                current = None
            plugin_ref = weakref.ref(self)
            OnClickListener = find_class("android.view.View$OnClickListener")

            class RichExitClickListener(dynamic_proxy(OnClickListener)):
                def onClick(self, v):
                    plugin = plugin_ref()
                    if plugin is None:
                        return
                    if not plugin._rich_exit_intercept():
                        if current is not None:
                            current.onClick(v)
                        else:
                            plugin._rich_editor_default_back(plugin._rich_editor_ref)
                        return
                    now = time.time()
                    if now - getattr(plugin, "_rich_exit_dialog_at", 0) < 1.0:
                        return
                    plugin._rich_exit_dialog_at = now
                    run_on_ui_thread(plugin._show_rich_exit_dialog)

            button.setOnClickListener(RichExitClickListener())
        except Exception as e:
            if attempt < 25:
                run_on_ui_thread(lambda: self._install_rich_exit_button(editor, attempt + 1), delay=200)
            else:
                pass

    def _save_downgraded_rich_result(self, idx, simple_text):
        try:
            text = str(simple_text or "")
            if not text.strip():
                return
            account = self._account_number()
            payload = {
                "v": RICH_PAYLOAD_VERSION,
                "text": text,
                "src": text,
                "entities": [],
                "source": text,
                "blob": "",
                "extended": False,
                "photos": [],
                "documents": [],
                "rich_ok": False,
            }
            entities = rich_plain_to_entities(simple_text, account)
            if entities is not None and not entities.isEmpty():
                payload["entities"] = entities_to_json(entities)
            self.set_setting(f"template_text_{idx}", text)
            self._write_rich_setting(idx, payload)
            try:
                tpl = self.templates[idx] if idx < len(self.templates) else {}
                tpl = tpl.copy()
                tpl["text"] = text
                tpl["enabled"] = bool(tpl.get("name", "") and text)
                self.templates[idx] = tpl
                self.set_setting("templates", self.templates)
            except Exception:
                pass
            self._rich_toast(t('template_saved_plain', lang=self.lang, n=idx + 1))
            run_on_ui_thread(self._reload_submenu, 400)
        except Exception as e:
            pass

    def _rich_editor_media_paths(self):
        out = {}
        editor = getattr(self, "_rich_editor_ref", None)
        if editor is None:
            return out
        try:
            list_view = None
            cls = editor.getClass()
            while cls is not None and list_view is None:
                for field in cls.getDeclaredFields():
                    try:
                        if str(field.getType().getName()) == "org.telegram.ui.iv.RichEditorListView":
                            field.setAccessible(True)
                            list_view = field.get(editor)
                            break
                    except Exception:
                        continue
                cls = cls.getSuperclass()
            if list_view is None:
                return out
            rows = None
            cls = list_view.getClass()
            while cls is not None and rows is None:
                for field in cls.getDeclaredFields():
                    if str(field.getName()) == "rows":
                        field.setAccessible(True)
                        rows = field.get(list_view)
                        break
                cls = cls.getSuperclass()
            if rows is None:
                return out
            for row in _java_list(rows):
                states = []
                try:
                    media = getattr(row, "media", None)
                    if media is not None:
                        states.append(media)
                except Exception:
                    pass
                try:
                    for state in _java_list(getattr(row, "medias", None)):
                        states.append(state)
                except Exception:
                    pass
                for state in states:
                    try:
                        path = str(getattr(state, "localPath", None) or "")
                    except Exception:
                        path = ""
                    if not path:
                        continue
                    try:
                        photo = getattr(state, "photo", None)
                        photo_id = int(getattr(photo, "id", 0) or 0) if photo is not None else 0
                    except Exception:
                        photo_id = 0
                    if photo_id:
                        out[("p", photo_id)] = path
                    try:
                        doc = getattr(state, "document", None)
                        doc_id = int(getattr(doc, "id", 0) or 0) if doc is not None else 0
                    except Exception:
                        doc_id = 0
                    if doc_id:
                        out[("d", doc_id)] = path
        except Exception as e:
            pass
        return out

    def _save_rich_editor_result(self, idx, blocks, photos, documents):
        try:
            if not blocks or blocks.isEmpty():
                return
            account = self._account_number()
            rich_media_register(photos, documents)
            rich = _rich_new_message(blocks, photos, documents)
            rows = _rich_flatten_for_copy(rich)
            plain = rich_rows_to_plain(rows) or rich_blocks_to_plain(blocks)
            html = rich_rows_to_html(rows)
            extended = rich_blocks_is_extended(blocks)
            media_paths = self._rich_editor_media_paths()
            payload = {
                "v": RICH_PAYLOAD_VERSION,
                "text": plain,
                "entities": [],
                "source": html,
                "blob": rich_message_to_json(rich),
                "extended": bool(extended),
                "photos": rich_media_ids(photos),
                "documents": rich_media_ids(documents),
                "media": {
                    "photos": rich_media_pack(photos, media_paths, False),
                    "documents": rich_media_pack(documents, media_paths, True),
                },
                "rich_ok": bool(html) and rich_source_roundtrips(html, plain),
            }
            styled = rich_rows_to_char_sequence(rows) or plain
            entities = rich_plain_to_entities(styled, account)
            if entities is not None and not entities.isEmpty():
                payload["entities"] = entities_to_json(entities)
            if not payload["blob"]:
                pass
            text_value = plain or self.get_setting(f"template_text_{idx}", "")
            if not str(text_value or "").strip():
                text_value = self._plain_text_from_source(payload.get("source") or "")
            if text_value and not payload.get("text"):
                payload["text"] = text_value
            payload["src"] = text_value
            self.set_setting(f"template_text_{idx}", text_value)
            self._write_rich_setting(idx, payload)
            try:
                tpl = self.templates[idx] if idx < len(self.templates) else {}
                tpl = tpl.copy()
                tpl["text"] = text_value
                tpl["enabled"] = bool(tpl.get("name", "") and text_value)
                self.templates[idx] = tpl
                self.set_setting("templates", self.templates)
            except Exception:
                pass
            if payload["extended"] and not self._account_is_premium(account):
                self._show_no_premium_bulletin()
            else:
                key = 'template_saved_rich' if payload["extended"] else 'template_saved_plain'
                self._rich_toast(t(key, lang=self.lang, n=idx + 1))
            run_on_ui_thread(self._reload_submenu, 400)
        except Exception as e:
            pass

    def _account_is_premium(self, account=None):
        try:
            if account is None:
                account = self._account_number()
            return bool(UserConfig.getInstance(int(account)).isPremium())
        except Exception as e:
            return False

    def _show_no_premium_bulletin(self):
        def _show():
            try:
                BulletinHelper.show_with_button(
                    t('no_premium_send', lang=self.lang),
                    getattr(R_tg.raw, 'error', 0),
                    t('close', lang=self.lang),
                    lambda: None,
                    None
                )
            except Exception as e:
                pass
        run_on_ui_thread(_show)

    def _rich_toast(self, message, error=False):
        def _show():
            try:
                if error:
                    BulletinHelper.show_error(message)
                else:
                    BulletinHelper.show_success(message, getattr(R_tg.raw, 'done', 0))
            except Exception as e:
                pass
        run_on_ui_thread(_show)

    def _open_template_rich_editor(self, idx):
        try:
            account = self._account_number()
            status, detail = rich_editor_status(account)
            if status == "missing_classes":
                missing = "\n".join(str(item) for item in (detail or []))
                self._rich_toast(t('rich_editor_missing_classes', lang=self.lang) + "\n\n" + missing,
                                 error=True)
                return
            if status == "disabled_by_config":
                pass
            if getattr(self, "_rich_editor_opening", False):
                self._rich_toast(t('rich_editor_busy', lang=self.lang), error=True)
                return
            self._rich_editor_opening = True
            self._rich_capture_index = idx
            self._rich_toast(t('rich_editor_opening', lang=self.lang))
            run_on_ui_thread(lambda: self._launch_rich_editor(idx))
        except Exception as e:
            self._abort_rich_editor()

    def _rich_editor_active(self):
        if not getattr(self, "_rich_editor_open", False):
            return False
        return getattr(self, "_rich_editor_ref", None) is not None

    def _rich_editor_session_alive(self):
        if not self._rich_editor_active():
            return False
        opened_at = getattr(self, "_rich_editor_opened_at", 0)
        try:
            if opened_at and (time.time() - opened_at) > RICH_EDITOR_SESSION_TTL:
                return False
        except Exception:
            pass
        editor = self._rich_editor_ref
        try:
            if editor is not None and editor.getFragmentView() is not None:
                return True
        except Exception:
            pass
        try:
            if opened_at and (time.time() - opened_at) < 5:
                return True
        except Exception:
            pass
        return False

    def _abort_rich_editor(self, error=None):
        self._rich_editor_opening = False
        self._rich_capture_index = None
        self._rich_capture_pending = False
        self._rich_editor_ref = None
        self._rich_editor_open = False
        self._rich_editor_opened_at = 0
        if error is not None:
            pass

    def _launch_rich_editor(self, idx):
        try:
            frag = get_last_fragment()
            if frag is None:
                self._abort_rich_editor()
                self._rich_toast(t('rich_editor_no_host', lang=self.lang), error=True)
                return
            if frag.getParentLayout() is None:
                self._abort_rich_editor()
                self._rich_toast(t('rich_editor_present_failed', lang=self.lang), error=True)
                return
            editor_cls = _rich_class("org.telegram.ui.iv.RichEditor")
            if editor_cls is None:
                self._abort_rich_editor()
                self._rich_toast(t('rich_editor_missing_classes', lang=self.lang), error=True)
                return
            payload = self._template_payload(idx)
            source = str(payload.get("source") or "")
            plain = str(payload.get("text") or "")
            rich = self._payload_rich_message(payload)
            if rich is not None:
                editor = editor_cls(rich)
            elif source:
                editor = editor_cls(str(source), True)
            else:
                editor = editor_cls(str(plain or ""))
            try:
                provider = frag.getResourceProvider()
                if provider is not None:
                    editor.setResourceProvider(provider)
            except Exception as e:
                pass
            chat = ChatActivity.of(jlong(self._self_dialog_id(self._account_number())))
            editor.setChatActivity(chat)
            self._rich_editor_ref = editor
            self._rich_editor_open = True
            self._rich_capture_pending = True
            self._rich_editor_opened_at = time.time()
            if not frag.presentFragment(editor):
                self._abort_rich_editor()
                self._rich_toast(t('rich_editor_present_failed', lang=self.lang), error=True)
                return
            self._rich_editor_opening = False
            self._install_rich_exit_button(editor)
        except Exception as e:
            self._abort_rich_editor()
            self._rich_toast(t('rich_editor_present_failed', lang=self.lang), error=True)

    def _self_dialog_id(self, account):
        return rich_self_dialog_id(account)

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
                        payload = self._template_payload(i, text)
                        current_dialog_id = 0
                        try:
                            frag = get_last_fragment()
                            if isinstance(frag, ChatActivity):
                                current_dialog_id = int(frag.getDialogId())
                        except Exception:
                            current_dialog_id = 0
                        if current_dialog_id and self._send_rich_payload(account, current_dialog_id, payload):
                            run_on_ui_thread(lambda: BulletinHelper.show_success(
                                t('template_n_sent', lang=self.lang, n=i + 1),
                                getattr(R_tg.raw, 'done', 0)))
                            return HookResult(strategy=HookStrategy.CANCEL)
                        text_value, entities = self._payload_text_and_entities(payload)
                        params.message = text_value
                        try:
                            params.searchLinks = self._template_link_preview(i)
                        except Exception:
                            pass
                        if hasattr(params, 'entities') and params.entities is not None:
                            params.entities.clear()
                        else:
                            params.entities = ArrayList()
                        for entity in entities:
                            params.entities.add(entity)
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
        if not text:
            payload = self._read_rich_setting(idx) or {}
            if not (payload.get("text") or payload.get("source") or payload.get("blob")
                    or payload.get("photos") or payload.get("documents")):
                run_on_ui_thread(lambda: BulletinHelper.show_error(t('fill_all_fields', lang=self.lang)))
                return
            text = str(payload.get("text") or "")
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
                token = self._start_picker_session(template_idx, template_name, template_text)
                args.putString(PICKER_TOKEN_KEY, token)
                picker = DialogsActivity(args)
                session = self._picker_sessions.get(token)
                if session is not None:
                    session["picker"] = picker
                delegate = _TargetPickerDelegate(self, template_idx, template_name, template_text, picker)
                self._picker_delegates.append(delegate)
                picker.setDelegate(delegate)
                fragment.presentFragment(picker)
                if session is not None:
                    self._prepare_picker_confirm(picker, session)
                    if self._take_picker_hint_slot():
                        run_on_ui_thread(lambda: self._show_picker_hint(picker, session), 600)
            except Exception as error:
                self._show_bulletin(t('chat_picker_error', lang=self.lang), "error")
        run_on_ui_thread(open_now)

    def _take_picker_hint_slot(self):
        try:
            try:
                shown = int(self.get_setting('multi_select_hint_count', 0))
            except Exception:
                shown = 0
            if shown < 0:
                shown = 0
            if shown >= PICKER_HINT_LIMIT:
                return False
            self.set_setting('multi_select_hint_count', shown + 1, reload_settings=False)
            return True
        except Exception:
            return False

    def _start_picker_session(self, template_idx, template_name, template_text):
        self._prune_picker_sessions()
        self._picker_token_seq += 1
        token = f"tpl-{int(time.time() * 1000)}-{self._picker_token_seq}"
        self._picker_sessions[token] = {
            "token": token,
            "picker": None,
            "confirm": None,
            "confirm_kind": None,
            "hint": None,
            "template_idx": template_idx,
            "template_name": template_name,
            "template_text": template_text,
        }
        return token

    def _prune_picker_sessions(self):
        for token in list(self._picker_sessions.keys()):
            session = self._picker_sessions.get(token)
            picker = session.get("picker") if session else None
            if picker is None:
                self._picker_sessions.pop(token, None)
                continue
            gone = False
            try:
                gone = bool(picker.wasRemoved())
            except Exception:
                gone = False
            try:
                if picker.getParentLayout() is None:
                    gone = True
            except Exception:
                pass
            if gone:
                session["confirm"] = None
                session["hint"] = None
                self._picker_sessions.pop(token, None)

    def _picker_session_for(self, fragment):
        if fragment is None:
            return None
        try:
            args = fragment.getArguments()
            if args is None:
                return None
            token = args.getString(PICKER_TOKEN_KEY)
        except Exception:
            return None
        if not token:
            return None
        return self._picker_sessions.get(token)

    def _setup_picker_multi_select_hooks(self):
        if self._picker_hooks_ready:
            return
        plugin = self

        class PickerLongPressHook(MethodHook):
            def __init__(self):
                MethodHook.__init__(self)

            def before_hooked_method(self, param):
                try:
                    fragment = param.thisObject
                    session = plugin._picker_session_for(fragment)
                    if session is None:
                        return
                    args = param.args
                    if args is None or len(args) < 7:
                        return
                    adapter = args[6]
                    try:
                        if "SearchAdapter" in str(adapter.getClass().getName()):
                            return
                    except Exception:
                        return
                    cell = args[1]
                    if cell is None:
                        return
                    try:
                        dialog_id = int(cell.getDialogId())
                    except Exception:
                        return
                    if dialog_id == 0:
                        return
                    plugin._picker_toggle_selected(fragment, session, cell, dialog_id)
                    param.setResult(True)
                except Exception:
                    pass

        class PickerSelectionHook(MethodHook):
            def __init__(self):
                MethodHook.__init__(self)

            def after_hooked_method(self, param):
                try:
                    fragment = param.thisObject
                    if plugin._picker_session_for(fragment) is None:
                        return
                    run_on_ui_thread(lambda: plugin._refresh_picker_button(fragment))
                except Exception:
                    pass

        class PickerFloatingButtonHook(MethodHook):
            def __init__(self):
                MethodHook.__init__(self)

            def after_hooked_method(self, param):
                try:
                    fragment = param.thisObject
                    if plugin._picker_session_for(fragment) is None:
                        return
                    run_on_ui_thread(lambda: plugin._refresh_picker_button(fragment))
                except Exception:
                    pass

        try:
            dialogs_cls = find_class("org.telegram.ui.DialogsActivity")
            if dialogs_cls is None:
                return
            long_method = None
            select_method = None
            fab_method = None
            for method in dialogs_cls.getClass().getDeclaredMethods():
                try:
                    name = method.getName()
                    params = method.getParameterTypes()
                    if long_method is None and name == "onItemLongClick" and len(params) == 7:
                        long_method = method
                    elif select_method is None and name == "addOrRemoveSelectedDialog" and len(params) == 2:
                        select_method = method
                    elif fab_method is None and name == "updateFloatingButtonVisibility" and len(params) == 1:
                        fab_method = method
                except Exception:
                    continue
            if long_method is not None:
                long_method.setAccessible(True)
                self.hook_method(long_method, PickerLongPressHook())
                self._picker_hooks_ready = True
            if select_method is not None:
                select_method.setAccessible(True)
                self.hook_method(select_method, PickerSelectionHook())
            if fab_method is not None:
                fab_method.setAccessible(True)
                self.hook_method(fab_method, PickerFloatingButtonHook())
        except Exception:
            pass

    def _picker_selected_dialogs(self, fragment):
        selected = self._get_private_field(fragment, "selectedDialogs")
        if selected is None:
            return None
        return selected

    def _picker_selected_targets(self, fragment):
        selected = self._picker_selected_dialogs(fragment)
        if selected is None:
            return []
        targets = []
        for value in _iter_collection(selected):
            dialog_id = self._to_java_long(value)
            if dialog_id == 0:
                continue
            targets.append((dialog_id, 0))
        return targets

    def _picker_toggle_selected(self, fragment, session, cell, dialog_id):
        try:
            selected = self._picker_selected_dialogs(fragment)
            if selected is None:
                return False
            index = int(selected.indexOf(jlong(int(dialog_id))))
            if index >= 0:
                selected.remove(jint(index))
                checked = False
            else:
                selected.add(jlong(int(dialog_id)))
                checked = True
            try:
                cell.setChecked(checked, True)
            except Exception:
                pass
        except Exception:
            return False
        self._refresh_picker_button(fragment, session)
        if session.get("fallback"):
            run_on_ui_thread(lambda: self._picker_confirm_dialog(fragment, session))
        return True

    def _show_picker_hint(self, fragment, session, attempt=0):
        try:
            if fragment is None or session.get("hint") is not None:
                return
            view = fragment.getFragmentView()
            if view is None:
                raise AttributeError("fragmentView is None")
            act = fragment.getParentActivity()
            if act is None:
                act = view.getContext()
            hint = TextView(act)
            hint.setText(t('select_chats_hint', lang=self.lang))
            hint.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 13)
            hint.setGravity(Gravity.CENTER)
            hint.setSingleLine(True)
            hint.setTextColor(Color.WHITE)
            hint.setPadding( AndroidUtilities.dp(14), AndroidUtilities.dp(8), AndroidUtilities.dp(14), AndroidUtilities.dp(8))
            hint.setShadowLayer(AndroidUtilities.dp(3), 0, AndroidUtilities.dp(1), Color.argb(128, 0, 0, 0))
            try:
                bg = GradientDrawable()
                bg.setCornerRadius(AndroidUtilities.dp(14))
                bg.setColor(Color.argb(180, 0, 0, 0))
                hint.setBackground(bg)
            except Exception:
                hint.setBackgroundColor(Color.argb(180, 0, 0, 0))
            top_margin = 0
            try:
                action_bar = fragment.getActionBar()
                if action_bar is not None:
                    top_margin = action_bar.getMeasuredHeight()
            except Exception:
                top_margin = 0
            if not top_margin:
                top_margin = AndroidUtilities.dp(56)
            hint.setAlpha(0.0)
            view.addView(hint, LayoutHelper.createFrame( -1, -2, Gravity.TOP | Gravity.CENTER_HORIZONTAL, AndroidUtilities.dp(16), top_margin + AndroidUtilities.dp(8), AndroidUtilities.dp(16), 0))
            hint.animate().alpha(1.0).setDuration(200).start()
            session["hint"] = hint

            def _fade_out():
                try:
                    hint.animate().alpha(0.0).setDuration(200).start()
                except Exception:
                    pass

            def _remove():
                _fade_out()
                run_on_ui_thread(lambda: view.removeView(hint), 250)

            run_on_ui_thread(_remove, 4000)
        except Exception:
            if attempt < 10:
                run_on_ui_thread( lambda: self._show_picker_hint(fragment, session, attempt + 1), 200)

    def _setup_channel_promo_hook(self):
        if not hasattr(self, '_promo_hook_refs'):
            self._promo_hook_refs = []
        if self._promo_hook_refs:
            return
        try:
            dialogs_cls = find_class("org.telegram.ui.DialogsActivity")
            if dialogs_cls is None:
                return
            plugin = self

            class ChannelPromoHook(MethodHook):
                def __init__(self):
                    MethodHook.__init__(self)

                def after_hooked_method(self, param):
                    try:
                        if param.thisObject is not None:
                            plugin._channel_promo_fill(param.thisObject)
                    except Exception:
                        pass

            refs = self.hook_all_methods(dialogs_cls, "updateDialogsHint", ChannelPromoHook())
            if refs:
                self._promo_hook_refs.extend(refs)
        except Exception:
            pass

    def _channel_promo_fill(self, fragment):
        try:
            if bool(self.get_setting('channel_promo_closed', False)):
                return
            if getattr(self, '_promo_check_state', None) is not False:
                return
            try:
                args = fragment.getArguments()
                if args is not None and args.getBoolean("onlySelect", False):
                    return
            except Exception:
                pass
            cell = get_private_field(fragment, "dialogsHintCell")
            panel = get_private_field(fragment, "topPanelLayout")
            if cell is None or panel is None:
                return
            if self._channel_promo_hidden(fragment):
                return
            first = not getattr(self, '_promo_cell_active', False)
            try:
                if panel.isViewVisible(cell) and first:
                    return
            except Exception:
                return
            title, subtitle = self._channel_promo_content(cell)
            cell.setText(title, subtitle)
            cell.setOnClickListener(OnClickListener(lambda v: self._channel_promo_open()))
            cell.setOnCloseListener(OnClickListener(lambda v: self._channel_promo_close(fragment)))
            need_show = first
            try:
                if not panel.isViewVisible(cell):
                    need_show = True
            except Exception:
                need_show = True
            if need_show:
                panel.setViewVisible(cell, True)
            self._promo_cell_active = True
            if first:
                root = fragment.getFragmentView()
                if root is not None:
                    root.requestLayout()
                class Finish(dynamic_proxy(Runnable)):
                    def run(self_):
                        try:
                            if cell.getAlpha() < 1.0:
                                panel.setChildVisibilityFactor(cell, 1.0)
                        except Exception:
                            pass
                cell.post(Finish())
        except Exception:
            pass

    def _channel_promo_hidden(self, fragment):
        try:
            if fragment.isInPreviewMode():
                return True
        except Exception:
            pass
        try:
            right = fragment.rightSlidingDialogContainer
            if right is not None and right.hasFragment():
                return True
        except Exception:
            pass
        try:
            search = get_private_field(fragment, "animatorSearchVisible")
            if search is not None and search.getValue():
                return True
        except Exception:
            pass
        return False

    def _channel_promo_content(self, cell):
        title = t('channel_promo_title', lang=self.lang)
        subtitle = t('channel_promo_text', lang=self.lang)
        try:
            index = title.find(CHANNEL_PROMO_EMOJI_CHAR)
            if index < 0:
                return title, subtitle
            offset = len(title[:index].encode('utf-16-le')) // 2
            length = len(CHANNEL_PROMO_EMOJI_CHAR.encode('utf-16-le')) // 2
            entities = ArrayList()
            entity = TLRPC.TL_messageEntityCustomEmoji()
            entity.document_id = jlong(CHANNEL_PROMO_EMOJI_ID)
            entity.offset = offset
            entity.length = length
            entities.add(entity)
            font_metrics = cell.titleView.getPaint().getFontMetricsInt()
            spanned = MessageObject.replaceAnimatedEmoji(SpannableStringBuilder(title), entities, font_metrics)
            return spanned, subtitle
        except Exception:
            return title, subtitle

    def _channel_promo_open(self):
        try:
            _open_url_in_telegram(CHANNEL_PROMO_URL)
        except Exception:
            pass
        try:
            if not getattr(self, '_promo_recheck_running', False):
                self._promo_recheck_running = True
                threading.Thread(target=self._channel_promo_recheck, daemon=True).start()
        except Exception:
            pass

    def _channel_promo_close(self, fragment):
        self._promo_cell_active = False
        try:
            self.set_setting('channel_promo_closed', True, reload_settings=False)
        except Exception:
            pass
        try:
            cell = get_private_field(fragment, "dialogsHintCell")
            panel = get_private_field(fragment, "topPanelLayout")
            if cell is not None and panel is not None:
                panel.setViewVisible(cell, False)
        except Exception:
            pass

    def _channel_promo_hide(self):
        try:
            self._promo_cell_active = False
            fragment = self._channel_promo_find_dialogs()
            if fragment is None:
                return
            cell = get_private_field(fragment, "dialogsHintCell")
            panel = get_private_field(fragment, "topPanelLayout")
            if cell is not None and panel is not None:
                panel.setViewVisible(cell, False)
        except Exception:
            pass

    def _channel_promo_recheck(self):
        try:
            time.sleep(15)
            self._channel_promo_check(start_delay=0)
        except Exception:
            pass
        finally:
            self._promo_recheck_running = False

    def _channel_promo_check(self, start_delay=6):
        try:
            if start_delay:
                time.sleep(start_delay)
            subscribed = False
            deadline = time.time() + 45
            try:
                max_accounts = int(UserConfig.MAX_ACCOUNT_COUNT)
            except Exception:
                max_accounts = 4
            for account in range(max(1, max_accounts)):
                if time.time() >= deadline:
                    break
                try:
                    account_config = UserConfig.getInstance(account)
                    if account_config is None or not account_config.isClientActivated():
                        continue
                    mc = MessagesController.getInstance(account)
                    if mc is None:
                        continue
                    waited_at = time.time()
                    while time.time() - waited_at < 15 and time.time() < deadline:
                        try:
                            if mc.dialogsLoaded:
                                break
                        except Exception:
                            break
                        time.sleep(0.5)
                    if self._channel_promo_account_subscribed(mc):
                        subscribed = True
                        break
                except Exception:
                    continue
            self._promo_check_state = subscribed
            if subscribed:
                run_on_ui_thread(self._channel_promo_hide)
            else:
                self._channel_promo_refresh()
        except Exception:
            self._promo_check_state = False
            self._channel_promo_refresh()

    def _channel_promo_account_subscribed(self, mc):
        try:
            chat = mc.getUserOrChat(CHANNEL_PROMO_USERNAME)
        except Exception:
            chat = None
        if chat is None:
            return False
        try:
            chat_id = int(chat.id)
        except Exception:
            return False
        if not chat_id:
            return False
        try:
            dialogs_dict = mc.dialogs_dict
        except Exception:
            dialogs_dict = None
        if dialogs_dict is None:
            return False
        for key in (chat_id, -chat_id):
            for variant in (key, Long.valueOf(key)):
                try:
                    if dialogs_dict.get(variant) is not None:
                        return True
                except Exception:
                    pass
        return False

    def _channel_promo_refresh(self):
        def go():
            try:
                fragment = self._channel_promo_find_dialogs()
                if fragment is None:
                    return
                try:
                    fragment.updateDialogsHint()
                    return
                except Exception:
                    pass
                try:
                    cls = find_class("org.telegram.ui.DialogsActivity")
                    for method in cls.getDeclaredMethods():
                        if str(method.getName()) == "updateDialogsHint":
                            method.setAccessible(True)
                            method.invoke(fragment)
                            return
                except Exception:
                    pass
            except Exception:
                pass
        run_on_ui_thread(go)

    def _channel_promo_find_dialogs(self):
        try:
            dialogs_cls = find_class("org.telegram.ui.DialogsActivity")
            if dialogs_cls is None:
                return None
            top = get_last_fragment()
            if top is None:
                return None
            if isinstance(top, dialogs_cls):
                return top
            parent = top.getParentLayout()
            if parent is None:
                return None
            stack = parent.getFragmentStack()
            for i in range(stack.size() - 1, -1, -1):
                fragment = stack.get(i)
                if isinstance(fragment, dialogs_cls):
                    return fragment
        except Exception:
            return None
        return None

    def _prepare_picker_confirm(self, fragment, session, attempt=0):
        try:
            if fragment is None or session.get("confirm") is not None:
                return
            fab = self._get_private_field(fragment, "floatingButton3")
            if fab is not None:
                try:
                    icon_id = 0
                    for icon_name in ("floating_check", "msg_check", "msg_done"):
                        icon_id = int(getattr(R_tg.drawable, icon_name, 0))
                        if icon_id:
                            break
                    if icon_id:
                        fab.setImageResource(icon_id)
                except Exception:
                    pass
                try:
                    fab.setContentDescription(t('select_chats_done', lang=self.lang))
                except Exception:
                    pass
                fab.setOnClickListener(OnClickListener(lambda v: self._on_picker_done(fragment, session)))
                session["confirm"] = fab
                session["confirm_kind"] = "fab"
                self._refresh_picker_button(fragment, session)
                return
            view = fragment.getFragmentView()
            if view is None:
                raise AttributeError("fragmentView is None")
            act = fragment.getParentActivity()
            if act is None:
                act = view.getContext()
            button = self._picker_button( act, t('select_chats_done', lang=self.lang), lambda v: self._on_picker_done(fragment, session), pad_h=0)
            view.addView(button, LayoutHelper.createFrame(-1, -2, Gravity.BOTTOM | Gravity.CENTER_HORIZONTAL, PICKER_PAD_H, 0, PICKER_PAD_H, 12))
            button.setVisibility(View.GONE)
            session["confirm"] = button
            session["confirm_kind"] = "button"
            self._refresh_picker_button(fragment, session)
        except Exception:
            if attempt < 20:
                run_on_ui_thread( lambda: self._prepare_picker_confirm(fragment, session, attempt + 1), 200)
            else:
                session["fallback"] = True
                try:
                    log("Templates: no confirm ui for the multi select picker")
                except Exception:
                    pass

    def _set_picker_confirm_visible(self, confirm, kind, visible):
        try:
            if kind == "fab":
                confirm.setButtonVisible(visible, True)
                return
        except Exception:
            pass
        confirm.setVisibility(View.VISIBLE if visible else View.GONE)

    def _refresh_picker_button(self, fragment, session=None):
        try:
            if session is None:
                session = self._picker_session_for(fragment)
            if session is None:
                return
            confirm = session.get("confirm")
            if confirm is None:
                self._prepare_picker_confirm(fragment, session)
                return
            count = len(self._picker_selected_targets(fragment))
            self._set_picker_confirm_visible(confirm, session.get("confirm_kind"), count > 0)
            if session.get("confirm_kind") == "button" and count > 0:
                confirm.setText(f"{str(t('select_chats_done', lang=self.lang)).upper()} ({count})")
        except Exception:
            pass

    def _on_picker_done(self, fragment, session):
        self._picker_finish_and_send(fragment, session)

    def _picker_confirm_dialog(self, fragment, session):
        try:
            targets = self._picker_selected_targets(fragment)
            if not targets:
                self._show_bulletin(t('no_chat_selected', lang=self.lang), "error")
                return
            frag = get_last_fragment()
            act = frag.getParentActivity() if frag else None
            if not act:
                return
            builder = AlertDialogBuilder(act)
            builder.set_title(t('send_template', lang=self.lang))
            builder.set_message(t('template_send_n_question', lang=self.lang, n=len(targets)))

            def on_yes(b, w):
                try:
                    self._picker_finish_and_send(fragment, session)
                finally:
                    b.dismiss()

            builder.set_positive_button(t('send_action', lang=self.lang), on_yes)
            builder.set_negative_button(t('cancel', lang=self.lang), lambda b, w: b.dismiss())
            builder.show()
        except Exception:
            pass

    def _picker_finish_and_send(self, fragment, session):
        try:
            targets = self._picker_selected_targets(fragment)
            if not targets:
                self._show_bulletin(t('no_chat_selected', lang=self.lang), "error")
                return
            self._picker_sessions.pop(session.get("token"), None)
            session["confirm"] = None
            session["hint"] = None
            self._picker_delegates.clear()
            self._send_templates_to_targets( targets, session.get("template_idx"), session.get("template_text"), session.get("template_name"))
            self._close_picker_fragments(fragment, None, fragment)
        except Exception:
            self._show_bulletin(t('template_send_error', lang=self.lang), "error")

    def _targets_from_dids(self, dids):
        if dids is None:
            return []
        targets = []
        for topic_key in _iter_collection(dids):
            dialog_id, topic_id = self._topic_key_parts(topic_key)
            if dialog_id == 0:
                continue
            targets.append((dialog_id, topic_id))
        return targets

    def _send_templates_to_targets(self, targets, template_idx, template_text, template_name=None):
        sent = 0
        first_dialog_id = 0
        for dialog_id, topic_id in targets:
            try:
                if self._send_template_to_peer(dialog_id, template_text, topic_id=topic_id, template_idx=template_idx):
                    if first_dialog_id == 0:
                        first_dialog_id = dialog_id
                    sent += 1
            except Exception:
                continue
        if sent <= 0:
            self._show_bulletin(t('template_send_error', lang=self.lang), "error")
            return sent
        try:
            icon_attr = getattr(R_tg.raw, 'done', None)
        except Exception:
            icon_attr = None
        if sent == 1:
            self._last_sent_dialog_id = first_dialog_id
            def _open():
                try:
                    self._open_chat_by_dialog_id(first_dialog_id)
                except Exception:
                    pass
            run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                t('template_n_sent', lang=self.lang, n=template_idx + 1),
                icon_attr if icon_attr else 0,
                t('open', lang=self.lang),
                _open,
                None
            ))
        else:
            def _open():
                try:
                    self._open_main_dialogs()
                except Exception:
                    pass

            run_on_ui_thread(lambda: BulletinHelper.show_with_button(
                t('template_sent_n', lang=self.lang, n=sent),
                icon_attr if icon_attr else 0,
                t('open', lang=self.lang),
                _open,
                None
            ))
        return sent

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

    def _template_link_preview(self, idx):
        try:
            if idx is None:
                return True
            return bool(self.get_setting(f"template_linkpreview_{idx}", True))
        except Exception:
            return True

    def _send_text_message(self, message_data, search_links=True, account=None):
        message_data = dict(message_data)
        message_data["searchLinks"] = bool(search_links)
        if search_links:
            try:
                send_message(message_data)
                return True
            except Exception as e:
                pass
        try:
            from org.telegram.messenger import SendMessagesHelper as SMH
            peer = self._to_java_long(message_data.get("peer"))
            params = SMH.SendMessageParams.of(str(message_data.get("message") or ""), peer)
            params.searchLinks = bool(search_links)
            params.notify = True
            entities = message_data.get("entities") or []
            if entities:
                items = ArrayList()
                for entity in entities:
                    try:
                        if hasattr(entity, "to_tlrpc_object"):
                            entity = entity.to_tlrpc_object()
                        items.add(entity)
                    except Exception:
                        pass
                if items.size() > 0:
                    params.entities = items
            reply_to = message_data.get("replyToMsg")
            if reply_to is not None:
                params.replyToMsg = reply_to
                reply_top = message_data.get("replyToTopMsg")
                if reply_top is not None:
                    params.replyToTopMsg = reply_top
            helper = SMH.getInstance(int(account if account is not None else self._account_number()))
            def _do():
                helper.sendMessage(params)
            if self._is_ui_thread():
                _do()
            else:
                run_on_ui_thread(_do)
            return True
        except Exception as e:
            try:
                send_message(message_data)
                return True
            except Exception as e2:
                return False

    def _send_template_to_peer(self, dialog_id, template_text, topic_id=0, account=None, template_idx=None):
        reply_to = None
        reply_to_top = None
        if topic_id > 0:
            topic_msg_obj = self._topic_message_obj(dialog_id, topic_id, account=account)
            if topic_msg_obj is not None:
                reply_to = topic_msg_obj
                reply_to_top = topic_msg_obj
        if account is None:
            account = self._account_number()
        payload = self._template_payload(template_idx, template_text) if template_idx is not None else None
        if payload is not None and self._send_rich_payload(account, dialog_id, payload, reply_to, reply_to_top):
            return True
        text_value, entities = self._plain_template_content(template_text, payload)
        message_data = {
            "peer": dialog_id,
            "message": text_value,
            "entities": entities
        }
        if reply_to is not None:
            message_data["replyToMsg"] = reply_to
            message_data["replyToTopMsg"] = reply_to_top
        self._send_text_message(message_data, self._template_link_preview(template_idx), account)
        return True

    def _entities_from_payload_blob(self, payload):
        rich = self._payload_rich_message(payload)
        if rich is None:
            return []
        try:
            styled = rich_blocks_to_char_sequence(rich.blocks)
            entities = rich_plain_to_entities(styled, self._account_number())
            if entities is None or entities.isEmpty():
                return []
            return entities_from_json(entities_to_json(entities))
        except Exception as e:
            return []

    def _plain_template_content(self, template_text, payload=None):
        if payload is not None:
            text_value, entities = self._payload_text_and_entities(payload)
            if text_value:
                items = [entities.get(i) for i in range(entities.size())]
                if not items:
                    items = self._entities_from_payload_blob(payload)
                return text_value, items
        if payload is not None and not str(template_text or "").strip():
            fallback = self._plain_text_from_source(payload.get("source") or "")
            if fallback:
                return fallback, []
        try:
            parsed = parse_markdown(preprocess_template_markdown(template_text))
            return str(parsed.text), [ent.to_tlrpc_object() for ent in parsed.entities]
        except Exception:
            return str(template_text or ""), []

    def _plain_text_from_source(self, source):
        try:
            text = re.sub(r"<[^>]+>", " ", str(source or ""))
            return re.sub(r"\s+", " ", text).strip()
        except Exception:
            return ""

    def _handle_template_picker_result(self, fragment, dids, template_idx, template_name, template_text, topics_fragment=None, picker=None):
        targets = self._targets_from_dids(dids)
        if not targets:
            self._show_bulletin(t('no_chat_selected', lang=self.lang), "error")
            return

        session = self._picker_session_for(picker) or self._picker_session_for(fragment)
        if session is not None:
            self._picker_sessions.pop(session.get("token"), None)
            session["confirm"] = None
            session["hint"] = None
        self._picker_delegates.clear()

        try:
            self._send_templates_to_targets(targets, template_idx, template_text, template_name)
            self._last_sent_dialog_id = targets[0][0]
            self._close_picker_fragments(fragment, topics_fragment, picker, topic_id=targets[0][1])
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

    def _show_language_sheet(self, _):
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        try:
            current = int(self.get_setting('plugin_lang', 0) or 0)
        except Exception:
            current = 0
        current = max(0, min(current, len(PLUGIN_LANG_CODES) - 1))
        labels = [self._t('system')] + [l for l in PLUGIN_LANG_LABELS[1:] if l]
        picked = [current]
        sheet, outer, subtitle_tv = self._picker_sheet_container(
            act, frag, t('plugin_language', lang=self.lang), labels[current])
        checkboxes = {}
        def on_pick(index, checkbox, key):
            picked[0] = index
            for other, other_cb in checkboxes.items():
                if other != key and other_cb is not None and other_cb.isChecked():
                    other_cb.setChecked(False, True)
            checkbox.setChecked(True, True)
            subtitle_tv.setText(labels[index])
        items_list = LinearLayout(act)
        items_list.setOrientation(LinearLayout.VERTICAL)
        for position, label in enumerate(labels):
            key = str(position)
            def on_toggled(value, key=key, position=position):
                if value:
                    on_pick(position, checkboxes[key], key)
                else:
                    checkboxes[key].setChecked(True, True)
            row, checkbox = self._picker_row(act, "", str(label), position == current, on_toggled, center_text=True, bold_text=True)
            checkboxes[key] = checkbox
            items_list.addView(row, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 8 if position < len(labels) - 1 else 0))
        dark_container, dark_lp = self._picker_scrolled_list(act, items_list, len(labels))
        outer.addView(dark_container, dark_lp)

        def on_apply(v=None):
            chosen = picked[0]
            try:
                sheet.dismiss()
            except Exception:
                pass
            if chosen != current:
                self._on_language_changed(chosen)

        outer.addView(self._picker_button(act, t('apply', lang=self.lang), on_apply), LayoutHelper.createLinear(-1, -2, PICKER_BUTTON_PAD_H, PICKER_BUTTON_TOP_PAD, PICKER_BUTTON_PAD_H, 16))
        self._picker_show_animated(sheet, outer)
        return sheet


    def _show_support_me_menu(self, _):
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return

        def on_support(v=None):
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
                gift_sheet = GiftSheet(last_fragment.getContext(), current_account, target_user_id, None, None)
                gift_sheet.show()
            except Exception:
                pass

        sheet, outer, subtitle_tv = self._picker_sheet_container(
            act, frag, t('support_me', lang=self.lang), '', ("mr_vestr/9", 9))
        dark_container, dark_lp = self._picker_body_block(
            act, t('support_me_text', lang=self.lang), max_height_dp=300, gravity=Gravity.CENTER, keep_scroll=False)
        outer.addView(dark_container, dark_lp)
        outer.addView(self._picker_button(act, t('support_me', lang=self.lang), on_support), LayoutHelper.createLinear(-1, -2, PICKER_BUTTON_PAD_H, PICKER_BUTTON_TOP_PAD, PICKER_BUTTON_PAD_H, 16))
        self._picker_show_animated(sheet, outer)
        return sheet

    def _show_template_picker_sheet(self, templates):
        frag = get_last_fragment()
        act = frag.getParentActivity() if frag else None
        if not act:
            return
        by_key = {str(template['index']): template for template in templates}
        items = [
            {
                "key": str(template['index']),
                "badge": str(template['index'] + 1),
                "name": self._picker_row_title(template.get('name'), template['index']),
                "subtitle": self._picker_row_subtitle(template.get('text'))
            }
            for template in templates
        ]

        def on_pick(key):
            self.menu_shown = False
            template = by_key.get(str(key))
            if not template:
                return
            self._send_template_to_current_chat(template['index'], template['name'], template['text'])

        def on_settings():
            self.menu_shown = False
            self.open_plugin_settings()

        def on_dismiss():
            self.menu_shown = False

        self.menu_shown = True
        sheet = self._build_template_send_sheet(
            act, frag, items,
            t('select_template', lang=self.lang) if items else t('no_templates_available', lang=self.lang),
            t('templates_count', lang=self.lang, n=len(items)),
            t('settings', lang=self.lang),
            on_pick, on_settings)
        try:
            sheet.setOnDismissListener(dynamic_proxy(DialogInterface.OnDismissListener)(on_dismiss))
        except Exception:
            pass
        return sheet

    def _show_template_popup_menu(self, input_field):
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
        return self._show_template_picker_sheet(active_templates)

    def _picker_pill(self, act, text, checked, on_toggle, with_checkbox=True):
        checkbox = None
        if with_checkbox:
            checkbox = CheckBox2(act, 21, None)
            checkbox.setColor(Theme.key_dialogRoundCheckBox, Theme.key_checkboxDisabled, Theme.key_dialogRoundCheckBoxCheck)
            checkbox.setDrawUnchecked(True)
            checkbox.setDrawBackgroundAsArc(10)
            checkbox.setChecked(checked, False)
            checkbox.setVisibility(1)
        container = FrameLayout(act)
        btn_bg = GradientDrawable()
        pill_radius = AndroidUtilities.dp(20)
        btn_bg.setCornerRadius(pill_radius)
        try:
            btn_bg.setColor(Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000)
        except Exception:
            btn_bg.setColor(Color.parseColor("#F0F0F0"))
        try:
            ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
            ripple_mask = GradientDrawable()
            ripple_mask.setCornerRadius(pill_radius)
            ripple_mask.setColor(Color.WHITE)
            container.setBackground(_safe_ripple(ripple_color, btn_bg, ripple_mask))
        except Exception:
            container.setBackground(btn_bg)
        inner_layout = LinearLayout(act)
        inner_layout.setOrientation(LinearLayout.HORIZONTAL)
        inner_layout.setGravity(Gravity.CENTER_VERTICAL)
        inner_layout.setPadding(AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(12), AndroidUtilities.dp(8))
        inner_layout.setMinimumHeight(AndroidUtilities.dp(40))
        if checkbox is not None:
            inner_layout.addView(checkbox, LayoutHelper.createLinear(24, 24, Gravity.CENTER_VERTICAL, 0, 0, 8, 0))
        else:
            inner_layout.setPadding(AndroidUtilities.dp(14), AndroidUtilities.dp(8), AndroidUtilities.dp(14), AndroidUtilities.dp(8))
        text_view = TextView(act)
        text_view.setText(text)
        text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
        text_view.setGravity(Gravity.CENTER_VERTICAL)
        text_view.setSingleLine(True)
        try:
            text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            text_view.setTextColor(Color.BLACK)
        inner_layout.addView(text_view)
        container.addView(inner_layout)
        def toggle(v):
            if checkbox is None:
                on_toggle(True)
                return
            value = not checkbox.isChecked()
            checkbox.setChecked(value, True)
            on_toggle(value)
        container.setOnClickListener(OnClickListener(toggle))
        self._apply_press_scale(container)
        return container, checkbox

    def _picker_row(self, act, badge, name, checked, on_toggle, on_click=None, subtitle="", center_text=False, bold_text=False):
        row = LinearLayout(act)
        row.setOrientation(LinearLayout.HORIZONTAL)
        row.setGravity(Gravity.CENTER_VERTICAL)
        row.setPadding(AndroidUtilities.dp(12), AndroidUtilities.dp(10), AndroidUtilities.dp(12), AndroidUtilities.dp(10))
        row.setClickable(True)
        row.setFocusable(True)
        try:
            row_bg = GradientDrawable()
            row_bg.setShape(GradientDrawable.RECTANGLE)
            row_bg.setCornerRadius(AndroidUtilities.dp(27))
            row_bg.setColor(Theme.getColor(Theme.key_dialogBackground))
            row.setBackground(row_bg)
        except Exception:
            pass
        if badge:
            badge_size = 34
            badge_frame = FrameLayout(act)
            try:
                badge_bg = GradientDrawable()
                badge_bg.setShape(GradientDrawable.OVAL)
                badge_bg.setColor(Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000)
                badge_frame.setBackground(badge_bg)
            except Exception:
                pass
            badge_tv = TextView(act)
            badge_tv.setText(badge)
            badge_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            badge_tv.setGravity(Gravity.CENTER)
            try:
                badge_tv.setTypeface(AndroidUtilities.bold())
                badge_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlue))
            except Exception:
                badge_tv.setTextColor(Color.BLUE)
            badge_frame.addView(badge_tv, FrameLayout.LayoutParams(-1, -1))
            row.addView(badge_frame, LayoutHelper.createLinear(badge_size, badge_size, Gravity.CENTER_VERTICAL, 0, 0, 10, 0))
        name_tv = TextView(act)
        name_tv.setText(name)
        name_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
        name_tv.setSingleLine(True)
        name_tv.setHorizontalFadingEdgeEnabled(True)
        name_tv.setFadingEdgeLength(AndroidUtilities.dp(24))
        if center_text:
            name_tv.setGravity(Gravity.CENTER)
        if bold_text:
            try:
                name_tv.setTypeface(AndroidUtilities.bold())
            except Exception:
                pass
        try:
            name_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            name_tv.setTextColor(Color.BLACK)
        text_col = LinearLayout(act)
        text_col.setOrientation(LinearLayout.VERTICAL)
        text_col.setGravity(Gravity.CENTER_VERTICAL)
        text_col.addView(name_tv, LayoutHelper.createLinear(-1, -2))
        if subtitle:
            subtitle_tv = TextView(act)
            subtitle_tv.setText(subtitle)
            subtitle_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 13)
            subtitle_tv.setSingleLine(True)
            subtitle_tv.setHorizontalFadingEdgeEnabled(True)
            subtitle_tv.setFadingEdgeLength(AndroidUtilities.dp(24))
            try:
                subtitle_tv.setTextColor(Theme.getColor(Theme.key_dialogTextGray))
            except Exception:
                subtitle_tv.setTextColor(Color.GRAY)
            text_col.addView(subtitle_tv, LayoutHelper.createLinear(-1, -2, 0, 2, 0, 0))
        row.addView(text_col, LayoutHelper.createLinear(0, -2, 1.0, Gravity.CENTER_VERTICAL))
        checkbox = None
        if on_click is None:
            checkbox = CheckBox2(act, 21, None)
            checkbox.setColor(Theme.key_dialogRoundCheckBox, Theme.key_checkboxDisabled, Theme.key_dialogRoundCheckBoxCheck)
            checkbox.setDrawUnchecked(True)
            checkbox.setDrawBackgroundAsArc(10)
            checkbox.setChecked(checked, False)
            checkbox.setVisibility(1)
            cb_lp = LinearLayout.LayoutParams(AndroidUtilities.dp(21), AndroidUtilities.dp(21))
            cb_lp.leftMargin = AndroidUtilities.dp(8)
            row.addView(checkbox, cb_lp)
            def click(v):
                value = not checkbox.isChecked()
                checkbox.setChecked(value, True)
                on_toggle(value)
        else:
            def click(v):
                on_click()
        row.setOnClickListener(OnClickListener(click))
        self._apply_press_scale(row)
        return row, checkbox

    def _picker_row_title(self, name, position):
        title = str(name or '').replace('\n', ' ').strip()
        while '  ' in title:
            title = title.replace('  ', ' ')
        return title or t('template_n', lang=self.lang, n=position + 1)

    def _picker_row_subtitle(self, text):
        value = str(text or '').replace('\n', ' ').strip()
        while '  ' in value:
            value = value.replace('  ', ' ')
        if len(value) > 60:
            value = value[:60].rstrip() + '...'
        return value

    def _picker_sheet_container(self, act, fragment, title, subtitle, sticker=None, swipe_dismiss=True):
        sheet = BottomSheet(act, swipe_dismiss, fragment.getResourceProvider() if fragment else None)
        sheet.setApplyBottomPadding(False)
        sheet.setApplyTopPadding(False)
        if not swipe_dismiss:
            sheet.setCanDismissWithSwipe(False)
        try:
            sheet.fixNavigationBar(Theme.getColor(Theme.key_dialogBackground))
        except Exception:
            pass
        outer = LinearLayout(act)
        outer.setOrientation(LinearLayout.VERTICAL)
        try:
            bg = GradientDrawable()
            bg.setShape(GradientDrawable.RECTANGLE)
            bg.setCornerRadii([AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), AndroidUtilities.dp(20), 0, 0, 0, 0,])
            bg.setColor(Theme.getColor(Theme.key_dialogBackground))
            outer.setBackground(bg)
        except Exception:
            pass
        if sticker:
            try:
                avatar_view = BackupImageView(act)
                avatar_view.setRoundRadius(AndroidUtilities.dp(45))
                try:
                    avatar_view.setTag(STICKER_TAG)
                except Exception:
                    pass
                outer.addView(avatar_view, LayoutHelper.createLinear(130, 130, Gravity.CENTER_HORIZONTAL, 0, AndroidUtilities.dp(6), 0, 5))
                self.load_sticker_with_fallback(avatar_view, sticker[0], sticker[1], "90_90")
            except Exception:
                pass
        title_tv = TextView(act)
        title_tv.setText(title)
        title_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 24)
        title_tv.setGravity(Gravity.CENTER)
        try:
            title_tv.setTypeface(AndroidUtilities.getTypeface("fonts/rmedium.ttf"))
            title_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        except Exception:
            pass
        subtitle_tv = TextView(act)
        subtitle_tv.setText(subtitle)
        subtitle_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
        subtitle_tv.setSingleLine(True)
        subtitle_tv.setGravity(Gravity.CENTER)
        try:
            subtitle_tv.setTextColor(Theme.getColor(Theme.key_windowBackgroundWhiteGrayText))
        except Exception:
            pass
        title_col = LinearLayout(act)
        title_col.setOrientation(LinearLayout.VERTICAL)
        title_col.setGravity(Gravity.CENTER_HORIZONTAL)
        title_col.addView(title_tv, LayoutHelper.createLinear(-2, -2, Gravity.CENTER_HORIZONTAL))
        if subtitle:
            title_col.addView(subtitle_tv, LayoutHelper.createLinear(-2, -2, Gravity.CENTER_HORIZONTAL, 0, 4, 0, 0))
        outer.addView(title_col, LayoutHelper.createLinear(-1, -2, PICKER_PAD_H, 12, PICKER_PAD_H, 16))
        return sheet, outer, subtitle_tv

    def _picker_show_animated(self, sheet, outer):
        try:
            outer.setAlpha(0.0)
            outer.setScaleX(0.3)
            outer.setScaleY(0.3)
            outer.setTranslationY(AndroidUtilities.dp(100))
        except Exception:
            pass
        for i in range(outer.getChildCount()):
            try:
                child = outer.getChildAt(i)
                if str(child.getTag()) == STICKER_TAG:
                    continue
                child.setAlpha(0.0)
                child.setScaleX(0.8)
                child.setScaleY(0.8)
                child.setTranslationY(AndroidUtilities.dp(30 + i * 10))
            except Exception:
                pass
        sheet.setCustomView(outer)
        sheet.show()
        def animate():
            try:
                outer.animate().alpha(1.0).scaleX(1.0).scaleY(1.0).translationY(0).setDuration(300).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
            except Exception:
                pass
            for i in range(outer.getChildCount()):
                try:
                    child = outer.getChildAt(i)
                    if str(child.getTag()) == STICKER_TAG:
                        continue
                    child.animate().alpha(1.0).translationY(0).scaleX(1.0).scaleY(1.0).setDuration(350).setStartDelay(50 + i * 50).setInterpolator(AndroidUtilities.decelerateInterpolator).start()
                except Exception:
                    pass
        run_on_ui_thread(animate)
        return sheet

    def _picker_scrolled_list(self, act, items_list, row_count, pad_h=PICKER_PAD_H, row_height_dp=54, max_height_dp=None, wrap=False, keep_scroll=True):
        items_scroll = ScrollView(act)
        items_scroll.setNestedScrollingEnabled(False)
        items_scroll.setVerticalScrollBarEnabled(False)
        items_scroll.setPadding(AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8))
        items_scroll.addView(items_list)
        try:
            items_scroll.setVerticalFadingEdgeEnabled(True)
            items_scroll.setHorizontalFadingEdgeEnabled(False)
            items_scroll.setFadingEdgeLength(AndroidUtilities.dp(20))
        except Exception:
            pass

        class _ScrollTouchListener(dynamic_proxy(View.OnTouchListener)):
            def __init__(self, keep):
                super().__init__()
                self._active = False
                self._keep = keep

            def onTouch(self, v, event):
                try:
                    action = event.getActionMasked()
                    if action == MotionEvent.ACTION_DOWN:
                        self._active = True
                        if self._keep:
                            v.getParent().requestDisallowInterceptTouchEvent(True)
                    elif action in (MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL):
                        if self._active:
                            self._active = False
                            if self._keep:
                                v.getParent().requestDisallowInterceptTouchEvent(False)
                except Exception:
                    pass
                return False

        items_scroll.setOnTouchListener(_ScrollTouchListener(keep_scroll))
        scroll_height_px = AndroidUtilities.dp(max_height_dp) if max_height_dp else min(row_count, 5) * AndroidUtilities.dp(row_height_dp)
        dark_container = FrameLayout(act)
        try:
            dark_field_color = Theme.getColor(Theme.key_windowBackgroundGray)
        except Exception:
            dark_field_color = Color.parseColor("#2C2C2C")
        dark_bg = GradientDrawable()
        dark_bg.setShape(GradientDrawable.RECTANGLE)
        dark_bg.setCornerRadius(AndroidUtilities.dp(26))
        dark_bg.setColor(dark_field_color)
        dark_container.setBackground(dark_bg)
        dark_container.addView(items_scroll, FrameLayout.LayoutParams(-1, -1))
        if wrap:
            dark_lp = LinearLayout.LayoutParams(-1, -2)
        else:
            dark_lp = LinearLayout.LayoutParams(-1, scroll_height_px + AndroidUtilities.dp(24))
        dark_lp.leftMargin = pad_h
        dark_lp.rightMargin = pad_h
        return dark_container, dark_lp

    def _picker_body_block(self, act, text, pad_h=PICKER_PAD_H, max_height_dp=300, gravity=None, link_color=None, selectable=True, keep_scroll=True):
        body_scroll = ScrollView(act)
        body_scroll.setNestedScrollingEnabled(False)
        body_scroll.setVerticalScrollBarEnabled(False)
        body_scroll.setPadding(AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8))
        try:
            body_scroll.setVerticalFadingEdgeEnabled(True)
            body_scroll.setHorizontalFadingEdgeEnabled(False)
            body_scroll.setFadingEdgeLength(AndroidUtilities.dp(20))
        except Exception:
            pass

        class _BodyTouchListener(dynamic_proxy(View.OnTouchListener)):
            def __init__(self, keep):
                super().__init__()
                self._active = False
                self._keep = keep

            def onTouch(self, v, event):
                try:
                    action = event.getActionMasked()
                    if action == MotionEvent.ACTION_DOWN:
                        self._active = True
                        if self._keep:
                            v.getParent().requestDisallowInterceptTouchEvent(True)
                    elif action in (MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL):
                        if self._active:
                            self._active = False
                            if self._keep:
                                v.getParent().requestDisallowInterceptTouchEvent(False)
                except Exception:
                    pass
                return False
        body_scroll.setOnTouchListener(_BodyTouchListener(keep_scroll))
        body_tv = TextView(act)
        body_tv.setText(text)
        body_tv.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 15)
        if selectable:
            body_tv.setTextIsSelectable(True)
        if gravity is not None:
            body_tv.setGravity(gravity)
        try:
            body_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            if link_color:
                body_tv.setLinkTextColor(Theme.getColor(link_color))
                body_tv.setMovementMethod(LinkMovementMethod.getInstance())
        except Exception:
            pass
        try:
            body_tv.setLineSpacing(AndroidUtilities.dp(4), 1.15)
        except Exception:
            pass
        body_scroll.addView(body_tv)
        dark_container, dark_lp = self._picker_scrolled_list(act, body_scroll, 1, pad_h, max_height_dp=max_height_dp, wrap=True, keep_scroll=keep_scroll)
        limit_px = AndroidUtilities.dp(max_height_dp) + AndroidUtilities.dp(24)
        if dark_lp.height == -2:
            class _CapLayoutListener(dynamic_proxy(View.OnLayoutChangeListener)):
                def onLayoutChange(self, v, left, top, right, bottom, old_left, old_top, old_right, old_bottom):
                    try:
                        if bottom - top > limit_px:
                            lp = v.getLayoutParams()
                            if lp.height != limit_px:
                                lp.height = limit_px
                                v.setLayoutParams(lp)
                    except Exception:
                        pass
            try:
                dark_container.addOnLayoutChangeListener(_CapLayoutListener())
            except Exception:
                pass
        return dark_container, dark_lp

    def _picker_icon_pill(self, act, icon_res, text, on_click, pad_h=20):
        container = FrameLayout(act)
        btn_bg = GradientDrawable()
        pill_radius = AndroidUtilities.dp(20)
        btn_bg.setCornerRadius(pill_radius)
        try:
            btn_bg.setColor(Theme.getColor(Theme.key_chat_inLoader) & 0x20FFFFFF | 0x10000000)
        except Exception:
            btn_bg.setColor(Color.parseColor("#F0F0F0"))
        try:
            ripple_color = ColorStateList.valueOf(Color.parseColor("#40000000"))
            ripple_mask = GradientDrawable()
            ripple_mask.setCornerRadius(pill_radius)
            ripple_mask.setColor(Color.WHITE)
            container.setBackground(_safe_ripple(ripple_color, btn_bg, ripple_mask))
        except Exception:
            container.setBackground(btn_bg)
        icon_view = ImageView(act)
        try:
            icon_view.setImageResource(getattr(R_tg.drawable, icon_res))
        except Exception:
            pass
        icon_view.setScaleType(ImageView.ScaleType.CENTER)
        try:
            icon_view.setColorFilter(Theme.getColor(Theme.key_dialogTextBlue))
        except Exception:
            pass
        inner = LinearLayout(act)
        inner.setOrientation(LinearLayout.HORIZONTAL)
        inner.setGravity(Gravity.CENTER_VERTICAL)
        inner.setMinimumHeight(AndroidUtilities.dp(40))
        if text:
            inner.setPadding(AndroidUtilities.dp(12), AndroidUtilities.dp(8), AndroidUtilities.dp(16), AndroidUtilities.dp(8))
            inner.addView(icon_view, LayoutHelper.createLinear(24, 24, Gravity.CENTER_VERTICAL, 0, 0, 8, 0))
            text_view = TextView(act)
            text_view.setText(text)
            text_view.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 14)
            text_view.setGravity(Gravity.CENTER_VERTICAL)
            text_view.setSingleLine(True)
            try:
                text_view.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            except Exception:
                text_view.setTextColor(Color.BLACK)
            inner.addView(text_view)
        else:
            inner.setPadding(AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8), AndroidUtilities.dp(8))
            inner.addView(icon_view, LayoutHelper.createLinear(24, 24, Gravity.CENTER))
        container.addView(inner)
        container.setClickable(True)
        container.setFocusable(True)
        container.setOnClickListener(OnClickListener(lambda *_: on_click()))
        self._apply_press_scale(container)
        return container

    def _picker_options_row(self, act, pill_views, pad_h=20):
        options_row = LinearLayout(act)
        options_row.setOrientation(LinearLayout.HORIZONTAL)
        options_row.setGravity(Gravity.CENTER_VERTICAL)
        for container in pill_views:
            options_row.addView(container, LayoutHelper.createLinear(-2, -2, Gravity.CENTER_VERTICAL, 0, 0, 8, 0))
        options_scroll = HorizontalScrollView(act)
        options_scroll.setHorizontalScrollBarEnabled(False)
        options_scroll.setOverScrollMode(View.OVER_SCROLL_NEVER)
        options_row_lp = FrameLayout.LayoutParams(-2, -2)
        options_row_lp.gravity = Gravity.CENTER_HORIZONTAL
        options_row.setLayoutParams(options_row_lp)
        options_scroll.addView(options_row)
        options_wrap = FrameLayout(act)
        options_wrap.addView(options_scroll, FrameLayout.LayoutParams(-1, -2))
        fades = {}

        def update_fades():
            try:
                max_scroll = max(0, options_row.getMeasuredWidth() - options_scroll.getWidth())
                scroll_x = options_scroll.getScrollX()
                left = fades.get('left')
                right = fades.get('right')
                if left is not None:
                    left.setVisibility(View.VISIBLE if scroll_x > 0 else View.GONE)
                if right is not None:
                    right.setVisibility(View.VISIBLE if max_scroll > 0 and scroll_x < max_scroll else View.GONE)
            except Exception:
                pass

        def center_options_row():
            try:
                lp = options_row.getLayoutParams()
                wanted = Gravity.START if options_row.getMeasuredWidth() > options_scroll.getWidth() else Gravity.CENTER_HORIZONTAL
                if lp.gravity != wanted:
                    lp.gravity = wanted
                    options_row.setLayoutParams(lp)
            except Exception:
                pass
            update_fades()

        class _OptionsLayoutListener(dynamic_proxy(View.OnLayoutChangeListener)):
            def onLayoutChange(self, v, left, top, right, bottom, old_left, old_top, old_right, old_bottom):
                center_options_row()
        try:
            options_scroll.addOnLayoutChangeListener(_OptionsLayoutListener())
        except Exception:
            pass
        class _OptionsScrollListener(dynamic_proxy(View.OnScrollChangeListener)):
            def onScrollChange(self, v, scroll_x, scroll_y, old_scroll_x, old_scroll_y):
                update_fades()
        try:
            options_scroll.setOnScrollChangeListener(_OptionsScrollListener())
        except Exception:
            pass
        try:
            bg_color = Theme.getColor(Theme.key_dialogBackground)
            transparent = Color.argb(0, (bg_color >> 16) & 0xFF, (bg_color >> 8) & 0xFF, bg_color & 0xFF)
            left_fade = FrameLayout(act)
            left_grd = GradientDrawable(GradientDrawable.Orientation.LEFT_RIGHT, [bg_color, transparent])
            left_fade.setBackground(left_grd)
            left_fade.setClickable(False)
            left_fade.setVisibility(View.GONE)
            options_wrap.addView(left_fade, FrameLayout.LayoutParams(AndroidUtilities.dp(16), -1, Gravity.LEFT))
            fades['left'] = left_fade
            right_fade = FrameLayout(act)
            right_grd = GradientDrawable(GradientDrawable.Orientation.RIGHT_LEFT, [bg_color, transparent])
            right_fade.setBackground(right_grd)
            right_fade.setClickable(False)
            right_fade.setVisibility(View.GONE)
            options_wrap.addView(right_fade, FrameLayout.LayoutParams(AndroidUtilities.dp(16), -1, Gravity.RIGHT))
            fades['right'] = right_fade
        except Exception:
            pass
        return options_wrap, center_options_row

    def _picker_button(self, act, text, on_click, pad_h=20):
        button = TextView(act)
        button.setText(text)
        button.setTextSize(TypedValue.COMPLEX_UNIT_DIP, 16)
        button.setTypeface(AndroidUtilities.bold())
        button.setGravity(Gravity.CENTER)
        button.setSingleLine(True)
        button.setPadding(0, AndroidUtilities.dp(14), 0, AndroidUtilities.dp(14))
        try:
            base_color = Theme.getColor(Theme.key_featuredStickers_addButton)
        except Exception:
            base_color = Theme.getColor(Theme.key_dialogTextBlue)
        try:
            pressed_color = Theme.getColor(Theme.key_featuredStickers_addButtonPressed)
        except Exception:
            pressed_color = base_color
        try:
            button.setBackground(Theme.createSimpleSelectorRoundRectDrawable(
                AndroidUtilities.dp(28), base_color, pressed_color))
            button.setTextColor(Theme.getColor(Theme.key_featuredStickers_buttonText))
        except Exception:
            button.setBackgroundColor(Color.BLUE)
            button.setTextColor(Color.WHITE)
        button.setOnClickListener(OnClickListener(on_click))
        self._apply_press_scale(button)
        return button

    def _build_template_picker_sheet(self, act, fragment, items, title, subtitle, button_text, extra_option_text=None, extra_option_checked=False, sticker=None, on_confirm=None):
        states = {}
        checkboxes = {}
        for item in items:
            states[item["key"]] = {"checked": True}
        sheet, outer, subtitle_tv = self._picker_sheet_container(act, fragment, title, subtitle, sticker)
        toggle_all_checkbox = [None]
        action_button = [None]

        def refresh():
            total = len(states)
            count = sum(1 for st in states.values() if st["checked"])
            subtitle_tv.setText(f"{t('selected_templates', lang=self.lang)} {count}/{total}")
            try:
                if toggle_all_checkbox[0] is not None:
                    toggle_all_checkbox[0].setChecked(count == total and total > 0, True)
            except Exception:
                pass
            try:
                button = action_button[0]
                if button is not None:
                    enabled = count > 0
                    button.setEnabled(enabled)
                    button.setAlpha(1.0 if enabled else 0.45)
            except Exception:
                pass

        items_list = LinearLayout(act)
        items_list.setOrientation(LinearLayout.VERTICAL)

        for i, item in enumerate(items):
            key = item["key"]

            def on_toggled(value, key=key):
                states[key]["checked"] = value
                refresh()

            row, checkbox = self._picker_row(act, item.get("badge", ""), item.get("name", ""), True, on_toggled)
            checkboxes[key] = checkbox
            items_list.addView(row, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 8 if i < len(items) - 1 else 0))

        def on_toggle_all(value):
            for key, st in states.items():
                st["checked"] = value
                cb = checkboxes.get(key)
                if cb is not None:
                    cb.setChecked(value, True)
            refresh()

        extra_state = {"checked": extra_option_checked}
        toggle_all_container, toggle_all_cb = self._picker_pill(
            act, t('select_all', lang=self.lang), True, on_toggle_all)
        toggle_all_checkbox[0] = toggle_all_cb
        pill_views = [toggle_all_container]
        if extra_option_text:
            def on_extra_toggled(value):
                extra_state["checked"] = value
            extra_container, _ = self._picker_pill(act, extra_option_text, extra_option_checked, on_extra_toggled)
            pill_views.append(extra_container)
        dark_container, dark_lp = self._picker_scrolled_list(act, items_list, len(items))
        outer.addView(dark_container, dark_lp)
        options_wrap, center_options_row = self._picker_options_row(act, pill_views)
        outer.addView(options_wrap, LayoutHelper.createLinear(-1, -2, PICKER_PAD_H, AndroidUtilities.dp(6), PICKER_PAD_H, AndroidUtilities.dp(2)))

        def on_button_click(v):
            selected_keys = [item["key"] for item in items if states[item["key"]]["checked"]]
            if not selected_keys:
                sheet.dismiss()
                BulletinHelper.show_error(t('no_templates_available', lang=self.lang))
                return
            extra = extra_state["checked"]
            sheet.dismiss()
            if on_confirm:
                on_confirm(selected_keys, extra)
        button = self._picker_button(act, button_text, on_button_click)
        action_button[0] = button
        outer.addView(button, LayoutHelper.createLinear(-1, -2, PICKER_BUTTON_PAD_H, PICKER_BUTTON_TOP_PAD, PICKER_BUTTON_PAD_H, 16))
        refresh()

        self._picker_show_animated(sheet, outer)
        try:
            options_wrap.post(center_options_row)
        except Exception:
            pass
        return sheet

    def _build_template_send_sheet(self, act, fragment, items, title, subtitle, button_text, on_pick, on_settings):
        sheet, outer, subtitle_tv = self._picker_sheet_container(act, fragment, title, subtitle)
        def pick(key):
            sheet.dismiss()
            if on_pick:
                on_pick(key)
        items_list = LinearLayout(act)
        items_list.setOrientation(LinearLayout.VERTICAL)
        for i, item in enumerate(items):
            def on_row_click(key=item["key"]):
                pick(key)
            row, _ = self._picker_row(act, item.get("badge", ""), item.get("name", ""), False, None, on_row_click, item.get("subtitle", ""))
            items_list.addView(row, LayoutHelper.createLinear(-1, -2, 0, 0, 0, 8 if i < len(items) - 1 else 0))
        if items:
            dark_container, dark_lp = self._picker_scrolled_list(act, items_list, len(items), row_height_dp=60, max_height_dp=340)
            outer.addView(dark_container, dark_lp)

        def on_settings_clicked(v):
            sheet.dismiss()
            if on_settings:
                on_settings()

        button = self._picker_button(act, button_text, on_settings_clicked)
        outer.addView(button, LayoutHelper.createLinear(-1, -2, PICKER_BUTTON_PAD_H, PICKER_BUTTON_TOP_PAD, PICKER_BUTTON_PAD_H, 16))
        self._picker_show_animated(sheet, outer)
        return sheet

    def _show_export_bottom_sheet(self):
        self._force_load_stickers()
        try:
            fragment = get_last_fragment()
            act = fragment.getParentActivity() if fragment else None
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
                        "text": text,
                        "rich": self._read_rich_setting(i),
                        "preview": bool(self.get_setting(f"template_linkpreview_{i}", True))
                    })
            if not templates:
                BulletinHelper.show_error(t('no_templates_available', lang=self.lang))
                return
            max_templates = min(len(templates), TEMPLATE_COUNT)
            items = [
                {
                    "key": str(position),
                    "badge": str(position + 1),
                    "name": self._picker_row_title(templates[position].get("name"), position),
                }
                for position in range(max_templates)
            ]

            def on_confirm(keys, embed_files):
                selected = []
                for key in keys:
                    try:
                        position = int(key)
                    except Exception:
                        continue
                    if 0 <= position < len(templates):
                        selected.append(templates[position])
                self._start_export(selected, bool(embed_files))

            def build():
                self._build_template_picker_sheet(
                    act, fragment, items,
                    t('export_templates', lang=self.lang),
                    t('export_question', lang=self.lang),
                    t('export', lang=self.lang),
                    t('embed_files', lang=self.lang), True, ("mr_vestr/11", 11), on_confirm)

            run_on_ui_thread(build)
        except Exception:
            pass

    def _start_export(self, selected, embed_files=True):
        try:
            account = self._account_number()
            try:
                BulletinHelper.show_success(t('export_preparing', lang=self.lang), getattr(R_tg.raw, 'done', 0))
            except Exception:
                pass

            def prepare_export():
                export_items = []
                try:
                    for template in selected:
                        export_item = {
                            "name": template["name"],
                            "text": template["text"],
                            "preview": bool(template.get("preview", True))
                        }
                        rich_payload = template.get("rich")
                        if isinstance(rich_payload, dict) and rich_payload:
                            export_item["rich"] = self._export_rich_payload(rich_payload, account, embed_files)
                        export_items.append(export_item)
                except Exception as build_error:
                    message = str(build_error)
                    run_on_ui_thread(lambda: BulletinHelper.show_error(
                        t('export_error', lang=self.lang, error=message)))
                    return
                run_on_ui_thread(lambda: self._open_export_share_alert(export_items))

            threading.Thread(target=prepare_export, daemon=True).start()
        except Exception as export_error:
            error_msg = str(export_error)
            run_on_ui_thread(lambda: BulletinHelper.show_error(t('export_error', lang=self.lang, error=error_msg)))

    def _open_export_share_alert(self, export_items):
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
                share_alert = ShareAlert(fragment.getParentActivity(), None, None, temp_file.getAbsolutePath(), None, None, False, None, None, False, False, False, None, None)
                share_alert.setDelegate(ShareDelegate(self))
                fragment.showDialog(share_alert)
        except Exception as e:
            BulletinHelper.show_error(t('export_error', lang=self.lang, error=str(e)))

    def _export_rich_payload(self, payload, account=None, embed_media=True):
        if not isinstance(payload, dict):
            return payload
        if account is None:
            account = self._account_number()
        media = payload.get("media")
        out = dict(payload)
        out_media = {}
        for key, is_document in (("photos", False), ("documents", True)):
            entries = media.get(key) if isinstance(media, dict) else None
            if not isinstance(entries, list) or not entries:
                entries = []
                try:
                    restored = rich_media_restore(payload.get(key) or [], is_document)
                    for obj in _iter_collection(restored):
                        encoded = _rich_encode(obj)
                        if isinstance(encoded, dict) and encoded.get("n"):
                            entries.append({"tl": encoded, "path": str(getattr(obj, "localPath", None) or "")})
                except Exception as e:
                    pass
            exported = []
            for entry in entries:
                if not isinstance(entry, dict) or not isinstance(entry.get("tl"), dict):
                    continue
                item = {"tl": entry["tl"], "path": str(entry.get("path") or "")}
                if embed_media:
                    try:
                        obj = _rich_decode(item["tl"])
                    except Exception:
                        obj = None
                    if obj is not None:
                        try:
                            info = rich_media_embed_file(obj, account, item["path"] or None, is_document)
                        except Exception as e:
                            info = None
                        if info:
                            item["file"] = info
                exported.append(item)
            out_media[key] = exported
        out["media"] = out_media
        return out

    def _import_rich_media_files(self, payload):
        if not isinstance(payload, dict):
            return payload
        media = payload.get("media")
        if not isinstance(media, dict):
            return payload
        account = self._account_number()
        cleaned = {}
        for key, is_document in (("photos", False), ("documents", True)):
            out_entries = []
            for entry in media.get(key) or []:
                if not isinstance(entry, dict) or not isinstance(entry.get("tl"), dict):
                    continue
                item = {"tl": entry["tl"], "path": str(entry.get("path") or "")}
                info = entry.get("file")
                try:
                    obj = _rich_decode(item["tl"])
                except Exception:
                    obj = None
                if obj is not None and isinstance(info, dict) and info.get("b64"):
                    written = rich_media_write_file(obj, str(info.get("b64") or ""), account, is_document)
                    if written:
                        item["path"] = written
                        try:
                            item["tl"] = _rich_encode(obj)
                        except Exception as e:
                            pass
                out_entries.append(item)
            cleaned[key] = out_entries
        payload["media"] = cleaned
        try:
            rich_media_register(rich_media_decode_entries(cleaned.get("photos")), rich_media_decode_entries(cleaned.get("documents")))
        except Exception as e:
            pass
        return payload

    def _apply_imported_template(self, index, item):
        if not item:
            self.set_setting(f"template_name_{index}", "")
            self.set_setting(f"template_text_{index}", "")
            self.set_setting(f"template_rich_{index}", "")
            self.set_setting(f"template_linkpreview_{index}", True)
            return "", ""
        name = str(item.get("name", "") or "")
        text = str(item.get("text", "") or "")
        rich = item.get("rich")
        payload = None
        if isinstance(rich, dict) and rich:
            try:
                payload = dict(rich)
                payload["v"] = RICH_PAYLOAD_VERSION
                payload["src"] = text
                if not str(payload.get("text") or ""):
                    payload["text"] = text
                if not payload.get("source"):
                    payload["source"] = text
                payload.setdefault("blob", "")
                payload.setdefault("entities", [])
                payload.setdefault("photos", [])
                payload.setdefault("documents", [])
                payload.setdefault("rich_ok", False)
                if payload.get("extended") and not payload.get("blob"):
                    payload["extended"] = False
                    payload["rich_ok"] = False
            except Exception:
                payload = None
        if payload is None and text:
            try:
                payload = self._compile_template_payload(index, text)
            except Exception:
                payload = None
        if payload is not None:
            payload = self._import_rich_media_files(payload)
        self.set_setting(f"template_name_{index}", name)
        self.set_setting(f"template_text_{index}", text)
        if payload is not None:
            self._write_rich_setting(index, payload)
        else:
            self.set_setting(f"template_rich_{index}", "")
        try:
            preview = item.get("preview", True)
        except Exception:
            preview = True
        self.set_setting(f"template_linkpreview_{index}", bool(preview))
        return name, text

    def _show_import_bottom_sheet(self, data, act=None):
        self._force_load_stickers()
        try:
            fragment = get_last_fragment()
            if act is None:
                act = fragment.getParentActivity() if fragment else None
            if not act:
                return
            templates = data.get("templates", []) if isinstance(data, dict) else []
            if not isinstance(templates, list):
                templates = []
            max_templates = min(len(templates), TEMPLATE_COUNT)
            if max_templates <= 0:
                BulletinHelper.show_error(t('no_templates_available', lang=self.lang))
                return
            items = [
                {
                    "key": str(position),
                    "badge": str(position + 1),
                    "name": self._picker_row_title(
                        templates[position].get("name") if isinstance(templates[position], dict) else None,
                        position),
                }
                for position in range(max_templates)
            ]

            def on_confirm(keys, clear_all):
                selected_templates = []
                for key in keys:
                    try:
                        position = int(key)
                    except Exception:
                        continue
                    if 0 <= position < len(templates):
                        selected_templates.append(templates[position])
                self._apply_import_selection(selected_templates, clear_all)

            def build():
                self._build_template_picker_sheet(
                    act, fragment, items,
                    t('import_dialog_title', lang=self.lang),
                    t('import_question', lang=self.lang),
                    t('import', lang=self.lang),
                    t('clear_all_templates', lang=self.lang), False,
                    ("mr_vestr/10", 10), on_confirm)

            run_on_ui_thread(build)
        except Exception:
            self._show_import_templates_alert(data, act)

    def _apply_import_selection(self, selected_templates, clear_all_enabled):
        try:
            if clear_all_enabled:
                self.set_setting("templates_created_count", min(max(len(selected_templates), 1), TEMPLATE_COUNT), reload_settings=True)
                self.templates = []
                for i in range(TEMPLATE_COUNT):
                    if i < len(selected_templates):
                        name, text = self._apply_imported_template(i, selected_templates[i] or {})
                    else:
                        name, text = self._apply_imported_template(i, None)
                    self.templates.append({"name": name, "text": text, "enabled": True if i == 0 else bool(name and text)})
            else:
                current_templates = self.get_setting("templates", [])
                existing_count = 0
                for i, template in enumerate(current_templates):
                    if template.get("name", "").strip() or template.get("text", "").strip():
                        existing_count = i + 1
                total_count = existing_count + len(selected_templates)
                if total_count > TEMPLATE_COUNT:
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
                    name, text = self._apply_imported_template(index, template or {})
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
        except Exception as e:
            error_msg = str(e)
            run_on_ui_thread(lambda: BulletinHelper.show_error(t('import_error', lang=self.lang, error=error_msg)))

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
                                name, text = self._apply_imported_template(i, templates[i] or {})
                            else:
                                name, text = self._apply_imported_template(i, None)
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
                        error_msg = str(e)
                        run_on_ui_thread(lambda: BulletinHelper.show_error(t('import_error', lang=self.lang, error=error_msg)))
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
            args = [get_account_instance(), arg1, arg2, None, mime, peer_id, None, None, None, None, None, None, jarray(jlong)([0]), True, caption, True, jint(0), int_array_value, True, None, jint(0), 0, False, 0, 0]
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
        return self._show_template_picker_sheet(templates)

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
            account = frag.getCurrentAccount()
            payload = self._template_payload(template_index, template_text)
            if not self._send_rich_payload(account, chat_id, payload, topic_msg_obj, topic_msg_obj):
                text_value, entities = self._plain_template_content(template_text, payload)
                try:
                    message_data = {
                        "peer": chat_id,
                        "message": text_value,
                        "entities": entities
                    }
                    if topic_msg_obj is not None:
                        message_data["replyToMsg"] = topic_msg_obj
                        message_data["replyToTopMsg"] = topic_msg_obj
                    self._send_text_message(message_data, self._template_link_preview(template_index), account)
                except Exception:
                    try:
                        from org.telegram.messenger import SendMessagesHelper as SMH
                        smh = SMH.getInstance(account)
                        params = SMH.SendMessageParams.of(text_value, chat_id)
                        params.entities = entities
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
        constructor = ChatActivityEnterView.getClass().getDeclaredConstructor(Activity, SizeNotifierFrameLayout, ChatActivity, jclass("java.lang.Boolean").TYPE, ResourcesProvider)
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

def _tv_list_sizes(adapter):
    parts = []
    try:
        for f in adapter.getClass().getDeclaredFields():
            try:
                if 'List' not in f.getType().getSimpleName():
                    continue
                f.setAccessible(True)
                v = f.get(adapter)
                if v is None:
                    parts.append(f"{f.getName()}=null")
                else:
                    parts.append(f"{f.getName()}={v.size()}")
            except Exception:
                pass
    except Exception:
        pass
    return ", ".join(parts) if parts else "none"


def _tv_dump_internals(container, adapter):
    if getattr(_tv_dump_internals, "done", False):
        return
    _tv_dump_internals.done = True
    try:
        pass
    except Exception as e:
        pass
    try:
        lp = container.getLayoutParams()
    except Exception as e:
        pass
    try:
        parts = [f"{f.getName()}:{f.getType().getSimpleName()}"
                 for f in container.getClass().getDeclaredFields()]
    except Exception as e:
        pass
    try:
        lv = container.listView
        lv_lp = lv.getLayoutParams()
    except Exception as e:
        pass
    try:
        parts = [f"{f.getName()}:{f.getType().getSimpleName()}"
                 for f in adapter.getClass().getDeclaredFields()]
    except Exception as e:
        pass
    try:
        parts = [f"{m.getName()}({len(m.getParameterTypes())})"
                 for m in adapter.getClass().getDeclaredMethods()]
    except Exception as e:
        pass
    try:
        parts = [f"{m.getName()}({len(m.getParameterTypes())})"
                 for m in container.getClass().getDeclaredMethods()]
    except Exception as e:
        pass


def _tv_read_field(obj, name):
    k = obj.getClass()
    while k is not None:
        try:
            f = k.getDeclaredField(name)
            f.setAccessible(True)
            return f.get(obj)
        except Exception:
            k = k.getSuperclass()
    raise AttributeError(f"field {name} not found")


def _tv_item_count(adapter):
    if adapter is None:
        return "none"
    for name in ("getItemCount", "getCount"):
        try:
            return getattr(adapter, name)()
        except Exception:
            continue
    return "?"


def _tv_probe_layout(container, adapter=None, label="probe"):
    def probe(tag):
        lv = None
        lv_adapter = None
        try:
            lv = container.listView
        except Exception as e:
            pass
        try:
            lp = container.getLayoutParams()
            lp_info = "none" if lp is None else (
                f"{lp.getClass().getSimpleName()} w={getattr(lp, 'width', '?')} "
                f"h={getattr(lp, 'height', '?')}")
        except Exception as e:
            pass
        for field in ("dismissed", "entering", "scrollYOffset"):
            try:
                pass
            except Exception as e:
                pass
        if lv is not None:
            try:
                lv_adapter = lv.getAdapter()
                same = "n/a" if adapter is None else str(lv_adapter is not None and lv_adapter == adapter)
            except Exception as e:
                pass
            try:
                lm = lv.getLayoutManager()
            except Exception as e:
                pass
        chain = []
        try:
            p = container.getParent()
            while p is not None and len(chain) < 5:
                chain.append(p.getClass().getSimpleName())
                p = p.getParent()
        except Exception as e:
            pass

    def first():
        probe(f"{label}#1")
        try:
            container.postDelayed(lambda: probe(f"{label}#2"), 450)
        except Exception:
            try:
                run_on_ui_thread(lambda: probe(f"{label}#2"), delay=450)
            except Exception:
                pass
    try:
        container.post(first)
    except Exception:
        try:
            run_on_ui_thread(first)
        except Exception:
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
        _tv_dump_internals(bot_container, bot_adapter)
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
        new_result_ephemeral = None
        try:
            ephemeral_field = bot_adapter.getClass().getDeclaredField("newResultEphemeral")
            ephemeral_field.setAccessible(True)
            new_result_ephemeral = ephemeral_field.get(bot_adapter)
        except Exception:
            pass
        new_result.clear()
        new_result_help.clear()
        if new_result_ephemeral is not None:
            new_result_ephemeral.clear()
        for index, cmd in enumerate(commands):
            new_result.add(cmd)
            new_result_help.add(descriptions[index])
            if new_result_ephemeral is not None:
                new_result_ephemeral.add(False)
        try:
            pass
        except Exception as e:
            pass
        bot_adapter.notifyDataSetChanged()
        try:
            pass
        except Exception:
            pass
        plugin_ref = weakref.ref(self)
        class ClickListener(dynamic_proxy(RecyclerListView.OnItemClickListener)):
            def onItemClick(self, view, position):
                plugin = plugin_ref()
                if not plugin:
                    return
                try:
                    has_command = hasattr(view, 'getCommand')
                    command = view.getCommand() if has_command else None
                    setting = (plugin.templates_view_current_settings.get(str(command)) if command is not None else None)
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
                enter_view_width = enter_view.getWidth()
                container_params = bot_container.getLayoutParams()
                list_params = bot_container.listView.getLayoutParams()
                if enter_view_width > 0:
                    if container_params:
                        container_params.width = enter_view_width
                        bot_container.setLayoutParams(container_params)
                    if list_params:
                        list_params.width = enter_view_width
                        bot_container.listView.setLayoutParams(list_params)
            except Exception as e:
                pass
            bot_container.requestLayout()
        except Exception as e:
            pass
        self.templates_view_custom_container = bot_container
        bot_container.show()
        _tv_probe_layout(bot_container, bot_adapter, "after-show")
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
            try:
                if self.templates_view_custom_container.isShown():
                    pass
            except Exception:
                pass
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
