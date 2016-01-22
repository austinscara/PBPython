import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = raw_input('Name of csv: ')
bDesc = 'Skynet: ' + raw_input("Enter a brief description of the error (will be used as email subject line): ") + ' Error'
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

#connect to pb server
sender = 'research@pitchbook.com'
password = 'January13'
server = smtplib.SMTP('smtp.emailsrvr.com:587')

server.starttls()
server.login(sender,password)

#loops through each email and adds all corresponding errors for that address into the email
for e in emails:

	#body of email
	html = ("""<html>
	<head></head>
	<body><p>Please take up to 10 minutes to fix the following error.</p>
	<p><b>Description of error:</b> """ + errDesc + """</p>
	<p><b>Process page for fixing error:</b> """ + conf + """</p>
	</body>
	<table>""")

	#cycles through the error list and adds any errors with that address to a table in the html
	with open(filename, 'rb') as file2:
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

	html += ("""</table><body><p>If you are confused by this email, please read this confluence page
							and talk with your manager: http://confluence.pitchbook.com:8090/display/TRW/Skynet+Email+Error+Distribution
	</p></body>
	""")

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
