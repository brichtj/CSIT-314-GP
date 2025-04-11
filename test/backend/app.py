

from flask import Flask, request, jsonify
from control import login_control
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)  # Allow React to call the backend


# login funtion
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # check empty username and empty password
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    try:
        # call controller
        user = login_control(1, username, password)

        # Object toString()
        user_dict = user.__dict__
        # return JSON
        return jsonify({"user": user_dict}), 200    # Success response

    except Exception as e:
        # print error messages for debug purposes
        print(str(e))
        # Return appropriate error message and status
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
