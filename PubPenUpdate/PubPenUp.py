import unicodecsv as csv
import bs4
import os
import requests
import smtplib
import sys
import ipdb
from time import sleep 
from datetime import  datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





class scrapeFunc(object):

		def generic_caller(self,code):
			try:	
				if code == "CalSTRS":
					return self.CalSTRS()
				elif code == "CalPERS":
					return self.CalPERS()
				elif code == "CamRet":
					return self.CamRet()
				elif code == "DCRB":
					return self.DCRB()
				
				# HIERS BLOCK
				elif code == "HIERS-PE":
					return self.HIERS('PE')
				elif code == "HIERS-VC":
					return self.HIERS('VC')
				elif code == "HIERS-RE":
					return self.HIERS('RE') 
				elif code == "HIERS-TI":
					return self.HIERS('TI')
			    ##############################
			    #San Jose Police & Fire Department Retirement Plan BLOCk
				elif code == "SJPF-PE":
					return self.SJPF('PE')
				elif code == "SJPF-RE":
					return self.SJPF('RE')
				############################
				elif code == "CCCERA":
					return self.CCCERA()
				elif code == "MEABF":
					return self.MEABF()
				elif code == "ACC":
					return self.ACC()
				############################	
				
				# Chicago Public School Teachers' Pension & Retirement Fund
				elif code == "CTPF-PE":
					return self.CTPF("PE")
				elif code == "CTPF-RE":
					return self.CTPF("RE")
				############################
				elif code == "BCFPERS":
					return self.BCFPERS()
				elif code == "CPPIB":
					return self.CPPIB()
				elif code == "GRRS":
					return self.GRRS()
				elif code == "GRPFRS":
					return self.GRPFRS()
				elif code == "COPERS":
					return self.COPERS()
				elif code == "RISIC":
					return self.RISIC()
				elif code == "FCERA":
					return self.FCERA()
				elif code == "UWS":
					return self.UWS()
				elif code == "WSIB":
					return self.WSIB()
				elif code == "MainePERS":
					return self.MainePERS()
				elif code == "MDOC":
					return self.MDOC()
				elif code == "NHRS":
					return self.NHRS()
				elif code == "NJSIC":
					return self.NJSIC()
				elif code == "NMERB":
					return self.NMERB()
				elif code == "NMSIC":
					return self.NMSIC()
				#### NYC- Pensions
				elif code == "NYC-BERS":
					return self.NYC("BERS")
				elif code == "NYC-ERS":
					return self.NYC("ERS")
				elif code == "NYC-FDPF":
					return self.NYC("FDPF")
				elif code == "NYC-PPF":
					return self.NYC("PPF")
				elif code == "NYC-TRS":
					return self.NYC("TRS")	
				##############################
				elif code == "OPPRS":
					return self.OPPRS()
				elif code == "PERSI":
					return self.PERSI()
				elif code == "SDCERS":
					return self.SDCERS()
				##### SJCERA Pensions
				elif code == "SJCERA-PA":
					return self.SJCERA("PA")
				elif code == "SJCERA-RE":
					return self.SJCERA("RE")
				##############################
				elif code == "FCERS":
					return self.FCERS()
				#### SanJosePF pensions
				elif code == "SanJosePF-PE":
					return self.SanJosePF("PE")
				elif code == "SanJosePF-RE":
					return self.SanJosePF("RE")
				#############################
				elif code == "SLOCPT":
					return self.SLOCPT()
				elif code == "SURSIl":
					return self.SURSIl()
				### Vermont pensions
				elif code == "V-SERS":
					return self.VERM("V-SERS")
				elif code == "V-MERS":
					return self.VERM("V-MERS")
				elif code == "V-STRS":
					return self.VERM("V-STRS")
				##############################
				elif code == "WMUFoundation":
					return self.WMUFoundation()
				elif code == "MERS":
					return self.MERS()
				elif code == "RBAC":
					return self.RBAC()
				elif code == "ICERS":
					return self.ICERS()
				elif code == "TCERA":
					return self.TCERA()
				elif code == "FWER":
					return self.FWER()
				elif code == "COBERS":
					return self.COBERS()
				elif code == "SIUEndowment":
					return self.SIUEndowment()
				elif code == "ElPasoFP":
					return self.ElPasoFP()
				elif code == "MFPRSI":
					return self.MFPRSI()
				elif code == "MWRAERS":
					return self.MWRAERS()
				elif code == "UCRegents":
					return self.UCRegents()	
				elif code == "GRS":
					return self.GRS()		
				elif code == "CRS":
					return self.CRS()
				elif code == "Islington":
					return self.Islington()		
				elif code == "MCERS":
					return self.MCERS()
				elif code == "Chattahoochee":
					return self.Chattahoochee()
				elif code == "FRSLA":
					return self.FRSLA()
				elif code == "NSHEEndowment":
					return self.NSHEEndowment()
				elif code == "gpMCP":
					return self.gpMCP()
				elif code == "gpCapMan":
					return self.gpCapMan()
				elif code == "gpAPEF":
					return self.gpAPEF()
				### AP3 Holdings
				elif code == "AP3-PE":
					return self.AP3("PE")
				elif code == "AP3-REIF":
					return self.AP3("REIF")
				############################
				elif code == "AP2":
					return self.AP2()
				elif code == "PUF":
					return self.PUF()
				elif code == "AfDB":
					return self.AfDB()
				elif code == "NYCRF":
					return self.NYCRF()
				elif code == "BLPK":
					return self.BLPK()
				elif code == "gpCapMan4q":
					return self.gpCapMan4q()
				elif code == "SBCERA":
					return self.SBCERA()
				elif code == "IowaRegents":
					return self.IowaRegents()
				elif code == "UWEndowment":
					return self.UWEndowment()
				### PSERS filings
				elif code == "PSERS-PE":
					return self.PSERS("PE")
				elif code == "PSERS-RE":
					return self.PSERS("RE")
				############################
				elif code == "SMWNPF":
					return self.SMWNPF()
				### Partners
				elif code == "Partners-P3":
					return self.Partners("P3")
				elif code == "Partners-Pearl":
					return self.Partners("Pearl")
				elif code == "Partners-Princess":
					return self.Partners("Princess")
				#############################
				elif code == "Lincolnshire":
					return self.Lincolnshire()
				elif code == "gpOnex":
					return self.gpOnex()
				elif code == "ASRS":
					return self.ASRS()
				elif code == "ATRS":
					return self.ATRS()
				elif code == "KPERS":
					return self.KPERS()
				elif code == "PSPRS":
					return self.PSPRS()	
				elif code == "PEERS":
					return self.PEERS()
				elif code == "SDIC":
					return self.SDIC()
				elif code == "WYPF":
					return self.WYPF()	
				elif code == "DPFP":
					return self.DPFP()
				elif code == "MDOC":
					return self.MDOC()
				#### OPERF reports
				elif code == "OPERF-PE":
					return self.OPERF("PE")
				elif code == "OPERF-RE":
					return self.OPERF("RE")
				elif code == "OPERF-ALT":
					return self.OPERF("ALT")
				elif code == "OPERF-OPP":
					return self.OPERF("OPP")
				#####################
				###PENNSERS 
				elif code == "PENNSERS-PE":
					return self.PENNSERS("PE")
				elif code == "PENNSERS-RE":
					return self.PENNSERS("RE")
				####################
				elif code == "IP-UL":
					return self.IP("UL")
				elif code == "IP-PROP":
					return self.IP("PROP")
				elif code == "IP-INF":
					return self.IP("INF")
				#####################
				elif code == "PEHAG":
					return self.PEHAG()
				elif code == "NBPEP":
					return self.NBPEP()
				elif code == "SLC":
					return self.SLC()
				elif code == "HBMHealth":
					return self.HBMHealth()
				elif code == "SPE":
					return self.SPE()
				elif code == "VPEG":
					return self.VPEG()

			except AttributeError:
				print code, "is not included"
			

		def CalSTRS(self):
			try:
				calsTrsPage = requests.get("http://www.calstrs.com/private-equity-portfolio-performance")
				calsTrsPageLine = bs4.BeautifulSoup(calsTrsPage.content, "html5lib").body.find("span", {'class':"link-text"}).contents
				calsTrsRawDate =  " ".join(calsTrsPageLine).split()[6:]
				calsTrsFinalDate =  " ".join(calsTrsRawDate)
				return  {"CalSTRS" : calsTrsFinalDate}
			except:
				self.CalSTRS()

		def CalPERS(self):
			try:
				calPersPage = requests.get('https://www.calpers.ca.gov/page/investments/asset-classes/private-equity/pep-fund-performance')
				calPersDateLine = str(bs4.BeautifulSoup(calPersPage.content, "html5lib").p).split()
				calPersDateLine = " ".join(calPersDateLine[6:9])
				return {"CalPERS": unicode(calPersDateLine[:-1])} 
			except:
				self.CalPERS()

		def CamRet(self):
			try:
				camRetPage = requests.get('http://www.cambridgeretirementma.gov/financial-reports')
				camRetPageLine = unicode(bs4.BeautifulSoup(camRetPage.content, "html5lib").body.find_all("span", {'class':"file"})[3])
				upDateLine = camRetPageLine.split()[11:14]
				upDateLine[0] = upDateLine[0].split(">")[1]
				return {"CamRet" : " ".join(upDateLine)}
			except:
				return self.CamRet()

		def DCRB(self):
			try:
				DCRBPage = requests.get('http://dcrb.dc.gov/service/investment-reports')
				DCRBPageLine = unicode(bs4.BeautifulSoup(DCRBPage.content, "html5lib").body.find("div", {'class':"field-item even"}, {'property':"content:encoded"}).h4.findNextSibling('h4').findNext('li')).split()
				upDateLine = DCRBPageLine[17:]
				upDateLine[2] = upDateLine[2].split("<")[0]
				return {"DCRB": " ".join(upDateLine)}
			except:
				return self.DCRB()

		def HIERS(self, signifier = None):
			sigDict = {"PE": "Not Needed" , "VC": 'title="HiTIP' , "RE": 'title="Real', "TI":'title="Timber'}
			try:
				if signifier == 'PE':

					HIERSPage = requests.get('http://ers.ehawaii.gov/investments/holdings')
					HIERSPageLine =  bs4.BeautifulSoup(HIERSPage.content, "html5lib").body.find_all("div", {"class":"attachments"})
					lines = [unicode(i).split() for i in HIERSPageLine]
					Raw_FinalLine = [i for i in lines if i[3] != 'title="HIERS' and i[3] != 'title="HiTIP' and i[3] != 'title="Real' and i[3] != 'title="Timber'][0][5:8]
					Raw_FinalLine[0] = Raw_FinalLine[0].split('>')[1]
					Raw_FinalLine[2] = Raw_FinalLine[2].split('<')[0]
					return {"HIERS-" + signifier: " ".join(Raw_FinalLine)}
					
			
				elif signifier == 'RE':
					HIERSPage = requests.get('http://ers.ehawaii.gov/investments/holdings')
					HIERSPageLine =  bs4.BeautifulSoup(HIERSPage.content, "html5lib").body.find_all('div', {'class': 'attachments'})
					lines = [unicode(i).split() for i in HIERSPageLine]
					Raw_FinalLine = [i for i in lines if i[3] == sigDict[signifier]][0][7:10]
					Raw_FinalLine[2] = Raw_FinalLine[2].split('"')[0]
					return {"HIERS-" + signifier: " ".join(Raw_FinalLine)}
				
				else:

					HIERSPage = requests.get('http://ers.ehawaii.gov/investments/holdings')
					HIERSPageLine =  bs4.BeautifulSoup(HIERSPage.content, "html5lib").body.find_all('div', {'class': 'attachments'})
					lines = [unicode(i).split() for i in HIERSPageLine]
					Raw_FinalLine = [i for i in lines if i[3] == sigDict[signifier]][0][6:9]
					Raw_FinalLine[2] = Raw_FinalLine[2].split('"')[0]
					return {"HIERS-" + signifier: " ".join(Raw_FinalLine)}
			
			except:
				return self.HIERS(signifier)
	
		def CCCERA(self):
			try:
				CCCERAPage = requests.get('http://www.cccera.org/investment-reports/quarterly-review-and-performance-measurement-reports')
				CCCERAPageLine = bs4.BeautifulSoup(CCCERAPage.content, "html5lib").body.find_all("p")[2]
				raw_updateLine = unicode(CCCERAPageLine).split()[9:]
				raw_updateLine[0] = raw_updateLine[0].split(">")[1] 
				raw_updateLine[2] = raw_updateLine[2].split("<")[0] 
				return {"CCCERA": " ".join(raw_updateLine)}
			except:
				return self.CCCERA()

		def MEABF(self):
			try:
				MEABFPage = requests.get('http://www.meabf.org/investments-reports.php')
				MEABFPageLine = bs4.BeautifulSoup(MEABFPage.content, "html5lib").body.find_all('a', {'class' : 'pub'})
				lines = [[unicode(i).split() for i in MEABFPageLine][1][3]]
				lines[0] = lines[0].split(">")[1]
				lines[0] = lines[0].split("<")[0]
				return {"MEABF": lines[0]}
			except:
				return self.MEABF()

		def ACC(self):
			try:
				ACCPage = requests.get('http://www.nespf.org.uk/Investment/inv_managers.asp')
				ACCPageLine = bs4.BeautifulSoup(ACCPage.content, "html5lib").body.find_all('a')
				ACCLinkList = [unicode(i).split() for i in ACCPageLine if 'Private Equity' in unicode(i) ][0][7:]
				ACCLinkList [0], ACCLinkList[1] = ACCLinkList [1], ACCLinkList[0] + "," 
				ACCLinkList[2] = ACCLinkList[2].split("<")[0] 
				return {"ACC": " ".join(ACCLinkList)}
			except:
				return self.ACC()

		def CTPF(Self, signifier = None):
			try:
				sigDict = {"PE": 'Callan' , "RE": 'Townsend'}
				CTPFPage = requests.get('http://www.ctpf.org/general_info/Investments_content.htm')
				CTPFPageLine = bs4.BeautifulSoup(CTPFPage.content, "html5lib").body.find_all("a")
				raw_upDateLine = [unicode(i).split(">") for i in CTPFPageLine if sigDict[signifier] in unicode(i)][0]
				finalUpdateLine = raw_upDateLine[1].split("<")[0]
				return {"CTPF-" + signifier : raw_upDateLine[1].split("<")[0]}
			except:
				return self.CTPF(signifier)

		def BCFPERS(self):
			## may need to put a month catch incase they report monthly
			try:
				BCFPERSPage = requests.get('http://bcfpers.org/services-view/investment-flash-reports/')
				BCFPERSLine = bs4.BeautifulSoup(BCFPERSPage.content, "html5lib").body.find("div", {"class":"post-content"}).find_all('a')
				rawLine = [unicode(i).split() for i in BCFPERSLine][0]
				checkLine = rawLine[9:11]

				if checkLine[0] in ["March","June", "September", "December"]:
					checkLine[1] = checkLine[1].split("<")[0]
					return {"BCFPERS": " ".join(checkLine)}
				else:
					return 
			except:
				return self.BCFPERS()

		def CPPIB(self):
			try:
				CPPIBPage = requests.get('http://www.cppib.com/en/what-we-do/our-investments.html')
				CPPIBLine = bs4.BeautifulSoup(CPPIBPage.content, "html5lib").body.find_all('a')
				raw_updateLine = [unicode(i).split(">")[1].split("<")[0].split()[6:] for i in CPPIBLine if unicode(i).split(">")[1].startswith("Private Equity")][0]
				return {"CPPIB" : " ".join(raw_updateLine)}
			except:
				return self.CPPIB()

		def GRRS(self):
			try:
				GRRSPage = requests.get("http://grcity.us/retirement-systems/General-Retirement-System/Pages/General-Investment-Performance-Reports.aspx")
				GRRSLine = bs4.BeautifulSoup(GRRSPage.content, "html5lib").body.find('p', {"class":"ms-rteElement-P"}).find("a")
				raw_GRRSLine = [unicode(i).split()[2:4] for i in GRRSLine][0]
				return {"GRRS" : " ".join(raw_GRRSLine)}
			except:
				return self.GRRS()

		def GRPFRS(self):
			try:
				GRPFRSPage = requests.get("http://grcity.us/retirement-systems/Police-and-Fire-Retirement-System/Pages/Police-and-Fire-Investment-Performance-Reports.aspx")
				GRPFRSLine = bs4.BeautifulSoup(GRPFRSPage.content, "html5lib").body.find("p").find("a")
				raw_GRPFRSLine = [unicode(i).split()[2:4] for i in GRPFRSLine][0]
				return {"GRPFRS" : " ".join(raw_GRPFRSLine)}
			except:
				return self.GRPFRS()

		def COPERS(self):
			try:
				COPERSPage = requests.get("https://www.phoenix.gov/copers/pension-plan-reports")
				COPERSLine = bs4.BeautifulSoup(COPERSPage.content, "html5lib").body.find_all('a')
				raw_updateLine = [unicode(i).split() for i in COPERSLine if "Real" in unicode(i)][0][1]
				return {"COPERS" : raw_updateLine}
			except:
				return self.COPERS()

		def RISIC(self):
			try:
				RISICPage = requests.get("http://investments.treasury.ri.gov/meetings-reports/")
				RISICLine = unicode(bs4.BeautifulSoup(RISICPage.content, "html5lib").body.find('h2').findNext('h2').findNext('li')).split()[1]
				return {"RISIC" : RISICLine}
			except:
				return self.RISIC()

		def FCERA(self):
			try:
				FCERAPage = requests.get("http://www2.co.fresno.ca.us/9200/investments.htm#Investment")
				FCERALine = bs4.BeautifulSoup(FCERAPage.content, "html5lib").body.find("ul").find_all('a')
				raw_FCERALine = [unicode(i).split()[4:7] for i in FCERALine][0]
				return {"FCERA" :  " ".join(raw_FCERALine)}
			except:
				return self.FCERA()

		def UWS(self):
			try:
				UWSPage = requests.get("https://www.wisconsin.edu/trust-funds/investments-and-reports/")
				UWSLine = bs4.BeautifulSoup(UWSPage.content, "html5lib").body.find_all('a', {"class":"doc-type pdf"})
				raw_UWSLine = [unicode(i).split() for i in UWSLine if 'Quarterly Investment Review' in unicode(i)][0][3]
				return {"UWS" : raw_UWSLine}
			except:
				return self.UWS()

		def WSIB(self):
			try:
				WSIBPage = requests.get("http://www.sib.wa.gov/financial/invrep_ir.asp")
				WSIBLine = bs4.BeautifulSoup(WSIBPage.content, "html5lib").body.find_all("option")
				raw_WSIBLine = [unicode(i).split()[1:4] for i in WSIBLine][0]
				raw_WSIBLine[0] = raw_WSIBLine[0].split(">")[1]
				return {"WSIB" : " ".join(raw_WSIBLine)}
			except:
				return self.WSIB()

		def MainePERS(self):
			try:
				MainePERSPage = requests.get("http://www.mainepers.org/Investments/Investments.htm")
				MainePERSLine = bs4.BeautifulSoup(MainePERSPage.content, "html5lib").body.find("a", href = True, text="Private Market Investments Summary")
				return {"MainePERS" : unicode(MainePERSLine).split()[2]}
			except:
				return self.MainePERS()

		def NHRS(self):
			try:
				NHRSPage = requests.get("https://www.nhrs.org/funding-and-investments/investments")
				NHRSLine = bs4.BeautifulSoup(NHRSPage.content, "html5lib").body.find("a", href = True, text="Quarter-End Private Market Investment Overview")
				return {"NHRS" : unicode(NHRSLine).split()[1]}
			except:
				return self.NHRS()

		def NJSIC(self):
			try:
				NJSICPage = requests.get("http://www.state.nj.us/treasury/doinvest/directorsreports.shtml")
				NJSICLine = bs4.BeautifulSoup(NJSICPage.content, "html5lib").body.find("tbody").find_all('a', title = True)
				raw_updateLine = [unicode(i).split() for i in NJSICLine]
				return  {"NJSIC" : raw_updateLine[0][2]}
			except:
				return self.NJSIC()	

