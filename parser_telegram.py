from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from webscrapping import parse_hh


SECRET_BOT_TOKEN = '5468722521:AAGEgDz90EjA9PON3avU_YaR6HhL8fkI5e4'
app = ApplicationBuilder().token(SECRET_BOT_TOKEN).build()
# Хендлер - Обработчик (события)


async def bot_reply(update: Update, ctx):
    await update.message.reply_text("Идет поиск вакансий ...")
    user_input = update.message.text  # Что написали боту?
    jobs_count = parse_hh(user_input)
    reply = f"Найдено вакансий: {jobs_count}"  # ToDo: Запустить Selenium
    await update.message.reply_text(reply)


handler = MessageHandler(filters.TEXT, bot_reply)
app.add_handler(handler)

app.run_polling()
