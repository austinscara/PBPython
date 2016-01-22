from column_dictionary import column_dic
import datetime
from calendar import monthrange
from operator import itemgetter, attrgetter, methodcaller
import copy
import time


'''
this used to increment YYYQ format dates. this is very hacky
'''

def date_incrementer(last_year, last_quarter, add_count):
## last_year and last_qquarter are feed from the return row

## add_count represents the number of quarters +/- from the current row the new
## YYYYQ Date is
	yyyyq = 0

## first if statement determines if we are going forwards or backwards through time
## it then sets up the variables representing the last return we have
	if add_count >= 0:
		last_quarter = int(last_quarter)
		last_year = int(last_year)



## the quotient of the year add is how much to increment the YYYY component
## with the %4 we are only adding whole years
		year_add = add_count / 4
		new_year = last_year + year_add


## now we have add_count remaining that does not make up a full quarter.
## and we add that to the current quarter we are in for the last YYYYQ code
		r_quarter = add_count - (year_add * 4)
## this q_change is the number of quarters we need to add to the base YYYY for the
# new code. This adds the quarters we have right now from the old YYYYQ and
## the new quarters from the r_quarter
		q_change = last_quarter + r_quarter


##if this change is greater than 4, we have another year that needs to be added to
## the base YYYY
## the new Q becomes the remainder of the total quarter change
## the new year gets an additional inrement to get to the proper year
		if q_change > 4:
			new_q = q_change % 4
			new_year = new_year + (q_change / 4)

## if it is not greater than 4, then just increment it
		else:
			new_q = q_change
		new_yyyyq = str(new_year)+str(new_q)
		yyyyq = new_yyyyq

## if we are going backwards such as the extend early set up the same variables
## but increment backwards the same way






	if add_count < 0:

		iterate_list = [4,3,2,1,4,3,2,1]
		last_quarter = int(last_quarter)
		last_year = int(last_year)
		year_add = abs(add_count) / 4
		new_year = last_year - year_add


		r_quarter = abs(add_count) - (year_add * 4)
		q_index = iterate_list.index(last_quarter)
		new_q_index = q_index + r_quarter
		if new_q_index >= 4:
			new_year = last_year - 1
			new_q = iterate_list[new_q_index]
		else:
			new_year = last_year
			new_q = iterate_list[new_q_index]
		new_yyyyq = str(new_year) + str(new_q)
		yyyyq = new_yyyyq
	return yyyyq
