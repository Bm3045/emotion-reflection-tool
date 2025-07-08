# Emotion Reflection Tool

A web application that analyzes text emotions with visual results. Users enter their feelings and receive an emotion analysis with corresponding images.

## Features
- Emotion analysis with visual feedback
- Mobile-responsive design
- Loading states and error handling
- Confidence visualization
- Emotion-specific images

## Technologies
- **Frontend**: Next.js, TypeScript, CSS Modules
- **Backend**: Python, FastAPI
- **API Integration**: RESTful communication

## System Requirements
- Node.js v16+
- Python 3.8+
- npm

## Setup Instructions

### 1. Backend Setup (Python API)
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate environment
# Linux/macOS:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend server
uvicorn main:app --reload --port 8000

## Frontend Setup (Next.js App)

# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
