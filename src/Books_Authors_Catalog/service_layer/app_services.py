"""Implements AppServices Class."""

from Books_Authors_Catalog.application_base import ApplicationBase
from Books_Authors_Catalog.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
from Books_Authors_Catalog.infrastructure_layer.book import Book
from Books_Authors_Catalog.infrastructure_layer.author import Author
from Books_Authors_Catalog.infrastructure_layer.bookauthor import BookAuthor
import inspect
import json
from typing import List, Dict

class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)

    def view_all_books(self)->str:
        """Returns all books as JSON string"""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.view_all_books()
            return results
            #return json.dumps(results)
        except Exception as e:
            self._logger_error(f'{inspect.currentframe().f_code.co_name}:{e}')

    def view_all_authors(self)->str:
        """Returns all authors as JSON string."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.view_all_authors()
            return results
        except Exception as e:
           self._logger_error(f'{inspect.currentframe().f_code.co_name}:{e}') 
    
    def view_all_bookauthor(self)->str:
        """Returns all authors as JSON string."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.view_all_bookauthor()
            return results
        except Exception as e:
           self._logger_error(f'{inspect.currentframe().f_code.co_name}:{e}') 

    def add_new_book(self, book:Book)-> Book:
        "Creates new book record."
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.add_new_book(book)
            return results
        except Exception as e:
            self._logger.log_error(f'In {inspect.currentframe().f_code.co_name}()...')

    def add_new_author(self, author:Author)-> Author:
        "Creates new author record."
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.add_new_author(author)
            return results
        except Exception as e:
            self._logger.log_error(f'In {inspect.currentframe().f_code.co_name}()...')

    def link_book_author(self, bookauthor:BookAuthor)->BookAuthor | None:
        "Creates new book-author link."
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.link_author_to_a_book(bookauthor)
            return results
        except Exception as e:
            self._logger.log_error(f'In {inspect.currentframe().f_code.co_name}()...')
            return None

    def delete_a_bookauthor_link(self, bookID: int, authorID:int)->int | None:
        "Deletes a book-author link."  
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.delete_a_bookauthor_link(bookID, authorID)
            return results   
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')  

    def delete_a_book(self, Book_ID: int)->int | None:
        "Deletes book record by Book_ID."
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.delete_a_book(Book_ID)
            return results   
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')

    def delete_an_author(self, Author_ID: int)->int | None:
        """Deletes an author by Author_ID."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.delete_an_author(Author_ID)
            return results   
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')