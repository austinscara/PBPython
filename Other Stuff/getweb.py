import requests
import bs4
r = requests.get('https://www.privateequityinternational.com/Templates/Pages/LPSearchResults.aspx?id=3164&partnerStatus=GP&advanced=true')

soup = bs4.BeautifulSoup(r.content, "html5lib")


print soup.prettify().encode('utf-8')
