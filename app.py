
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# home
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# echo
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify(data)


# run

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)