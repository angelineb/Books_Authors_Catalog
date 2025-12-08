"""Defines the MySQLPersistenceWrapper class."""

from Books_Authors_Catalog.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json
from typing import List
from Books_Authors_Catalog.infrastructure_layer.book import Book
from Books_Authors_Catalog.infrastructure_layer.author import Author
from Books_Authors_Catalog.infrastructure_layer.bookauthor import BookAuthor
from enum import Enum

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
		
		#Book Column ENUMS
		self.BookColumns = \
			Enum('BookColumns', [('Book_ID', 0), ('Title', 1), 
				('Genre', 2), ('Publication_Year', 3), ('ISBN', 4)])
		#Author Column ENUMS
		self.AuthorColumns = \
			Enum('AuthorColumns', [('Author_ID', 0), ('First_Name', 1),
				('Last_Name', 2), ('Birth_Year', 3), ('Country', 4) ])
		#BookAuthor Columns ENUMS
		self.BookAuthorColumns = \
			Enum('BookAuthorColumns', [('bookID, 0'), ('authorID, 1')])

		# SQL String Constants

		self.VIEW_ALL_BOOKS = \
			f"SELECT Book_ID, Title, Genre, Publication_Year, ISBN " \
			f"FROM Books_Table"
		
		self.VIEW_ALL_AUTHORS = \
			f"SELECT Author_ID, First_Name, Last_Name, Birth_Year, Country " \
			f"FROM Authors_Table"
		
		self.VIEW_ALL_BOOKAUTHOR = \
			f"SELECT bookID, authorID  " \
			f"FROM Books_Authors_XREF " \
			f"ORDER BY bookID, authorID"
		
		self.ADD_NEW_BOOK = \
			f"INSERT INTO Books_Table (Book_ID, Title, Genre, Publication_Year, ISBN) " \
			f"VALUES (%s, %s, %s, %s, %s)"
		
		self.ADD_NEW_AUTHOR = \
			f"INSERT INTO Authors_Table (Author_ID, First_Name, Last_Name, Birth_Year, Country) " \
			f"VALUES (%s, %s, %s, %s, %s)"
		
		self.LINK_AUTHOR_TO_A_BOOK = \
			f"INSERT INTO Books_Authors_XREF (bookID, authorID) " \
			f"VALUES (%s, %s)"

		self.DELETE_A_BOOKAUTHOR_LINK = \
			f"DELETE FROM Books_Authors_XREF " \
			f"WHERE bookID = %s AND authorID = %s"
		
		self.DELETE_A_BOOK = \
			f"DELETE FROM Books_Table " \
			f"WHERE Book_ID LIKE %s"

		self.DELETE_AN_AUTHOR = \
			f"DELETE FROM Authors_Table " \
			f"WHERE Author_ID = %s"
	




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
				book_list = self._populate_book_objects(results)
			#for book in book_list:

				#return results
				return book_list
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
				author_list = self._populate_author_objects(results)
				#return results
				return author_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def view_all_bookauthor(self)-> list:
		"Returns a list of all books-authors links."
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor(dictionary=True)
				with cursor:
					cursor.execute(self.VIEW_ALL_BOOKAUTHOR)
					results = cursor.fetchall()
					booksauthors_list = self._populate_booksauthors_objects(results)
				
				return booksauthors_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
	

	def add_new_book(self, book:Book)-> Book:
		"""Adds a new book to the list and Book_ID."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.ADD_NEW_BOOK, 
						([book.Book_ID, book.Title, book.Genre, book.Publication_Year, book.ISBN]))
					connection.commit()
					self._logger.log_debug(f"Updated {cursor.rowcount} row.")
					self._logger.log_debug(f"Last Row Book_ID: {cursor.lastrowid}.")
					book.Book_ID = cursor.lastrowid
					#results = cursor.fetchall()
				
				return book
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def add_new_author(self, author:Author)-> Author:
		"""Adds a new author to the list and Author_ID."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.ADD_NEW_AUTHOR,
						([author.Author_ID, author.First_Name, author.Last_Name, author.Birth_Year, author.Country]))
					connection.commit()
					self._logger.log_debug(f"Updated {cursor.rowcount} row.")
					self._logger.log_debug(f"Last Row Book_ID: {cursor.lastrowid}.")
					author.Author_ID = cursor.lastrowid
					#results = cursor.fetchall()
				
				return author
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def link_author_to_a_book(self, bookauthor:BookAuthor)-> BookAuthor | None:
		"""Returns a list that contains the new author-book link."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.LINK_AUTHOR_TO_A_BOOK, 
						([bookauthor.bookID, bookauthor.authorID]))
					connection.commit()
					self._logger.log_debug(f"Updated {cursor.rowcount} row.")
					#self._logger.log_debug(f"Last Row Book ID: {cursor.lastrowid}.")
					#self._logger.log_debug(f"Last Row Author ID: {cursor.lastrowid}.")
					#bookauthor.bookID = cursor.lastrowid
					#bookauthor.authorID = cursor.lastrowid
					#results = cursor.fetchall()
				
				return bookauthor
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
	
	def delete_a_bookauthor_link(self, bookID: int, authorID: int)-> int:
		"""Deletes book-author link."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.DELETE_A_BOOKAUTHOR_LINK, (bookID, authorID))
					connection.commit()
				
					#results = cursor.fetchall()
				
					#return results
					rows_deleted = cursor.rowcount
					return rows_deleted
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
	
	def delete_a_book(self, Book_ID: int)-> int:
		"""Deletes a book by its Book_ID."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					#Deletes the corresponding bookid from xref before book table.
					xref_code = "DELETE FROM Books_Authors_XREF WHERE bookID = %s"
					cursor.execute(xref_code, (Book_ID,))
					cursor.execute(self.DELETE_A_BOOK, (Book_ID,))
					connection.commit()
					
					rows_deleted = cursor.rowcount
					connection.commit()
					return rows_deleted
				
					#results = cursor.fetchall()
				
				#return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def delete_an_author(self, Author_ID: int)-> int:
		"""Deletes an author by its Author_ID."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					#Deletes the corresponding authorid from xref before author table.
					xref_code = "DELETE FROM Books_Authors_XREF WHERE authorID = %s"
					cursor.execute(xref_code, (Author_ID,))
					cursor.execute(self.DELETE_AN_AUTHOR, (Author_ID,))
					connection.commit()
					#results = cursor.fetchall()
				
				#return results
					rows_deleted = cursor.rowcount
					connection.commit()
					return rows_deleted
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

	def _populate_book_objects(self, results:List)->List[Book]:
		"""Populates and returns a list of Book objects"""
		book_list = []
		try:
			for row in results:
				book = Book()
				book.Book_ID = row[self.BookColumns['Book_ID'].value]
				book.Title = row[self.BookColumns['Title'].value]
				book.Genre = row[self.BookColumns['Genre'].value]
				book.Publication_Year = row[self.BookColumns['Publication_Year'].value]
				book.ISBN = row[self.BookColumns['ISBN'].value]
				book_list.append(book)
			return book_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def _populate_author_objects(self, results:List)->List[Author]:
		"""Populates and returns a list of Author objects"""
		author_list = []
		try:
			for row in results:
				author = Author()
				author.Author_ID = row[self.AuthorColumns['Author_ID'].value]
				author.First_Name = row[self.AuthorColumns['First_Name'].value]
				author.Last_Name = row[self.AuthorColumns['Last_Name'].value]
				author.Birth_Year = row[self.AuthorColumns['Birth_Year'].value]
				author.Country = row[self.AuthorColumns['Country'].value]
				author_list.append(author)
			return author_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def _populate_booksauthors_objects(self, results:List)->List[BookAuthor]:
		"""Populates and returns a list of BooksAuthors objects"""
		booksauthors_list = []
		try:
			for row in results:
				booksauthors = BookAuthor()
				booksauthors.bookID = row["bookID"]
				booksauthors.authorID = row["authorID"]
				#booksauthors.bookID = row[self.BookAuthorColumns['bookID'].value]
				#booksauthors.authorID = row[self.BookAuthorColumns['authorID'].value]
				booksauthors_list.append(booksauthors)
			return booksauthors_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
			
	


