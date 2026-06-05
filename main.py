from fastapi import FastAPI
from database import get_db, sessionmaker


app = FastAPI()

@app.get("/")
def home ():
    return {"message": "Welcome to House Tax System"}



