"""Contains the definition for the BookAuthor class."""
import json

class BookAuthor():
    """Implements an BookAuthor entity."""

    def __init__(self):
        self.bookID: int = 0
        self.authorID:int = 0
        

    def __str__(self)->str:
        return self.to_json()
    
    def __repr__(self)->str:
        return self.to_json()
    
    def to_json(self)->str:
        booksauthors_dict = {}
        booksauthors_dict['bookID'] = self.bookID
        booksauthors_dict['authorID'] = self.authorID
        return json.dumps(booksauthors_dict)
        