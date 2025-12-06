"""Implements AppServices Class."""

from Books_Authors_Catalog.application_base import ApplicationBase
from Books_Authors_Catalog.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
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

    def search_books_by_title(self, Title)->str:
        """Returns the searched books by title."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.search_books_by_title(Title)
            return results
        except Exception as e:
           self._logger_error(f'{inspect.currentframe().f_code.co_name}:{e}')    
