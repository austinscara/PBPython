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
chrome_profile = webdriver.ChromeOptions()
profile = {"plugins.plugins_disabled": ["Chrome PDF Viewer"]}
chrome_profile.add_experimental_option("prefs", profile)



with open(r'\\mowgli\Research\Fund Performance\5500 & 990\990 PF\990 Tracking CSV\990 Downloading CSV\990 Downloader List.csv', 'rb') as fiftyFive:
	reader = csv.reader(fiftyFive, delimiter = ",")
	next(reader)
	infoList = []
	for row in reader:
		infoList.append(row)

	
# print infoList

os.chdir("C:\\Users\\"+ userName +"\\Downloads")
	
for eachLi in infoList:
	for i in eachLi:
		ein = i[:9]
		year =i[-4:]
		driver = webdriver.Chrome(r"\\mowgli\Research\Fund Performance\5500 & 990\990 PF\990 Tracking CSV\990 Downloading CSV\Chrome Selenium Web Driver\chrome\chromedriver.exe", chrome_options=chrome_profile)  #arg is the path where the chrome driver is located "\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Chrome Selenium Web Driver\\chromechromedriver.exe"
		driver.implicitly_wait(10) #Sets the wait time for the browser checks every .5 seconds
		driver.get("http://foundationcenter.org/findfunders/990finder/")
		driver.find_element_by_name("ei").send_keys(ein)
		driver.find_element_by_name("fy").send_keys(year)
		driver.find_element_by_name("action").click()
		time.sleep(2)

		try:
			link = driver.find_element_by_xpath('//*[@id="MainContent_GridView1"]/tbody/tr[2]/td[1]/a')
			fileName = link.get_attribute('href').split('/')[-1]
			link.click()

			while os.path.exists('C:\\Users\\'+ userName +'\Downloads\\' + fileName) is False:
				time.sleep(2)

			try:	
				os.rename('C:\\Users\\'+ userName +'\Downloads\\' + fileName,
					       r"\\mowgli\Research\Fund Performance\5500 & 990\990 PF\Down Loaded 990\\" + fileName)
				driver.quit()
			except WindowsError:
				print name + "Already exists"
				os.remove('C:\\Users\\'+ userName +'\Downloads\\' + fileName)
				driver.quit()
				continue

		except:
			driver.quit()

