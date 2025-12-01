"""Contains the definition for the Book class."""
import json

class Book():
    """Implements a Book entity."""

    def __init__(self):
        self.Book_ID:int = 0
        self.Title:str = ""
        self.Genre:str = ""
        self.Publication_Year:int = 0
        self.ISBN:str = ""

    def __str__(self)->str:
        return self.to_json()
    
    def __repr__(self)->str:
        return self.to_json()
    
    def to_json(self)->str:
        book_dict = {}
        book_dict['Book_ID'] = self.Book_ID
        book_dict['Title'] = self.Title
        book_dict['Genre'] = self.Genre
        book_dict['Publication_Year'] = self.Publication_Year
        book_dict['ISBN'] = self.ISBN
        