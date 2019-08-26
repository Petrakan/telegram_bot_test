from telegram import Bot, Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

from config import REQUEST_KWARGS, TOKEN

updater = Updater(TOKEN)




############################### Функции ############################################
def start(bot, update):
  update.message.reply_text('Выберите вид товара',
                            reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите вид товара',
                        reply_markup=main_menu_keyboard())


# Функции кругов

def kr_menu(bot, update):
  query = update.callback_query
  bot.send_photo(chat_id=query.message.chat_id,
                 photo='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAKAAdwMBIgACEQEDEQH/xAAcAAAABwEBAAAAAAAAAAAAAAAAAQIDBQYHBAj/xAA+EAACAQMDAQUFBQYEBwEAAAABAgMABBEFEiExBhNBUWEiMnGBkQcUI6HBFUJisdHhM0NSgiRTcqLC8PEW/8QAGQEAAwEBAQAAAAAAAAAAAAAAAAECAwQF/8QAIxEAAgICAgIBBQAAAAAAAAAAAAECEQMhEjEEUUETMkJSYf/aAAwDAQACEQMRAD8A09eDzSiaIihjNWZBMPGjQ0fhSelACh1oeNFzRgUDAao3aLt3Kt+dL7N2yXd0rFHmlBKBv4ADliOcnp8asHbC/k07s7eTQlu/cLDFg4O52C5+QJPyqL7HaNa2NsWiXfIyDe/mfKssmTiVGDm6M11vtX2yhnZLvU5rc59yGNEAPyXP50vTftS7Q2LRC6NtfxJ7wkj2O3+5f54rX73SNNu4mS5gUhutUvtB9nGiyRZsVeGZgTkyHGfpWcc6X3FvxZfiy0di+1ll2r09p7ZHhuIdq3ML/wCWxzjB8QcHB9OgqxVgWhi77D9qbO4a4X7u8qwXQB9kxMcEn4dflW+fA5FbxkpK0ZuLi6YsHFDo1FSsZqgDbFFSc4NHQITnIpNGR9KPgigAqM4IzScZoelAg6MUCKMUDKz2ygOo2TWm8RhJ4ivPLsevyAbPyp+edtMsoUto09lQBu3YwB/CCTXZqK7JixHv9D8AM/yFLgcNCUyB+Vedlbc2mehjjHimiAtO1ltcN3EgU+0U7yPwYHBUggEc0u+1O0WN0klVXBx7bbcV2wrYfe5DGFkuFzk53bT5DPQ1Uda05b/XNSkUbZ41jCSr1HGfEEc8+FZy26vRorS/pXNXtJL7WbO3g9qSe6jVSpDY9sZJ/nW4H2iT61k32f6XL/8As3ku9sn3aFpAUxgE+yvTjOCfpWrqcV2+NGoHBmdztigKPpRZ5o88V0GYRyeaFGrZ4oUCCx4UCMGjPJomOeKAEnrQ6mnEjZlzjAPTNKEWDxzQAkISBmnBEoGCDn1pRG2PJHI5pQJck460Dorus3Ci/Ntn/DiVj8WJ/oK4J3ZoH7vJkxhVDYLH9Kd7SQFdZlkUf4lvGR8QWB/LbUNFqiwsO/A2r++PD4152bc3Z3Y3UDi1C11dbGGCdLeKRW3KBsJHIJIbO7J55AznFVXs/qNxbXeoGV5Hcj8RmJ9cDnx4q8apqml3VuSHWQqCV5zVKM01x31vGhihlcZbbyF8alQcnxSKlkjBXZcvsst5Wg1TU5chbmVY48jqE3EkfN/yNXvjFQvZ+901LK2sbANCqIFjjfqfPnxOck+dTPSvRhDhFRPPlNTk5CkPFGSKRnijzmqEGw8aOknyoUxDvSgF3NxQxxS4Bl6RSH9gKbSAR60kJt91sDyPhTvQU2wDEleG8R51KKCPtBt3gpzzmuO7mutpisYyrdO9YDj4CnnYg5Xx4p9Dl39Dx9BVdEvZQ4/2hLGlzqLPIYnKsX67GHPyDKvwyaitasjEdyKzqejKOR8a0i4gTay7Rgk5BGeDWf6k66dqs9uz8RsNiHPtKeR+grk8mKT5G+BuuJWHhWPMjqMjnJ4+tSHZns7camovrgFYrj3Af+WOh+fJ+lSum6O+v6lEl0gSyB3vGP31HOD8eB860UW6RoxVVAUfICr8X9mZ+RH4Ktd6Xb2tzapbhllhxISc7T1Uc+eccegqbiMgtla4dWPiwGBUZpNnc3cX3i8lOHbcFY9TnIPwA8Klp7ZZECMCUBBCeBx4n+ldkjkgn2H0OCKA4NNQybtyscspwfh4U7moNUwyc9KFJ3AUVAzqpy26tnrSWpCybbqFD++SPypFHYxx1pDKGOQcN50HKj3z7J+lNsGQZT2l8s8ilRTGJXKzIGODu5FOROWZJOcMgJHrXNeSLt7xjjb446+lPWYIgjR/eC81T6M12dM43pxVD7ZWhh1W01GXeI5F7iTagPIyy+oJBbpnpzV3L92cN7prh7SxLPocsnBkt8TKR19k5P1GfrWeSNwaNIOpWM9mLdVimnRAqu2xAPIdT68n8q7dTfftsQTukH4hH7qf3p62jGn6dEjklo0APmzeP1Oa4bWOQyvLKcySnk+XpRihURZZWzvUIsaRRgBQMEDyo2DAcDAoRAZJAPlmlkj1q/kkisCO+ceLRg4+Z/rTpNNXssAvIlQgzNkdegHJ/Sl7xgZpshABo6bJwc0KAskOTxXNcyJEitJkOrblYdKO5uBBLEpAIkJ53DK48ceI8PTIpU0ksJ/ERZIieuKRZ3qyyINvKsM02YdhzE5Uf6TyKas5klQiA4C8bcdK6CfZJYgY6kc0iu0cN3D3yMGG05BOD1wc0q3b2VY9SOafVC53bWC/xdT8q5p9yA9ypPPFUn8ENVsfk2uuCeaaihL5glAeNvPy8aiUubq6lKRqyjoc5GK7i7WkMgZ9zBcD4n+w/Oq40SpWx3vTfXch/wAmI7V/ibxNHJIkEckjnCopZifADkmkR4t7aCFT+JIef1rh1MX1y3c6cigbwJJpcbVGRng+9xSBsmbYDuFwzZPtHdzyeT/OlSLleRuU+VMsJAPwwH+BFc6XZEhWY4B46UqZfL2IuoYk2SCIKUORgfWmmOGyemaaur8AywycFQc/TP8AI0ed4GSelOSoztN6HmIIBFCmckcGhSApkHbez1jt3+z4lBtPu8ltbz8/iSZVyf8ApOwgfD14vmmXoYfdpyCV90nxH9a8tx3E8E0dxbTPFNEwdHU8qw6Gt47L69F2k0aLUIdqTqdlzGP8t/6HqP7UqHGTqy6PBHF7cZKhjzg9PWh3Mjtl7jKDoB1NRkOoex3c2SCMZril16WxIhSz+8zscJI1yix/POMH05pPSLstRIiTCkk46k5NNRpuGWJznpUPCLi3tzearcqkjdI0OQPQedO2+oSyL+HA58jimuhcvZLphHzUfqcQR43GNhbcUwSSeP6Cm3ubhcb1KsemfCkjJO92LMfE/pWOTLxdLs1ji5K30Isr64WRfvVsJpTnaYgDsHkD/P8AOphriGSEOrgqw4OPy/tVY1HVHsO8uUhE0KIS8YO1iRghh4Hp0yOlUW07dX01rPK6x/j3Mkkarn2I+AB+R/OnhfN7ZGZ/TVmorMHlYxkCRPeUHrURrOoRR3x/EwrRByo65yc1D6PrSaZp76lq7BHlG6KAPl5TgYPPQYxVP1DWZb28kuWRpHl91YeVX0B8ePE11Jxi9s5ZOUo6RP6hrMT6lcMj74xxjwJxirqrZAI8Rms/7GdmpLorquozRvAx3x28bZ5z++enGMFfr5Vf1frmpnNSqgxRkr5AbmhTbnHQkH0oVJoeZcHPpUt2X7Q3fZjVVvbQd5Gw23FuxwsqeXofI1FLSW9rIHlVNCT2eitL1TTtc04ajpM3fWx4kQ+/C3+lh5/+iontJZNPbl4eVxzisX0TWb7QL4XmmzNE3R1U8SL5MPGtG0/tzb3qhpFELnhgPdz8PD+XrUNJqi7raIePXNX0aX/gb2eIqeEJ3IP9pyPyqW0rtr221q4FrY3UO4Y3SGKNQgPicj0PAGad1O30/VRuVe6lPOUHB+NDsto0ej/f9SvJANkYWFsEHzb/AMR9a5pJ44tm2Nqcki+xXE0biK5uXuZ44lMsjqBu684HAyQeBSzqMbouHCsTgbvOqr+1ZLfSS/eJ+0r5l2rJ0yThFyOgGck+pNcra1G+r6Xo/cSRM07Ryux5cImS6nnIY+NcseT2drpaOjtfez3EMWm2AEl3ev3cSBhk8ZPp0yao1zpGsaZJbWdzo9wu4iKED2hIc4xuHBJPP59K07RNKhfWbnWGO4x5t4FP7ni7fE5A+R86f7Wb2sIQuqtpoEnEgBAeTB2Kzfurkcn9a6sUXGN+ziztSlXoxDTr+yk1KN9QVmywy/UfXyrSttnaRMcO+VEkBWMsOPeBIHAOR8eazC6tW/Yt6xtreMwaiqMQp7xdyt7AP+gbemM5qZ0zVC+jRuzv3sWY3IYg9CM56AdDRlh8muKdLiaXY6jbWs4e0B7i4CzFPJSQGOPNTg/AkeFWRzgmsz0eB5IrdbVjciGzkV5I8kyIx27gOuOQcYzj4VokMjtbwmUbZTGpfIxhsDNPDdUzLOknZ0DDLjxoUxIQDkUdbWYHmkOQaPd4ik7QfQ0XI4NaAK4x86TnnIJFFmhmkM7rXWL+0IEM7ADoM8CrVo/aZ9Ut7fQpLd2lllJaRDxJnk7gfIA/EgetUjHiKEbSRSCSJ2R1OQynBBqZQUkVCXFmlzaibntLulKG30uMsUA2gucqAfh+lRPZa7XUe1d1qc4AisoXZFOSOQV5+RY/Sqet7dr32LiT8fHe+1nvMdM+dNxTzQbxDK8YkXa+xsbl8jWCwVezoeZNl3+zu5vr37QO/tnkS3kaWS5CE7DGFO3I8eSoHjzWr9pMyaRPH9wW/EhRGtiue8BYA/Agc58Dz4VU/sasLaLs7cX8eTdTztHKT+6q42r/AN2fn6VdbzHcSGS7ktFUEmWMqCvr7QI/KtulRzye7MCcQtpWsKjyti4geJ2DYKe3kMTxu93rycHHjTHdCPs8sqo6zG9Kl8Y3oYxhQfqfTPHWpaQT912nZ3izG9tLJhWIdu9wGGfAltxz1zXJfGQ9mC8xG06h7KquCCYs5PyA46+poKs2bRLO3tYEuIbP7rJPEheIE4TjgYPQ+fqKkZGB6c4rj05x+yrfbP357pfxsEd4fE888nP/AMp1GXBB60dGTd9ii5xjxoU1IxHT8qFOyTzr1HqKQ1HQxnJHgMmrLE0KPbmi6GkMMHFGWFINFQKhRNJo8UMUDNH+xvWTBf3Wjuo23CmeNh1DKOR9OflWp3jOYHeKJZZF9pUYA5IrE/stuIrftjbCZSTNFLFGf9LFc8/IEfOtr7zA4HFZy7BmISrA2oa8IopoW7likbFsxEONysR4Dkc+lR85R+zM0m1lc34BkxwR3Z9nPx5x+tXztz2VuJtRbV9LV5pbnEdxAZFUDgbWBJHHsjI8+fOq3pHY3UJb2FL1IYIzIpZjdRFgoPIADEk8UaHZq2nPIunWu+3SBu5X8Bc4j44X5DAo33K+4Hg0GkJ3ZPU5+dJLYXGOtK7IaBuynB+tCmSWj6H50KVsR//Z')
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите вид круга:',
                        reply_markup=kr_menu_keyboard())

def kr_kr_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите колличество красных кругов: ',
                        reply_markup=kr_kr_volume_keyboard())

def kr_sn_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите колличество синих кругов: ',
                        reply_markup=kr_sn_volume_keyboard())

# Функции квадратов

def kv_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите вид квадрата:',
                        reply_markup=kv_menu_keyboard())

def kv_kr_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите колличество красных квадратов: ',
                        reply_markup=kv_kr_volume_keyboard())

def kv_sn_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите колличество синих квадратов: ',
                        reply_markup=kv_sn_volume_keyboard())

# Функции треугольников

def tr_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите вид треугольника:',
                        reply_markup=tr_menu_keyboard())

def tr_kr_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите колличество красных треугольников: ',
                        reply_markup=tr_kr_volume_keyboard())

def tr_sn_volume_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text= 'Выберите колличество синих треугольников: ',
                        reply_markup=tr_sn_volume_keyboard())



############################ Основное меню #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Товар Круг', callback_data='kr1')],
              [InlineKeyboardButton('Товар Квадрат', callback_data='kv2')],
              [InlineKeyboardButton('Товар Трекгольник', callback_data='tr3')]]
  return InlineKeyboardMarkup(keyboard)

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


############################# Handlers #########################################

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))

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
