import telebot
import config

from random import randint
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

pictureThemesMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
themesButton = types.KeyboardButton("THEMES")
pictureThemesMarkup.add(themesButton)


@bot.message_handler(content_types=['text'], commands=['start', 'help'])
def handle_start_help(message):
    if message.text == "/start":
        bot.send_sticker(message.chat.id, sticker=config.StartSticker)
        bot.send_message(message.chat.id,
                         text="Hello, {0.first_name}!\nI am <b>{1.first_name}</b>, and I am <b>Picture Bot</b>. \nI hope I can help you somehow. ❤️".format(
                             message.from_user, bot.get_me()), parse_mode='HTML', reply_markup=pictureThemesMarkup)
    if message.text == "/help":
        bot.send_sticker(message.chat.id, sticker=config.HelpSticker)
        bot.send_message(message.chat.id, text="Choose theme and I will send you a picture!",
                         reply_markup=pictureThemesMarkup)


@bot.message_handler(content_types=['text'])
def message_checker(message):
    if message.chat.type == 'private':
        if message.text == 'THEMES':
            choosing_theme(message)
        else:
            error(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        send_photo(call)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=":3",
                              reply_markup=None)
    except Exception as e:
        print(repr(e))


def error(message):
    bot.send_message(message.chat.id, text="Sorry, unknown command, please, check your input.")


def choosing_theme(message):
    themes_markup = types.InlineKeyboardMarkup(row_width=1)
    themes = config.themes
    for i in range(len(themes)):
        item = types.InlineKeyboardButton(themes[i], callback_data=str(i))
        themes_markup.add(item)

    bot.send_message(message.chat.id, text="Choose your fighter! :3", reply_markup=themes_markup)


def send_photo(call):
    ID = call.message.chat.id
    match call.data:
        case "0":
            bot.send_photo(ID, config.links_to_GM_pics[randint(0, len(config.links_to_GM_pics) - 1)])

        case "1":
            bot.send_photo(ID, config.links_to_GN_pics[randint(0, len(config.links_to_GN_pics) - 1)])

        case "2":
            bot.send_photo(ID, config.links_to_GTS_pics[randint(0, len(config.links_to_GTS_pics) - 1)])

        case "3":
            bot.send_photo(ID, config.links_to_HAU_pics[randint(0, len(config.links_to_HAU_pics) - 1)])

        case "4":
            bot.send_photo(ID, config.links_to_YAA_pics[randint(0, len(config.links_to_YAA_pics) - 1)])

        case "5":
            bot.send_photo(ID, config.links_to_IMU_pics[randint(0, len(config.links_to_IMU_pics) - 1)])

        case "6":
            bot.send_photo(ID, config.links_to_confused_pics[randint(0, len(config.links_to_confused_pics) - 1)])

        case "7":
            bot.send_photo(ID, config.links_to_LU_pics[randint(0, len(config.links_to_LU_pics) - 1)])

        case "8":
            bot.send_photo(ID, config.links_to_DBU_pics[randint(0, len(config.links_to_DBU_pics) - 1)])

        case "9":
            bot.send_photo(ID, config.links_to_JRCP[randint(0, len(config.links_to_JRCP) - 1)])


bot.polling(none_stop=True)
