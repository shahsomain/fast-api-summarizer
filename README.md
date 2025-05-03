# FastAPI Text Summarizer

This is a simple FastAPI-based API that summarizes a block of text using Hugging Face's Transformers.

## Features

- Uses `facebook/bart-large-cnn` model
- Accepts raw text via POST
- Returns a concise summary

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
Visit the Swagger UI at: http://127.0.0.1:8000/docs
