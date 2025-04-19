from flask import Flask
from app.boundary.user_login_boundary import login_bp
from app.boundary.user_logout_boundary import logout_bp

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)

if __name__ == '__main__':
    app.run(debug=True)