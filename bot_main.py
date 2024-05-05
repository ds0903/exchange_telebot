import datetime as dt
import sqlite3
import time as t
from datetime import datetime

import telebot

# import webbrowser as wb
bot = telebot.TeleBot("6044868878:AAGyBoDF0cqjSHkb1QY6851PHR2GPJvRKds")


@bot.message_handler(commands=["vidguk"])
def vidguk(message):
    otzi = "t.me/otziv_exchange7"
    bot.send_message(message.chat.id, otzi, parse_mode="html")
    return 0


@bot.message_handler(commands=["start"])
def start(message):
    name = f"Вітаю вас 😁{message.from_user.first_name}\nУ цьому боті ви можете обміняти токени в грн та навпаки на будь-яку картку банку України 🇺🇦💳"  # noqa
    news = "⚠ На даний момент бот приймає тільки\n\n <b><u>SWEAT/UAH</u></b> - 1 sweat = 0.22UAH - Продаж\n <b><u>USDT/UAH</u></b> - 1 USDT = 38.50 UAH - Продаж\n <b><u>UAH/USDT</u></b> - 39.50UAH = 1 USDT - Покупка \n\nДля продажу натисніть /sell для допомоги натисніть /help\nЯкщо бажаєте переглянути відгуки натисніть /vidguk"  # noqa

    bot.send_message(message.chat.id, name, parse_mode="html")
    t.sleep(0.5)

    #  bot.send_message(message.chat.id, text, parse_mode='html')
    #  time.sleep(0.5)
    bot.send_message(message.chat.id, news, parse_mode="html")
    #  time.sleep(0.5)
    #  bot.send_message(message.chat.id, price, parse_mode='html')

    # =======# створення бази данних
    connect = sqlite3.connect("BASE.db")
    cursor = connect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Gosti(
               Name TEXT, Time TEXT
                      )"""
    )

    connect.commit()
    gost = message.from_user.first_name

    time_posiheniya = dt.datetime.now()
    cursor.execute("INSERT INTO Gosti VALUES(?,?);", (gost, time_posiheniya))

    connect.commit()
    # =======#


@bot.message_handler(commands=["help"])
def help(message):
    help = "🛠 Якщо вам потрібна допомога, зверніться за цим контактом @danilsergeyevich :/"  # noqa
    t.sleep(0.5)
    bot.send_message(message.chat.id, help, parse_mode="html")


@bot.message_handler(commands=["sell"])
def sell(message):
    # near = "a27d49a2b5c166d871aeb15dedf4a48c3cc9e0ab1793a97662bd40fc969bf2a7"
    warning = f"⚠<u><b>Попереджуєм вас</b></u>, можете і не пробувати обдурити бота, оскільки всі транзакції адміністратор перевіряє вручну і після цього відправляє валюту на картку вашого банку 💳 або криптогаманець💸"  # noqa
    sell = f"Для продажу або купівлі виберіть пару, яка вас цікавить🪙\n\n /SWEAT_UAH - продаж min - 10 sweat\n /USDT_UAH - продаж min - 5$\n /UAH_USDT - купівля min - 5$"  # noqa

    t.sleep(0.5)
    bot.send_message(message.chat.id, sell, parse_mode="html")
    # photo= open('wallet_near_sweat.jpg','rb')
    # time.sleep(0.5)
    # bot.send_photo(message.chat.id, photo)
    t.sleep(1)
    bot.send_message(message.chat.id, warning, parse_mode="html")


@bot.message_handler(commands=["SWEAT_UAH"])
def help_SWEAT(message):
    near = "a27d49a2b5c166d871aeb15dedf4a48c3cc9e0ab1793a97662bd40fc969bf2a7"
    # warning = f'⚠<u><b>Попереджуєм вас</b></u>, можете і не пробувати обдурити бота, оскільки всі транзакції адміністратор перевіряє вручну і після цього відправляє валюту на картку вашого банку 💳 ' # noqa
    sellSweat = f"Для продажу надішліть Токени <u><b> Sweat в мережі NEAR </b></u> На гаманець бота\n\n<code>{near}</code>\n\n<b>Після відправлення токенів, надішліть скріншот Боту❗</b>"  # \n\n{warning}❗' # noqa

    t.sleep(0.5)
    bot.send_message(message.chat.id, sellSweat, parse_mode="html")
    photo = open("wallet_near_sweat.jpg", "rb")
    t.sleep(0.5)
    bot.send_photo(message.chat.id, photo)

    @bot.message_handler(content_types=["photo"])
    def handle_file(message):
        try:
            # chat_id = message.chat.id

            file_info = bot.get_file(
                message.photo[len(message.photo) - 1].file_id
            )  # noqa
            downloaded_file = bot.download_file(file_info.file_path)

            src = "/home/danilsergeyevich/" + file_info.file_path.replace(
                "photos/", "SWEAT_UAH_"
            )
            # abe = file_info.file_path.replace('photos/', '')
            with open(src, "wb") as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, "Квитанція збережена")
            t.sleep(1)
            bot.send_message(
                message.chat.id,
                "Тепер введіть через команду /cardS номер карти. \nМи підтримуєм виключно. \n💳monobank,💳privatbank,💳alfabank.\nЯкщо у вас карта іншого Українського, банку напишіть адміністратору через \n/help",  # noqa
            )

            # photo = open('', 'rb')
            # bot.send_photo(1059137693, photo)
            new_user = "Новий клієнт"
            bot.send_message(1059137693, new_user)

        except Exception as e:
            bot.reply_to(message, e)

    return 0


@bot.message_handler(commands=["UAH_USDT"])
def help_UAH(message):
    # warning = f'⚠<u><b>Попереджуєм вас</b></u>, можете і не пробувати обдурити бота, оскільки всі транзакції адміністратор перевіряє вручну і після цього відправляє валюту на картку вашого банку 💳 ' # noqa
    Monobank = "5375414126632131"
    PrivatBank = "5457082297550985"
    BuyUSDT = f"Для покупки USDT надішліть ГРН На Банківську карту бота\n\nMonobank - <code>{Monobank}</code>\nМожуть бути комісії банку🏦\nPrivatBank - <code>{PrivatBank}</code>\n\n<b>Після відправлення токенів, надішліть скріншот Боту❗</b>"  # \n\n{warning}❗' # noqa
    t.sleep(0.5)
    bot.send_message(message.chat.id, BuyUSDT, parse_mode="html")

    @bot.message_handler(content_types=["photo"])
    def handle_file(message):
        try:
            # chat_id = message.chat.id

            file_info = bot.get_file(
                message.photo[len(message.photo) - 1].file_id
            )  # noqa
            downloaded_file = bot.download_file(file_info.file_path)

            src = (
                "/home/danilsergeyevich/Crypto_Exchange"
                + file_info.file_path.replace("photos/", "UAH_USDT_")
            )
            # abe = file_info.file_path.replace('photos/', '')
            with open(src, "wb") as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, "Квитанція збережена")
            t.sleep(1)
            bot.send_message(
                message.chat.id,
                "Тепер введіть через команду /usdtbuy адрес криптогаманця. Або почту аккаунта bybit \nМи підтримуєм тільки \n\n💳BEP20 Binance smart chain\n\nЯкщо у вас гаманець в іншій мережі, наприклад Tron, Solana або Ethereum, будь ласка, напишіть адміністратору через команду \n/help",  # noqa
            )

            # photo = open('', 'rb')
            # bot.send_photo(1059137693, photo)
            new_user = "Новий клієнт"
            bot.send_message(1059137693, new_user)

        except Exception as e:
            bot.reply_to(message, e)

    return 0


@bot.message_handler(commands=["USDT_UAH"])
def help_USDT(message):
    # warning = f'⚠<u><b>Попереджуєм вас</b></u>, можете і не пробувати обдурити бота, оскільки всі транзакції адміністратор перевіряє вручну і після цього відправляє валюту на картку вашого банку 💳 ' # noqa
    BEP20 = "0xee7c66a41315692fa6e295c874bc5f560e9c1c31"
    sellUAH = f"Для продажу надішліть Токени <u><b> USDT в мережі BEP20 </b></u> На гаманець бота\n\n<code>{BEP20}</code>\n\n<b>Після відправлення токенів, надішліть скріншот Боту❗</b>"  # \n\n{warning}❗' # noqa
    t.sleep(0.5)
    bot.send_message(message.chat.id, sellUAH, parse_mode="html")

    t.sleep(0.5)
    photo = open("wallet_USDT_BEP20.jpg", "rb")
    bot.send_photo(message.chat.id, photo)

    @bot.message_handler(content_types=["photo"])
    def handle_file(message):
        try:
            # chat_id = message.chat.id

            file_info = bot.get_file(
                message.photo[len(message.photo) - 1].file_id
            )  # noqa
            downloaded_file = bot.download_file(file_info.file_path)

            src = (
                "/home/danilsergeyevich/Crypto_Exchange"
                + file_info.file_path.replace("photos/", "USDT_UAH_")
            )
            # abe = file_info.file_path.replace('photos/', '')
            with open(src, "wb") as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, "Квитанція збережена")

            t.sleep(1)
            bot.send_message(
                message.chat.id,
                "Тепер введіть через команду /usdtsell номер карти. \nМи підтримуєм виключно. \n💳monobank,💳privatbank,💳alfabank.\nЯкщо у вас карта іншого Українського банку, напишіть адміністратору через \n/help",  # noqa
            )

            # photo = open('', 'rb')
            # bot.send_photo(1059137693, photo)
            new_user = "Новий клієнт"
            bot.send_message(1059137693, new_user)
        except Exception as e:
            bot.reply_to(message, e)

    return 0


@bot.message_handler(commands=["cardS"])  # продажа свиткоина за грн
def handle_message(message):
    num = bot.send_message(
        message.chat.id, "Введіть номер вашої банківської картки 💳"
    )  # вывод сообщения которое написал пользователь
    bot.register_next_step_handler(num, Sweat_text)
    return 0


def Sweat_text(message):
    global time
    my_text = f"Номер вашої банківської картки 💳 -- {message.text} -- \nВаша заявка надійшла в обробку ✅ \nПісля перевірки кошти будуть надіслані на ваш банківський рахунок 💸 \n\nСередній час обробки транзакції 2 години "  # noqa
    bot.send_message(message.chat.id, my_text)

    t.sleep(2)
    ate = " 🛠 Якщо у вас виникли труднощі або переплутали данні, то введіть команду \n/help"  # noqa
    bot.send_message(message.chat.id, ate)

    # =======# створення бази данних
    connect = sqlite3.connect("BASE.db")
    cursor = connect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS SweatUAH(
                             User_name1 TEXT, Card1 TEXT, Time1 TEXT, Order_type TEXT # noqa
                        )"""
    )

    connect.commit()
    user_name = message.from_user.first_name
    user_card = message.text
    time = dt.datetime.now()
    Order_type = "Продажа sweat"
    cursor.execute(
        "INSERT INTO SweatUAH VALUES(?,?,?,?);",
        (user_name, user_card, time, Order_type),
    )

    connect.commit()
    # =======#
    return 0


