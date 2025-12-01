"""Entry point for the Employee Training Application."""

import json
from argparse import ArgumentParser
from Books_Authors_Catalog.service_layer.app_services \
	import AppServices
from Books_Authors_Catalog.presentation_layer.user_interface import UserInterface



def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())
		
		#db = MySQLPersistenceWrapper(config)
		service_layer = AppServices(config)

		books_list = service_layer.view_all_books_as_json()
		#books_list = service_layer.view_all_books()
		print(books_list)
		
		#for books in books_list:
			#print(f'{books}')

	#ui = UserInterface(config)
	#print("")
	#ui.start()
			
		


def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start the application with a configuration file.',
	epilog='POC: Angeline Blandine Ngando | aen64491@marymount.edu')

	parser.add_argument('-c','--configfile',
					help="Configuration file to load.",
					required=True)
	args = parser.parse_args()
	return args



if __name__ == "__main__":
	main()