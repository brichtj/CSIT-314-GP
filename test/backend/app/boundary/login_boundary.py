from flask import Blueprint, request, jsonify
from app.control.user_login_controller import UserLoginController
import json

login_bp = Blueprint('login_bp', __name__)

user_controller = UserLoginController()


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    UserProfileID = data.get('UserProfileID')
    Email = data.get('Email')
    Password = data.get('Password')

    result = user_controller.login(UserProfileID, Email, Password)

    if result['success']:
        output = json.dumps(result['user'])
        return jsonify(output), 200
    else:
        return jsonify({'error': result['error']}), 401


@login_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify('Logout successfully'), 200