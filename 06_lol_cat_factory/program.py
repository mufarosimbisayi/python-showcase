print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import os
import requests
import shutil
import subprocess

#get or create folder
#download cats
#display cats

def get_or_create_folder():
	folder = 'cat_folder'
	folder = os.path.abspath(os.path.join('.',folder))
	print("... Creating cat folder ...")
	if not os.path.exists(folder) or os.path.isdir(folder):
		os.makedirs(folder)
	else:
		print("... Cat folder already exists ...")
	return folder

def download_and_save_cat(name, folder):
	print("... Downloading {} ...".format(name))
	r = requests.get("http://consuming-python-services-api.azurewebsites.net/cats/random", stream=True)
	if r.status_code == 200:
		file_name = os.path.join(folder, name)
		print("... Download successful, saving {} to {} ...".format(name, file_name))
		with open(file_name, 'wb') as fout:
			shutil.copyfileobj(r.raw, fout)

def display_cats(folder):
	print("... Displaying Cats ...")
	subprocess.call(['open', folder])

def main():
	folder = get_or_create_folder()
	for i in range(1, 10):
		name = "cat_number_{}.jpeg".format(i)
		download_and_save_cat(name, folder)
	display_cats(folder)

if __name__ == "__main__":
	main()
