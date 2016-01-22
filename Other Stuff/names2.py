import os
import mysql


connection = mysql.connection.connect(user = 'skylar.marcum', password = 'kev34eno', database = 'ext.pitchbook.com')
cursor = connection.cursor()


sql = ("SELECT * FROM Gender")

result = cursor.execute(sql)
print result



cursor.close
connection.close
