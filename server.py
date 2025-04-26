from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landingPage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/submit')
def disease():
    return render_template('disease.html')

@app.route('/crop_rec')
def crop_recom():
    return render_template('index.html')

@app.route('/track')
def track():
    return render_template('track.html')

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.route('/seeds')
def seeds():
    return render_template('seeds.html')

@app.route('/predict_price')
def price():
    return render_template('price.html')

@app.route('/problems_solved')
def problems():
    return render_template('problems.html')

@app.route('/height')
def height():
    return render_template('height.html')

@app.route('/simple_irrigation')
def simple_irrigation():
    return render_template('simple_irrigation.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port) 