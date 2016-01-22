def dedup_transform(loaded_data):
    global stats_dic
    dic = column_dic()
    id_list = []
    fund_dic = dict()
    flp_dic = dict()
    flp_list = []
    single_lp_data = dict()


#getting the unique funds, setting to a list and storing key transparency data

    for row in loaded_data:
        id_list.append(row[dic['Fund ID']])
    fund_set = set(id_list)
    stats_dic['Distinct Funds Considered'] = len(fund_set)
    stats_dic['Total Fund Lines Considered'] = len(id_list)

#creating a dic used to find the best fund-lp relationship based on return
#consistency
    for row in loaded_data:
        flpid = row[dic['Fund-LP Unique ID']]
        score = row[dic['Consistency']]
        fund_id = row[dic['Fund ID']]
        rtuple = (flpid, score)
        fund_dic.setdefault(fund_id, []).append(rtuple)
    for key, val in fund_dic.iteritems():
        sorted_val = sorted(val, key=itemgetter(1), reverse=True)
        fund_dic[key] =  sorted_val[0]

#creating a dic that stores flpid: all returns. used as a lookup once best
# fundLP relation chosen for each fund
    for key, val in fund_dic.iteritems():
        flp_list.append(val[0])

    for row in loaded_data:
        flp_id = row[dic['Fund-LP Unique ID']]
        flp_dic.setdefault(flp_id, []).append(row)


#final return the dictionary {fund ID: all returns for best LP, n.....}
    for relationid in flp_list:
        single_lp_data.setdefault(relationid, []).append(flp_dic[relationid])

#strip away one of the unneded list wrappers so its {id: [[]]}
    better_dic = dict()

    for key, val in single_lp_data.iteritems():
        better_dic[key] = val[0]

    for key, val in better_dic.iteritems():
         sval = sorted(val, key=itemgetter(dic['Report YYYYQ']), reverse=True)
         better_dic[key] = sval
    return better_dic
