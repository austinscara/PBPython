import csv
import getpass
import os
import time
import zipfile
from datetime import date
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def stageReader(filePath):
	lister = []
	with open(filePath, 'rb') as fileObject:
		reader = csv.reader(fileObject, delimiter = ",")
		for line in reader:
			try:
				lister.append(line[0])
			except IndexError:
				lister.append(line)
	return lister


def filterFunc(scH, againstList, indexPosition = None):
	newH = []
	for item in scH:
		if item[:indexPosition] not in againstList:
			newH.append(item)
	return newH


def appender(fileName, schH):
	with open(fileName, 'ab') as updateLog:
		writer = csv.writer(updateLog) 
		for line in schH:
			writer.writerow(line)

userName = getpass.getuser()


nextYear = 2009
yearList = []
while nextYear < date.today().year:
	yearList.append(nextYear)
	nextYear += 1


for year in yearList:

	driver = webdriver.Chrome('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Chrome Selenium Web Driver\\chrome\\chromedriver.exe')  #arg is the path where the chrome driver is located
	driver.implicitly_wait(10) #Sets the wait time for the browser checks every .5 seconds
	driver.get("https://askebsa.dol.gov/FOIA%20Files/" + str(year) + "/Latest/F_SCH_H_" + str(year) + "_Latest.zip")
	while os.path.exists("C:\\Users\\"+ userName +"\\Downloads\\F_SCH_H_"+ str(year) +"_Latest.zip") is False:
				time.sleep(2)	
	driver.quit()
	os.rename("C:\\Users\\"+ userName +"\\Downloads\\F_SCH_H_"+ str(year) +"_Latest.zip","\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\F_SCH_H_"+ str(year) +"_Latest.zip")



for files in os.listdir('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater'):
	if files.endswith(".zip"):
		with zipfile.ZipFile("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\"+ files) as zf:
			zf.extractall("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater")
	else:
		pass



scheduleH = []
for files in os.listdir("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater"):

	if files.endswith(".csv"):
		year = files[8:12]
		with open("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\" + files, 'rb') as scH:
			reader = csv.reader(scH, delimiter = ",")
			next(reader)
			for line in reader:
				try:
					if int(line[46]) > 10000:
						scheduleH.append(line[4] + "_" + line[3] + "_" + year)
					else:
						pass
				except ValueError:
					pass



accountedEin = stageReader('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnLPIDConnect.csv')
nonAccountedEin = stageReader('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnThatNeedLPID.csv')
alreadyCaughtInUpdater = stageReader('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Filings Found In Updater.csv')



scheduleH = filterFunc(scheduleH, accountedEin, 13)
scheduleH = filterFunc(scheduleH, nonAccountedEin, 13)
scheduleH = filterFunc(scheduleH, alreadyCaughtInUpdater,)

scheduleH = [[x] for x in scheduleH]



appender('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Filings Found In Updater.csv', scheduleH)
appender('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Downloader List.csv',scheduleH)
# appender('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500tracking\\EinPnThatNeedLPID.csv', scheduleH, 13)


try:
	files = [r"\\Mowgli\Research\Fund Performance\5500 & 990\5500\5500 Tracking CSV\5500 Downloading & Updating CSV\Updater\\" + files for files in os.listdir(r"\\Mowgli\Research\Fund Performance\5500 & 990\5500\5500 Tracking CSV\5500 Downloading & Updating CSV\Updater\\")]
	for item in files:
		os.remove(item)
	# for files in os.listdir("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater"):
	# 		os.remove("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\" + files)
except IOError:
	print "neigh"


