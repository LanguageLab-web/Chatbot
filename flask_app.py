import sys
import os
from flask import Flask, request, jsonify
from datetime import datetime

# Add the directory containing `main.py` to the Python path
sys.path.append("C:\Users\Anish\OneDrive\Attachments\chatbot\my_app")

# Import methods from main.py
from main import royal_plaza_bot, faisal_mss_bot, load_logs

app = Flask(__name__)

# Load logs once to simulate real-time processing
logs = load_logs()

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    try:
        data = request.json
        message = data.get('message', '')
        sender = data.get('sender', '')

        if not message:
            return jsonify({"error": "No message provided"}), 400

        royal_response = royal_plaza_bot(message, logs)
        faisal_response = faisal_mss_bot(message, logs)

        return jsonify({"royal_response": royal_response, "faisal_response": faisal_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/start', methods=['GET'])
def start_bot():
    return jsonify({"message": "Chatbot is running."})

@app.route('/shutdown', methods=['POST'])
def shutdown_bot():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return jsonify({"error": "Not running with the Werkzeug Server"}), 500
    func()
    return jsonify({"message": "Chatbot is shutting down."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
