from flask import Flask, render_template, send_from_directory
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get backend API URL from environment variable
BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:5000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/disease')
def disease():
    return render_template('disease.html')

@app.route('/crop_recom')
def crop_recom():
    return render_template('crop_recom.html')

@app.route('/track')
def track():
    return render_template('track.html')

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.route('/seeds')
def seeds():
    return render_template('seeds.html')

@app.route('/price')
def price():
    return render_template('price.html')

@app.route('/problems')
def problems():
    return render_template('problems.html')

@app.route('/height')
def height():
    return render_template('height.html')

@app.route('/simple_irrigation')
def simple_irrigation():
    return render_template('simple_irrigation.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port) 