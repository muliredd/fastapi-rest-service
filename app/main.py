from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sample Python app running successfully!"}

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/simha")
def health_s():
    cities = ["Hyderabad", "Bangalore", "Chennai"]
    return cities