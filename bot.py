#!/usr/bin/env python

"""
Programa que impide usar LA coletilla de pwaqo a extraños
"""

import emoji
import logging

from telegram.ext import Updater, MessageHandler, Filters
from config import TOKEN


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def copyright(bot, update):

    if update.message.text:

        txt = update.message.text.lower()
        if "general" in txt or "particular" in txt:
            if "general" in txt and "particular" in txt:

                # Excepcion para @jruib por ser amigo del régimen
                if update.message.from_user.username == 'jruib':
                    msg = emoji.emojize("Guapo tú sí puedes usarlo :kissing_face: \n")

                # Destrozar mentalmente al resto
                elif not update.message.from_user.username == 'pwaqo':
                    msg = emoji.emojize("Violación de Copyright :copyright: :exclamation_mark:\n")
                    msg += emoji.emojize("Esta coletilla pertenece a @pwaqo :pouting_face:")

                # Excepción para el dictador supremo
                else:
                    msg = emoji.emojize(":smiling_face_with_smiling_eyes: :thumbs_up:")

            elif "en general" in txt:
                msg = "¿Y en particular?"
            elif "en particular" in txt:
                msg = "¿Y en general?"

            # quote=True hace que sea una respuesta
            update.message.reply_text(msg, quote=True)


updater = Updater(TOKEN)

# Enviar todos los mensajes a la funcion copyright
updater.dispatcher.add_handler(MessageHandler(Filters.all, copyright))

updater.start_polling()
updater.idle()
