# from flask import Flask

# app = Flask(__name__)

# @app.route("/")

# def home():
#     return "Hello Kushagra devops"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=6002, debug=True)

from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Python Backend!",
        "service": "backend-api",
        "container": os.getenv('HOSTNAME', 'unknown')
    })

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "backend-api"
    })

@app.route('/api/data')
def get_data():
    return jsonify({
        "users": [
            {"id": 1, "name": "Keshav", "role": "DevOps Engineer"},
            {"id": 2, "name": "Infra Warrior", "role": "Cloud Architect"}
        ],
        "message": "Data from Python Backend via Docker Network"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)