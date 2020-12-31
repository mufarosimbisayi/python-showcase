print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import os

def get_folder_name():
	folder = input("Please enter the folder you would like to search: ")
	if not os.path.exists(folder) or not os.path.isdir(folder):
		return None
	else:
		folder_path = os.path.abspath(folder)
		return folder_path

def get_search_text():
	text = input("Please enter the text that you would like to search: ")
	if not text:
		return None
	else:
		return text.lower()

def search_file(path_to_file, item, text):
	#matches = []
	with open(path_to_file, 'r') as fin:
		line = fin.readline()
		line_counter = 1
		while line:
			if line.lower().find(text) >= 0:
				yield (item, line_counter, line)
			line_counter += 1
			line = fin.readline()

def search_folder(folder, text):
	items = os.listdir(folder)
	#all_matches = []
	for item in items:
		path_to_file = os.path.abspath(os.path.join(folder, item))
		if os.path.isdir(path_to_file):
			yield from search_folder(path_to_file, text)
			
		else:
			yield from search_file(path_to_file, item, text)

def main():
	folder = get_folder_name()
	if not folder:
		print("Sorry we can't search that location")
		return

	text = get_search_text()
	if not text:
		print("Sorry we can't search for that text")
		return
	matches = search_folder(folder, text)
	for match in matches:
		print("Match found, File: {}, Line: {}, Text: {}".format(
			match[0], match[1], match[2]
		))

if __name__ == '__main__':
	main()
