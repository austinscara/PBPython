Updater

userName = getpass.getuser()



	driver = webdriver.Chrome('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Chrome Selenium Web Driver\\chrome\\chromedriver.exe')  #arg is the path where the chrome driver is located
	driver.implicitly_wait(10) #Sets the wait time for the browser checks every .5 seconds
	driver.get("https://askebsa.dol.gov/FOIA%20Files/" + str(year) + "/Latest/F_SCH_H_" + str(year) + "_Latest.zip")
	while os.path.exists("C:\\Users\\"+ userName +"\\Downloads\\F_SCH_H_"+ str(year) +"_Latest.zip") is False:
				time.sleep(2)	
	os.rename("C:\\Users\\"+ userName +"\\Downloads\\F_SCH_H_"+ str(year) +"_Latest.zip","\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\F_SCH_H_"+ str(year) +"_Latest.zip")

for files in os.listdir('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater'):
	if files.endswith(".zip"):
		with zipfile.ZipFile("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\"+ files) as zf:
for files in os.listdir("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater"):
"\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\" + files, 'rb') as scH:



'\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnLPIDConnect.csv')
'\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Tracking Files CSV\\EinPnThatNeedLPID.csv')
'\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Filings Found In Updater.csv')
'\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Downloader List.csv',scheduleH)

"\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater"):
		
os.remove("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Updater\\" + files)
except IOError:
	print "neigh"

##############################################
Downloader


userName = getpass.getuser()




with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\5500 Downloader List.csv', 'rb') as fiftyFive:
os.chdir("C:\\Users\\"+ userName +"\\Downloads")
if os.path.exists("C:\\Users\\"+ userName +"\\Downloads\\filing.pdf"):
	os.remove("filing.pdf")

		driver = webdriver.Chrome("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Chrome Selenium Web Driver\\chrome\\chromedriver.exe")  #arg is the path where the chrome driver is located "\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\5500 Tracking CSV\\5500 Downloading & Updating CSV\\Chrome Selenium Web Driver\\chromechromedriver.exe"
		driver.implicitly_wait(10) #Sets the wait time for the browser checks every .5 seconds
		driver.get("https://www.efast.dol.gov/portal/app/disseminate?execution=e1s1")
	
			while os.path.exists("C:\\Users\\"+ userName +"\\Downloads\\filing.pdf") is False:
				time.sleep(2)	
			os.rename("filing.pdf","\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\Down Loaded 5500\\" + name)
			driver.quit()
		
			
				
	


