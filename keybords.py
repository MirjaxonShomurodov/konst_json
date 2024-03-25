from telegram import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from db import get_all__of__them,get_bolim_by_modda,get_modda
from typing import Union
def home_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("Konstitutsiya 📖")],
            [KeyboardButton(text="Izoh qoldirish 📬"),KeyboardButton(text='Savol berish 🔍')]
        ],
        resize_keyboard=True
    )

def bulim_keyboard():
    keyboards_btns = []
    row = []
    for brend in get_all__of__them():
        row.append(InlineKeyboardButton(brend,callback_data=f'modda:{brend}'))
        if len(row) == 2:
            keyboards_btns.append(row)
            row = []

    if row:
        keyboards_btns.append(row)
    return InlineKeyboardMarkup(
        keyboards_btns
        )
def bulims_keyboard(brend:str):
    api = get_bolim_by_modda(brend)
    keyboard = []
    for bulim in api:
        keyboard.append(
            [
                InlineKeyboardButton(text=bulim['modda'],callback_data=f"bolim:{brend}:{bulim.doc_id}:{'moddalar'}")
            ]
        )
    return InlineKeyboardMarkup(keyboard)
def modda_keyboard(bolim:str, doc_id):
    print(bolim, doc_id)
    api = get_modda(bolim, doc_id=doc_id)
    print(type(api))
    keyboard = []
    for item in api:
        keyboard.append(
            [
                InlineKeyboardButton(text=item,callback_data=f"moddalar")
            ]
        )
    return InlineKeyboardMarkup(keyboard)