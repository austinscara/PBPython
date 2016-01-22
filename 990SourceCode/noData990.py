import os
import csv
import ipdb
# from os import listdir


def noData990():
	downloaded = []
	for filling in os.listdir(r"\\mowgli\Research\Fund Performance\5500 & 990\990 PF\No Data Archive"):
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


	einLpidDict = {}	
	for i in adjDate:
		try:
			einLpidDict[EinPnLPIDConnection[i[:9]]] = i[-4:]
		except KeyError:
			pass

	einLpidDict = {int(i) : einLpidDict[i] for i in  einLpidDict}		
	return einLpidDict

# print noData990()

