from telegram import KeyboardButton, ReplyKeyboardMarkup
import globals


def send_main_menu(context, chat_id, lang_id, message_id=None):
    buttons = [
        [KeyboardButton(text=globals.BTN_ORDER[lang_id])],
        [KeyboardButton(text=globals.BTN_MY_ORDERS[lang_id]), KeyboardButton(text=globals.BTN_EVOS_FAMILY[lang_id])],
        [KeyboardButton(text=globals.BTN_COMMENTS[lang_id]), KeyboardButton(text=globals.BTN_SETTINGS[lang_id])]
    ]
    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=globals.TEXT_MAIN_MENU[lang_id],
            reply_markup=ReplyKeyboardMarkup(
                keyboard=buttons,
                resize_keyboard=True
            )
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text=globals.TEXT_MAIN_MENU[lang_id],
            reply_markup=ReplyKeyboardMarkup(
                keyboard=buttons,
                resize_keyboard=True
            )
        )