from fastapi import FastAPI
from datetime import *

app = FastAPI()

@app.get("/a")
def index():
  
  return {"current_time":datetime.now()}