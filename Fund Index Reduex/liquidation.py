import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic
import copy


'''
this module determines if the fund is liquidated and adds a binary 0/1 identifier
to te dictionary value for reference later on
'''


def liquid_test(index_data):
    dic = column_dic()
    remove_data = []


    for key, val in index_data.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]
    for key, val in index_data.iteritems():
        for freturn in val:
            return_nav = float(freturn[dic['Return NAV']])
            return_comm = float(freturn[dic['Committed']])
            liq_pers = return_nav/return_comm
            freturn.append(liq_pers)
            if liq_pers < 0.02:
                freturn.append(1)
            else:
                freturn.append(0)
    liq_data = copy.copy(index_data)
    return liq_data
