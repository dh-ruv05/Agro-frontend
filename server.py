from flask import Flask, render_template, send_from_directory, jsonify
import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get backend API URL from environment variable with fallback
BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:5000')

@app.route('/')
def index():
    return render_template('index.html', api_url=BACKEND_API_URL)

@app.route('/login')
def login():
    return render_template('login.html', api_url=BACKEND_API_URL)

@app.route('/signup')
def signup():
    return render_template('signup.html', api_url=BACKEND_API_URL)

@app.route('/disease')
def disease():
    return render_template('disease.html', api_url=BACKEND_API_URL)

@app.route('/crop_recom')
def crop_recom():
    return render_template('crop_recom.html', api_url=BACKEND_API_URL)

@app.route('/track')
def track():
    return render_template('track.html', api_url=BACKEND_API_URL)

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html', api_url=BACKEND_API_URL)

@app.route('/seeds')
def seeds():
    return render_template('seeds.html', api_url=BACKEND_API_URL)

@app.route('/price')
def price():
    return render_template('price.html', api_url=BACKEND_API_URL)

@app.route('/problems')
def problems():
    return render_template('problems.html', api_url=BACKEND_API_URL)

@app.route('/height')
def height():
    return render_template('height.html', api_url=BACKEND_API_URL)

@app.route('/simple_irrigation')
def simple_irrigation():
    return render_template('simple_irrigation.html', api_url=BACKEND_API_URL)

@app.route('/health')
def health_check():
    try:
        # Check backend health
        response = requests.get(f"{BACKEND_API_URL}/test")
        return jsonify({
            "status": "healthy",
            "backend_status": response.json()
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port) 