import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic
from liquidation import liquid_test
from missingearly import filter_early
from extend_forward import date_sort_to_quarters , date_difference
import copy



'''

this module excludes funds from the benchmark calculation wh are missing
returns data from the 3 quarters previous to the user defined analysis period
'''


def missing_recent(fund_data, yyyy, mm, qq, dd):

    delete_list = []
    dic = column_dic()
    data = copy.copy(fund_data)
    end_date_yyyyq = str(yyyy) + str(qq)

    remove_data = []


    for key, val in fund_data.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]

    end_date_int = date_sort_to_quarters(end_date_yyyyq)

    for key, val in data.iteritems():
        top_return_line = val[0]
        top_return_liquidated = top_return_line[dic['Liquidated']]
        period_code = top_return_line[dic['Report YYYYQ']]


        user_period = str(yyyy) + str(qq)
        converted_user = date_sort_to_quarters(user_period)
        converted_top_return = date_sort_to_quarters(period_code)

        date_diff = int(converted_user) - int(converted_top_return)

        if date_diff >= 4 and top_return_liquidated == 0:
            delete_list.append(key)
        else:
            pass
    for ids in delete_list:
        del data[ids]

    for key, val in data.iteritems():
        new_val = []
        for row in val:
            row_period = row[dic['Report YYYYQ']]
            row_period_int = date_sort_to_quarters(int(row[dic['Report YYYYQ']]))
            if int(row_period_int) <= int(end_date_int):
                new_val.append(row)
        data[key] = new_val






    return data
