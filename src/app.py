import sys
import os
from flask_cors import CORS  # type: ignore # Correct import for Flask-CORS
from flask import Flask
from flask_session import Session  # type: ignore # Correct import for Flask sessions
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Auth import auth



app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS for all routes
app.secret_key = os.getenv("SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'   # Use filesystem-based sessions
app.config['SESSION_PERMANENT'] = False
Session(app)  # Initialize Flask-Session

app.register_blueprint(auth, url_prefix='/auth')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run the Flask app in debug mode
