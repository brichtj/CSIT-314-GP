from flask import Blueprint, request, jsonify
from control.user_login_controller import UserLoginController
import json

create_bp = Blueprint('create_bp', __name__)

user_controller = UserLoginController()


@create_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    UserProfileID = data.get('UserProfileID')
    Email = data.get('Email')
    Password = data.get('Password')

    result = user_controller.login(UserProfileID, Email, Password)

    if result['success']:
        output = json.dumps(result['user'])
        return jsonify('Login successfully', {'User': output}), 200
    
    return jsonify({'error': result['error']}), 401

@create_bp.route('/',methods=['GET'])
def default():
    return jsonify({'success':True})
