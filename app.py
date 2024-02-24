from flask import Flask, render_template
from functions import start_conversation

app = Flask(__name__)

conversation_bot = []
welcome_message = start_conversation()
conversation_bot.append({'bot': welcome_message})
top_3_laptops = None
print("Hello world -----")

@app.route("/")
def default_func():
    global conversation_bot, conversation, top_3_laptops
    return render_template("index.html", conversation_list = conversation_bot)

if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0", port="5000")