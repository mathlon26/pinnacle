from flask import Flask, render_template
from flask_socketio import SocketIO
from components.Pinnacle import Pinnacle
from components.color import C
from os import system
from time import sleep

bot = Pinnacle()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://127.0.0.1:5000")

def draw(msg=None, color=None):
    system('cls')
    print(f"{C(color)}{msg}{C('RESET')}")
    sleep(1)


@app.route('/')
def index():
    return render_template('dashboard.html')

@socketio.on('start_bot')
def start_bot(data=None):
    if data:
        print('Received stop_bot message with data:', data)
    bot.start(callback_function=draw)


@socketio.on('stop_bot')
def stop_bot(data=None):
    if data:
        print('Received stop_bot message with data:', data)
    bot.stop(callback_function=draw)
    
if __name__ == '__main__':
    socketio.run(app, debug=True)