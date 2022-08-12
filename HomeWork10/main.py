

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from commands import *
import token_id


token_bot = token_id.token_id()
updater = Updater(token = token_bot, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
info_handler = CommandHandler("info", info)
rules_game_handler = CommandHandler("rulesgame", rules_game)
game_option_handler = CommandHandler("gameoption", game_option)
game_handler = CommandHandler("game", game)
play_handler = MessageHandler(Filters.text, play)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(rules_game_handler)
dispatcher.add_handler(game_option_handler)
dispatcher.add_handler(game_handler)
dispatcher.add_handler(play_handler)


updater.start_polling()
updater.idle()