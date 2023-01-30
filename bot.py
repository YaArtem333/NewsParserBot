import telebot # Библиотека для ботов
from time import sleep

import database as DB # Файл database.py , где лежат функции для работы с БД
import newspaper_parse as req
import settings

# Создание бота по токену
bot = telebot.TeleBot(settings.TOKEN)

# Описание команды /start
@bot.message_handler(commands = ["start"])
def start_message(message):

    # Получение id и имени пользователя в Telegram
    user_id = message.from_user.id
    username = message.from_user.username

    # Провеока на наличие пользователя в БД и добавление его туда при отсутствии
    status = DB.check_user_in_db(user_id)
    if status == 0:
        DB.add_user(user_id = user_id, username = username)
        bot.send_message(message.chat.id, "Hello, you're added to the database!\n"
                                          "I'll send you news from the gazeta.ru every day")
    if status == 1:
        bot.send_message(message.chat.id, "You're already recieving news from me")

    # Отправка пользователю сообщений при наличии его id в БД
    while True:
        try:
            # Если пользователь есть в БД, то каждые 10 минут ему приходит рассылка с последними новостями сайта Gazeta.ru
            status1 = DB.check_user_in_db(user_id)
            if status1 == 1:
                try:
                    bot.send_message(message.from_user.id, req.send_news())
                    sleep(60 * 10)
                except telebot.apihelper.ApiException:
                    DB.delete_user(user_id)
            else:
                break

        # Если пользователь заблокировал бота, то его данные удаляются из БД
        except telebot.apihelper.ApiException:
            DB.delete_user(user_id)

# Команда для запуска бота
def start_bot():
    bot.polling(none_stop=True)
