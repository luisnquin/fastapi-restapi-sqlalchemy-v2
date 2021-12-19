pip install -r requirements.txt
uvicorn src.main:app --reload --port=8000
echo "Listening on http://127.0.0.1:8000"
echo "Visit this http://127.0.0.1:8000/docs"