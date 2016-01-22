import os
import csv
# from os import listdir


def readyForRanj():
	downloaded = []
	for filling in os.listdir("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\India\\Ready For Ranjit"):
		if filling.endswith(".pdf"):
			downloaded.append(filling[:18])



	# EinPnLPIDConnection = []
	with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnLPIDConnect.csv', 'rb') as EinPnLPIDConnect:
		reader = csv.reader(EinPnLPIDConnect, delimiter = ",")
		EinPnLPIDConnection = {rows[0]:rows[1] for rows in reader}
		EinPnLPIDConnect.close()

	try:
		einLpidDict = {} #dictionary of {ein_pn_year:LPID}
		for i in downloaded:
			for j in EinPnLPIDConnection:
				einLpidDict[i] = EinPnLPIDConnection[i[:13]]
		#print einLpidDict
	except KeyError:
		badEIN = []
		badEIN.append(i[:13])


		existingLog = []
		with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnThatNeedLPID.csv', 'rb') as badEinCheck:
			reader = csv.reader(badEinCheck, delimiter = ",")
			for badEINitem in reader:
				existingLog.append(badEINitem)

		if badEIN not in existingLog:
			with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnThatNeedLPID.csv', 'a') as einResearchLog:
				writer = csv.writer(einResearchLog, delimiter = ',') 
				writer.writerow(badEIN)
				einResearchLog.close()
		else:
			pass
	return einLpidDict



