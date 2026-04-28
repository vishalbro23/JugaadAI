import os
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini setup (NEW)
client = genai.Client(api_key=GEMINI_API_KEY)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_msg
        )
        ai_reply = response.text
    except Exception as e:
        ai_reply = "Error: " + str(e)

    await update.message.reply_text(ai_reply)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Bot chal reha aa 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
