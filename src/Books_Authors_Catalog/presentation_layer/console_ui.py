"""Contains the definition for a ConsoleUI class."""

from Books_Authors_Catalog.service_layer.app_services import AppServices
from Books_Authors_Catalog.application_base import ApplicationBase
from prettytable import PrettyTable
from Books_Authors_Catalog.infrastructure_layer.book import Book
from Books_Authors_Catalog.infrastructure_layer.author import Author
from Books_Authors_Catalog.infrastructure_layer.bookauthor import BookAuthor
import sys
import inspect

class ConsoleUI(ApplicationBase):
    """Defines the ConsoleUI class."""
    def __init__(self, config:dict)->None:
        """Initializes object."""
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__,
                         logfile_prefix_name=self.META["log_prefix"])
        self.app_services = AppServices(config)

    #Public Methods
    def display_menu(self)->None:
        """Display the menu."""
        print(f"\n\n\t\tThe Books and Authors Catalog Menu")
        print()
        print(f"\t1. View all Books")
        print(f"\t2. View all Authors")
        print(f"\t3. View all Book-Author Links")
        print(f"\t4. Search Books by Title")
        print(f"\t5. Search Authors by Last Name")
        print(f"\t6. Add New Book")
        print(f"\t7. Add New Author")
        print(f"\t8. Link Author to a Book (By Book_ID & Author_ID)")
        print(f"\t9. Delete a Book-Author Link (By Book_ID & Author_ID)")
        print(f"\t10. Delete a Book (By Book_ID)")
        print(f"\t11. Delete an Author (By Author_ID)")
        print(f"\t12. Exit")
        print()

    def process_menu_choice(self)->None:
        """Processes users menu choice."""
        menu_choice = input("\tMenu Choice: ")

        match menu_choice:
            case '1': self.view_all_books()
            case '2': self.view_all_authors()
            case '3': self.view_all_bookauthor()
            case '4': self.search_books_by_title()
                #title_ask = input(f"What's the title of the book you're looking for? ")
                #self.search_books_by_title()

            case '5': self.search_authors_by_last_name()
            case '6': self.add_new_book()
            case '7': self.add_new_author()
            case '8': self.link_author_to_a_book()
            case '9': self.delete_a_bookauthor_link()
            case '10': self.delete_a_book_by_bookID()
            case '11': self.delete_author_by_authorID()
            case '12': sys.exit()
            case _: print(f"Invalid Menu Choice {menu_choice[0]}")

    def view_all_books(self)->None:
        """Display books."""
        print("\n\tThe Book Table! ")
        books = self.app_services.view_all_books()
        book_table = PrettyTable()
        book_table.field_names = ['Book_ID', 'Title', 'Genre', 
                                'Publication_Year', 'ISBN']
        for book in books:
            book_table.add_row([book.Book_ID, book.Title, book.Genre, book.Publication_Year, book.ISBN])
        #print("Debug:", type(books), books)
        #for (Book_ID, Title, Genre, Publication_Year, ISBN) in books:
            #book_table.add_row([Book_ID, Title, Genre, Publication_Year, ISBN])
        print(book_table)


    #def view_all_books(self)->None:
        #"""Display books."""
        #print("view_all_books() method stub called ...")

    def view_all_authors(self)->None:
        """Display authors."""
        print("\n\tThe Author Table! ")
        authors = self.app_services.view_all_authors()
        author_table = PrettyTable()
        author_table.field_names = ['Author_ID', 'First_Name', 'Last_Name', 
                                'Birth_Year', 'Country']
        for author in authors:
            author_table.add_row([author.Author_ID, author.First_Name, author.Last_Name, author.Birth_Year, author.Country])
        #print("Debug:", type(authors), authors)
        #for (Author_ID, First_Name, Last_Name, Birth_Year, Country) in authors:
            #author_table.add_row([Author_ID, First_Name, Last_Name, Birth_Year, Country])
        print(author_table)

    def view_all_bookauthor(self)->None:
        """Display book-author links."""
        print("\n\tThe Book-Author Table! ")
        bookauthor = self.app_services.view_all_bookauthor()
        bookauthor_table = PrettyTable()
        bookauthor_table.field_names = ['bookID', 'authorID']
        for ba in bookauthor:
            bookauthor_table.add_row([ba.bookID, ba.authorID])
        print(bookauthor_table)

    def search_books_by_title(self)->None:
        """List searched books by title."""
        print(f"\nSearch Book List! ")
        title_ask = input(f"What's the title of the book you're looking for? ")
        #print(title_ask)
        
       #searchbook = Book()
        #searchbook.Title = title_ask

        results = self.app_services.search_books_by_title(title_ask)
        searchbook_table = PrettyTable()
        searchbook_table.field_names = ['Book_ID', 'Title', 'Genre', 'Publication_Year', 'ISBN']
        if not results:
            print(f"\nNo books found with that title.")
            return
        else:
            #searchbook_table = PrettyTable()
            #searchbook_table.field_names = ['Book_ID', 'Title', 'Genre', 'Publication_Year', 'ISBN']
            for books in results:
                searchbook_table.add_row([books.Book_ID, books.Title, books.Genre, books.Publication_Year, books.ISBN])
                print(f"\nBook(s) was found!")
                #print(searchbook_table)
            return results
        #print("search_books_by_title() method stub called ...")
        #if title_ask not in searchbook_table:
            #print("Book was not found!")
        #else:
            #print("Book was found!")
            #print(searchbook_table)
    
    def search_authors_by_last_name(self)->None:
        """List searched authors by last name."""
        print("search_authors_by_last_name() method stub called ...")

    def add_new_book(self)->None:
        """List new book."""
        print("\n\tAdd New Book! ")
        book = Book()
        try:
            book.Title = input("Title: ")
            book.Genre = input("Genre: ")
            book.Publication_Year = input("Publication_Year: ")
            book.ISBN = input("ISBN: ")
            book = self.app_services.add_new_book(book=book)
            print(f"New Book_ID: {book.Book_ID}")
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                   f'{e}')

    def add_new_author(self)->None:
        """List new author."""
        print("\n\tAdd New Author! ")
        author = Author()
        try:
            author.First_Name = input("First Name: ")
            author.Last_Name = input("Last Name: ")
            author.Birth_Year = input("Birth Year: ")
            author.Country = input("Country: ")
            author = self.app_services.add_new_author(author=author)
            print(f"New Author_ID: {author.Author_ID}")
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                   f'{e}')

    def link_author_to_a_book(self):
        """List author-book link."""
        print("\n\tAdd new book-author link! ")
        bookID = int(input("Enter Book ID: "))
        authorID = int(input("Enter Author ID: "))
        try:
            bookauthor = BookAuthor()
            bookauthor.bookID = bookID
            bookauthor.authorID = authorID
            results = self.app_services.link_book_author(bookauthor=bookauthor)
        #try:
            #bookID = int(input("Enter Book ID: "))
            #authorID = int(input("Enter Author ID: "))
            #results = self.app_services.link_book_author(bookauthor=bookauthor)
            #print(f"New Book ID: {bookauthor.bookID}")
            #print(f"New Author ID: {bookauthor.authorID}")
            if results is None:
                print("\nCould not create link. Check that the Book_ID and Author_ID exist.")
            else:
                print(f"\nLinked Book {results.bookID} to Author {results.authorID}.")
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                   f'{e}') 

    def delete_a_bookauthor_link(self):
        """Delete a book-author link."""
        print(f"\n\tDelete a Book-Author Link! ")
        print(f"\n\tYou need the Book ID and Author ID for the link you would like to delete!")
        bookID = int(input("Enter Book ID: "))
        authorID = int(input("Enter Author ID: "))
        try: 
            entry_deleted = self.app_services.delete_a_bookauthor_link(bookID, authorID)

        #print(f"\n [DEBUG] entry_deleted = {entry_deleted!r} (type: {type(entry_deleted)})\n")
            if entry_deleted is None:
            #print(f"\nBook-Author {bookID}, {authorID} link deleted!!!")
            #print(f"\nNo existing Book-Author Link.")
                print(f"\nError with deletion")
            elif entry_deleted == 0:
                print(f"\nNo existing Book-Author Link.")
            else:
            #print(f"\nNo existing Book-Author Link.")
                print(f"\nBook-Author {bookID}, {authorID} link deleted!!!")
        except Exception as e:
           self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                   f'{e}')  
    
    def delete_a_book_by_bookID(self)->None:
        """Delete book."""
        print(f"\n\tDelete a Book! ")
        print(f"\n\tYou need the Book_ID for the author you would like to delete!")
        Book_ID = int(input("Enter Book_ID: "))
        try:
            entry_deleted = self.app_services.delete_a_book(Book_ID)
            if entry_deleted is None:
                print(f"\nError with deletion!")
            elif entry_deleted == 0: 
                print(f"\nNo existing Book.")
            else:
                print(f"\nBook {Book_ID} was deleted!")
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                   f'{e}') 
        
    def delete_author_by_authorID(self)->None:
        """Delete an author."""
        print(f"\n\tDelete an Author! ")
        print(f"\n\tYou need the Author_ID for the author you would like to delete!")
        Author_ID = int(input("Enter Author_ID: "))
        try:
            entry_deleted = self.app_services.delete_an_author(Author_ID)
            if entry_deleted is None:
                print(f"\nError with deletion")  
            elif entry_deleted == 0:
                print(f"\nNo existing Author.")
            else:
                print(f"\nAuthor {Author_ID} was deleted!")
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                   f'{e}') 
    
    def start(self)->None:
        while True:
            self.display_menu()
            self.process_menu_choice()

       