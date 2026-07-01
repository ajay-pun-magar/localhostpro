from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Get the directory where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def read_index():
    # Build the path to your index.html file
    index_path = os.path.join(BASE_DIR, "index.html")
    return FileResponse(index_path)