### SCRAPE BLOCKER!!!!!!!
		def NMERB(self):
			try:
				NMERBPage = requests.get("http://www.nmerb.org/Investments.htm")
				NMERBLine = bs4.BeautifulSoup(NMERBPage.content, "html5lib").body#.find_all('a', {"class": "style6"})   #.find_all('a')
				print NMERBLine

				

				return "Yes"  #{"NMERB" : raw_updateLine[0][2]}
			except:
				return "NO"#self.NMERB()
#########################		

		def NMSIC(self):
			try:
				NMSICPage = requests.get("http://www.sic.state.nm.us/private-equity-investments.aspx")
				NMSICLine = bs4.BeautifulSoup(NMSICPage.content, "html5lib").body.find("div", {"class": "flTitle"}).find("a")
				return {"NMSIC" : unicode(NMSICLine).split(">")[1].split("<")[0]}
			except:
				return  self.NMSIC()



		def NYC(self, signifier = None):
			currentYear = datetime.now().year
			pension = {"BERS"	:["https://www.opendatanyc.com/browse?category=BERS+%28NYC+Board+of+Education+Retirement+System%29&tags=meeting+agendas+%26+performance+","BERS"],
					   "ERS"	    :["https://www.opendatanyc.com/browse?category=NYCERS+%28NYC+Employees%27+Retirement+System%29&tags=meeting+agendas+%26+performance+", "NYCERS"],
 					   "FDPF"	:["https://www.opendatanyc.com/browse?category=FIRE+%28NYC+Fire+Department+Pension+Fund%29&tags=meeting+agendas+%26+performance+", "NYC Fire Department Pension Fund"],
                       "PPF"     :["https://www.opendatanyc.com/browse?category=POLICE+%28NYC+Police+Pension+Fund%29&tags=meeting+agendas+%26+performance+", "NYC Police Department Pension Fund"],
					   "TRS"	    :["https://www.opendatanyc.com/browse?category=TRS+%28Teachers%27+Retirement+System+City+of+New+York%29&tags=meeting+agendas+%26+performance+", "TRS"]}
			

			months = {'January,': 1, "February,": 2, "March," : 3, "April,": 4, "May,": 5, "June," : 6, "July,": 7, "August,":8, "September,": 9, "October,": 10, "November,": 11, "December," : 12, 
			          'January': 1, "February": 2, "March" : 3, "April": 4, "May": 5, "June" : 6, "July": 7, "August":8, "September": 9, "October": 10, "November": 11, "December" : 12,
			          '+January,': 1, "+February,": 2, "+March," : 3, "+April,": 4, "+May,": 5, "+June," : 6, "+July,": 7, "+August,":8, "+September,": 9, "+October,": 10, "+November,": 11, "+December," : 12,
			            1: "January", 2: "February", 3:"March", 4 : "April", 5: "May", 6: "June", 7:"July",  8:"August", 9:"September", 10:"October", 11: "November", 12: "December",
			            '\'January': 1, "\'February": 2, "\'March" : 3, "\'April": 4, "\'May": 5, "\'June" : 6, "\'July": 7, "\'August":8, "\'September": 9, "\'October": 10, "\'November": 11, "\'December" : 12,}
			


			global csvRead
			Reader = csvRead()

			### determine what year to use:
			if months[Reader['NYC'+ '-' + signifier][4].split()[0]] == 12:
				year = str(currentYear + 1)
			else:
				year = str(currentYear)
			##############################	
			
			try:
				NYCPage = requests.get(pension[signifier][0] + str(year))
				NYCLine = bs4.BeautifulSoup(NYCPage.content, "html5lib").body.find('table', {"class": "gridList"}).find_all('span', {"class" : "name"})
				raw_updateLine = [unicode(i).split() for i in NYCLine if pension[signifier][1] in unicode(i) and "Cancelled" not in unicode(i) and  unicode(i).split()]

				if signifier in ["BERS", "ERS", "FDPF", "PPF"]:
					findmax = months[max(months[i[-2]] for i in raw_updateLine)]
				else:
					findmax = months[max([months[i[-2]] for i in raw_updateLine if i[-2] in months])]
				return {"NYC-"+ signifier : findmax+ " " +year}
			except:
				return self.NYC(signifier)
			

		def OPPRS(self):
			qtrs = {"March," : 3,  "June," : 6,  "September,": 9, "December," : 12,  "March" : 3, "June" : 6,  "September": 9, "December" : 12,}
			try:
				OPPRSPage = requests.get("http://www.ok.gov/OPPRS/Monthly_Investment_Returns/index.html")
				OPPRSLine = bs4.BeautifulSoup(OPPRSPage.content, "html5lib").body.find_all("a")
				
				OPPRSLine_filtered = [unicode(i).split()[8:10] for i in OPPRSLine if unicode(i).split()[8:10] and len(unicode(i).split()[8:10]) == 2 and  unicode(i).split()[9].isnumeric()][0]

				OPPRSLine_filtered[0] = OPPRSLine_filtered[0].split(">")[1]
				
				if OPPRSLine_filtered[0] in qtrs:
					return { "OPPRS" : " ".join(OPPRSLine_filtered)} 
				else:
					global csvRead
					Reader = csvRead()
					return {"OPPRS" :Reader["OPPRS"][4]}
			except:
				return self.OPPRS()


		def PERSI(self):
			try:
				PERSIPage = requests.get("http://www.persi.idaho.gov/investments/reports.cfm")
				PERSILine = bs4.BeautifulSoup(PERSIPage.content, "html5lib").body.find_all('a')
				raw_updateLine = [unicode(i).split(">") for i in PERSILine if "PE" in unicode(i).split()][0]
				return {"PERSI" : raw_updateLine[1].split()[0]}
			except:
				return self.PERSI()


		def SDCERS(self):
			months = {'January,': 1, "February,": 2, "March," : 3, "April,": 4, "May,": 5, "June," : 6, "July,": 7, "August,":8, "September,": 9, "October,": 10, "November,": 11, "December," : 12, 'January': 1, "February": 2, "March" : 3, "April": 4, "May": 5, "June" : 6, "July": 7, "August":8, "September": 9, "October": 10, "November": 11, "December" : 12}
			try:
				SDCERSPage = requests.get("https://board.sdcers.org/sirepub/meetresults.aspx?isyear=true&meettype=Investment%20Committee")
				SDCERSLine = bs4.BeautifulSoup(SDCERSPage.content, "html5lib").body.find_all("tr")
				

				raw_updateLine = [unicode(i).split()[4:7] for i in SDCERSLine if "INVESTMENT" in unicode(i)][1:]

				YearMax = set()
				for i in raw_updateLine:
					i[-1] = i[-1].split("<")[0]
					YearMax.add(i[-1])
					del i[1]


				second_filter = [i for i in raw_updateLine if i[1] == max(YearMax)]
				
				monthCheck = set()
				for i in second_filter:
					monthCheck.add(months[i[0]])

				return  {"SDCERS" : " ".join([i for i in second_filter if months[i[0]] == max(monthCheck)][0])}
			except:
				return self.SDCERS()

		def SJCERA(self, signifier = None):
			pension = {"PA":"cs_popup_name_9" , "RE":"cs_popup_name_11"}
			try:
				SJCERAPage = requests.get("http://www.sjcera.org/Pages/content/investments/index.html")
				SJCERALine = bs4.BeautifulSoup(SJCERAPage.content, "html5lib").body.find("select", {"name":pension[signifier]})
				raw_updateLine = [unicode(i).split() for i in SJCERALine][3][-2:]
				raw_updateLine[1] = raw_updateLine[1].split("<")[0]
				return  {"SJCERA-"+ signifier : " ".join(raw_updateLine)}
			except:
				return self.SJCERA(signifier)


		def FCERS(self):
			try:
				FCERSPage = requests.get("https://www.sjretirement.com/Fed/Investments/Investments-Performance.asp")
				FCERSLine = bs4.BeautifulSoup(FCERSPage.content, "html5lib").body.find_all('a', {"id":"Fed"})
				FCERSLine_filter = [unicode(i).split() for i in FCERSLine if "Private Market" in unicode(i)][0][-3:]
				FCERSLine_filter[2] = FCERSLine_filter[2].split("<")[0]
			
				return {"FCERS" : " ".join(FCERSLine_filter)}
			except:
				return self.FCERS()

		def SanJosePF(self, signifier = None):
			pension = {"PE":"Private Equity" , "RE":"Real Estate"}
			try:
				SanJosePFPage = requests.get("https://www.sjretirement.com/PF/Investments/Investments-Performance.asp")
				SanJosePFLine = bs4.BeautifulSoup(SanJosePFPage.content, "html5lib").body.find_all('a', {"id":"PF"})
				SanJosePFLine_filter = [unicode(i).split() for i in SanJosePFLine if pension[signifier] in unicode(i)][0][-3:]
				SanJosePFLine_filter[2] = SanJosePFLine_filter[2].split("<")[0]
				return {"SanJosePF-" + signifier : " ".join(SanJosePFLine_filter)}
			except:
				return self.SanJosePF(signifier)

		def SLOCPT(self):
			try:
				SLOCPTPage = requests.get("http://www.slocounty.ca.gov/PensionTrust/agendas.htm")
				SLOCPTLine = bs4.BeautifulSoup(SLOCPTPage.content, "html5lib").body.find_all('li', {"class" : "ipf-nestedlist-file"})
				raw_updateLine = [unicode(i).split() for i in SLOCPTLine if "Agenda &amp; Board Materials" in unicode(i)][0][4]
				return {"SLOCPT" : raw_updateLine}
			except:
				return self.SLOCPT()

		def SURSIl(self):
			try:
				SURSIlPage = requests.get("http://www.surs.org/quarterly-standard-investment-reports")
				SURSIlLine = bs4.BeautifulSoup(SURSIlPage.content, "html5lib").body.find("tbody").find_all('a')
				raw_updateLine = [unicode(i).split() for i in SURSIlLine][0][-2:]
				raw_updateLine[1] = raw_updateLine[1].split("<")[0]
				return  {"SURSIl" : " ".join(raw_updateLine)}
			except:
				return self.SURSIl()

		def VERM(self, signifier = None):
			pension = {"V-SERS": "http://www.vermonttreasurer.gov/retirement/state-financial-reports", "V-MERS": "http://www.vermonttreasurer.gov/retirement/muni-financial-reports", "V-STRS": "http://www.vermonttreasurer.gov/retirement/vstrs-financial-reports"}
			try:
				VERMPage = requests.get(pension[signifier])
				VERMLine = bs4.BeautifulSoup(VERMPage.content, "html5lib").body.find("tbody").find('a')
				raw_updateLine = [unicode(i).split(">") for i in VERMLine][0]
				return {signifier : " ".join(raw_updateLine)}
			except:
				return  self.VERM()

		def WMUFoundation(self):
			try:
				WMUFoundationPage = requests.get("http://www.mywmu.com/s/1428/gid2/index.aspx?sid=1428&gid=2&pgid=429")
				WMUFoundationLine = bs4.BeautifulSoup(WMUFoundationPage.content, "html5lib").body.find("tbody").find('a')
				raw_updateLine = unicode(WMUFoundationLine).split(">")[1].split("<")[0]
				return {"WMUFoundation" : raw_updateLine}
			except:
				return self.WMUFoundation()

		def MERS(self):
			try:
				MERSPage = requests.get("http://www.michigan.gov/treasury/0,4679,7-121-1753_37621_66445---,00.html")
				MERSLine = bs4.BeautifulSoup(MERSPage.content, "html5lib").body.find_all("a", {"class": "bodylinks"} )#target = "_blank")
				raw_updateLine = [unicode(i).split() for i in MERSLine][0]
				return {"MERS" : raw_updateLine[2]}
			except:
				return self.MERS()

		def RBAC(self):
			try:
				RBACPage = requests.get("http://www.alleghenycounty.us/retirement/reports/reports.aspx")
				RBACLine = bs4.BeautifulSoup(RBACPage.content, "html5lib").body.find('h3').findNext("h3").findNext("h3").findNext("h3").findNext("ul").find_all("a")
				raw_updateLine = [unicode(i).split('"') for i in RBACLine][0][-1:]
				raw_updateLine[0] = raw_updateLine[0].split(">")[1]
				raw_updateLine[0] = raw_updateLine[0].split("<")[0]
				return {"RBAC" : raw_updateLine[0]}
			except:
				return self.RBAC()

		def ICERS(self):
			try:
				ICERSPage = requests.get("http://www.icers.info/QuarterlyInvestments/QuarterlyInvestments.htm")
				ICERSLine = bs4.BeautifulSoup(ICERSPage.content, "html5lib").body.find_all('option')
				raw_updateLine =[unicode(i).split() for i in ICERSLine if "Select" not in unicode(i)][0][3]
				return {"ICERS" : raw_updateLine }
			except:
				return self.ICERS()

		def TCERA(self):
			try:
				TCERAPage = requests.get("http://tcera.org/Publications.php")
				TCERALine = bs4.BeautifulSoup(TCERAPage.content, "html5lib").body.find_all('td')
		

				raw_updateLine = [unicode(i).split() for i in TCERALine if "Investment Performance Report -" in unicode(i)]
				first_filter = [j.split("_")[-3::2] for i in raw_updateLine for j in i if "Performance" in j and len(j) > 20]
	
				s_year = set()
				for i in first_filter:
					i[0] = int(i[0][0])
					i[1] = int(i[1].split(".")[0])
					s_year.add(i[1])
				
				max_Year_Filter = [i for i in first_filter if i[1] ==  max(s_year)]
 
 				s_qtr = set()
 				for i in max_Year_Filter:
 					s_qtr.add(i[0])

 				final_date = [i for i in max_Year_Filter if i[0] == max(s_qtr)]

 				upDateLine = final_date[0]

				return {"TCERA" : "Q" + str(upDateLine[0])+ " " + str(upDateLine[1])}
			except:
				return  self.TCERA()

