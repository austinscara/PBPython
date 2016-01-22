import time
import os
import sys
import csv
import time
import getpass
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

userName = getpass.getuser()




with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Downloader List.csv', 'rb') as fiftyFive:
	reader = csv.reader(fiftyFive, delimiter = ",")
	next(reader)
	infoList = []
	for row in reader:
		if int(row[0][14:]) > 2008:
			infoList.append(row)

	
# print infoList

os.chdir("C:\\Users\\"+ userName +"\\Downloads")
if os.path.exists("C:\\Users\\"+ userName +"\\Downloads\\filing.pdf"):
	os.remove("filing.pdf")
else:	
	pass
	
for eachLi in infoList:
	for i in eachLi:
		ein = i[:9]
		pn = i[10:13]
		year =i[14:]
		name = ein+"_"+pn+"_"+year+".pdf"
		driver = webdriver.Chrome("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Chrome Selenium Web Driver\\chrome\\chromedriver.exe")  #arg is the path where the chrome driver is located "\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Chrome Selenium Web Driver\\chromechromedriver.exe"
		driver.implicitly_wait(10) #Sets the wait time for the browser checks every .5 seconds
		driver.get("https://www.efast.dol.gov/portal/app/disseminate?execution=e1s1")
		driver.find_element_by_id("ein").send_keys(ein)
		driver.find_element_by_id("pn").send_keys(pn)
		driver.find_element_by_name("formYear").send_keys(year)
		driver.find_element_by_id("form:nextbtn").click()

		
		try:
			driver.find_element_by_id("form:msgInfomessage")
			driver.quit()

		except:
			driver.find_element_by_id("form:filingTreeTable:0:einLnk").click()
			while os.path.exists("C:\\Users\\"+ userName +"\\Downloads\\filing.pdf") is False:
				time.sleep(2)

			try:	
				os.rename("filing.pdf","\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\Down Loaded 5500\\" + name)
				driver.quit()
			except WindowsError:
				print name + "Already exists"
				os.remove("C:\\Users\\"+ userName +"\\Downloads\\filing.pdf")
				driver.quit()
				continue
		
			
				
	


