from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str = Field(description="Title of the movie")
    year: int = Field(gt = 1970)
    genre: str = Field(description="Genre of the movie, e.g. Comedy, Drama, Action, if there are multiple genres, pick the dominant one")
    rating: int = Field(gt = 0, lt =6, description="higher rating the better, keep ratings realistic")
    
    class Promt(BaseModel):
        prompt: str = Field(description="""Promt from user to find movie, try to find closest movie even i the user promts something else""")