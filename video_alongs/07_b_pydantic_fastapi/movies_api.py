from fastapi import FastAPI
from agents import movie_agent
from data_models import Prompt

app = FastAPI()

@app.get("/movies")
async def read_movies():
    pass

@app.post("/movies/create_movie")
async def create_movie(query: Prompt):
    result = await movie_agent.run(query.prompt)
    movie = result.output
    
    return movie