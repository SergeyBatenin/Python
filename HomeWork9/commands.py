from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

# arg = context.args
# context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")

FIRST = 0
SECOND = 1
ANSWER = 2

def start(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text(f'Hello {update.effective_user.first_name}')
    name = update.effective_user.first_name
    context.bot.send_message(update.effective_chat.id, f"Привет {name}.")

def info(update: Update, context: CallbackContext) -> None:
    #update.message.reply_text(f'/hello\n/info')
    context.bot.send_message(update.effective_chat.id, "/start - Приветственная команда\n/info - Справка по доступным командам\n/calc - Калькулятор комплексных чисел")


def msg(update, context):
    text = update.message.text
    if text.lower() == "привет":
        context.bot.send_message(update.effective_chat.id, "И тебе привет")
    else:
        context.bot.send_message(update.effective_chat.id, "What did you say?")


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, "Unknown command")
    context.bot.send_message(update.effective_chat.id, "Enter /info for help")


def calc(update, context):
    context.bot.send_message(update.effective_chat.id, f"Введи мнимую и действительную часть первого числа\nЧерез пробел")
    return FIRST


def first_number(update, context):
    global first
    text = update.message.text.split()
    first = complex(int(text[0]), int(text[1]))
    context.bot.send_message(update.effective_chat.id, f"Первое число : {first}")
    context.bot.send_message(update.effective_chat.id, f"Введи мнимую и действительную часть второго числа\nЧерез пробел")
    return SECOND


def second_number(update, context):
    global second
    text = update.message.text.split()
    second = complex(int(text[0]), int(text[1]))
    context.bot.send_message(update.effective_chat.id, f"Второе число : {second}")
    context.bot.send_message(update.effective_chat.id, f"Введи желаемую операцию ('+', '-', '*', '/')")
    return ANSWER


def answer(update, context):
    text = update.message.text
    if text == "+":
        result = add(first, second)
    elif text == "-":
        result = sub(first, second)
    elif text == "*":
        result = mult(first, second)
    else:
        result = div(first, second)
    context.bot.send_message(update.effective_chat.id, f"{first} {text} {second} = {result}")
    return ConversationHandler.END


def cancel(update, context):
    return ConversationHandler.END


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y