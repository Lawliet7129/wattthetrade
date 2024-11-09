# app.py
from flask import Flask, jsonify
from flask import send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Renewable Energy Trading Platform API!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('backend', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/api/option-prices')
def get_option_prices():
    try:
        with open('optionPrices.json') as f:
            option_prices = json.load(f)
        return jsonify(option_prices)
    except FileNotFoundError:
        return jsonify({"error": "Option prices file not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
