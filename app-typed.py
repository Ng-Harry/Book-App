from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

app = FastAPI()

class Book(BaseModel):
    id: str
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
    
class Books(BaseModel):
    books: list[Book]

class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = None
    error_message: Optional[str] = None
    data: Optional[Book | Books]
    
books: dict[str, Book] = {}

@app.get("/")
def home():
    return {"message": "Hello from the books API"}

@app.get("/books")
def get_books():
    return books

@app.get("/books/{id}")
def get_book_by_id(id: UUID):
    book = books.get(str(id))
    if not book:
        return {"error": "Book not found"}
    return book

@app.post("/books")
def add_book(book_in: BookCreate):
    book = Book(
        id=str(uuid4()), **book_in.model_dump()
    )
    books[book.id] = book
    return Response(message="Book added successfully", data=book)

@app.put("/books/{id}")
def update_book(id: UUID, book_in: BookUpdate):
    book = books.get(str(id))
    if not book:
        return {"error": "Book not found"}
    
    book.title = book_in.title
    book.pages = book_in.pages
    
    return Response(message="Book updated successfully")

