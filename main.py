from fastapi import FastAPI

app = FastAPI()

@app.get("/a")
def index():
  return {"msg":"WORKING..."}