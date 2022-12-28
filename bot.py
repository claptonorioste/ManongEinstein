import telegram.ext
from process import ask, append_interaction_to_chat_log
import logging, os

PORT = int(os.environ.get('PORT', '8443'))

# with open('token.txt', 'r') as f:
#     TOKEN = str(f.read())
TOKEN = '5979185099:AAEFFYkQR2ci0_icTk0lkUjvsd8mzCE7jSE'

session = {}


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hello! my friend \nI'm Einstein, your virtual helper. \nYou can ask me everything you wanted to know. \n\nYou can ask help for your homework, help you with a tough decision, anything!\n\nType /contact to view Developer Info \nType /about to view bot description")


def help(update, context):
    update.message.reply_text("""
    The Following commands are available:
    /start -> Welcome to ManongEinstein
    /help ->This Message
    /about -> About ManongEinstein
    /contact -> Developer Info
    
    """)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', context)


def about(update, context):
    update.message.reply_text("""
            ManongEinstein is not just a chatbot. It's so much more than that. It's an AI-enabled students service solution that answers your questions.
        """)


def contact(update, context):
    update.message.reply_text("Developer: Clapton Orioste \nEmail: clapton.five@gmail.com\nPortfolio: claptonorioste.com")


def handle_message(update, context):
    chat_log = session.get('chat_log')
    answer = ask(update.message.text, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(update.message.text, answer,
                                                         chat_log)
    update.message.reply_text(f"{str(answer)}")


def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    bot = updater.dispatcher

    bot.add_handler(telegram.ext.CommandHandler("start", start))
    bot.add_handler(telegram.ext.CommandHandler("help", help))
    bot.add_handler(telegram.ext.CommandHandler("about", about))
    bot.add_handler(telegram.ext.CommandHandler("contact", contact))
    bot.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_message))

    bot.add_error_handler(error)
    updater.start_polling()

    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN,
        webhook_url='https://web3taskbot.herokuapp.com/' + TOKEN
    )

    updater.idle()


if __name__ == '__main__':
    main()
