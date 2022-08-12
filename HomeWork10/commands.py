

import random
from telegram.ext import ConversationHandler


CANDIES = 101
MIN_STEP = 1
MAX_STEP = 13


def start(update, context):
    name = update.effective_user.first_name
    context.bot.send_message(update.effective_chat.id, f"Привет {name}. Для обзора команд введите /info")


def info(update, context):
    info_message = "/start - Приветственная команда\n/info - Справка по доступным командам\
    \n/game - Игра в конфеты\nПрочитать правила подробнее - /rulesgame\n/gameoption arg1 arg2 arg3 -\
    изменить параметры игры. Подробнее в правилах."
    context.bot.send_message(update.effective_chat.id, info_message)


def rules_game(update, context):
    rules = "ПРАВИЛА!\n Имеется некоторое количество конфет (по умолчанию равное 101).\
    Игрок и компьютер берут по очереди из кучи конфеты в количество от 1 до 13.\
    Выигрывает тот, кто забирает из кучи последние конфеты.\n\
    Чтобы изменить параметры игры введите команду:\n/gameoption arg1 arg2 arg3\n\
    Где arg1, arg2, arg3 указаны через пробел - общее количество\
    конфет, минимальное количество конфет и максимальное количество конфет для хода."

    context.bot.send_message(update.effective_chat.id, rules)


def game_option(update,context):
    global CANDIES
    global MIN_STEP
    global MAX_STEP
    
    arg = context.args
    if len(arg) < 3 or len(arg) > 3 :
        context.bot.send_message(update.effective_chat.id, "Неверное количество параметров. Попробуйте еще раз.")
    else:
        CANDIES = int(arg[0])
        MIN_STEP = int(arg[1])
        MAX_STEP = int(arg[2])
        infoText = f"Установлены следующие параметры игры\nМакс.кол-во конфет = {CANDIES}\nМин.шаг = {MIN_STEP}\nМакс.шаг = {MAX_STEP}"
        context.bot.send_message(update.effective_chat.id, infoText)


def game(update, context):
    global candies

    candies = CANDIES
    infoText = f"В куче осталось {candies} конфет\nСколько вы желаете взять? (от {MIN_STEP} до {MAX_STEP})"
    context.bot.send_message(update.effective_chat.id, infoText)


def play(update, context):
    global candies
    text = update.message.text
    step = int(text)
    if check_for_winner(candies):
        infoText = "Игра завершена, /game для начала новой игры"
        context.bot.send_message(update.effective_chat.id, infoText)
    elif step < MIN_STEP or step > MAX_STEP:
        infoText = f"такое количество конфет взять невозможно! Введите еще раз.\n\
        Доступный диапазон хода от {MIN_STEP} до {MAX_STEP}"
        context.bot.send_message(update.effective_chat.id, infoText)
    else:
        candies -= int(text)
        infoText = f"Осталось {candies} конфет.\n"
        context.bot.send_message(update.effective_chat.id, infoText)
        if check_for_winner(candies):
            infoText = "Поздравляем! Вы победили!!!\nЕсли хотите сыграть еще введите /game"
            context.bot.send_message(update.effective_chat.id, infoText)
        else:
            bot_step = comp(candies)
            candies -= bot_step
            infoText = f"Ходит бот\nБот взял {bot_step} конфет\nОсталось {candies} конфет.\n"
            if check_for_winner(candies):
                infoText += "Лууузер. Вы проиграли!!!\nЕсли хотите сыграть еще введите /game"
            context.bot.send_message(update.effective_chat.id, infoText)


def comp(candy):

    if candy > MAX_STEP:
        turn = candy % (MAX_STEP + 1)
    else:
        turn = candy
    
    if turn != 0:
        comp_turn = turn
    else:
        comp_turn = random.randint(MIN_STEP,MAX_STEP)

    return comp_turn


def check_for_winner(count):
    if count == 0:
        return True
    else:
        return False