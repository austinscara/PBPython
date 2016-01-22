import os
import csv

# from os import listdir


def readyForRanjNineNine():
	downloaded = []
	for filling in os.listdir(r"\\mowgli\Research\Fund Performance\5500 & 990\990 PF\India 990\Ready For Ranjit"):
		if filling.endswith(".pdf"):
			downloaded.append(filling[:16])
	
	try:
		adjDate = []
		for filling in downloaded:
			dateCode = filling[10:16]
			if int(dateCode[-2:]) == 12:
				adjDate.append(filling.split('_')[0] + "_" + dateCode[:4])
			else:
				adjDate.append(filling.split('_')[0] + "_" + str(int(dateCode[:4]) - 1))
	except ValueError:
		pass


	with open(r'\\mowgli\Research\Fund Performance\5500 & 990\990 PF\990 Tracking CSV\990 Tracking Files CSV\EinPnLPIDConnect.csv', 'rb') as EinPnLPIDConnect:
		reader = csv.reader(EinPnLPIDConnect, delimiter = ",")
		EinPnLPIDConnection = {rows[0]:rows[1] for rows in reader}
		EinPnLPIDConnect.close()
		
	try:
		einLpidDict = {} #dictionary of {ein_year:LPID}
		for i in adjDate:
			einLpidDict[EinPnLPIDConnection[i[:9]]] = i[-4:]						 
	except KeyError:
		badEIN = []
		badEIN.append(i[:9])
		
		existingLog = []
		with open(r'\\mowgli\Research\Fund Performance\5500 & 990\990 PF\990 Tracking CSV\990 Tracking Files CSV\EinPnThatNeedLPID.csv', 'rb') as badEinCheck:
			reader = csv.reader(badEinCheck, delimiter = ",")
			for badEINitem in reader:
				existingLog.append(badEINitem)

		if badEIN not in existingLog:
			with open(r'\\mowgli\Research\Fund Performance\5500 & 990\990 PF\990 Tracking CSV\990 Tracking Files CSV\EinPnThatNeedLPID.csv', 'a') as einResearchLog:
				writer = csv.writer(einResearchLog, delimiter = ',') 
				writer.writerow(badEIN)
				einResearchLog.close()
		else:
			pass	
	

	return einLpidDict

