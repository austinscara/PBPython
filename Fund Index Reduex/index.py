import csv
import json
from operator import itemgetter, attrgetter, methodcaller
from column_dictionary import column_dic
from liquidation import liquid_test
from missingearly import filter_early
from missing_late import missing_recent
from dedup import dedup_funds
from extend_forward import extend_forward
from extend_back import extend_back
from interpolate_missing import interpolate_missing
from cashflow_transform import cash_transform
'''
this index is for the end to end pooled returns index. errors to cleanup from
previous iteration are the multiple LP-GP relationships appearing in the
calculation phases, and the strange NAV seen in the later rounds
'''


'''
KEY THINGS TO KNOW:
    - All date incrementation is done on the YYYYQ data. so all date-based
      aggregation should be done by this field. no other dates are completely
      incremented for all of the interpolation/extension modules.

    - To get a custom report end data, simply comment the section in this
      script with the test dates, and uncomment the user input dates. this
      will allow you to enter whatever report end date you want in the command
      prompy
    - when copying the SQL data to excel, INCLUDE HEADERS
'''


raw_data = []

stats_dic = {}


dic = column_dic()

'''
load the csv, ready to transform
'''


def load_data(csv_path):

    dic = column_dic()

    global raw_data

    with open(csv_path, 'rb') as names:
        fileread = csv.reader(names, delimiter=',')
        for row in fileread:
            raw_data.append(row)
    raw_data = raw_data[1:]
    return raw_data


'''
get the data in a flpid : returns dictionary format
'''


def group_returns(loaded_data):
    dic = column_dic()
    flp_dict = dict()
    for row in loaded_data:
        fund_lp_id = row[dic['Fund-LP Unique ID']]
        flp_dict.setdefault(fund_lp_id, []).append(row)
    for key, val in flp_dict.iteritems():
        sval = sorted(val, key=itemgetter(dic['Report YYYYQ']), reverse=True)
        flp_dict[key] = sval
    return flp_dict




'''
Main execution secton of the code. all modules are contained in their own
files within the fund index reduex folder
'''


load_data('C:\\Users\\austin.scara\\Python\\Fund Index Reduex\\Input\\VC Europe.csv')

#AS: Put local path for running

'''
three modularized functions contained within seperate files in the folder
'''

grouped = group_returns(raw_data)

for key, val in grouped.iteritems():
    for row in val:
        if int(row[dic['Close to Report Q']]) < 0:
            val.remove(row)

liquid_done = liquid_test(grouped)
early_gone = filter_early(liquid_done)


'''
get user input for when the index should be calculated from. this will be
where the end NAV is distributed and you go back x quarters plus one additional
to get the negative NAV for the buy in
'''
#
# print '\nEnter the year of your index end date in the format YYYY\n'
# user_yyyy = int(raw_input('Selection: '))
#
# print '\nEnter the month of your index end date in the format MM\n'
# user_mm = int(raw_input('Selection: '))
#
# print '\nEnter the quarter of your index end date in the format Q\n'
# user_qq = int(raw_input('Selection: '))
#
# print '\nEnter the day of your index end date in the format DD\n'
# user_dd = int(raw_input('Selection: '))

test_year = 2015
test_month = 6
test_quarter = 2
test_day = 30


'''
This section is completely modularized. each one of these funciton calls is containted
within a seperate file in the folder
'''
late_gone = missing_recent(early_gone, test_year, test_month, test_quarter, test_day)
deduped_data = dedup_funds(late_gone)
extended_forward = extend_forward(deduped_data, test_year,test_quarter)
extended_back = extend_back(extended_forward)
interpolated_missing = interpolate_missing(extended_back)
transformed_flow = cash_transform(interpolated_missing)

################################################


# def sliceMech(transformed_flow, fundType = None, Reigion = None):


YYYYQlist = [] #contains ALL the YYYYQ codes from all the returns lines
for key, val in transformed_flow.iteritems():
    for row in val:
        YYYYQlist.append(row[dic['Report YYYYQ']])

#following creates a dictionary from the set of unique YYYYQ codes ===> set(YYYYQlist)

reportYYYYQ = {} # the dictionary that will store {YYYYQ:[[sum of nav],[sum of contrib],[sum of distributed],[count of funds]]
for yearQtrCode in set(YYYYQlist):
    reportYYYYQ[yearQtrCode] = [[],[],[],[], set({})] # [nav, contriub, distrib, count,set({})funds included]

# for i in sorted(reportYYYYQ):
# 	print i, reportYYYYQ[i]
# ^^^^^
# 19972: [[], [], [], []]
# 19973: [[], [], [], []]
# 19974: [[], [], [], []]
# 19981: [[], [], [], []]
# 19982: [[], [], [], []]
# 19983: [[], [], [], []]
# 19984: [[], [], [], []]
# 19991: [[], [], [], []]
# 19992: [[], [], [], []]


newListofRets = []  # the list shell, to store the values of transformed_flow
for key, val in transformed_flow.iteritems():
    for line in val:
        newListofRets.append(line)


for item in newListofRets:

    reportYYYYQ[item[dic['Report YYYYQ']]][0].append(float(item[dic['Return NAV']]))
    reportYYYYQ[item[dic['Report YYYYQ']]][1].append(float(item[dic['Return Contributed']]))
    reportYYYYQ[item[dic['Report YYYYQ']]][2].append(float(item[dic['Return Distributed']]))
    reportYYYYQ[item[dic['Report YYYYQ']]][4].add(item[dic['Fund Name']])



#print s_Region, '\n', s_FundType
# print reportYYYYQ


# this is where we will slice by what we want 
# print sorted(reportYYYYQ)


for i in reportYYYYQ: 
    reportYYYYQ[i][3] = len(reportYYYYQ[i][0]) #Gets the number of funds for each qtr
    reportYYYYQ[i][0] = sum(reportYYYYQ[i][0])
    reportYYYYQ[i][1] = sum(reportYYYYQ[i][1])
    reportYYYYQ[i][2] = sum(reportYYYYQ[i][2])
 



with open(r'C:\Users\austin.scara\Python\Fund Index Reduex\fundoutput.csv', 'wb') as output:
	writer = csv.writer(output, delimiter = ',') 
	for i in sorted(reportYYYYQ):
		if int(i) >= 20044:
			writer.writerow('\n')
			writer.writerow(i.split())
			for j in reportYYYYQ[i][4]:
				writer.writerow([''.join(j)])
		else:
			continue



#to get nav dist contib out put
# for i in sorted(reportYYYYQ):
# 		print i, ":", reportYYYYQ[i]




'''
now the next step is to add the unique funds filter piece '''
