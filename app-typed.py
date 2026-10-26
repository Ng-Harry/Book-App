from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id; str
    title: str
    author: str
    year: int
    pages: int
    language: str
    
    
class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    language: str

class BookUpdate(BaseModel):
    title: str
    pages: int
    
