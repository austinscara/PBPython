import pymssql
import unicodecsv as csv
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename


retsPull = """
			SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
						SELECT 
			case
				when month(irv.ReportDate) != 12 or day(irv.ReportDate) != 31
				then year(irv.ReportDate) - 1
				else year(irv.ReportDate)
			end as [Date],
			 
			irv.LPEntityID, irv.FundID, irv.CommitType      
			from LimitedPartner lp
			inner join IrrTool_ReturnsDataView irv on lp.BusinessEntityId = irv.LPEntityID
			where lp.LPType in (3,18)"""
            # took this out because it may not be needed , coalesce(convert(varchar, irv.CommitDate, 110),'') as [Commit Date]   


RegcommitsPull = """
            SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
			select cmt.LPEntityID, cmt.FundID, cmt.CommitType, 
			coalesce(convert(varchar, cmt.CommitDate, 110) ,'') as [Commit Date]
			from LimitedPartner lp
			inner join IrrTool_CommitmentView cmt on lp.BusinessEntityId = cmt.LPEntityID
			where lp.LPType in (3, 18, 19)"""


####################################

fofCommitsPull = """  
            SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
			select cmt.LPEntityID, cmt.FundID, cmt.CommitType, 
			coalesce(convert(varchar, cmt.CommitDate, 110) ,'') as [Commit Date],
			coalesce(cmt.FoFFundID,'')
			from LimitedPartner lp
			inner join IrrTool_CommitmentView cmt on lp.BusinessEntityId = cmt.LPEntityID
			where lp.LPType in (3, 18, 19) """


fofRetsPull = """
			SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
			SELECT 
			case
				when month(irv.ReportDate) != 12 and day(irv.ReportDate) != 31
				then year(irv.ReportDate) - 1
				else year(irv.ReportDate)
			end as [Date],

			irv.LPEntityID, irv.FundID,irv.CommitType, convert(varchar, irv.CommitDate, 110) as [Commit Date], irv.FoFFundID
			from LimitedPartner lp
			inner join IrrTool_ReturnsDataView irv on lp.BusinessEntityId = irv.LPEntityID
			where lp.LPType in (3,18,19) and irv.FoFFundID is not null"""

###################################

dnuPull = """ 
	SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
	Select iff.FundName, iff.EntityID 
	from InvestorFund iff
	where iff.FundName like '[_]%'
	order by iff.EntityID asc""" 

def sqlPulls(querey):

	mssql_conn = pymssql.connect(host='ext.pitchbook.com',user='skylar.marcum',password='kev34eno',database='dbd_copy')  
	mssql_cursor = mssql_conn.cursor()
	mssql_cursor.execute(querey)

	# pullList is a list of tuples which came from the SQL querey
	pull = {tuple(x):"" for x in mssql_cursor.fetchall()}

	return pull



def makeRets(retsCSV):
	try:

		returnsFile = masterSelection("Select Returns File")
		retsHeader = ["Action",	"ReturnsID",	"ReportDate",	"LPEntityID",	"LPName",
			          "FundID",	"FundName",	"CommitmentID",	"CommitType",	"CommitDate", 
			          "Commited",	"Vintageyear",	"Contributed",	"UnfundedCommited",	
			          "Distributed",	"DistAndRemain",	"RemainingValue",	"Irr",	"Dpi",
			          "Rvpi",	"Tvpi",	"GainSinceIncept",	"Currency",	"CalcMethod",	"Source", 
			          "ngFees",	"CalledDown",	"FoFFundID",	"FoFFundName",	"Source Files"]
		
		with open(returnsFile, 'wb') as retsFile:
				writer = csv.writer(retsFile, delimiter = ',') 
				writer.writerow(retsHeader)
				for line in retsCSV:
					writer.writerow(line)
		return 0

	except IOError:
		return "You have exited the Returns/Commits Generator"




