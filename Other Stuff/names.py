import pymssql


def WomanName():
	mssql_conn = pymssql.connect(host='ext.pitchbook.com',user='skylar.marcum',password='kev34eno',database='dbd_copy')
	mssql_cursor = mssql_conn.cursor()
	mssql_cursor.execute("""
                    SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
					;with names as (
					select pe.FirstName, 
					(select COUNT(pem.EntityID) from PersonEntity pem where pem.FirstName = pe.FirstName and pem.Gender = 1) as CountOfMale,
					(select COUNT(pef.EntityID) from PersonEntity pef where pef.FirstName = pe.FirstName and pef.Gender = 2) as CountOfFemale
					from PersonEntity pe
					where pe.Gender = 2) 


					Select DISTINCT *, 
					(Select  CAST(CountOfMale as DECIMAL(9,2))/(CountOfMale+CountOfFemale))*100 as PerCentMale,
					(Select  CAST(CountOfFemale as DECIMAL(9,2))/(CountOfMale+CountOfFemale))*100 as PerCentFemale
					from names
					Where names.FirstName not like '.' and
					names.FirstName not like '-' and
					names.FirstName not like '_DNU%'
					
					order by names.FirstName
					""")

	domain_data = mssql_cursor.fetchall()
	for line in domain_data:
		print line, '\n'
	
	
	
def ManName():
	mssql_conn = pymssql.connect(host='ext.pitchbook.com',user='skylar.marcum',password='kev34eno',database='dbd_copy')
	mssql_cursor = mssql_conn.cursor()
	mssql_cursor.execute("""
                    SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
					;with names as (
					select pe.FirstName, 
					(select COUNT(pem.EntityID) from PersonEntity pem where pem.FirstName = pe.FirstName and pem.Gender = 1) as CountOfMale,
					(select COUNT(pef.EntityID) from PersonEntity pef where pef.FirstName = pe.FirstName and pef.Gender = 2) as CountOfFemale
					from PersonEntity pe
					where pe.Gender = 1) 


					Select DISTINCT *, 
					(Select  CAST(CountOfMale as DECIMAL(9,2))/(CountOfMale+CountOfFemale))*100 as PerCentMale,
					(Select  CAST(CountOfFemale as DECIMAL(9,2))/(CountOfMale+CountOfFemale))*100 as PerCentFemale
					from names
					Where names.FirstName not like '.' and
					names.FirstName not like '-' and
					names.FirstName not like '_DNU%'
					
					order by names.FirstName
					""")

	domain_data = mssql_cursor.fetchall()
	for line in domain_data:
		print line, '\n'

def PercentMen():
	print "man"

def PercentWoman():
	print "man"

def NameSynonym():
	print "man"



print"""
Welcome To PersonEntity Gender Module
-------------------------------------
MENU:
Return First Name For Women  : 1
Return First Name For Men    : 2
Return First Name % for Men  : 3
Return First Name % for Women: 4
Return Name Synonym Sets     : 5
"""

Function_Choice = int(raw_input("Which function do you wish to run?"))
	
if Function_Choice == 1: 
	WomanName()
elif Function_Choice == 2:
	ManName()
elif Function_Choice == 3:
	PercentMen()
elif Function_Choice == 4:
	PercentWoman()
elif Function_Choice == 5:
	NameSynonym()




# mssql_conn = pymssql.connect(host='ext.pitchbook.com',user='skylar.marcum',password='kev34eno',database='dbd_copy')
# mssql_cursor = mssql_conn.cursor()

# mssql_cursor.execute("""
                    # Select pe.EntityID, pe.FirstName, g.description
					# From PersonEntity pe
					# INNER JOIN Gender g on pe.Gender = g.id
					# Where pe.FirstName not like '_D%' and g.description not like '' and pe.FirstName not like '-'
					# order by g.id asc, pe.firstname asc""")

# domain_data = mssql_cursor.fetchall()
# for line in domain_data:
	# print line, '\n'









	
	
	
