import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic

'''
this module is intended to iterate through all the distinct funds to GP relatins
and determine which one has the best return consistency, which will be the only
one used when the pooled returns index is calculated later on in the program.
consitency is defined by the # of quarters since the close of the fund where they
have returns data for.
'''


def dedup_funds(fdata):

    dic = column_dic()
    comparison_dict = dict()
    top_flpid = []
    new_fdata = {}
    remove_data = []


    for key, val in fdata.iteritems():
        if len(val) == 0:
            remove_data.append(key)

    for ids in remove_data:
        del fdata[ids]

    for key, val in fdata.iteritems():
        top_line = val[0]

        fundid = top_line[dic['Fund ID']]
        flpid = key
        fundscore = top_line[dic['Consistency']]
        test_tuple = (fundid, flpid, float(fundscore))
        comparison_dict.setdefault(fundid, []).append(test_tuple)


    for key in comparison_dict:
        val = comparison_dict[key]
        sorted_val = sorted(val, key=itemgetter(2), reverse=True)
        top_val = sorted_val[0]
        top_flpid.append(top_val[1])



    for key, val in fdata.iteritems():
        if key in top_flpid:
            new_fdata[key] = val
    return new_fdata
    #
    #
    # return new_fdata
