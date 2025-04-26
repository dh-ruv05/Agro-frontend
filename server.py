from flask import Flask, render_template, send_from_directory, jsonify
import os
from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get backend API URL from environment variable with fallback
BACKEND_API_URL = os.getenv('BACKEND_API_URL', 'http://localhost:5000')

def check_backend_health():
    try:
        response = requests.get(f"{BACKEND_API_URL}/test", timeout=5)
        return response.ok
    except RequestException:
        return False

@app.route('/')
def index():
    backend_healthy = check_backend_health()
    return render_template('index.html', api_url=BACKEND_API_URL, backend_healthy=backend_healthy)

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
        # Check backend health with timeout
        response = requests.get(f"{BACKEND_API_URL}/test", timeout=5)
        return jsonify({
            "status": "healthy",
            "frontend_version": "1.0.0",
            "backend_status": response.json() if response.ok else "unavailable"
        })
    except RequestException as e:
        return jsonify({
            "status": "partially healthy",
            "frontend_version": "1.0.0",
            "backend_status": "unavailable",
            "error": str(e)
        }), 200  # Still return 200 as frontend is working
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Create the app instance
app = app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port) 