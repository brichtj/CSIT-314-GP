from flask import Flask, request, jsonify
import psycopg2

from boundary.user_login_gateway import UserLoginGateway
from control.user_controller import UserController

app = Flask(__name__)

# Setup DB connection
host = "localhost"       # "localhost" or an IP address
database = "csit314"     # your_database name
user = "root"       # user
password = "root123"  # password

try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    # Set the client encoding to UTF-8 explicitly
    connection.set_client_encoding('UTF8')
    cursor = connection.cursor()

    print("Database: Connection established successfully!")

    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Database: PostgreSQL version: {db_version}")

except Exception as e:
    print(f"Error connecting to the database: {e}")

# Inject gateway into controller
login_gateway = UserLoginGateway(cursor)

user_controller = UserController(login_gateway)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    profile = data.get('user_profile')
    email = data.get('email')
    password = data.get('password')

    result = user_controller.login(profile, email, password)

    if result['success']:
        return jsonify(result['user']), 200
    else:
        return jsonify({'error': result['error']}), 401


if __name__ == '__main__':
    app.run(debug=True)