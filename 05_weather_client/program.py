print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import requests
from bs4 import BeautifulSoup

def get_region_url(region):
	region = region.split(',')
	return region[2].lower().strip() + "/" + region[1].lower().strip() + "/" + region[0].lower().strip()

def get_html_doc(region_url):
	return requests.get("https://www.wunderground.com/weather/" + region_url)

def get_weather_info(html_doc):
	soup = BeautifulSoup(html_doc.text, 'html.parser')
	soup.prettify()
	temp = soup.find("span" ,class_ = "wu-value wu-value-to").contents[0]
	clouds = soup.find_all("span" ,class_ = "wx-value")[1].contents[0]
	return (temp, clouds)

def print_weather_info(weather, region):
	print("The weather in {} is {} F and Clouds: {}.".format(region, weather[0], weather[1]))

def main():
	region = raw_input("Enter your location  (e.g Portland, OR, US): ")
	region_url = get_region_url(region)
	html_doc = get_html_doc(region_url)
	weather = get_weather_info(html_doc)
	print_weather_info(weather, region)

main()
