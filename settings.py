from dotenv import load_dotenv

import os
load_dotenv()

def get_token():
    TOKEN = os.getenv('TOKEN')
    if not TOKEN:
        raise ValueError("Token mavjud emas.")
    return TOKEN