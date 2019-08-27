from telegram import Bot, Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, MessageHandler

import requests

from config import REQUEST_KWARGS, TOKEN

updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)


############################### Функции ############################################

def start(bot, update):
  update.message.reply_text(text='В нашем сервисе вы найдете все что нужно: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                            parse_mode='HTML',
                            reply_markup=start_keyboard())

def open_start_page(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите вид товара: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=start_keyboard())

def help(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=' Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: Выберите вид товара: ',
                        # parse_mode='HTML',
                        reply_markup=help_keyboard())

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите вид товара: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=main_menu_keyboard())

# Функции кругов

def kr_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите вид круга: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=kr_menu_keyboard())

def kr_kr_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите колличество красных кругов: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=kr_kr_volume_keyboard())

def kr_sn_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите колличество синих кругов: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=kr_sn_volume_keyboard())

# Функции квадратов

def kv_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите вид кводратов: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=kv_menu_keyboard())

def kv_kr_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите колличество красных квадратов: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=kv_kr_volume_keyboard())

def kv_sn_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите колличество синих квадратов: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=kv_sn_volume_keyboard())


# Функции треугольников

def tr_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите вид треугольника: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=tr_menu_keyboard())

def tr_kr_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите количества красных треугольников: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=tr_kr_volume_keyboard())

def tr_sn_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Выберите колличество синих треугольников: <a href="https://telegram.org/img/t_logo.png">&#8205;</a>',
                        parse_mode='HTML',
                        reply_markup=tr_sn_volume_keyboard())


############################ Клавиатуры #########################################

def start_keyboard():
  keyboard = [[InlineKeyboardButton('Перейти к выбору товара', callback_data='main')],
              [InlineKeyboardButton('Помощь', callback_data='help')]]
  return InlineKeyboardMarkup(keyboard)

def help_keyboard():
  keyboard = [[InlineKeyboardButton('Назад', callback_data='open_start_page')]]
  return InlineKeyboardMarkup(keyboard)

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Товар Круг', callback_data='kr1')],
              [InlineKeyboardButton('Товар Квадрат', callback_data='kv2')],
              [InlineKeyboardButton('Товар Трекгольник', callback_data='tr3')],
              [InlineKeyboardButton('Назад', callback_data='open_start_page')]]
  return InlineKeyboardMarkup(keyboard)


# Клавиатуры товаров

#Меню кругов

def kr_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Красный круг', callback_data='kr_kr_vol')],
              [InlineKeyboardButton('Синий круг', callback_data='kr_sn_vol')],
              [InlineKeyboardButton('Вернуться в начало', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

#Меню количества кругов

def kr_kr_volume_keyboard():
  keyboard = [[InlineKeyboardButton('Мало красных кругов', callback_data='kr_vol_1')],
              [InlineKeyboardButton('Средне красных кругов', callback_data='kr_vol_2')],
              [InlineKeyboardButton('Много красных кругов', callback_data='kr_vol_3')],
              [InlineKeyboardButton('Назад', callback_data='kr1')]]
  return InlineKeyboardMarkup(keyboard)

def kr_sn_volume_keyboard():
  keyboard = [[InlineKeyboardButton('Мало синих кругов', callback_data='kr_vol_1')],
              [InlineKeyboardButton('Средне синих кругов', callback_data='kr_vol_2')],
              [InlineKeyboardButton('Много синих кругов', callback_data='kr_vol_3')],
              [InlineKeyboardButton('Назад', callback_data='kr1')]]
  return InlineKeyboardMarkup(keyboard)

#Меню квадратов

def kv_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Красный квадрат', callback_data='kv_kr_vol')],
              [InlineKeyboardButton('Синий квадрат', callback_data='kv_sn_vol')],
              [InlineKeyboardButton('Вернуться в начало', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

#Меню количества квадратов

def kv_kr_volume_keyboard():
  keyboard = [[InlineKeyboardButton('Мало красных квадратов', callback_data='kv_vol_1')],
              [InlineKeyboardButton('Средне красных квадратов', callback_data='kv_vol_2')],
              [InlineKeyboardButton('Много красных квадратов', callback_data='kv_vol_3')],
              [InlineKeyboardButton('Назад', callback_data='kv2')]]
  return InlineKeyboardMarkup(keyboard)

def kv_sn_volume_keyboard():
  keyboard = [[InlineKeyboardButton('Мало синих квадратов', callback_data='kv_vol_1')],
              [InlineKeyboardButton('Средне синих квадратов', callback_data='kv_vol_2')],
              [InlineKeyboardButton('Много синих квадратов', callback_data='kv_vol_3')],
              [InlineKeyboardButton('Назад', callback_data='kv2')]]
  return InlineKeyboardMarkup(keyboard)

#Меню треугольников

def tr_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Красный треугольник', callback_data='tr_kr_vol')],
              [InlineKeyboardButton('Синий треугольник', callback_data='tr_sn_vol')],
              [InlineKeyboardButton('Вернуться в начало', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

#Меню количества треугольников

def tr_kr_volume_keyboard():
  keyboard = [[InlineKeyboardButton('Мало красных треугольников', callback_data='tr_vol_1')],
              [InlineKeyboardButton('Средне красных треугольников', callback_data='tr_vol_2')],
              [InlineKeyboardButton('Много красных треугольников', callback_data='tr_vol_3')],
              [InlineKeyboardButton('Назад', callback_data='tr3')]]
  return InlineKeyboardMarkup(keyboard)

def tr_sn_volume_keyboard():
  keyboard = [[InlineKeyboardButton('Мало синих треугольников', callback_data='tr_vol_1')],
              [InlineKeyboardButton('Средне синих треугольников', callback_data='tr_vol_2')],
              [InlineKeyboardButton('Много синих треугольников', callback_data='tr_vol_3')],
              [InlineKeyboardButton('Назад', callback_data='tr3')]]
  return InlineKeyboardMarkup(keyboard)


############################# Регистрация обработчиков #########################################


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(help, pattern='help'))
updater.dispatcher.add_handler(CallbackQueryHandler(open_start_page, pattern='open_start_page'))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))

# Товары
updater.dispatcher.add_handler(CallbackQueryHandler(kr_menu, pattern='kr1'))
updater.dispatcher.add_handler(CallbackQueryHandler(kr_kr_volume_menu, pattern='kr_kr_vol'))
updater.dispatcher.add_handler(CallbackQueryHandler(kr_sn_volume_menu, pattern='kr_sn_vol'))

updater.dispatcher.add_handler(CallbackQueryHandler(kv_menu, pattern='kv2'))
updater.dispatcher.add_handler(CallbackQueryHandler(kv_kr_volume_menu, pattern='kv_kr_vol'))
updater.dispatcher.add_handler(CallbackQueryHandler(kv_sn_volume_menu, pattern='kv_sn_vol'))

updater.dispatcher.add_handler(CallbackQueryHandler(tr_menu, pattern='tr3'))
updater.dispatcher.add_handler(CallbackQueryHandler(tr_kr_volume_menu, pattern='tr_kr_vol'))
updater.dispatcher.add_handler(CallbackQueryHandler(tr_sn_volume_menu, pattern='tr_sn_vol'))


updater.start_polling()
updater.idle()
