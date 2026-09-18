from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from gtts import gTTS
import os

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")

def balas(update: Update, context: CallbackContext):
    teks = update.message.text
    if not teks:
        update.message.reply_text("👋 Halo! Kirim pesan teks saja!")
        return
    update.message.reply_text(f"✅ Terima: {teks}")
    suara = "narasi.mp3"
    gTTS(text=teks, lang="id").save(suara)
    with open(suara, "rb") as f:
        update.message.reply_audio(f, caption="Suara perintah")
    os.remove(suara)

def utama():
    if not TOKEN:
        print("❌ Token belum diisi!")
        return
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, balas))
    print("🤖 BOT BERJALAN! ✅ Coba kirim pesan ke Telegram!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    utama()

