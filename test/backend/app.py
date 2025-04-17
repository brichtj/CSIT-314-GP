from flask import Flask, request, jsonify
from flask_cors import CORS
from control import login_control

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    profile = data.get('login_profile')
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    try:
        user = login_control(profile, username, password)
        return jsonify({"user": user.__dict__}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)