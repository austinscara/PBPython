import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = raw_input('Name of csv: ')
bDesc = raw_input("Enter a brief description of the error (will be used as email subject line): ") + ' Error'
errDesc = raw_input('Enter a full description of the error: ')
conf = raw_input('Enter the url for the Confluence page that explains this error: ')

#pulls a list of unique emails from the csv
emails = []
with open(filename, 'rb') as file:
	readit = csv.reader(file)
	skiphead = readit.next()
	for row in readit:
		if row[0] not in emails:
			emails.append(row[0])
	file.close()		

#connects to gmail
sender = 'eyre.nathan@gmail.com'
password = 'grizzle12'
server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()
server.login(sender,password)

#loops through each email and adds all corresponding errors for that address into the email
for e in emails:
	
	#body of email
	html = ("""<html>
	<head></head>
	<body><p>Below is a list of errors that need to be cleaned. </p>
	<p>Description of error: """ + errDesc + """</p>
	<p>Corresponding confluence page: """ + conf + """</p>
	</body>
	<table>""")
	
	#cycles through the error list and adds any errors with that address to a table in the html
	with open('emailtest.csv', 'rb') as file2:
		readit2 = csv.reader(file2)
		r = 0
		for row2 in readit2:
			if r == 0:
				html += '<tr>'    
				for column in row2:
					html += ('<th>' + column + '</th>')
				html += '</tr>'
			elif e == row2[0]:
				html += '<tr>'    
				for column in row2:
					html += ('<td>' + column + '</td>')
				html += '</tr>'
			r += 1
	
	#email stuff
	msg = MIMEMultipart('alternative')
	msg['Subject'] = bDesc
	msg['From'] = sender
	msg['To'] = e
	part = MIMEText(html, 'html')
	msg.attach(part)
	
	#send message
	server.sendmail(sender,e,msg.as_string())

#disconnect from server
server.quit()