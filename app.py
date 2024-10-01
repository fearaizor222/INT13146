from flask import Flask
import os
from routes import init_routes

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)