@bot.message_handler(commands=["usdtbuy"])  # покупка долара за грн
def message_usdtbuy(message):
    num = bot.send_message(
        message.chat.id, "Введіть номер вашого криптогаманця у мережі BEP20 💳"
    )  # вывод сообщения которое написал пользователь
    bot.register_next_step_handler(num, usdtbuy_text)
    return 0


def usdtbuy_text(message):
    my_text = f"Номер вашого криптогаманця💳\n -- {message.text} -- \nВаша заявка надійшла в обробку ✅ \nПісля перевірки кошти будуть надіслані на ваш банківський рахунок 💸 \n\n Середній час обробки транзакції 2 години "  # noqa
    bot.send_message(message.chat.id, my_text)
    t.sleep(2)
    ate = " 🛠 Якщо у вас виникли труднощі або переплутали данні, то введіть команду \n/help"  # noqa
    bot.send_message(message.chat.id, ate)

    # =======# створення бази данних
    connect = sqlite3.connect("BASE.db")
    cursor = connect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS  USDTBUY(
            User_name TEXT, BEP20_adress TEXT, Order_time TEXT, Order_type TEXT
                      )"""
    )

    connect.commit()
    user_name = message.from_user.first_name
    BEP20_adress = message.text
    Order_time = dt.datetime.now()
    Order_type = "Покупка $"
    cursor.execute(
        "INSERT INTO USDTBUY VALUES(?,?,?,?);",
        (user_name, BEP20_adress, Order_time, Order_type),
    )

    connect.commit()
    # =======#
    return 0


@bot.message_handler(commands=["usdtsell"])  # продажа долара за грн
def handle_USDTSell(message):
    num3 = bot.send_message(
        message.chat.id, "Введіть номер вашого криптогаманця у мережі BEP20 💳"
    )  # вывод сообщения которое написал пользователь
    bot.register_next_step_handler(num3, bep20_text)
    return 0


def bep20_text(message):
    my_text = f"Номер вашої банковскої карти💳\n -- {message.text} -- \nВаша заявка надійшла в обробку ✅ \nПісля перевірки кошти будуть надіслані на ваш банківський рахунок 💸 \n\n Середній час обробки транзакції 2 години "  # noqa
    bot.send_message(message.chat.id, my_text)
    t.sleep(2)
    ate = " 🛠 Якщо у вас виникли труднощі або переплутали данні, то введіть команду \n/help"  # noqa
    bot.send_message(message.chat.id, ate)

    # =======# створення бази данних
    connect = sqlite3.connect("BASE.db")
    cursor = connect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS USDTSELL(
            User_name3 TEXT, BEP20_adress3 TEXT, Order_time3 TEXT, Order_type TEXT # noqa
                 )"""
    )

    connect.commit()
    user_name = message.from_user.first_name
    user_card = message.text
    time_order = dt.datetime.now()
    Order_type = "Продажа $"
    cursor.execute(
        "INSERT INTO USDTSELL VALUES(?,?,?,?);",
        (user_name, user_card, time_order, Order_type),
    )

    connect.commit()
    # =======#
    return 0


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Даня":
        bot.send_message(message.chat.id, "Мой создатель", parse_mode="html")

    elif message.text == "Слава Україні":
        bot.send_message(message.chat.id, "Героям слава!", parse_mode="html")

    elif message.text == "Смерть ворогам":
        bot.send_message(message.chat.id, "Слава нації!", parse_mode="html")

    elif message.text == "Wassa":
        bot.send_message(
            message.chat.id, "Бета тестер топчик", parse_mode="html"
        )  # noqa

    else:
        bot.send_message(
            message.chat.id,
            "Будь ласка, введіть одну з команд\n /start   /sell   /help",
            parse_mode="html",
        )
    return 0


bot.polling(none_stop=True)
