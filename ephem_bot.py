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
import logging
import ephem

from datetime import datetime
# import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="bot.log",
)


PROXY = {
    "proxy_url": "socks5://t1.learn.python.ru:1080",
    "urllib3_proxy_kwargs": {"username": "learn", "password": "python"},
    "read_timeout": 6,
    "connect_timeout": 7,
}


def greet_user(bot, update):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(text)


def planet(bot, update):
    user_text = update.message.text
    print("planet", user_text)
    print(user_text.split(" "))
    if user_text. len(user_text.split(" ")) != 2:
        update.message.reply_text("enter valid planet name")
        return

    planet_name = user_text.split(" ")[1].capitalize()
    try:
        planet_obj = getattr(ephem, planet_name)(datetime.now().strftime("%d/%m/%Y"))
    except AttributeError:
        update.message.reply_text("enter valid planet name")
        return
    planet_obj.compute()
    planet_constellation = ephem.constellation(planet_obj)
    update.message.reply_text(planet_constellation[1])


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(
        "1081465226:AAHeq3mmCCTIHXT2V-3heAHULBjgAhgYg7Y", request_kwargs=PROXY
    )
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()