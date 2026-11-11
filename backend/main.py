from fastapi import FastAPI
import uvicorn

klu = FastAPI(title="AI Tutor", 
              description="AI Tutor Pbl Project",
              version="1.0.0")

@klu.get("/")
def home():
    return {"message":"Welcome to AI Tutor project"}

@klu.get("/demo")
def demo():
    return {"message":"KL-University"}

@klu.get("/askquestion")
def ask():
    return {"message":"What is LLM", "Answer":"Large Language Model"}

@klu.get("/student")
def student():
    return {"id":1,"name":"Ram","gender":"male","course":"DSA"}

@klu.get("/students")
def getstudents():
    return [{"id":1,"name":"Ram","gender":"male","course":"DSA"},
            {"id":2,"name":"Sita","gender":"female","course":"DSA-2"},
            {"id":3,"name":"Samyuktha","gender":"female","course":"DSA-3"}]

if __name__ == "__main__":
    uvicorn.run("main:klu",host="127.0.0.1",port=2027,reload=True)