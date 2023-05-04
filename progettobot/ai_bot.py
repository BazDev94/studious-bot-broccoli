import logging
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from environs import Env

env = Env()
env.read_env()

TELEGRAM_TOKEN = env('TOKEN')
OPENAI_API_KEY = env('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

mode = {}


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Ciao! Scegli una modalità tra /chat o /image e inviami un messaggio.")


def chat_mode(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    mode[user_id] = 'chat'
    update.message.reply_text("Modalità chat attivata. Inviami un messaggio e risponderò.")


def image_mode(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    mode[user_id] = 'image'
    update.message.reply_text("Modalità immagine attivata. Inviami una parola chiave e cercherò un'immagine per te.")


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = response.choices[0].text.strip()
    return message


def create_image(query):
    # Implementa la tua funzione di ricerca immagini qui
    # Inserisci la tua chiave API delle API per la generazione di immagini
    response = openai.Image.create(
    prompt=query,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def process_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in mode:
        update.message.reply_text("Seleziona prima una modalità usando i comandi /chat o /image.")
        return

    if mode[user_id] == 'chat':
        user_input = update.message.text
        prompt = f"Rispondi a questa domanda: {user_input}"
        ai_response = generate_response(prompt)
        update.message.reply_text(ai_response)

    elif mode[user_id] == 'image':
        query = update.message.text
        image_url = create_image(query)
        if image_url:
            update.message.reply_photo(photo=image_url)
        else:
            update.message.reply_text("Non ho trovato nessuna immagine per la tua ricerca. Prova con un'altra parola chiave.")


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("chat", chat_mode))
    dp.add_handler(CommandHandler("image", image_mode))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
