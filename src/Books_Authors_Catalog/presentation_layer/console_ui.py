"""Contains the definition for a ConsoleUI class."""

from Books_Authors_Catalog.service_layer.app_services import AppServices
from Books_Authors_Catalog.application_base import ApplicationBase

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
        print(f"\t\tThe Books and Authors Catalog Menu")
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

    def start(self)->None:
        self.display_menu()

       