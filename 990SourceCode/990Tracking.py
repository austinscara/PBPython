import _mssql
import pymssql
import socket
import decimal
import uuid
import collections
import unicodecsv as csv
import DownLoaded990
import ReadyForRanjit990
import InIndia990
import CompletedByRanjit990
import noData990


def header(header):
	header = []
	for i in pullList:
		header.append(int(i[2][len(i[2])-4:]))
		header = list(set(header))
		header.sort()
	header.insert(0, "LP EntityName")
	header.insert(0, "LP EntityID")
	tuple(header)
	return header ### may need to rework by + year <=== list
	
def year(pullList):
	years = []
	for i in pullList:
		years.append(int(i[2][len(i[2])-4:]))
		years = list(set(years))
		years.sort()
		#years.append(2014) # add part which adds one year to the last year
	return years

def LPID(pullList):
	LPIDs = []
	for i in pullList:
		LPIDs.append(int(i[0]))
		LPIDs = list(set(LPIDs))
	return LPIDs

def dedupedPull(pullList):
	sinlgeLi = list(set(pullList))   #list(set(pullList))
	return sinlgeLi

def unTuple(deDupedList):
	for i in deDupedList:
		deDupedList[deDupedList.index(i)] = list(i)
	return deDupedList

def makeLPShell(dedupedUntuplePull, years):
	shellList = []
	for i in dedupedUntuplePull:
		uniqueShell = []
		uniqueShell.extend((i[0],i[1]))
	 	shellList.append(tuple(uniqueShell))
	
	return set(shellList)


def lpLineFill(lpLineWithDateDict, stageFunction, functionCode):
	for i in stageFunction:
		for j in lpLineWithDateDict:
			if int(i) == j[0] and int(stageFunction[i]) not in j[2].keys():
				j[2][int(stageFunction[i])] = functionCode
			else:
				pass
	return LpLineWithDateDict



def csvWrite(header, finalLpTrackLines):

	with open(r'\\mowgli\Research\Fund Performance\5500 & 990\990 PF\990 Tracking CSV\990 Tracking Files CSV\990Tracking.csv', 'wb') as tracking:
		writer = csv.writer(tracking) #, delimiter = ',') 
		writer.writerow(header)
		writer.writerows(finalLpTrackLines)

		# for lpReturnsLines in finalLpTrackLines:
		# 	writer.writerows(lpReturnsLines)
		
	return None


# Creates connection to SQL server with credentials, and SQL querey	
mssql_conn = pymssql.connect(host='ext.pitchbook.com',user='skylar.marcum',password='kev34eno',database='dbd_copy')  
mssql_cursor = mssql_conn.cursor()
mssql_cursor.execute("""
					SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
					SELECT irr.LPEntityID, irr.LPName, convert(varchar, irr.ReportDate, 110) as [Report Date]
					from IrrTool_ReturnsDataView irr
					INNER JOIN LimitedPartner lp on irr.LPEntityID = lp.BusinessEntityId
					where lp.LPType=8
					""")

#pullList is a list of tuples which came from the SQL querey
pullList = mssql_cursor.fetchall()
years = year(pullList) # Creates a list of years included from the querey eg[2009, 2010, 2011, 2012, 2013]
LPID = LPID(pullList) #from raw pull[930, 359621, 17288, 17161, 17355, 541269, 539382]
header = header(pullList) # Creates a header for the tracking sheet from raw pull['LP EntityID', 'LP EntityName', 2009, 2010, 2011, 2012, 2013]
dedupedUntuplePull = unTuple(dedupedPull(pullList)) #[[lpid, lpname, mm/dd/yyyy]] <== list of lists
returnsLines = dict(collections.Counter(pullList)) # Returns a dictionary where keys are tuples and values are the # of returns lines for those unique key values{(lpid, lpname, mm/dd/yyyy): returns lines} <== list of tuples
###^^ OK


lpShells = unTuple(list(makeLPShell(dedupedUntuplePull, years))) # Creates shell from "dedupedUntuplePull" and "years": [[lpid, lpname, year, year year, year]]





lpShellskeyd = {}
for i in lpShells:    #returns a dictionary of lpid : lpShell
	lpShellskeyd[i[0]] = i




mockShellwithRets = dedupedUntuplePull 
for i in mockShellwithRets:        #generates list [lpid, lpname, {year: returns number}] 
	i.append(returnsLines[tuple(i)]) 
	i[2] = int(i[2][len(i[2])-4:])
	dateRetPair = {}  
	dateRetPair[i[2]] = i[3]
	i.append(dateRetPair)
	del i[2:4]    




for shellId in lpShellskeyd:
	for row in mockShellwithRets:
		if shellId == row[0]:
			lpShellskeyd[row[0]].append(row[2])	
		else:
			pass



# now must sort  the dictonaries in the slice of a list
LpLineNoKey = []
for i in lpShellskeyd:
	LpLineNoKey.append(lpShellskeyd[i])


# use year list and counters

for i in LpLineNoKey:
	lpDatesSorted = []
	for j in i[2:]:
		lpDatesSorted.append(j)
	i.append(sorted(lpDatesSorted))
	del i[2:len(i)-1]



for i in LpLineNoKey:
	dateRetsDictionary = {}
	for j in i[2]:
		dateRetsDictionary.update(j)
	i.append(dateRetsDictionary)
	del i[2]

#################################
LpLineWithDateDict = LpLineNoKey


LpLineWithDateDict = lpLineFill(LpLineWithDateDict, DownLoaded990.dlNineNine(),           "Downloaded")
LpLineWithDateDict = lpLineFill(LpLineWithDateDict, ReadyForRanjit990.readyForRanjNineNine(),      "Ready For Ranjit")
LpLineWithDateDict = lpLineFill(LpLineWithDateDict, InIndia990.inIndiaNineNine(),                  "In India")
LpLineWithDateDict = lpLineFill(LpLineWithDateDict, CompletedByRanjit990.completedByRanjNineNine(), "Completed By Ranjit")
LpLineWithDateDict = lpLineFill(LpLineWithDateDict, noData990.noData990(),                    "No Data")



for i in LpLineWithDateDict:
	for y in years:
		if y in i[2].keys():
			pass
		else:
			i[2][y] = "#N/A" 


for i in  LpLineWithDateDict:
	for d in i[2]:
		i.append(i[2][d])
	del i[2]


# for i in LpLineWithDateDict:
# 	print i

finalLpTrackLines = LpLineWithDateDict
csvWrite(header, finalLpTrackLines)
