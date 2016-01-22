import csv
import os





with open('\\\\Mowgli\Research\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\5500Tracking.csv', 'rb') as fiftyFive:
	reader = csv.reader(fiftyFive, delimiter = ",")
	lpReturnslines = []
	for row in reader:
		lpReturnslines.append(row)
	fiftyFive.close()
	


with open('\\\\Mowgli\Research\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\EinPnLPIDConnect.csv', 'rb') as fiftyFive:
	reader = csv.reader(fiftyFive, delimiter = ",")
	einConnect = []
	for row in reader:
		einConnect.append(row)
	fiftyFive.close()
	
LpIDEinDict ={}
for subList in einConnect:
	LpIDEinDict[subList[1]] = subList[0]




yearsEin = []
for lpid in LpIDEinDict:
	for returnsLines in lpReturnslines:
		if lpid == returnsLines[0]:
			returnsLines.append(LpIDEinDict[lpid])
			yearsEin.append(returnsLines[2:])
		else:
			pass



years = lpReturnslines[0][2:]
years.append("ein")



dlListPerLP = []
for yearRetsEinLine in yearsEin:
	yReL = dict(zip(years,yearRetsEinLine))
	# print yReL
	for item in yReL:
		if yReL[item] == "#N/A":
			yReL[item] = yReL['ein']+"_"+ item
	del yReL["ein"]
	dlListPerLP.append(yReL)



# print dlListPerLP

dlList = []
for lp in dlListPerLP:
	for key, val in lp.iteritems():
		if len(val) == 18:
			dlList.append(val)
		else:
			pass

dlList = [[x] for x in dlList]
# print dlList


with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Downloader List.csv', 'wb') as finalDlList:
    writer = csv.writer(finalDlList, delimiter = ',') 
    for i in dlList:
        writer.writerow(i)
    
