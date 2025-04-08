# app.py (Flask server)
from flask import Flask, request, jsonify
from control import login_control
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)  # Allow React to call the backend


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    try:
        user = login_control(1, username, password)

        user_dict = user.__dict__        
        return jsonify({"user": user_dict}), 200    # Success response

    except Exception as e:
        return jsonify({"error": str(e)}), 400   # Return appropriate error message and status

    print(f"controller end")

if __name__ == '__main__':
    app.run(debug=True)
