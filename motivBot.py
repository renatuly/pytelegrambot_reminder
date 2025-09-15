import random
import traceback
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8393233080:AAFQl83f-WKowzk85yXEC8EMK3KQtElUHf4"

QUOTES = [
    "🌸 Remember, success is not only in dunya but in Akhirah. Every small effort you make today can be your sadaqah jariyah tomorrow.",
    "✨ Don’t forget to say Bismillah before you start — with Allah’s name, every task becomes blessed.",
    "💪 Allah does not burden a soul beyond what it can bear (2:286). Whatever challenge you face today, you are strong enough for it.",
    "🌅 Wake up with gratitude — Alhamdulillah for another chance to make sujood and get closer to Jannah.",
    "😄 Every time you smile at someone, it is charity (hadith). So don’t underestimate your smile today.",
    "☀️ Pray two rak’ahs of Duha today, and your rizq will come in ways you never expected.",
    "🕌 Even the smallest good deed can outweigh mountains on the Day of Judgment. Never think your effort is too small.",
    "🤲 Today, make lots of istighfar — each one wipes away sins and opens doors you never imagined.",
    "🌿 The Prophet ﷺ said: The most beloved deeds to Allah are those that are consistent, even if small.",
    "🏞️ When you feel tired, remember Jannah is the real rest. Keep striving, every step is worth it.",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Assalamu Alaikum {user.first_name}! 🌙\n"
        "I will send you Islamic reminders every 2 hours inshaAllah 🤲"
    )

    chat_id = update.effective_chat.id
    job_queue = context.job_queue
    job_queue.get_jobs_by_name(str(chat_id))
    job_queue.run_repeating(send_reminder, interval=2*60*60, first=5, chat_id=chat_id, name=str(chat_id))

async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    quote = random.choice(QUOTES)
    await context.bot.send_message(job.chat_id, text=quote)

def main():
    print("Starting bot... (press Ctrl+C to stop)")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    try:
        app.run_polling()
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    main()
