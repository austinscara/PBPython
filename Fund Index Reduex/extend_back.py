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
this module takes the funds missing returns data immediately prior to their close
date and extends this data backwards through linear interpolation
'''



def extend_back(flpdata):

    dic = column_dic()
    remove_data = []
    new_dic = {}

    for key, val in flpdata.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]

    for key, val in flpdata.iteritems():
        val = sorted(val, key=itemgetter(dic['Report YYYYQ']), reverse=True)
        new_val = copy.copy(val)
        last_return = val[-1]
        last_return_nav = float(last_return[dic['Return NAV']])
        last_return_distributed = float(last_return[dic['Return Distributed']])
        last_return_contributed = float(last_return[dic['Return Contributed']])
        last_return_yyyyq = last_return[dic['Report YYYYQ']]
        last_return_yyyy = last_return_yyyyq[0:4]
        last_return_qq = last_return_yyyyq[4:]
        missing_quarters = int(last_return[dic['Close to Report Q']])

        contributed_drop = float(last_return_contributed) /float(missing_quarters)
        distribute_dtop = float(last_return_distributed) / float(missing_quarters)
        nav_drop = float(last_return_nav) / float(missing_quarters)

        rows_to_add = missing_quarters - 1
        steper = 1
        date_changer = -1

        while rows_to_add > 0:
            new_row = copy.copy(last_return)
            new_row[dic['Return NAV']] = last_return_nav - (nav_drop * steper)
            new_row[dic['Return Contributed']] = last_return_contributed - (contributed_drop * steper)
            new_row[dic['Return Distributed']] = last_return_distributed - (distribute_dtop * steper)
            new_row[dic['Report YYYYQ']] = date_incrementer(last_return_yyyy, last_return_qq, date_changer)
            new_val.append(new_row)
            rows_to_add = rows_to_add - 1
            steper = steper + 1
            date_changer -= 1
        new_dic[key] = new_val

    return new_dic
