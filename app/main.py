from fastapi import FastAPI, Body
from transformers import pipeline

app = FastAPI()

# Load summarization model (ringan)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.post("/summarize")
def summarize(text: str = Body(...), keyword: str = Body(default="")):
    prompt = f"{keyword}. {text}" if keyword else text
    result = summarizer(prompt, max_length=100, min_length=30, do_sample=False)
    return {"summary": result[0]['summary_text']}
