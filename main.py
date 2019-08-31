from telegram import Bot, Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, MessageHandler, Filters

from geopy.distance import vincenty

from config import REQUEST_KWARGS, TOKEN

import locations

updater = Updater(TOKEN)


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
                        reply_markup=help_keyboard())
                        
def let_geo(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Предоставьте данные о вашей локации, что бы бот мог определить расположение близжайшего склада с нужным товаром.\n\n Для этого нажмите сюда >>> /location <<<  или введите эту команду в ручную \n\n (Это совершенно безопасно и анонимно)',
                        reply_markup=let_geo_keyboard())
                          
def request_location(bot, update):
  bot.send_message(chat_id=update.message.chat_id,
                        text='Нажмите на кнопку: \n\n Отправить геолокацию',
                        reply_markup=request_location_keyboard())
                        
def location_handler(bot, update):
	lat=update.message.location.latitude
	lon=update.message.location.longitude
	distance=[]
	for m in locations.LOCATIONS:
		result = vincenty((m['latitude'], m['longitude']), (lat, lon)).kilometers
		distance.append(result)
	index = distance.index(min(distance))
	bot.send_message(chat_id=update.message.chat_id, text='Близжайший склад')
	bot.send_venue(chat_id=update.message.chat_id,latitude=locations.LOCATIONS[index]['latitude'],longitude=locations.LOCATIONS[index]['longitude'],title=locations.LOCATIONS[index]['title'],address=locations.LOCATIONS[index]['adress'])
	bot.send_message(chat_id=update.message.chat_id, text='Для получения точного описания расположения + фото склада необходимо оплатить указанную цену по реквизитам: \n\n QIWI: +71234567890 \n\n Карта: 9876 5432 1123 4567 \n\n Что бы бот определил что оплату произвели именно вы, необходимо: \n\n В комментарии к платежу укажите +++ваш_комментарий(Обратите внимание комментарий необходимо начать с трех плюсов, это важно!) \n Например: +++ 24061941 \n\n После перевода средств отправьте этот комментарий боту и он моментально скинет все что нужно в ответ.\n\n\n Если забыли цену жмите сюда /price ')
	
def send_price(bot. update):
    bot.send_message(chat_id=update.message.chat_id, text='Санкт-Петербург:\n\n Круги 1000\n\nКвадраты 2000\n\nТреугольники 3000')

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
  
def let_geo_keyboard():
  keyboard = [[InlineKeyboardButton('Помощь', callback_data='let_geo')]]
  return InlineKeyboardMarkup(keyboard)
  
def request_location_keyboard():
	keyboard=[[KeyboardButton('Отправить геолокацию', request_location=True)]]
	return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

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
  keyboard = [[InlineKeyboardButton('Мало красных кругов', callback_data='let_geo')],
              [InlineKeyboardButton('Средне красных кругов', callback_data='let_geo')],
              [InlineKeyboardButton('Много красных кругов', callback_data='let_geo')],
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
updater.dispatcher.add_handler(CallbackQueryHandler(let_geo, pattern='let_geo'))
updater.dispatcher.add_handler(CommandHandler('location', request_location))
updater.dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

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
