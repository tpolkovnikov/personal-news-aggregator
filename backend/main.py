from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/send_message")
def read_root():
    return {"message": "Hello, FastAPI!"}