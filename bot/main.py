import telebot  # импорт библиотеки
import random  # для работы со случайными числами

from telebot import types

# токен
token = '6297828421:AAEdDYibhM1mxnF0cbmVNVzU5GqA_VChpFE'

# создание экземпляра бота
bot = telebot.TeleBot(token)

# набор фильмов
films = ['Мир2', 'Ад3', 'Крепкий орешек', 'Аватар']


# функции реакций
@bot.message_handler(commands=['start', 'начать'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


@bot.message_handler(commands=['stop'])
def stop_message(message):
    bot.send_message(message.chat.id, "Пока")


@bot.message_handler(commands=['film'])
def recommend_film(message):
    bot.send_message(message.chat.id, random.choice(films))


@bot.message_handler(commands=['language'])
def language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/ru")
    btn2 = types.KeyboardButton('/en')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(commands=['ru'])
def ru(message):
    bot.send_message(message.chat.id, 'установлен русский язык')


@bot.message_handler(commands=['en'])
def en(message):
    bot.send_message(message.chat.id, 'установлен английский язык')


def get_from_file():
    try:
        file = open('score.txt', "r")
    except IOError as e:
        print('не удалось открыть файл')
        return {}
    else:
        with file:
            print('делаем что-то с файлом')
            d = {}
            for line in file:
                data = line.strip().split(":")
                id_ = int(data[0])
                score = int(data[1])
                d[id_] = score
        return d


def put_to_file(d):
    print("запись в файл")
    with open("score.txt", "w") as file:
        for id_ in d:
            file.write(str(id_) + ":" + str(d[id_]) + "\n")


@bot.message_handler(commands=['random'])
def random_1(message):
    print(message.chat)
    id_ = message.chat.id
    first_name = message.chat.first_name
    user_name = message.chat.username
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(str(id_) + ":" + first_name + ":" + user_name + "\n")
    score = random.randint(1, 6)
    d = get_from_file()
    if id_ in d:
        d[id_] += score
    else:
        d[id_] = score
    put_to_file(d)
    bot.send_message(id_, score)

# постоянная прослушка
bot.infinity_polling()
