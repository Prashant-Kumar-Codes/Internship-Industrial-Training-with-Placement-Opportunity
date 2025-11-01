from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.secret_key = "My@1SecretKey"

# MySQL connection
    app.config['MYSQL_HOST'] = "localhost"
    app.config['MYSQL_USER'] = "root"
    app.config['MYSQL_PASSWORD'] = "admin123"
    app.config['MYSQL_DATABASE'] = "Student_Management_System_Database"

# Mail_Setup: Brevo SMTP config
    app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = '969fcc001@smtp-brevo.com'
    app.config['MAIL_PASSWORD'] = '6za2MbPwpVrB04ch'
    app.config['MAIL_DEFAULT_SENDER'] = 'pkthisisfor1234@gmail.com'
    mail.init_app(app)

# Import routes
    from app.routes.auth import auth
    app.register_blueprint(auth)

    return app



# from flask import Flask
# from flask_socketio import SocketIO

# socketio = SocketIO()

# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'your_secret_key_here_change_this'
    
#     socketio.init_app(app, cors_allowed_origins="*")
    
#     # CORRECT: Import Blueprint directly from auth.py
#     from app.routes.auth import auth
#     app.register_blueprint(auth)
    
#     # Import socketio events
#     from app import socketio_events
    
#     return app
