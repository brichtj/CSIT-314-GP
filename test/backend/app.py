

from flask import Flask, request, jsonify
from control import login_control, createUser_control
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)  # Allow React to call the backend


# login funtion
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    profile = data.get('login_profile')
    email = data.get('email')
    password = data.get('password')

    # check empty username and empty password
    if not email or not password:
        return jsonify({"error": "email and password required"}), 400

    try:
        # call controller
        user = login_control(profile, email, password)

        # Object toString()
        user_dict = user.__dict__
        # return JSON
        return jsonify({"user": user_dict}), 200    # Success response

    except Exception as e:
        # print error messages for debug purposes
        print(str(e))
        # Return appropriate error message and status
        return jsonify({"error": str(e)}), 400


@app.route('/createUser', methods=['POST'])
def createUser():
    data = request.get_json()
    profile = data.get('user_profile')
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    phone = data.get('phone')
    add = data.get('address')

    if not username or not email or not phone:
        return jsonify({"error": "missing data when creating user"})

    try:
        # maybe password creation need another funtion
        if createUser_control(profile, username, password, email, phone, add):
            return jsonify({"User created"}), 200    # Success response
    except Exception as e:
        # print error messages for debug purposes
        print(str(e))
        # Return appropriate error message and status
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
