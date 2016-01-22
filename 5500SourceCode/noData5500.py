import os
import csv

# from os import listdir


def noData():
	downloaded = []
	for filling in os.listdir("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\No Data Archive"):
		if filling.endswith(".pdf"):
			downloaded.append(filling[:18])


	# EinPnLPIDConnection = []
	
	with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnLPIDConnect.csv', 'rb') as EinPnLPIDConnect:
		reader = csv.reader(EinPnLPIDConnect, delimiter = ",")
		EinPnLPIDConnection = {rows[0]:rows[1] for rows in reader}



	einLpidDict = {}
	 #dictionary of {ein_pn_year:LPID}
	for i in downloaded:
		for j in EinPnLPIDConnection:
			try:
				einLpidDict[i] = EinPnLPIDConnection[i[:13]]	
			except KeyError:
				pass
	
	return einLpidDict



