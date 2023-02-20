from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import Variables


def on_start_command(update, context):
    print('Start event message received!')
    print(f'update: {update}')
    update.message.reply_text(f'Hi, {update.message.chat.username}!')


def main():
    bot = Updater(token=Variables.token)
    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', on_start_command))

    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()

