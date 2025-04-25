# Agro Nexus Frontend

This is the frontend application for Agro Nexus, built with Flask, HTML, CSS, and JavaScript. It provides a user interface for plant disease detection, crop recommendations, and agricultural data analysis.

## Project Structure

```
frontend/
├── templates/          # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── ...
├── static/            # Static files
│   ├── stylesheets/   # CSS files
│   ├── scripts/       # JavaScript files
│   ├── images/        # Image assets
│   └── components/    # Reusable components
└── server.py          # Simple Flask server for frontend
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with the following variables:
```
BACKEND_API_URL=your_backend_api_url
```

4. Run the frontend server:
```bash
python server.py
```

The application will be available at `http://localhost:3000`.

## Features

- Plant Disease Detection
- Crop Recommendations
- Agricultural Data Analysis
- User Authentication
- Dashboard
- Irrigation System
- Seed Management
- Price Tracking

## Deployment

This frontend is configured for deployment on Vercel. Make sure to:

1. Connect your GitHub repository to Vercel
2. Set up the environment variables in your Vercel project settings
3. Configure the build settings for a Flask application
4. Deploy your application

## Tech Stack

- Flask
- HTML5
- CSS3
- JavaScript
- Bootstrap
- jQuery
- Chart.js 