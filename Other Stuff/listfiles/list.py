import os 
import csv


spath = "\\\\mowgli\\Research\\Fund Performance\\New Projects - Investment Memorandum\\D-Fees"


fileList = []
for roots, dirs, files in os.walk(spath):
	for filling in files:
		fileList.append(filling)

printList = [[x] for x in fileList]



with open('C:\\Users\\austin.scara\\Python\\listfiles\\list.csv', 'wb') as listfile:
	writer = csv.writer(listfile, delimiter = ',') 
	for name in printList:
		writer.writerow(name)


	