#### Need to Complete!!!
		def FWER(self):
			try:
				FWERPage = requests.get("http://fortworthretirementtx-investments.minutesondemand.com")
				FWERLine = bs4.BeautifulSoup(FWERPage.content, "html5lib").body.find_all('li', {"rel": "file"})     #find("div", {"id":"MOD-results"})



				for i in  FWERLine:
					print i

				print FWERLine


				# raw_updateLine =[unicode(i).split() for i in ICERSLine if "Select" not in unicode(i)][0][3]
				return "yes" # {"FWER" : raw_updateLine }
			except:
				return "No" #self.FWER()

####Need to Complete!!!
		def COBERS(self):
			try:
				COBERSPage = requests.get("http://bcers.org/investmentreports.html")
				COBERSLine = bs4.BeautifulSoup(COBERSPage.content, "html5lib").body.find_all("a")
				print COBERSLine

				# for i in COBERSLine:
				# 	print i

				# raw_updateLine =[unicode(i).split() for i in COBERSLine if "Select" not in unicode(i)][0][3]
				return "Yes" #{"COBERS" : raw_updateLine }
			except:
				return "No" #self.COBERS()


#### Unscrapeable ??
		def SIUEndowment(self):
			try:
				SIUEndowmentPage = requests.get("http://www.siuf.org/financial/investmentperformancedetail.pdf")
				SIUEndowmentLine = bs4.BeautifulSoup(SIUEndowmentPage.content, "html5lib").body#.find_all("a")
				print SIUEndowmentLine

				# for i in COBERSLine:
				# 	print i

				# raw_updateLine =[unicode(i).split() for i in COBERSLine if "Select" not in unicode(i)][0][3]
				return "Yes" #{"SIUEndowment" : raw_updateLine }
			except:
				return "No" #self.SIUEndowment()

			ElPasoFP
	
		def ElPasoFP(self):
			try:
				ElPasoFPPage = requests.get("http://elpasofireandpolice.org/fr_investment.asp")
				ElPasoFPLine = bs4.BeautifulSoup(ElPasoFPPage.content, "html5lib").body.find_all("a")
		
				raw_filter = [unicode(i).split() for i in ElPasoFPLine if "Quarter" in unicode(i)]

				YearMax = set()
				for i in raw_filter:
					YearMax.add(i[-1][:4])

				sec_filter = [i for i in raw_filter if max(YearMax) in i[-1]]

				qtrMax = set()
				for i in sec_filter:
					qtrMax.add(i[-3][:1])


				final_filter = [i for i in sec_filter if max(qtrMax) in i[-3]][0]

				return {"ElPasoFP" : final_filter[1]}
			except:
				return self.ElPasoFP()

		def MFPRSI(self):
			try:
				MFPRSIPage = requests.get("http://www.mfprsi.org/about-mfprsi/investments/")
				MFPRSILine = bs4.BeautifulSoup(MFPRSIPage.content, "html5lib").body.find("h3")
				return {"MFPRSI" : unicode(MFPRSILine) }
			except:
				return self.MFPRSI()

		def MWRAERS(self):
			months = [3,6,9,12]
			try:
				MWRAERSPage = requests.get("http://www.mwraretirement.com/general/page/investment-performance")
				MWRAERSLine = bs4.BeautifulSoup(MWRAERSPage.content, "html5lib").body.find_all("a")
				
				first_filter = [unicode(i).split()[-3].split(">")[1] for i in MWRAERSLine if "Flash Report" in unicode(i)][0]

				if int(first_filter[:-8]) in months:
					return {"MWRAERS" : first_filter}
				else:
					global csvRead
					Reader = csvRead()
					return {"MWRAERS": Reader["MWRAERS"][4]}

			except:
				return self.MWRAERS()



		def UCRegents(self):
			try:
				UCRegentsPage = requests.get("http://www.ucop.edu/investment-office/investment-reports/index.html")
				UCRegentsLine = bs4.BeautifulSoup(UCRegentsPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split() for i in UCRegentsLine if "Alternative Investments: Private Equity Internal Rates of Return" in unicode(i)][0][1]
				return {"UCRegents" : first_filter }
			except:
				return self.UCRegents()

		def GRS(self):
			months = ["March","June","September","December"]
			try:
				MWRAERSPage = requests.get("http://www.greenwichct.org/government/boards/retirement_board/investment_performance_reports/")
				MWRAERSLine = bs4.BeautifulSoup(MWRAERSPage.content, "html5lib").body.find_all("a")
	

				first_filter = [unicode(i).split(">")[1].split()[0] for i in MWRAERSLine if "- Private Equity Flash Report" in unicode(i)][0]
				
				if first_filter in months:
					return {"GRS": first_filter}
				else:
					global csvRead
					Reader = csvRead()
					return {"GRS": Reader["GRS"][4]}
			except:
				return self.GRS()

		def CRS(self):
			try:
				CRSPage = requests.get("http://www.cincinnati-oh.gov/retirement/financial-information/investment-reports-2015/")
				CRSLine = bs4.BeautifulSoup(CRSPage.content, "html5lib").body.find_all('strong')
				first_filter = [unicode(i) for i in CRSLine if "Quarter Report" in unicode(i)][-1]
				return {"CRS" : first_filter.split(">")[1].split("<")[0] }
			except:
				return self.CRS()

		def Islington(self):
			try:
				IslingtonPage = requests.get("http://www.islington.gov.uk/about/council-works/councilfinance/Pages/policies.aspx")
				IslingtonLine = bs4.BeautifulSoup(IslingtonPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split() for i in IslingtonLine if "Islington Pension Fund" in unicode(i)][0][1]
				return  {"Islington" : first_filter}
			except:
				return self.Islington()

		def MCERS(self):
			months = {"March": 3, "June": 6, "September":9, "December": 12}
			try:
				MCERSPage = requests.get("http://county.milwaukee.gov/Retirement/Reports/Investment.htm")
				MCERSLine = bs4.BeautifulSoup(MCERSPage.content, "html5lib").body.find_all('u')
				first_filter = { unicode(i): [months[x] for x in months if x in unicode(i)]  for i in MCERSLine if ".pdf" in unicode(i) and any(j in unicode(i) for j in months)}

				if first_filter:
					checkLine = {max(first_filter, key=first_filter.get): first_filter[max(first_filter, key=first_filter.get)]}
					return {"MCERS" : checkLine.keys()[0].split()[1]}
				else:
					global csvRead
					Reader = csvRead()
					return {"MCERS": Reader["MCERS"][4]}
			except:
				return self.MCERS()


		def Chattahoochee(self):
			try:
				ChattahoocheePage = requests.get("http://www.cfcv.com/plaintext/aboutus/investmentperformance.aspx")
				ChattahoocheeLine = bs4.BeautifulSoup(ChattahoocheePage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split('"') for i in ChattahoocheeLine if "Most Recent Investment Performance" in unicode(i)][0][1]
				return  {"Chattahoochee" : first_filter}
			except:
				return self.Chattahoochee()

		def FRSLA(self):
			months = ["March", "June", "September", "December"]
			try:
				FRSLAPage = requests.get("http://www.lafirefightersret.com/investment.html")
				FRSLALine = bs4.BeautifulSoup(FRSLAPage.content, "html5lib").body.find("strong")
				if [unicode(i) for i in FRSLALine if  any(j in unicode(i) for j in months)]:
					return {"FRSLA" : unicode(FRSLALine).split(">")[1].split("<")[0]}
				else:
					global csvRead
					Reader = csvRead()
					return {"FRSLA": Reader["FRSLA"][4]}
			except:
				return self.FRSLA()



		def NSHEEndowment(self):
			qtrs = {"First": 1, "Second": 2, "Third": 3, "Fourth": 4}

			try:
				NSHEEndowmentPage = requests.get("http://system.nevada.edu/Nshe/index.cfm/data-reports/financial-reports/quarterly-investment-reports/")
				NSHEEndowmentLine = bs4.BeautifulSoup(NSHEEndowmentPage.content, "html5lib").body.find_all('a', target = "_blank")
		

				first_filter = [unicode(i).split() for i in NSHEEndowmentLine]

				YearMax = set()
				
				for i in first_filter:
					YearMax.add(i[-5])

				second_filter = [i for i in first_filter if i[-5] == max(YearMax)]

				quarters = set()
				for i in second_filter:
					quarters.add(qtrs[i[-7].split(">")[1]])


				last_filter = [i for i in second_filter if qtrs[i[-7].split(">")[1]] == max(quarters)][0][-7:-4]
				last_filter[0] = last_filter[0].split(">")[1] 		

				return   {"NSHEEndowment" : " ".join(last_filter)}
			except:
				return    self.NSHEEndowment()


		def gpMCP(self):
			try:
				gpMCPPage = requests.get("http://www.mithrascapital.com/reports/")
				gpMCPLine = bs4.BeautifulSoup(gpMCPPage.content, "html5lib").body.find('div', {"class": "report"}).find("a")
				finalLine = [unicode(i) for i in gpMCPLine][0]
				return  {"gpMCP" : finalLine}
			except:
				return self.gpMCP()

		
		def gpCapMan(self):
			try:
				gpCapManPage = requests.get("http://www.capman.com/capman-group/earnings-model-and-financials/result")
				gpCapManLine = bs4.BeautifulSoup(gpCapManPage.content, "html5lib").body.find('div', {"class": "release"}).find("a")
				finalLine = [unicode(i) for i in gpCapManLine][0]
				return {"gpCapMan" : finalLine}
			except:
				return self.gpCapMan()

		def gpAPEF(self):
			try:
				gpAPEFPage = requests.get("http://www.aberdeenprivateequity.co.uk/en/itprivateequityfund/literature/historic-reports")
				gpAPEFLine = bs4.BeautifulSoup(gpAPEFPage.content, "html5lib").body.find("ul", {"class" : "doc-list"}).find_all('li')
			
				first_filter = [unicode(i).split() for i in gpAPEFLine][0][-2:]
				first_filter[1] = first_filter[1].split("<")[0]

				return {"gpAPEF" : " ".join(first_filter)}
			except:
				return self.gpAPEF()

		def AP3(self, signifier = None):
			holdings = {"PE": "Private equity investments" , "REIF": "Timberland, real estate and infrastructure holdnings" }
			try:
				AP3Page = requests.get("http://www.ap3.se/sites/english/portfolio/totalportfolio/Pages/Securitiesholding.aspx")
				AP3line = bs4.BeautifulSoup(AP3Page.content, "html5lib").body.find("tbody").find_all("a")
				first_filter = [unicode(i).split() for i in AP3line if ".pdf" in unicode(i) and holdings[signifier] in unicode(i)][0][-3:-1]
				return {"AP3-" + signifier : " ".join(first_filter)}
			except:
				return self.AP3(signifier)


		def AP2(self):
			try:
				AP2Page = requests.get("http://www.ap2.se/en/Portfolio/portfolio/")
				AP2Line = unicode(bs4.BeautifulSoup(AP2Page.content, "html5lib").body.find("a", {"class": "pdf"})).split()[3]
				AP2Line = AP2Line.split(">")[0]
				return {"AP2" : AP2Line}
			except:
				return self.AP2()

		def PUF(self):
			try:
				PUFPage = requests.get("http://www.utimco.org/scripts/internet/fundsdetail.asp?fnd=2")
				PUFLine = bs4.BeautifulSoup(PUFPage.content, "html5lib").body.find_all("a")
				first_filter = [unicode(i).split(">")[1].split("<")[0] for i in PUFLine if "Semi-Annual report" in unicode(i)][0]
				return {"PUF" : first_filter}
			except:
				return self.PUF()

		def AfDB(self):
			try:
				AfDBPage = requests.get("http://www.afdb.org/en/documents/financial-information/financial-statements-and-data/")
				AfDBLine = bs4.BeautifulSoup(AfDBPage.content, "html5lib").body.find("tbody").find_all("a")
				first_filter = [unicode(i).split(">")[1].split()[0] for i in AfDBLine if "AfDB Financial Statements" in unicode(i)][0]			
				return {"AfDB" : first_filter}
			except:
				return self.AfDB()

		def NYCRF(self):
			try:
				NYCRFPage = requests.get("http://www.osc.state.ny.us/retire/about_us/financial_statements_index.php#cafr")
				NYCRFLine = bs4.BeautifulSoup(NYCRFPage.content, "html5lib").body.find_all("a", title = True)
				first_filter = [unicode(i).split() for i in NYCRFLine if "Comprehensive Annual Financial Report" in unicode(i)][0][1]
				return  {"NYCRF" : first_filter}
			except:
				return self.NYCRF()

		def BLPK(self):
			try:
				BLPKPage = requests.get("http://www.blpk.ch/Home/infocenter/geschaeftsberichte.html")
				BLPKLine = bs4.BeautifulSoup(BLPKPage.content, "html5lib").body.find_all("a")
				first_filter = [unicode(i).split() for i in BLPKLine if "Download" in unicode(i)][0][1]
				return  {"BLPK" : first_filter}
			except:
				return self.BLPK()

		def gpCapMan4q(self):
			try:
				gpCapMan4qPage = requests.get("http://www.capman.com/capman-group/funds/fund-returns")
				gpCapMan4qLine = bs4.BeautifulSoup(gpCapMan4qPage.content, "html5lib").body.find_all("h2")
				first_filter = [unicode(i) for i in gpCapMan4qLine if "The funds' returns as at" in unicode(i)][0]
				return  {"gpCapMan4q" : first_filter}
			except:
				return self.gpCapMan4q()


		def SBCERA(self):
			try:
				SBCERAPage = requests.get("https://www.sbcera.org/Investments/FiscalYearPerformance.aspx")
				SBCERALine = bs4.BeautifulSoup(SBCERAPage.content, "html5lib").body.find("a", text = "latest quarterly investment report")
				return {"SBCERA" : unicode(SBCERALine).split()[1]}
			except:
				return self.SBCERA()


		def IowaRegents(self):
			try:
				IowaRegentsPage = requests.get("http://www.regents.iowa.gov/Meetings/DocketMemos/agendaitems.html")
				IowaRegentsLine = bs4.BeautifulSoup(IowaRegentsPage.content, "html5lib").body.find('blockquote').find('blockquote').find('ul').find_all('li')
				first_filter = [unicode(i).split('"') for i in IowaRegentsLine][-1][1]
				return {"IowaRegents" : first_filter}
			except:
				return  self.IowaRegents()




		def UWEndowment(self):
			try:
				UWEndowmentPage = requests.get("https://uwff-dev1.s.uw.edu/treasury2/CEF/reports")
				UWEndowmentLine = bs4.BeautifulSoup(UWEndowmentPage.content, "html5lib").body.find("div", {"class":"content"}).find_all('a')
				first_filter = [unicode(i).split('"') for i in UWEndowmentLine if "Private Investment Disclosure Requirement as of" in unicode(i)][0][1]
				return {"UWEndowment" : first_filter}
			except:
				return self.UWEndowment()


		def PSERS(self, signifier = None):
			pensions = {"PE":"PSERS Private Markets Investment Performance (Net of Fees)", 
						"RE":"PSERS Real Estate Investment Performance (Net of Fees)"}
			try:
				PSERSPage = requests.get("http://www.psers.state.pa.us/investment/invest.htm")
				PSERSLine = bs4.BeautifulSoup(PSERSPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split('"') for i in PSERSLine if pensions[signifier] in unicode(i)][0][1]
				return {"PSERS-" + signifier : first_filter}
			except:
				return self.PSERS()

		
		def SMWNPF(self):
			months = {'January': 1, "February": 2, "March" : 3, "April": 4, "May": 5, "June" : 6, "July": 7, "August":8, "September": 9, "October": 10, "November": 11, "December" : 12}
			try:
				SMWNPFPage = requests.get("http://www.smwnpf.org/about-the-fund/financial-documents/")
				SMWNPFLine = bs4.BeautifulSoup(SMWNPFPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split(">")[1].split() for i in SMWNPFLine if "Financial Statement" in unicode(i)]
				
				years = set()				
				for i in first_filter:
					years.add(i[2])

				second_filter = [i for i in first_filter if max(years) in i]
				third_filter = { months[i[0]] : i for i in second_filter}
				return {"SMWNPF" : " ".join(max(third_filter.values()))}
			except:
				return self.SMWNPF()

		def Partners(self, signifier = None):
			reports = {"P3":"http://pgdatahotel.net/index.php?site=download&product=P3&type=Quarterly%20Report", "Pearl": "http://pgdatahotel.net/index.php?site=download&product=Pearl&type=Quarterly%20Report", "Princess": "http://pgdatahotel.net/index.php?site=download&product=Princess&type=Quarterly%20Report"}
			try:
				PartnersPage = requests.get(reports[signifier])
				PartnersLine = bs4.BeautifulSoup(PartnersPage.content, "html5lib").body.find("select", id = "year").find_all("option")
				first_filter = [unicode(i) for i in PartnersLine][2]
				return  {"Partners-" + signifier : first_filter}
			except:
				return self.Partners(signifier)

		def Lincolnshire(self):
			try:
				LincolnshirePage = requests.get("http://www.wypf.org.uk/Member/Investments/Lincoln/Lincoln_Investments_Index.aspx")
				LincolnshireLine = bs4.BeautifulSoup(LincolnshirePage.content, "html5lib").body.find_all('a', text = "Private equity and property investments")
				first_filter = [unicode(i).split('"')[1] for i in LincolnshireLine][0]
				return  {"Lincolnshire" : first_filter}
			except:
				return  self.Lincolnshire()

		def gpOnex(self):
			try:
				gpOnexPage = requests.get("http://www.onex.com/Our_Return_on_Invested_Capital.aspx")
				gpOnexLine = bs4.BeautifulSoup(gpOnexPage.content, "html5lib").body.find('em').find("span")
				return  {"gpOnex" : [unicode(i) for i in gpOnexLine][2]}
			except:
				return  self.gpOnex()

		def ASRS(self):
			try:
				ASRSPage = requests.get("https://www.azasrs.gov/content/annual-reports")
				ASRSLine = bs4.BeautifulSoup(ASRSPage.content, "html5lib").body.find_all("a")
				first_filter = [unicode(i).split("(")[-1].split(")")[0] for i in ASRSLine if "Comprehensive Annual Financial Report" in unicode(i)][0]
				return   {"ASRS" : first_filter}
			except:
				return  self.ASRS()


		def ATRS(self):
			try:
				ATRSPage = requests.get("https://www.artrs.gov/publications")
				ATRSLine = bs4.BeautifulSoup(ATRSPage.content, "html5lib").body.find("section", {"class" : "span12"}).find_all('a')
				first_filter = [unicode(i).split(">")[1].split("<")[0] for i in ATRSLine if  "Annual_Report.pdf" in unicode(i)][0]		
				return  {"ATRS" : first_filter}
			except:
				return  self.ATRS()

		def KPERS(self):
			try:
				KPERSPage = requests.get("http://www.kpers.org/about/reports.html")
				KPERSLine = bs4.BeautifulSoup(KPERSPage.content, "html5lib").body.find("div" ,{"class":"sidebar1box sidebar1pad floatleft"}).find('p').find('a')
				return {"KPERS" : unicode(KPERSLine).split('"')[1]}
			except:
				return self.KPERS()
		

		def PSPRS(self):
			try:
				KPERSPage = requests.get("http://www.psprs.com/sys_psprs/AnnualReports/cato_annual_rpts_psprs.htm")
				KPERSLine = bs4.BeautifulSoup(KPERSPage.content, "html5lib").body.find('div', {"class" : "content"}).find_all("a")
				return  {"PSPRS" : [unicode(i).split(">")[1].split("<")[0] for i in KPERSLine][0]}
			except:
				return self.PSPRS()


		def PEERS(self):
			try:
				PEERSPage = requests.get("https://www.psrs-peers.org/Investments/Annual-Report.html")
				PEERSLine = bs4.BeautifulSoup(PEERSPage.content, "html5lib").body.find('h2')
				return  {"PEERS" :unicode(PEERSLine)}
			except:
				return self.PEERS()

		def SDIC(self):
			try:
				SDICPage = requests.get("http://www.sdrs.sd.gov/reportarchives.aspx")
				SDICLine = bs4.BeautifulSoup(SDICPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split('>')[1].split("<")[0] for i in SDICLine if "FY" in unicode(i)][0]
				return  {"SDIC" :first_filter}
			except:
				return  self.SDIC()


		def WYPF(self):
			try:
				WYPFPage = requests.get("http://www.wypf.org.uk/Member/Investments/PrivateEquityPortfolio/PrivateEquityPortfolio.aspx")
				WYPFLine = bs4.BeautifulSoup(WYPFPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split('"')[1] for i in WYPFLine if "PrivateEquityPortfolio" in unicode(i) and 'class="InvestmentsMenu"' not in unicode(i)][0]
				return  {"WYPF" :first_filter}
			except:
				return   self.WYPF()


		def DPFP(self):
			try:
				DPFPPage = requests.get("https://www.dpfp.org/Agendas.html")
				DPFPLine = bs4.BeautifulSoup(DPFPPage.content, "html5lib").body.find_all('li')
				first_filter = [unicode(i).split('"')[1] for i in DPFPLine if "Regular Agenda plus background material" in unicode(i)][0]
				return  {"DPFP" :first_filter}
			except:
				return   self.DPFP()

