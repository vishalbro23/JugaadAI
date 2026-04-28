import os
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=text
        )
        answer = response.text if response.text else "Koi reply nahi aaya 😅"
    except Exception as e:
        answer = "Error: " + str(e)

    await update.message.reply_text(answer)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Bot chal reha aa 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
