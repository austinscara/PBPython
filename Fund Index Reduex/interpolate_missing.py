import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic
from liquidation import liquid_test
from missingearly import filter_early
from missing_late import missing_recent
from dedup import dedup_funds
from date_incrementer import date_incrementer
from extend_forward import date_difference, date_sort_to_quarters
import copy


'''
This module takes the returns data and looks for any missing returns lines in
the middle and uses linier interpolation to fill them in
'''


def interpolate_missing(flpdata):

    dic = column_dic()

    remove_data = []
    new_return_dic = {}

    for key, val in flpdata.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]



    for key, val in flpdata.iteritems():
        last_row = val[0]
        val = sorted(val, key=itemgetter(dic['Report YYYYQ']), reverse=False)
        new_val = []
        test_len = len(val)
        fund_name = val[0][dic['Fund Name']]
        lp_name = val[0][dic['LP Name']]


        for i in range(0, test_len-1):

            current_row = val[i]
            current_row_nav = float(current_row[dic['Return NAV']])
            current_row_distributed = float(current_row[dic['Return Distributed']])
            current_row_contributed = float(current_row[dic['Return Contributed']])
            current_row_yyyyq = current_row[dic['Report YYYYQ']]
            current_row_yyyy = current_row_yyyyq[0:4]
            current_row_qqq = current_row_yyyyq[4:]

            next_row = val[i + 1]
            next_row_nav = float(next_row[dic['Return NAV']])
            next_row_distributed = float(next_row[dic['Return Distributed']])
            next_row_contributed = float(next_row[dic['Return Contributed']])
            next_row_yyyyq = next_row[dic['Report YYYYQ']]


            step_nav_difference = next_row_nav - current_row_nav
            step_distributed_difference = next_row_distributed - current_row_distributed
            step_contributed_difference  = next_row_contributed - current_row_contributed
            close_q_difference2 = date_difference(next_row_yyyyq, current_row_yyyyq)


            q_to_add = close_q_difference2 - 1
            new_val.append(current_row)
            incrementer = 1

            while q_to_add > 0:
                new_row = copy.copy(current_row)
                new_row[dic['Return NAV']] = float(new_row[dic['Return NAV']]) + ((step_nav_difference / close_q_difference2) * incrementer)
                new_row[dic['Return Contributed']] = float(new_row[dic['Return Contributed']]) + ((step_contributed_difference / close_q_difference2) * incrementer)
                new_row[dic['Return Distributed']] = float(new_row[dic['Return Distributed']]) + ((step_distributed_difference / close_q_difference2) * incrementer)
                new_period = date_incrementer(current_row_yyyy, current_row_qqq, incrementer)

                new_row[dic['Report YYYYQ']] = new_period
                new_val.append(new_row)
                q_to_add -= 1
                incrementer += 1
        new_val.append(last_row)
        new_return_dic[key] = new_val
    return new_return_dic
