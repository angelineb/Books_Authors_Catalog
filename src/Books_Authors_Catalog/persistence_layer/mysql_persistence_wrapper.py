"""Defines the MySQLPersistenceWrapper class."""

from Books_Authors_Catalog.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json

class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		self.META = config["meta"]
		self.DATABASE = config["database"]
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = \
			self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = \
			self._initialize_database_connection_pool(self.DB_CONFIG)
		

		# SQL String Constants

		self.VIEW_ALL_BOOKS = \
			f"SELECT * " \
			f"FROM Books_Table"
		
		self.VIEW_ALL_AUTHORS = \
			f"SELECT * " \
			f"FROM Authors_Table"
		
		self.SEARCH_BOOKS_BY_TITLE = \
			f"SELECT * " \
			f"FROM Books_Table" \
			f"WHERE Title LIKE '%'"
		
		self.SEARCH_AUTHORS_BY_LASTNAME = \
			f"SELECT * " \
			f"FROM Authors_Table" \
			f"WHERE Last_Name LIKE '%s'"
		
		self.ADD_NEW_BOOK = \
			f"INSERT INTO Books_Table (Book_ID, Title, Genre, Publication_Year, ISBN) " \
			f"VALUES (%s, %s, %s, %s, %s)"
		
		self.ADD_NEW_AUTHOR = \
			f"INSERT INTO Authors_Table (Author_ID, First_Name, Last_Name, Birth_Year, Country) " \
			f"VALUES (%s, %s, %s, %s, %s)"
		
		self.LINK_AUTHOR_TO_A_BOOK = \
		f"INSERT INTO Books_Authors_XREF (bookID, authorID) " \
		f"VALUES (%s, %s)"

		self.DELETE_A_BOOK = \
		f"DELETE FROM Books_Table " \
		f"WHERE ISBN LIKE '%s'"

		self.DELETE_AN_AUTHOR = \
		f"DELETE FROM Authors_Table " \
		f"WHERE Author_ID LIKE '%s'"
	




	# MySQLPersistenceWrapper Methods

	def view_all_books(self)-> list:
		"""Returns a list of all books."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.VIEW_ALL_BOOKS)
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


	def view_all_authors(self)-> list:
		"""Returns a list of all authors."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.VIEW_ALL_AUTHORS)
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def search_books_by_title(self, Title: str)-> list:
		"""Return the book search by title."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SEARCH_BOOKS_BY_TITLE, ([Title]))
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
		
	def search_authors_by_lastname(self, Last_Name: str)-> list:
		"""Return the author search by last name."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SEARCH_AUTHORS_BY_LASTNAME, ([Last_Name]))
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def add_new_book(self)-> list:
		"""Adds a new book to the list and Book_ID."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.ADD_NEW_BOOK)
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def add_new_authors(self)-> list:
		"""Adds a new author to the list and Author_ID."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.ADD_NEW_AUTHOR)
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def link_author_to_a_book(self, bookID, authorID)-> list:
		"""Returns a list that contains the new author-book link."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.LINK_AUTHOR_TO_A_BOOK, (bookID, authorID))
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
	
	def delete_a_book(self, ISBN)-> list:
		"""Deletes a book by its ISBN."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.DELETE_A_BOOK)
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def delete_an_author(self, Author_ID)-> list:
		"""Deletes an author by its Author_ID."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.DELETE_AN_AUTHOR)
					results = cursor.fetchall()
				
				return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

		##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config:dict)->MySQLConnectionPool:
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = \
				MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
					pool_size=self.DATABASE["pool"]["size"],
					pool_reset_session=self.DATABASE["pool"]["reset_session"],
					use_pure=self.DATABASE["pool"]["use_pure"],
					**config)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem creating connection pool: {err}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Check DB cnfg:\n{json.dumps(self.DATABASE)}')
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Problem creating connection pool: {e}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Check DB conf:\n{json.dumps(self.DATABASE)}')