### no sigifiying link title
		def OPERF(self, signifier = None):

			reports = {"PE":"OPERF Private Equity Portfolio Information", 
					   "RE":"OPERF Real Estate Portfolio Information", 
					   "ALT":"OPERF Alternatives Portfolio Information",
					   "OPP":"OPERF Opportunity Portfolio Information"}

			try:
				OPERFPage = requests.get("http://www.oregon.gov/treasury/Divisions/Investment/Documents/OPERF%20Alternatives%20Portfolio%20Information.pdf")
				OPERFLine = bs4.BeautifulSoup(OPERFPage.content, "html5lib").body#.find("div", {"class": "article-content"}).find("ul").find_all('li')
				print OPERFLine
				# first_filter = [unicode(i).split('"')[1] for i in OPERFLine if reports[signifier] in unicode(i)][0]
			
			

				return  {"OPERF-" + signifier :first_filter}
			except:
				return "NO" #  self.OPERF()

		def PENNSERS(self, signifier = None):

			reports = {"PE":"Private Holdings as of", 
					   "RE":"Real Asset Holdings as of"}
			try:
				PENNSERSPage = requests.get("http://sers.pa.gov/investments.aspx")
				PENNSERSLine = bs4.BeautifulSoup(PENNSERSPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split()[-3:] for i in PENNSERSLine if reports[signifier] in unicode(i)][0]
				return {"PENNSERS-" + signifier :" ".join(first_filter)}
			except:
				return self.PENNSERS()

		def IP(self, signifier = None):

			reports = {"UL":"Unoterede aktier", 
					   "PROP":"Ejendomme",
					   "INF" :"Infrastruktur"}
			try:
				IPPage = requests.get("https://www.industrienspension.dk/da/Om%20Industriens%20Pension/Investeringer#accordion=Aktiver")
				IPLine = bs4.BeautifulSoup(IPPage.content, "html5lib").body.find_all('a')
				first_filter = [unicode(i).split('"')[1] for i in IPLine if reports[signifier] in unicode(i)]
				
				
				return  {"IP-" + signifier :first_filter[0]}
			except:
				return self.PENNSERSno


		def PEHAG(self):
			try:
				PEHAGPage = requests.get("http://www.peh.ch/")
				PEHAGLine = bs4.BeautifulSoup(PEHAGPage.content, "html5lib").body.find("div", id = "box3").find_all('a')
				first_filter = [unicode(i).split('"')[1] for i in PEHAGLine][0]
				return  {"PEHAG" :first_filter}
			except:
				return  self.PEHAG()

		def NBPEP(self):
			try:
				NBPEPPage = requests.get("http://www.nbprivateequitypartners.com/financialreport.aspx")
				NBPEPLine = bs4.BeautifulSoup(NBPEPPage.content, "html5lib").find("a", id = 'gvDocuments_ctl02_HyperLink1')
				first_filter = [unicode(i) for i in NBPEPLine][0]
				return  {"NBPEP" :first_filter}
			except:
				return  self.NBPEP()


	#### No Signifying date
		def SLC(self):
			try:
				SLCPage = requests.get("http://www.slcapital.com/products/slepet/index.html")
				SLCLine = bs4.BeautifulSoup(SLCPage.content, "html5lib").find("a", title = " - Interim Report")
				print SLCLine
				return "yes" #{"SLC" :first_filter}
			except:
				return'n' #self.SLC()

		def HBMHealth(self):
			try:
				HBMHealthPage = requests.get("http://www.hbmhealthcare.com/en/portfolio/monatsuebersicht.php")
				HBMHealthLine = bs4.BeautifulSoup(HBMHealthPage.content, "html5lib").find_all("a", {"class" : "pdf"})
				first_filter = [unicode(i).split('"')[-1] for i in HBMHealthLine if "Quarterly Report" in unicode(i)][0]
				return {"HBMHealth" :first_filter}
			except:
				return self.HBMHealth()


		def SPE(self):
			try:
				SPEPage = requests.get("http://www.speas.dk/default.asp?id=166")
				SPELine = bs4.BeautifulSoup(SPEPage.content, "html5lib").find("div", {"class" : "txt_select"}).find_all('a')
				first_filter = [unicode(i) for i in SPELine][0]
				return  {"SPE" :first_filter}
			except:
				return  self.SPE()

		def VPEG(self):
			try:
				VPEGPage = requests.get("http://vpeg.info/investor-information/financials")
				VPEGLine = bs4.BeautifulSoup(VPEGPage.content, "html5lib").find_all("a")
				first_filter = [unicode(i).split('"')[1] for i in VPEGLine if "Quarterly-Report-June-" in unicode(i)][-1]
				return {"VPEG" :first_filter}
			except:
				return self.VPEG()




