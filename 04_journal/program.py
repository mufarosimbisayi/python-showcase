print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import sys
import os

def get_journal(file_name):
	with open(file_name, 'r') as fin:
		return fin.readlines()

def write_to_journal(file_name, file_list):
	with open(file_name, "w") as fout:
		for line in file_list:
			fout.write(line)

def list_journal_contents(file_list):
	for num, line in enumerate(file_list, start=1):
		sys.stdout.write("{}. {}".format(num, line))

def add_to_journal(text, file_list):
	return file_list.append(text + '\n')

def main():
	file_name = os.path.abspath('journal.txt')
	file_list = get_journal(file_name)
	print("... loading journal from {} ...".format(file_name))
	print("... loaded {} entries ...".format(len(file_list)))
	while 1:
		task = raw_input("What do you want to do? [L]ist, [A]dd, E[x]it? ")
		if task == 'L':
			list_journal_contents(file_list)
		elif task == 'A':
			text = raw_input("Enter your journal entry. ")
			add_to_journal(text, file_list)
		elif task == 'x':
			write_to_journal(file_name, file_list)
			print("... saving to {} ...".format(file_name))
			print("... save complete ...")
			break

main()
		
