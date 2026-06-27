from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def helth_check():
    return {"status": "ok"}