import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic
from liquidation import liquid_test
from missingearly import filter_early
from missing_late import missing_recent
from dedup import dedup_funds
from date_incrementer import date_incrementer
import copy
'''
this module takes the cash flow data for each fund and transforms it into actual flow data.
the returns data is a rolling sum, so this makes it into a quarter over quarter diff
'''


def cash_transform(fdata):
    dic = column_dic()

    remove_data = []


    for key, val in fdata.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]
    for key, val in fdata.iteritems():
        val = sorted(val, key=itemgetter(dic['Report YYYYQ']), reverse=False)
        transformed_val = []

        transformed_val.append(val[0])

        for i in range(1, len(val) - 1):

            current_row = val[i]
            current_row_nav = float(current_row[dic['Return NAV']])
            current_row_distributed = float(current_row[dic['Return Distributed']])
            current_row_contributed = float(current_row[dic['Return Contributed']])

            previous_row = val[(i - 1)]
            previous_row_nav = float(previous_row[dic['Return NAV']])
            previous_row_distributed = float(previous_row[dic['Return Distributed']])
            previous_row_contributed = float(previous_row[dic['Return Contributed']])

            new_row = copy.copy(current_row)


            step_up_nav = current_row_nav - previous_row_nav
            step_up_distributed = current_row_distributed - previous_row_distributed
            step_up_contributed = current_row_contributed - previous_row_contributed

            # new_row[dic['Return NAV']] = step_up_nav
            new_row[dic['Return Distributed']] = step_up_distributed
            new_row[dic['Return Contributed']] = step_up_contributed
            # print current_row_nav, current_row[dic['Report YYYYQ']],previous_row_nav, previous_row[dic['Report YYYYQ']]
            transformed_val.append(new_row)
        transformed_val = sorted(transformed_val, key=itemgetter(dic['Report YYYYQ']), reverse=True)
        fdata[key] = transformed_val
    cash_return = copy.copy(fdata)

    return cash_return
