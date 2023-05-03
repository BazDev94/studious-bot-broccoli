import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google_images_search import GoogleImagesSearch

# Sostituisci con il tuo token API del bot Telegram, la chiave API di Google e l'ID del motore di ricerca personalizzato
TOKEN = "6043130273:AAHkJs8QYynqS0Gpqqr_GIWQpLmVvAt4pPI"
GOOGLE_API_KEY = "AIzaSyC_RMi7O6ndfm6hwQ9NDO6ArWUOfjm4sIk"
SEARCH_ENGINE_ID = "108905974852183232718"

gis = GoogleImagesSearch(GOOGLE_API_KEY, SEARCH_ENGINE_ID)

# Abilita il logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Ciao! Inviami una parola chiave e cercherò un'immagine per te.")

def search_image(query):
    search_params = {
        "q": query,
        "num": 1,
        "imgSize": "medium",
        "fileType": "jpg"
    }

    gis.search(search_params)
    results = gis.results()

    if results:
        return results[0].url
    else:
        return None

def search_query(update: Update, context: CallbackContext):
    query = update.message.text
    image_url = search_image(query)

    if image_url:
        update.message.reply_photo(photo=image_url)
    else:
        update.message.reply_text("Non ho trovato nessuna immagine per la tua ricerca. Prova con un'altra parola chiave.")

def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_query))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
