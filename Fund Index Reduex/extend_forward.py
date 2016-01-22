import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic
from liquidation import liquid_test
from missingearly import filter_early
from dedup import dedup_funds
from date_incrementer import date_incrementer
import copy


'''
this module takes the remaining returns data and uses
extends  them forward to the finish which is the yyyyq combo the user chose
'''

def date_sort_to_quarters(date):
    """This function converts YYYYQ to quarter integer, with quarter=[(YYYY*4)+Q]
        to be used by the date_diff function"""

    if type(date)==str:
        date=int(date)

    try:
        return int((((date-date%10)/10)*4)+(date%10)-1)
    except:
        print('failed to convert to quarters: '+str(date)+'. string length: '+str(len(date))+'.')
        print(len(date))
        return 0

def date_difference(date2,date1):
    """This function finds how many quarters are between two dates."""

    # converts YYYYQ to quarter integer, with quarter=[(YYYY*4)+Q]
    quarter1=date_sort_to_quarters(date1)
    quarter2=date_sort_to_quarters(date2)

    # take difference between the quarter count
    difference=int(quarter2-quarter1)

    # return result
    return difference



'''
for the fist missing quarter, NAV is dumped as a distribution and set to 0
for all remanning missing quarters, the values stay the same so the quarterly
flow will be 0
'''

def extend_forward(fdata, yyyy, qq):
    new_data = {}
    dic = column_dic()
    end_yyyyq = str(yyyy) + str(qq)
    negative_count = 0
    pos_count = 0
    remove_data = []


    for key, val in fdata.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]
    for key, val in fdata.iteritems():
        val = sorted(val, key=itemgetter(int(dic['Report YYYYQ'])),reverse=True)
        top_return_line = val[0]
        top_return_yyyyq = top_return_line[dic['Report YYYYQ']]
        top_return_year = top_return_yyyyq[0:4]
        top_return_quarter = top_return_yyyyq[4:]
        top_return_distributed = top_return_line[dic['Return Distributed']]
        top_return_nav = top_return_line[dic['Return NAV']]

        quarter_diff = date_difference(end_yyyyq, top_return_yyyyq)
        date_adder = 1
        new_row = copy.copy(top_return_line)
        new_row[dic['Return Distributed']] = float(top_return_nav) + float(top_return_distributed)
        new_row[dic['Return NAV']] = 0

        # return new_row[dic['Return NAV']],new_roic['Return Distributed']], top_return_line[dic['Return NAV']], top_return_line[dic['Return Distributed']]
        new_row_yyyy = new_row[dic['Report YYYYQ']][0:4]
        new_row_qq = new_row[dic['Report YYYYQ']][4:]
        new_row[dic['Report YYYYQ']] = date_incrementer(new_row_yyyy, new_row_qq, date_adder)
        val.insert(0, new_row)


        quarter_diff = quarter_diff - 1
        date_adder += 1

        while quarter_diff > 0:

            more_row = copy.copy(new_row)
            more_row_yyyy = new_row[dic['Report YYYYQ']][0:4]
            more_row_qq = new_row[dic['Report YYYYQ']][4:]
            more_row[dic['Report YYYYQ']] = date_incrementer(top_return_year, top_return_quarter, date_adder)
            quarter_diff -= 1
            date_adder += 1
            val.insert(0, more_row)
        new_data[key] = val
    return new_data
