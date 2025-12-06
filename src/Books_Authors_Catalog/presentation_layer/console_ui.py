"""Contains the definition for a ConsoleUI class."""

from Books_Authors_Catalog.service_layer.app_services import AppServices
from Books_Authors_Catalog.application_base import ApplicationBase
from prettytable import PrettyTable
import sys

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
        print(f"\t3. Search Books by Title")
        print(f"\t4. Search Authors by Last Name")
        print(f"\t5. Add New Book")
        print(f"\t6. Add New Author")
        print(f"\t7. Link Author to a Book")
        print(f"\t8. Delete a Book (By ISBN)")
        print(f"\t9. Delete an Author (By Author_ID)")
        print(f"\t10. Exit")
        print()

    def process_menu_choice(self)->None:
        """Processes users menu choice."""
        menu_choice = input("\tMenu Choice: ")

        match menu_choice[0]:
            case '1': self.view_all_books()
            case '2': self.view_all_authors()
            case '3': 
                title_ask = input(f"What's the title of the book you're looking for? ")
                self.search_books_by_title()

            case '4': self.search_authors_by_last_name()
            case '5': self.add_new_book()
            case '6': self.add_new_author()
            case '7': self.link_author_to_a_book()
            case '8': self.delete_a_book_by_isbn()
            case '9': self.delete_author_by_authorID()
            case '10': sys.exit()
            case _: print(f"Invalid Menu Choice {menu_choice[0]}")

    def view_all_books(self)->None:
        """Display books."""
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

    def search_books_by_title(self, Title:str)->None:
        """List searched books by title."""
        #title_ask = input(f"What's the title of the book you're looking for? ")
        #print(title_ask)
        searchbooks = self.app_services.search_books_by_title()
        searchbook_table = PrettyTable()
        searchbook_table.field_names = ['Book_ID', 'Title', 'Genre', 
                                'Publication_Year', 'ISBN']
        for books in searchbooks:
            searchbook_table.add_row([books.Book_ID, books.Title, books.Genre, books.Publication_Year, books.ISBN])
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
        print("add_new_book() method stub called...")

    def add_new_author(self)->None:
        """List new author."""
        print("add_new_author() method stub called...")

    def link_author_to_a_book(self)->None:
        """List author-book link."""
        print("link_author_to_a_book() method stub called...")

    def delete_a_book_by_isbn(self)->None:
        """Delete book."""
        print("delete_a_book_by_isbn() method stub called...")
        
    def delete_author_by_authorID(self)->None:
        """Delete author."""
        print("delete_author_by_authorID() method stub called...")
    
    def start(self)->None:
        while True:
            self.display_menu()
            self.process_menu_choice()

       