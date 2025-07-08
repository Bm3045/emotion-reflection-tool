# 🧠 Emotion Reflection Tool

A simple web application where users can reflect on their emotions in a sentence and receive a mock "emotion analysis" from a backend API.

---

## 📦 Tech Stack

- **Frontend:** Next.js (TypeScript, TailwindCSS)
- **Backend:** FastAPI (Python)
- **API Response:** Mocked emotion and confidence score

---

## 🚀 Features

- Mobile-first, clean UI/UX
- Input form for reflections
- Loading + error states
- API integration with mock emotion output

---

## 🛠️ Local Setup Instructions

### 📁 1. Clone the Repository

## Backend Setup (FastAPI)
git clone https://github.com/yourusername/emotion-reflection-tool.git
cd emotion-reflection-tool
cd backend
python -m venv venv         # Create virtual environment (optional)
source venv/bin/activate    # Activate on macOS/Linux
venv\Scripts\activate       # Activate on Windows

pip install fastapi uvicorn
