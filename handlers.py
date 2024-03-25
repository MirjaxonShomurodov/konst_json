from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext
import keybords
import db
def start(update:Update,context:CallbackContext):
    user = update.effective_user
    update.message.reply_text(
        text=f"Assalom aleykum bizning kanalimizga aʼzo bulganigizdan hursandmiz 🚻 {user.first_name},🧑‍⚖️ Konstitusiya nomli botmiz sizga yordam beradi deb oʻylaymiz.",
        reply_markup=keybords.home_keyboard()
    )

def bulim(update:Update,context:CallbackContext):
    update.message.reply_text(
        text="Kerakli boʻlimni tanlang ⬇️",
        reply_markup=keybords.bulim_keyboard(),
    )

def bob(update:Update,context:CallbackContext):    
    bulim = update.callback_query.data.split(':')[1]
    update.callback_query.message.reply_text(
        text="Kerakli bobni tanlang ⬇️",
        reply_markup=keybords.bulims_keyboard(bulim)
    )


def moddas(update:Update,context:CallbackContext):
    bolim = update.callback_query.data.split(":")[1]
    doc_id = update.callback_query.data.split(":")[2]
    update.callback_query.message.reply_text(
        text="Kerakli moddani tanlang ⬇️",
        reply_markup=keybords.modda_keyboard(bolim=bolim, doc_id=doc_id)
    )
def one_modda(update: Update, context: CallbackContext):
    bolim = update.callback_query.data.split(":")[1]
    doc_id = update.callback_query.data.split(":")[2]
    key_id = update.callback_query.data.split(":")[3]
    text = db.key_modda(bulim=bolim, doc_id=doc_id, key_id=key_id)
    update.callback_query.message.reply_text(
        text=text,
        reply_markup=keybords.modda_keyboard(bolim=bolim, doc_id=doc_id)
    )