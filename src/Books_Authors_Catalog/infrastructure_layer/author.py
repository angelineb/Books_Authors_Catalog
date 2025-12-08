"""Contains the definition for the Author class."""
import json

class Author():
    """Implements an Author entity."""

    def __init__(self):
        self.Author_ID:int = 0
        self.First_Name:str = ""
        self.Last_Name:str = ""
        self.Birth_Year:int = 0
        self.Country:str = ""

    def __str__(self)->str:
        return self.to_json()
    
    def __repr__(self)->str:
        return self.to_json()
    
    def to_json(self)->str:
        author_dict = {}
        author_dict['Author_ID'] = self.Author_ID
        author_dict['First_Name'] = self.First_Name
        author_dict['Last_Name'] = self.Last_Name
        author_dict['Birth_Year'] = self.Birth_Year
        author_dict['Country'] = self.Country
        