import requests 
import html5lib
import csv
import os
import itertools
import time
from multiprocessing.dummy import Pool  # This is a thread-based Pool
from multiprocessing import cpu_count
from bs4 import BeautifulSoup
from datetime import datetime
"""
This Modules is scraping for links that contain fightevent information
it will grab links and read it in to a list
That list will then be read to loop through the fights and individual bouts
"""

startScript = datetime.now()

def csvWritter(data, csvName):
    # data must be list of lists or yeild the same type
    with open(csvName, 'w') as csvLog:
        writer = csv.writer(csvLog, lineterminator = '\n') 
        for eventData in data:
            writer.writerow(eventData)
    return None


def investorListFinder(url): 
    # Scrapes for all events on page 
    website = requests.get(url).content
    # Finds the main table where data resides*
    soup = BeautifulSoup(website, 'html5lib').body.find('table', id = 'listing').find('tbody').find_all('a')
    firmList = [a.contents[0] for a in soup if a.contents[0] != 'View Website']
    firmSite = [a['href'] for a in soup if 'businessdetail' not in a['href']]
    listZip = zip(firmList, firmSite)
    return listZip



# investorListFinder('http://www.dealmakerportal.com/index.php?show=' + str(2) + '&page=listing&category=1&mode=&search=')

csvName = r'C:\Users\austin.scara\Python\InvestorScrape\invSite.csv'



pg = (investorListFinder('http://www.dealmakerportal.com/index.php?show=' + str(i) + '&page=listing&category=1&mode=&search=') for i in range(2,194))

finalList = []
for i in pg:
	for j in i:
		finalList.append(j)

csvWritter(finalList, csvName)