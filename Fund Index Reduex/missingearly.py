import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic
from liquidation import liquid_test


'''
this module removes and LP returns data where there was no info within there
first year of the fund close
'''
tester = {'tester': 5}
def filter_early(fund_data):
    dic = column_dic()
    remove_data = []


    for key, val in fund_data.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]
    approved_returns = dict()
    fdata = fund_data
    for key, val in fdata.iteritems():

        returns_len = len(val)
        early_return =  val[-1]
        t_from_close = int(early_return[dic['Close to Report Q']])
        if t_from_close <= 8:
            approved_returns[key] = val
        else:
            pass
    return approved_returns
