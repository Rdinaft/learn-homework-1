"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem, datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import key

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Enter planet name:'
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_planet = update.message.text.capitalize()
    time_now = datetime.datetime.now()
    if user_planet in str(ephem._libastro.builtin_planets()):
        planet = getattr(ephem, user_planet)(time_now)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Now, {user_planet} is in {const[1]} constellation')
    else:
        update.message.reply_text('Try another')


def main():
    mybot = Updater(key.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
