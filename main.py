from flask import Flask, render_template, send_from_directory, request, jsonify
from flask.logging import default_handler
from flask_socketio import SocketIO
from components.Pinnacle import Pinnacle
from components.color import C
import os
from time import sleep
import json

bot = Pinnacle()
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://127.0.0.1:5000")


with open('logs/server.log', 'w') as file:
    file.write('')
with open('logs/bot.log', 'w') as file:
    file.write('')

def draw(msg=None, color=None):
    bot_log_file = open('logs/bot.log', 'a')
    bot_log_file.write(f"{msg}\n")
    bot_log_file.flush()  # Ensure data is written immediately
    bot_log_file.close()

@app.route('/status')
def serve_status():
    directory = os.path.join(os.path.dirname(__file__))
    return send_from_directory(directory, 'status.json')

@app.route('/config')
def serve_config():
    directory = os.path.join(os.path.dirname(__file__))
    return send_from_directory(directory, 'config.json')

@app.route('/save-config', methods=['POST'])
def save_config():
    try:
        # Receive the updated config data from the client
        updated_config = request.json

        # Update the config.json file with the new data
        with open('config.json', 'w') as config_file:
            json.dump(updated_config, config_file, indent=4)

        return jsonify({'success': True, 'message': 'Config saved successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error saving config: {str(e)}'})

@app.route('/logs/<filename>')
def serve_log(filename):
    logs_directory = os.path.join(os.path.dirname(__file__), 'logs')
    return send_from_directory(logs_directory, filename)

@app.route('/')
def index():
    return render_template('dashboard.html')



@socketio.on('start_bot')
def start_bot(data=None):
    if data:
        print('Received start_bot message with data:', data)
    bot.start(callback_function=draw)

@socketio.on('stop_bot')
def stop_bot(data=None):
    if data:
        print('Received stop_bot message with data:', data)
    bot.stop(callback_function=draw)
    

if __name__ == '__main__':
    socketio.run(app, debug=True)


