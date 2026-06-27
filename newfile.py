from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8888974688:AAHT2Xoul0yeQ9ULSFm6hojGUFHKidJxpHk"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "1":
        await update.message.reply_text("Naruto")
    elif text == "2":
        await update.message.reply_text("One Piece")
    else:
        await update.message.reply_text("1 yoki 2 ni yuboring.")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot ishga tushdi!")
app.run_polling()