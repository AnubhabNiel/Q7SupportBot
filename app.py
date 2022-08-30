import os
from flask import Flask
from testBot import TestBot 
app = Flask(__name__)


@app.route('/')
def do():
    bot=TestBot(input_dir='')
    bot.run()
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)