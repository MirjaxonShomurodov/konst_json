from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from settings import get_token
import handlers
def main():
    try:
        Token = get_token()
    except ValueError():
        print('400')
        return 'Token not found'
    
    updater = Updater(Token)
    
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', handlers.start))
    dp.add_handler(MessageHandler(Filters.text("Konstitutsiya 📖"), handlers.bulim))

    dp.add_handler(CallbackQueryHandler(handlers.bob, pattern="modda:"))
    dp.add_handler(CallbackQueryHandler(handlers.moddas, pattern=''))
    dp.add_handler(CallbackQueryHandler(handlers.one_modda, pattern=''))

    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()