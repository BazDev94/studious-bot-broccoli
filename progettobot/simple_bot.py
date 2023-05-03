# import telepot
# import cambio
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
# TOKEN = 


# print ('In ascolto ...')

#     # import time
#     # while 1:
#     #     time.sleep(10)

# def extract_number(text):
#     return text.split()[1].strip()

# def convert_usd(update, context):
#     usd=float(extract_number(update.message.text))
#     eur=cambio.from_usd_to_eur(usd)
#     print(f'Eseguita conversione da {usd} dollori Americano a {eur} Euro')
#     update.message.reply_text(f'{eur} EURI')

# def convert_eur(update, context):
#     eur=float(extract_number(update.message.text))
#     usd=cambio.from_eur_to_usd(eur)
#     print(f'Eseguita conversione di {eur} EURI a {usd} dollori Americano')
#     update.message.reply_text(f'{usd} USD')

# def on_chat_message(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     if content_type == 'text':
#         name = msg["from"]["first_name"]
#         txt = msg['text']
#         bot.sendMessage(chat_id, 
#         'ciao %s sono un bot creato da badredin jamjama'%name)
#         bot.sendMessage(chat_id, 'ho ricevuto questo: %s'%txt)

# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao sono BazBot, posso convertire la valuta USD/EUR oppure EUR/USD. Ti basta scrivere /usd oppure /eur + l'importo e farò tutto io")

# # metodo che ripete cio che scrive l'utente
# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
# #metodo che non capisce
# def unknown(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# def main():   
#     upd= Updater(TOKEN, use_context=True)
#     disp=upd.dispatcher

#     echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#     start_handler = CommandHandler('start', start)
#     unknown_handler = MessageHandler(Filters.command, unknown)
   
#     disp.add_handler(unknown_handler)
#     disp.add_handler(echo_handler)
#     disp.add_handler(start_handler)
#     disp.add_handler(CommandHandler("usd", convert_usd))
#     disp.add_handler(CommandHandler("eur", convert_eur))

#     upd.start_polling()

#     upd.idle()

# if __name__=='__main__':
#     main()
