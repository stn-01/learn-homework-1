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
import datetime
import bot_settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def get_constellation(update, context):                                 # Определил фунцию для получения созвездия.

    print(f"Пользователь {update['message']['chat']['username']}:")     # Отобразил имя пользователя в консоли.
    print('Команда вызвана: /planet')
    user_text = update.message.text
    print('Cообщение: ', user_text)
    planet = user_text.split(' ')[1]                                    # Получил название планеты.
    print('Планета:   ', planet)
    today = str(datetime.datetime.now())[0:10].replace('-', '/')        # Получил дату.
    print('Сегодня:   ', today)

    if planet.lower() == 'mars':                                        # Выбор созвездия (только для трех планет).
        mars = ephem.Mars(today)
        constellation = str(ephem.constellation(mars)[1])               # Беру созвездие из кортежа в виде строки.
        print('Созвездие: ', constellation)
    elif planet.lower() == 'venus':
        venus = ephem.Venus(today)
        constellation = str(ephem.constellation(venus)[1])
        print('Созвездие: ', constellation)
    elif planet.lower() == 'pluto':
        pluto = ephem.Pluto(today)
        constellation = str(ephem.constellation(pluto)[1])
        print('Созвездие: ', constellation)
    else:
        constellation = ('Пока что не могу ответить.')
        print(constellation)

    update.message.reply_text(constellation)                            # Ответчик на команду с сообщением.


def talk_to_me(update, context):
    print(f"Пользователь {update['message']['chat']['username']}:")     # Отобразил имя пользователя в консоли.
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('Ответ на сообщение.')                    #


def main():
    mybot = Updater(bot_settings.TOKEN, use_context=True)               # Cпрятал токен в отдельный файл для импорта.

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))         # Создал обработчик команды /planet.
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
