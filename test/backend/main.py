from flask import Flask
from flask_cors import CORS  # Import CORS
from app.boundary.user_login_boundary import login_bp
from app.boundary.user_logout_boundary import logout_bp

app = Flask(__name__)

# Enable CORS for your app
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])  # Add your frontend URL

# Register your blueprints
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)

