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

    def view_all_books_as_json(self)->str:
        """Returns all books as JSON string"""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.view_all_books()
            #return results
            return json.dumps(results)
        except Exception as e:
            self._logger_error(f'{inspect.currentframe().f_code.co_name}:{e}')
