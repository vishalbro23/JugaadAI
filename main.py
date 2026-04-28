import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    try:
        response = model.generate_content(user_msg)
        ai_reply = response.text if response.text else "Koi reply nahi aaya 😅"
    except Exception as e:
        ai_reply = "Error aa gaya: " + str(e)

    await update.message.reply_text(ai_reply)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Gemini Bot chal reha aa 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
