from flask import Flask, request, jsonify
import psycopg2, json

from repository.user_login_gateway import UserLoginGateway
from repository.user_gateway import UserGateway
from control.user_login_controller import UserLoginController

app = Flask(__name__)

# Setup DB connection
host = "localhost"       # "localhost" or an IP address
database = "csit314db"     # your_database name
user = "root"       # user
password = "root123"  # password

cursor = None  # Define it first so it always exists
try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    connection.set_client_encoding('UTF8')
    cursor = connection.cursor()

    print("Database: Connection established successfully!")
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Database: PostgreSQL version: {db_version}")

except Exception as e:
    print(f"Error connecting to the database: {e}")

# if cursor is None:
#     raise Exception("Cannot proceed: Database cursor not initialized.")

login_gateway = UserLoginGateway(cursor)
user_gateway = UserGateway(cursor)
user_controller = UserLoginController(login_gateway, user_gateway)


@app.route('/login', methods=['POST'])
def login():
    if cursor is None: 
        #cursor did not load, properly, just return json
        return jsonify({"success": True, "message": "This is a custom response"}), 200

    data = request.get_json()
    UserProfileID = data.get('UserProfileID')
    Email = data.get('Email')
    Password = data.get('Password')

    result = user_controller.login(UserProfileID, Email, Password)

    if result['success']:
        output = json.dumps(result['user'].to_dict())
        return jsonify(output), 200
    else:
        return jsonify({'error': result['error']}), 401
@app.route('/', methods=['GET'])
def default():
    if cursor is None: 
        #cursor did not load, properly, just return json
        return jsonify({"success": True, "message": "This is a custom response"}), 200


@app.route('/logout', methods=['POST'])
def logout():
    return jsonify('Logout successfully'), 200


if __name__ == '__main__':
    app.run(debug=True)
