from fastapi import FastAPI
app= FastAPI()

@app.get("/home")
def welcomeMessage():
    return {"message":"Welcome to ICICI Bank Mumbai"}

@app.get("/login")
def loginApp():
    return {"message":"Welcome to Login Page"}

@app.get("/register")
def registerApp():
    return {"message":"Welcome to Registration Page"}