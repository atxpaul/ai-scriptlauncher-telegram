from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import os
from assistant import send_chat_request

TOKEN = os.getenv('BOT_TOKEN')

async def start (update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Bienvenido! Envía un mensaje o usa un comando para interactuar con el bot"
    )

async def process_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = send_chat_request(user_message)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    app.run_polling()

if __name__ == "__main__":
    main()
