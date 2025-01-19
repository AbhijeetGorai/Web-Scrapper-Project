from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from web_scrapper.crew import WebScrapper

app = FastAPI(
    title="Web Scraper API",
    description="API for web scraping with configurable topics",
    version="1.0.0"
)

class ScrapingInput(BaseModel):
    topic: str

class TrainingInput(BaseModel):
    topic: str
    n_iterations: int
    filename: str

class TestInput(BaseModel):
    topic: str
    n_iterations: int
    openai_model_name: str

class ReplayInput(BaseModel):
    task_id: str

@app.post("/scrape")
async def scrape(input_data: ScrapingInput):
    try:
        crew = WebScrapper().crew()
        result = crew.kickoff(inputs={"topic": input_data.topic})
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/train")
async def train(input_data: TrainingInput):
    try:
        crew = WebScrapper().crew()
        result = crew.train(
            n_iterations=input_data.n_iterations,
            filename=input_data.filename,
            inputs={"topic": input_data.topic}
        )
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/test")
async def test(input_data: TestInput):
    try:
        crew = WebScrapper().crew()
        result = crew.test(
            n_iterations=input_data.n_iterations,
            openai_model_name=input_data.openai_model_name,
            inputs={"topic": input_data.topic}
        )
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/replay")
async def replay(input_data: ReplayInput):
    try:
        crew = WebScrapper().crew()
        result = crew.replay(task_id=input_data.task_id)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to Web Scraper API"} 