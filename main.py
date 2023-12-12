from flask import Flask, jsonify, render_template, send_from_directory, request
import logging
import json
from logging.handlers import RotatingFileHandler
from flask_socketio import SocketIO
from components.Pinnacle import Pinnacle
import yaml
import os
import re

with open('auth.yaml', 'r') as file:
    auth = yaml.safe_load(file)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://127.0.0.1:5000")

logging.basicConfig(filename='logs/server.log',level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


bot = Pinnacle(auth_file="auth.yaml")
bot.logger.reset()


@app.route('/')
def index(data=None):
    return render_template('dashboard.html')
    

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

@app.route('/terminal/<terminal>')
def serve_terminal(terminal):
    logs_directory = os.path.join(os.path.dirname(__file__), 'logs/')
    if terminal == "bot":
        log_file_path = os.path.join(logs_directory, 'bot.log')
        with open(log_file_path, 'r') as file:
            log_entries = file.read()
        return log_entries
        
    else:
        log_file_path = os.path.join(logs_directory, 'server.log')
        with open(log_file_path, 'r') as file:
            log_entries = file.readlines()
            relevant_entries = [re.sub(r'^.*?INFO', 'INFO', entry) for entry in log_entries if 'INFO' in entry]
        return '\n'.join(relevant_entries)

@socketio.on('start_bot')
def start_bot(data=None):
    if data:
        print('Received start_bot message with data:', data)
    bot.login()
    bot.start(callback_function=bot.logger.log)

@socketio.on('stop_bot')
def stop_bot(data=None):
    if data:
        print('Received stop_bot message with data:', data)
    bot.stop(callback_function=bot.logger.log)
    
@app.route('/bot/<action>')
def serve_bot_action(action):
    if action == "status":
        print(bot.mt5.status)
        return jsonify({"status": bot.mt5.status})
    
    
if __name__ == '__main__':
    socketio.run(app, debug=True)




'''
with open('logs/server.log', 'w') as file:
    file.write('')
with open('logs/bot.log', 'w') as file:
    file.write('')

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

@app.route('/info')
def info():
    
    account_info = bot.account_info()

    with open('accountdata.json', 'w') as accountdata:
            json.dump(account_info, accountdata, indent=4)
    
    return send_from_directory(os.path.dirname(__file__), 'accountdata.json')


@socketio.on('start_bot')
def start_bot(data=None):
    if data:
        print('Received start_bot message with data:', data)
    bot.start(callback_function=draw)
    draw(bot.account_info())

@socketio.on('stop_bot')
def stop_bot(data=None):
    if data:
        print('Received stop_bot message with data:', data)
    bot.stop(callback_function=draw)
    
    
@app.route('/account/')
def bot_action(action=None):
    bot.action(action)
    
@app.rout('/ta/')
    
@app.route('/bot/')
def bot_action(action=None):
    bot.action(action)
'''