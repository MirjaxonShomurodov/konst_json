from flask import Flask,request

import telegram

TOKEN = "5923509687:AAE04EHlrwqvh7cGCIyXrOn3obe_cAwPuys"
bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route('/',methods=['POST'])
def main():
    data = request.get_json()
    chat_id = data['message']['id']
    bot.send_message(chat_id=chat_id,text=data['message']['text'])
    return "hello world"

if __name__=="__main__":
    app.run(debug=True,port=8000)