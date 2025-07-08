from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    text: str

# Emotion to image mapping
emotion_images = {
    "Happy": "https://emojicdn.elk.sh/😄",
    "Sad": "https://emojicdn.elk.sh/😢",
    "Anxious": "https://emojicdn.elk.sh/😰",
    "Excited": "https://emojicdn.elk.sh/🤩",
    "Angry": "https://emojicdn.elk.sh/😠",
    "Calm": "https://emojicdn.elk.sh/😌",
    "Confused": "https://emojicdn.elk.sh/😕",
    "Surprised": "https://emojicdn.elk.sh/😲",
    "Neutral": "https://emojicdn.elk.sh/😐"
}

@app.post("/analyze")
async def analyze_emotion(request: AnalysisRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text input is required")
    
    text = request.text.lower()
    
    keyword_map = {
        "nervous": "Anxious", "anxious": "Anxious", "stressed": "Anxious", "worried": "Anxious",
        "happy": "Happy", "joy": "Happy", "great": "Happy", "good": "Happy",
        "sad": "Sad", "depressed": "Sad", "unhappy": "Sad", "down": "Sad",
        "angry": "Angry", "mad": "Angry", "furious": "Angry", "annoyed": "Angry",
        "calm": "Calm", "peaceful": "Calm", "relaxed": "Calm", "serene": "Calm",
        "confused": "Confused", "unsure": "Confused", "puzzled": "Confused",
        "surprised": "Surprised", "shocked": "Surprised", "amazed": "Surprised",
        "excited": "Excited", "thrilled": "Excited", "pumped": "Excited"
    }
    
    # Find emotion based on keywords
    emotion = next((e for word, e in keyword_map.items() if word in text), "Neutral")
    
    confidence = round(random.uniform(0.7, 0.99), 2)
    
    # Get image URL for emotion
    image_url = emotion_images.get(emotion, emotion_images["Neutral"])
    
    return {
        "emotion": emotion,
        "confidence": confidence,
        "image_url": image_url
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}