#baseUrl = "https://api.telegram.org/bot"


from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from commands import *
import token_id


#app = ApplicationBuilder().token("your token here").build()
token_bot = token_id.token_id()
#bot = Bot(token = token_bot)
updater = Updater(token = token_bot, use_context=True)
dispatcher = updater.dispatcher


start_handler = CommandHandler("start", start)
info_handler = CommandHandler("info", info)
unknown_handler = MessageHandler(Filters.command, unknown)
#msg_handler = MessageHandler(Filters.text, msg)
cancel_handler = CommandHandler("cancel", cancel)
calc_handler = CommandHandler("calc", calc)
first_handler = MessageHandler(Filters.text, first_number)
second_handler = MessageHandler(Filters.text, second_number)
answer_handler = MessageHandler(Filters.text, answer)
conv_handler = ConversationHandler(entry_points=[calc_handler], 
                                    states={FIRST: [first_handler],
                                            SECOND: [second_handler],
                                            ANSWER: [answer_handler]},
                                    fallbacks=[cancel_handler])


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(unknown_handler)
#dispatcher.add_handler(msg_handler)



updater.start_polling()
updater.idle()
