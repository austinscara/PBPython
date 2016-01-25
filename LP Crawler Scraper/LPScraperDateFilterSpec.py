import unicodecsv as csv
import bs4
import os
import codecs
import getpass
from datetime import date
from Tkinter import Tk
from tkFileDialog import askopenfilename


# This function filters out any "URL" that does not end in ".pdf"
# AND formats the data for RTS uploading
def lpScraper(htmlFile, date):
		# Context manager which opens the selection ".html" file
		# scrapes and and creates a list of html table row <tr> where delimination = ","
		# then closes said file
		try:	
			f = codecs.open(htmlFile, 'r')
			scrapeLine = bs4.BeautifulSoup(f.read(), "html5lib").body.find_all('tr')
		finally:	
			f.close()

		# Converts the single list of <tr>'s into a list of lists where each sublist is an individual table row
		# and where each sublist has the "status" column removed => [1:]
		filtered = [i.get_text('\\').split('\\')[1:] for i in scrapeLine]
		
		# for each <tr> it inserts a date in the 5th collumn
		# NOTE!!! python indexes collumns @ 0 so index 4 is the 5th collumn
		# Flip-Flops the 1st index[0] and 2nd index[1] collums 
		# finally it checks to see if each row is the required length if not it fills the appropriate field with "NULL"
		for i in filtered:
			i.insert(4, "-".join(date.split('.')))
			i[0], i[1] = i[1], i[0]
			if len(i) == 5:
				i.insert(2, "NULL")

		# Creates a list which filters out <tr> whose "URL" does not end with ".pdf"
		filtered = [i for i in filtered if i[5].endswith(".pdf")]
		return filtered
	

def dateFilter(postLPScraper):
	# Creates a date range in accordance to the LP methodology that provides all years that we want to exclude
	# year 2000 - currentYear - 3 
	# NOTE: Range() 2nd argument is non inclusive so it is really current year - 1 - 2
	dateRng = [unicode(i) for i in range(2000, date.today().year - 2)]

	# Creates a list which filters out any line which contains the years we want to exclude
	return [i for i in postLPScraper if not any(yr in i[3] for yr in dateRng)]


def masterSelection(message):
	# we don't want a full GUI, so keep the root window from appearing
	Tk().withdraw() 

	# show an "Open" dialog box and return the path to the selected file with title = "Select HTML file to scrape"
	filename = askopenfilename(title = message) 

	# Checks to see if the user selected a file to be run through the filters
	if filename:
		return filename

	# If the user closes file Dialog without choosing file err is rasied and program is closed
	else:
		print "You canceled the program has been aborted"
		raise SystemExit



def writer(filename,date):
	# Gets the user's system username (name of your profile in windows)
	user = getpass.getuser()

	# Creates path String of where the end file will be saved
	mainSave = "C:\\Users\\"+ user +"\\Documents\\Crawler Uploads"
	
	# Performs system check to see if user has path on their machine
	# If not, Foler is created
	if not os.path.exists(mainSave):
		print "path does not exist"
   		os.makedirs(mainSave)
   	else:
   		print "path exists"

   	# Creates Shell File where output will be saved
	newFile = open(mainSave + "\\LP Doc Crawler Report_" + date + ".csv", 'w')
	newFile.close()
	
	# Context manager which writes header info and Data from 'filename' into CSV and saves file
	with open(mainSave + "\\LP Doc Crawler Report_" + date + ".csv", 'wb') as newCSV:
		writer = csv.writer(newCSV, delimiter = ',') 
		header = ["Entity pbID", "Record ID", "Title", "Type", "Date", "Link"]
		writer.writerow(header)
		for j in filename:
			writer.writerow(j)
	return None	


##### START OF SCRIPT #####

# Gets the file to be processed see "def masterSelection" above (ex: "Report_01.03.2016.html")
filename = masterSelection("Select HTML file to scrape")

# Splits the Date out of the .html file select from the function above
newFileName = filename.split("_")[1][:-5]

# Returns a list of lists of <tr>'s which is formatted and has all non-relevant files removed
preDatefilter = lpScraper(filename,newFileName)

# See dateFilter Funcition above
# Writes final output to CSV, See 'def writer' above
writer(dateFilter(preDatefilter), newFileName)

print "Scrape is complete"