#####################################################
#####################################################
#####################################################	
#####################################################

	


"""
If there is a montly check, then I will need to put a catch in to the compare
function to make sure that there isn't an email sent un-nesscessarily 
"""




#############################
# C:\\Users\\austin.scara\\Python\\PubPenUpdate
def csvRead():
	os.chdir("C:\\Users\\austin.scara\\Python\\PubPenUpdate")
	with open('LastCheck.csv', 'rb') as LastCheck:
		reader = csv.reader(LastCheck, delimiter = ",")
		next(reader)
		return {row[2]: row for row in reader}
	

	
def getNewDates(websites):
	sf = scrapeFunc()
	newDatesDict = {}
	try:
		for i in websites:
			print i
			print sf.generic_caller(i).keys()[0]
			print sf.generic_caller(i).values()[0] 
			newDatesDict[sf.generic_caller(i).keys()[0]] = sf.generic_caller(i).values()[0] 
		# newDatesDict = {sf.generic_caller(i).keys()[0] : sf.generic_caller(i).values()[0] for i in websites}
	except AttributeError:
		print i
	return newDatesDict


		



def comparePensions():   #o,n,w
	

	newDates = getNewDates(csvRead())
	oldDates = csvRead() 
	upDateWrites =[]

	sender = 'research@pitchbook.com'
	password = 'January13'
	server = smtplib.SMTP('smtp.emailsrvr.com:587')
	server.starttls()
	server.login(sender,password)

	try:
		for i in oldDates:
			if oldDates[i][4] != "'" + newDates[i] + "'":
				oldDates[i][4] = unicode("'" + newDates[i] + "'")
				upDateWrites.append(oldDates[i])
				emailUpdates(oldDates[i], server, sender)
			else:
				upDateWrites.append(oldDates[i])
		csvWrite(upDateWrites)
	except KeyError:
		print i + ' has no key'


	for i in upDateWrites:
		print i
	return None

		
def emailUpdates(updates,server, sender):
	
	# sender = 'research@pitchbook.com'
	# password = 'January13'
	# server = smtplib.SMTP('smtp.emailsrvr.com:587')

	# server.starttls()
	# sleep(10)
	# server.login(sender,password)


	#body of email
	html = ("""<html>
	<head></head>
	<body><p>The following public pensions have been updated: """ + updates[1] + """, Code:""" + updates[2] + """, Link:""" + updates[3] + """</p>""")
	
	#email stuff
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Public Pension Updates :D"
	msg['From'] = sender
	msg['To'] = 'amy.mills@pitchbook.com'
	part = MIMEText(html, 'html')
	msg.attach(part)

	#send message

	server.sendmail(sender,'amy.mills@pitchbook.com',msg.as_string())


	#disconnect from server
	# server.quit()
	
	return None
	

	
def csvWrite(newDates):
	with open('LastCheck.csv', 'wb') as newCheck:
		writer = csv.writer(newCheck, delimiter = ',') 
		header = ['PBID', 'LP Name', 'Code', 'Data Website', 'Last Check Date']
		writer.writerow(header)
		for j in newDates:
			writer.writerow(j)
	return None
	



comparePensions()


