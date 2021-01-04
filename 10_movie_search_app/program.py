print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import requests.exceptions
from movie_client import MovieClient

def print_results(search_results):
	print("Found {} results ...".format(len(search_results)))
	for result in search_results:
		print("{} -- {}".format(result.year, result.title))


def main():
	while True:
		try:
			search_text = input("Enter search text (x to exit): ")
			if search_text == 'x':
				print("Exiting ...")
				break
			else:
				search_results = MovieClient(search_text).perform_search()
				print_results(search_results)
		except requests.exceptions.ConnectionError as ce:
			print("Error: either your network is down or the host is unreachable")
		except ValueError as ve:
			print("Error: Your search string is invalid {}".format(ve))
		except Exception as e:
			print("Error: {}".format(e))

if __name__ == "__main__":
	main()
