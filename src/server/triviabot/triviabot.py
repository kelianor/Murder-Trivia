import telebot
import game
from config import BOT_TOKEN

# Запуск Telegram бота
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    userID = message.chat.id
    status = game.users.addUser(userID)
    if status:
        bot.send_message(userID, "Вы успешно зарегистрированы!") # TODO: Поменять сообщение
    else:
        bot.send_message(userID, "Вы уже зарегистрированы!") # TODO: Поменять сообщение

@bot.callback_query_handler(func=lambda call: call.data == 'participating')
def participating_btn(call):
    userID = call.message.chat.id
    users.addUser(userID)
    if not game_started:
        players[userID] = {}
        bot.answer_callback_query(call.id)
        bot.send_message(userID, 'Вы подписали контракт с @Mihuyka на участие в смертельной вечеринке :)')
    else:
        bot.send_message(userID, 'Игра уже началассь. Что поделаешь...')

@bot.callback_query_handler(func=lambda call: call.data == 'not_participating')
def not_participating_btn(call):
    userID = call.message.chat.id
    if not game_started:
        players.pop(userID, None)
        bot.answer_callback_query(call.id)
        bot.send_message(userID, 'Вы разорвали контракт смертельной вечеринки :(')
    else:
        bot.send_message(userID, 'Игра уже началассь. Что поделаешь...')

def start_game():
    game_started = True
    for uid in players.keys():
        playerList = "Игра началась :) В вечеринке участвуют: "
        for uid in players.keys():
            playerList += "@" + bot.get_chat(uid).username + " "

        bot.send_message(uid, playerList)

def get_answers():
    keyboard = telebot.types.InlineKeyboardMarkup()
    Abtn = telebot.types.InlineKeyboardButton(text="A", callback_data='answerA')
    Bbtn = telebot.types.InlineKeyboardButton(text="B", callback_data='answerB')
    Cbtn = telebot.types.InlineKeyboardButton(text="C", callback_data='answerC')
    Dbtn = telebot.types.InlineKeyboardButton(text="D", callback_data='answerD')
    keyboard.row(Abtn, Bbtn, Cbtn, Dbtn)

    for userID in users:
        try:
            bot.send_message(userID, "Выберите один из варинатов ответа: ", reply_markup=keyboard)
        except Exception as e:
            print(f"Ошибка отправки пользователю {userID}: {e}")

@bot.callback_query_handler(func=lambda call: call.data == 'answerA')
def Abtn(call):
    userID = call.message.chat.id
    if userID in players.keys():
        players[userID] = 'A'
        bot.send_message(userID, "Вариант ответа A учитан")
    else:
        bot.send_message(userID, "Вы не в игре!")

@bot.callback_query_handler(func=lambda call: call.data == 'answerB')
def Bbtn(call):
    userID = call.message.chat.id
    if userID in players.keys():
        players[userID] = 'C'
        bot.send_message(userID, "Вариант ответа B учитан")
    else:
        bot.send_message(userID, "Вы не в игре!")

@bot.callback_query_handler(func=lambda call: call.data == 'answerC')
def Cbtn(call):
    userID = call.message.chat.id
    if userID in players.keys():
        players[userID] = 'C'
        bot.send_message(userID, "Вариант ответа C учитан")
    else:
        bot.send_message(userID, "Вы не в игре!")

@bot.callback_query_handler(func=lambda call: call.data == 'answerD')
def Dbtn(call):
    userID = call.message.chat.id
    if userID in players.keys():
        players[userID] = 'D'
        bot.send_message(userID, "Вариант ответа D учитан")
    else:
        bot.send_message(userID, "Вы не в игре!")