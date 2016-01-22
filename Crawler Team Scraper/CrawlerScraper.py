import unicodecsv as csv
import bs4
import os
import ipdb
import codecs
import getpass
from Tkinter import Tk
from tkFileDialog import askopenfilename

def lpScraper(htmlFile, date):
		# qtrs = {"March," : 3,  "June," : 6,  "September,": 9, "December," : 12,  "March" : 3, "June" : 6,  "September": 9, "December" : 12,}
		
		date = "-".join(date.split('.'))
	
		try:	
			f = codecs.open(filename, 'r')
			scrapeLine = bs4.BeautifulSoup(f.read(), "html5lib").body.find_all('tr')
		finally:	
			f.close()

		filtered = [i.get_text('\\').split('\\')[1:] for i in scrapeLine]
		

		for i in filtered:
			i.insert(4, "-".join(date.split('.')))
			i[0], i[1] = i[1], i[0]
			if len(i) == 5:
				i.insert(2, "NULL")

		filtered = [i for i in filtered if i[5].endswith(".pdf")]
		return filtered
	


def masterSelection(message):
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename(title = message) # show an "Open" dialog box and return the path to the selected file
	if filename:
		return filename
	else:
		print "You canceled the program has been aborted"
		raise SystemExit



def writer(filename,date):
	user = getpass.getuser()
	mainSave = "C:\\Users\\"+ user +"\\Documents\\Crawler Uploads"
	
	if not os.path.exists(mainSave):
		print "path does not exist"
   		os.makedirs(mainSave)
   	else:
   		print "path exists"

	newFile = open(mainSave + "\\LP Doc Crawler Report_" + date + ".csv", 'w')
	newFile.close()
	
	with open(mainSave + "\\LP Doc Crawler Report_" + date + ".csv", 'wb') as newCSV:
		writer = csv.writer(newCSV, delimiter = ',') 
		header = ["Entity pbID", "Record ID", "Title", "Type", "Date", "Link"]
		writer.writerow(header)
		for j in filename:
			writer.writerow(j)


	return None	


filename = masterSelection("Select HTML file to scrape")
newFileName = filename.split("_")[1][:-5]
writer(lpScraper(filename,newFileName), newFileName)

print "Scrape is complete"