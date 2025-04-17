from flask import Blueprint, jsonify
login_bp = Blueprint('login_bp', __name__)

logout_bp = Blueprint('logout_bp', __name__)

@logout_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify('Logout successfully'), 200
