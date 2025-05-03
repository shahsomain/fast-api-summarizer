from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    text = request.text
    try:
        summary = summarizer(text, max_length=60, min_length=15, do_sample=False)
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        return {"error": str(e)}
