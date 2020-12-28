print('###########################################################')
print('                                                           ')
print('            Author: Mufaro Simbisayi                       ')
print('                                                           ')
print('###########################################################')

import datetime

def create_date():
	year_input = int(input("What year were you born? [YYYY] "))
	month_input = int(input("What month were you born? [MM] "))
	day_input = int(input("What day were you born? [DD] "))

	birth_date = datetime.datetime(year_input, month_input, day_input)
	return birth_date

def compute_days_between_dates(original_date):
	target_date = datetime.datetime.now()
	current_year = datetime.datetime(target_date.year, original_date.month, original_date.day)
	delta = current_year - target_date

	return delta.days

def output_birthday_info(birth_date, days):
	print("It looks like you were born on {}".format(birth_date))
	if days > 0:
		print("Looks like your birthday is in {} days.".format(days))
		print("Hope you're looking forward to it.")
	else:
		print("Looks like your birthday was {} days ago.".format(-days))
		print("Hope it was pleasant.")

def main():
	birth_date = create_date()
	days = compute_days_between_dates(birth_date)
	output_birthday_info(birth_date, days)

main()