def makeCommits(cmtsCSV):
	try:
		commitsFile = masterSelection("Select Commitments File")

		comitsHeader = ["Action", "CommitmentID",	"LPEntityID",	"LPName",	"FundID",	
	   					"FundName",	"CommitDate",	"OrigCommit",	"1stReportDate",
	   					"Currency",	"returnsDataStopCalc",	"NewCommit",	"NewReportDate",
	   					"NewCurrency",	"CommitType",	"CommitStatus",	"IRR Linked",	
	   					"IRR Wrongly Linked",	"InternalNotes",	"ExternalNotes",	
	   					"FoFFundID"]
		
		with open(commitsFile, 'wb') as cmtFile:
					writer = csv.writer(cmtFile, delimiter = ',') 
					writer.writerow(comitsHeader)
					for line in cmtsCSV:
						writer.writerow(line)
		return 0

	except IOError:
		return "You have exited the Returns/Commits Generator"





def readMaster():
	try:
		masterChecker = masterSelection("Select Master File")
		os.chdir(os.path.dirname(masterChecker))
		with open( masterChecker, "r") as masterSheet:
			reader = csv.reader(masterSheet)
			pullLines = []
			for row in reader:
				pullLines.append(row)
		return pullLines
		
	except IOError: 
		return "You have exited Returns/Commits Generator"


def masterSelection(message):
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename(title = message) # show an "Open" dialog box and return the path to the selected file
	return filename


		#this function takes the report date and returns the adjusted report year
def yearCheck(date):
	if int(date[:2]) == 12 and int(date[3:5]) == 31:
		return int(date[6:])
	else:
		return  int(date[6:]) - 1





def FundDNUCheck(masterCreator):
	
	keys_with_Dnu = []
	DNUID = [x[1] for x in  sqlPulls(dnuPull)]
	for keys in masterCreator:
		if keys[2] in DNUID:
			keys_with_Dnu.append(keys)

	for dnuKeys in keys_with_Dnu:
		if dnuKeys in masterCreator:
			del masterCreator[dnuKeys]

	if keys_with_Dnu:
		with open('\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500\\Master Creator\\DNU_KickBack.csv', 'wb') as DNU_DFunds:
				writer = csv.writer(DNU_DFunds, delimiter = ',') 
				for i in keys_with_Dnu:
					writer.writerow(i)
		raise ValueError(
			 """There were funds found with DNU'd Fund ID's Plese see DNU_KickBack.csv
			    Potential Issue: Fund re-ID'd under new investor
			    Potential Issue: Fund is dupe Under same investor
			    Solution: Find new fund ID and change in MasterCreator Workbook's Fund ID sheet""")
	return  masterCreator

def commitZeroCheck(commit):
	try:
		return int(commit)/1000000
	except ValueError:
		return None	


		#set default path to start
os.chdir("\\\\Mowgli\\Research\\Fund Performance\\5500 & 990\\5500")


		#For reading the master creator file and creating a dictionary of values to check against &
		#Fist Filter: Removing any lines where there is a DNU'd fund
d_MasterCreator = FundDNUCheck({(yearCheck(sublist[2]),int(sublist[3]), int(sublist[5]), int(sublist[8]), sublist[9], sublist[27]):sublist for sublist in readMaster() if sublist[5].isnumeric()})


		#Set Control flow to determine if 5500/990 OR FOF:
if d_MasterCreator.keys()[0][5] == "":
   		#Second Filter Creating Commitments Table
	commitments = sqlPulls(RegcommitsPull)
	d_Reg_Commits_MasterCreator= {(keyItem[1],keyItem[2],keyItem[3],keyItem[4]):keyItem for keyItem in d_MasterCreator}
	commitmentLines = [d_MasterCreator[d_Reg_Commits_MasterCreator[i]] for i in d_Reg_Commits_MasterCreator if i not in commitments]
	adjCmtLines = [[item[0],'', item[3], item[4], item[5], item[6], item[9], commitZeroCheck(item[10]), item[2], item[22], '', '','', item[22], item[8], 1] for item in commitmentLines]
		
		#Make Returns Table
	returns = sqlPulls(retsPull)
	d_Reg_Returns_MasterCreator = {(keyItem[0], keyItem[1], keyItem[2], keyItem[3]):keyItem for keyItem in d_MasterCreator}
	returnsLines = [d_MasterCreator[d_Reg_Returns_MasterCreator[i]] for i in d_Reg_Returns_MasterCreator if i not in returns and int(d_MasterCreator[d_Reg_Returns_MasterCreator[i]][16]) > 1]
		# else signifies filings are of the fund of fund type
else: 
	pass


makeCommits(adjCmtLines)
makeRets(returnsLines)






