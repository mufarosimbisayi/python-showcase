print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import os
import csv
import requests
import statistics
from  purchase import Purchase

def get_and_save_csv():
	file_name = os.path.abspath("data.csv")
	if os.path.exists(file_name):
		return file_name

	apiUrl = "https://raw.githubusercontent.com/mikeckennedy/python-jumpstart-course-demos/master/apps/09_real_estate_analyzer/you_try/SacramentoRealEstateTransactions2008.csv"
	chunk_size = 100

	response = requests.get( apiUrl )

	with open(filename, 'wb') as fout:
		for chunk in response.iter_content(chunk_size):
			fout.write(chunk)
	return file_name

def load_data(file_name):
	with open(file_name, 'r') as fin:
		reader = csv.DictReader(fin)
		return [Purchase(row) for row in reader]

def compute_data(purchases):
	purchases.sort(key = lambda p: p.price)
	#most expensive house
	print("The most expensive house: {}-bed, {}-bath house for ${} in {}".format(
		purchases[-1].beds, purchases[-1].baths, purchases[-1].price, purchases[-1].city
	))
	#least expensive house
	print("The least expensive house: {}-bed, {}-bath house for ${} in {}".format(
		purchases[0].beds, purchases[0].baths, purchases[0].price, purchases[0].city
	))
	#average price house
	print("The average price for a house is ${}".format(round(statistics.mean((
		purchase.price for purchase in purchases
	)))))
	#average price of 2 bedroom house
	print("The average price for a 2 bedroom house is ${}".format(round(statistics.mean((
		purchase.price for purchase in purchases if purchase.beds == 2
	)))))


def main():
	file_name = get_and_save_csv()
	purchases = load_data(file_name)
	compute_data(purchases)

if __name__ == "__main__":
	main()
