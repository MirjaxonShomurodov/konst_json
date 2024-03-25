from tinydb import TinyDB,Query
from typing import Union
import json
db = TinyDB('db.json',indent=4,encoding = 'utf-8')
item = db.table('bolim')
q = Query()

def get_all__of__them():
    brends = db.tables()
    return brends

def get_bolim_by_modda(bulim:str)->list:
    if bulim in get_all__of__them():
        collection = db.table(bulim)
        return collection.all()
    return []

# print(get_bolim_by_modda("Birinchi bo'lim."))

def get_modda(bulim:str,doc_id:Union[str,int]):
    if bulim in get_all__of__them():
        card = db.table(bulim)
        bob_id = card.get(doc_id=doc_id)
        moddalar = []
        for i, v in bob_id['moddalar'].items():
            moddalar.append(i)
        return moddalar
    return []

def key_modda(bulim:str,doc_id:Union[str,int], key_id):
    if bulim in get_all__of__them():
        car_modda = db.table(bulim)
        modda = car_modda.get(doc_id=doc_id)
        return modda['moddalar'][f'{key_id}']

def clear_items(user_id:Union[int, str]):
    items = item.remove(q.user_id == user_id)
    return items
