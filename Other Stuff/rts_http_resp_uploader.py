import boto.sqs
import csv 
import urlparse
import requests
from requests.exceptions import RequestException
from datetime import datetime
import MySQLdb
import _mysql
import sys
import csv 
import time
import urlparse
import urllib2
import requests
import boto.sqs
from boto.sqs.message import Message, RawMessage
import ssl
import httplib
import socket
import pymssql
reload(sys)
sys.setdefaultencoding("utf-8")

def clean_url (url):    
    if url.startswith('http://', 0, 7):
        url = url[7:]
    if url.startswith('https://', 0, 8):
        url = url[8:]
    if url.startswith('www.', 0, 4):
        url = url[4:]
    while url.rfind('/') != -1:
        dash_pos = url.rfind('/')
        url = url[:dash_pos]
    return url


rts_url_set = {}
dupe_set = []

conn = boto.sqs.connect_to_region("us-west-2", \
    aws_access_key_id="AKIAJUD2FO22B4JPF2XQ", \
    aws_secret_access_key="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")

q = conn.get_queue('rts_url_test')

#with open('/home/ec2-user/load/master_list.csv', 'r') as csvfile:

counter = 0


mssql_conn = pymssql.connect(host='pitchbook27.pitchbook.com',user='tyler.martinez',password='zev92ina',database='dbd')
print 'Connected to MSSQL'
mssql_cursor = mssql_conn.cursor()
mssql_cursor.execute("SELECT top 100 be.pbid, be.entityname, bed.value\
    FROM dbo.BusinessEntity be\
    INNER JOIN dbo.BusinessEntityDomain bed\
    ON be.entityId = bed.businessentityid\
    WHERE bed.value <> ''\
    AND bed.value is not null \
    ")
print 'Selected from MSSQL'
domain_data = mssql_cursor.fetchall()


mssql_cursor.execute("SELECT top 100 be.pbid, be.entityname, be.WebURL\
    FROM dbo.BusinessEntity be\
    WHERE be.WebURL is not null \
    AND be.WebURL <> ''\
    ")
print 'Selected from MSSQL-2'
web_data = mssql_cursor.fetchall()



for row in domain_data:
    try:
        pbid_for_url = row[0]
        co_name = row[1].replace(',','').encode('utf-8')
        url_to_check = clean_url(row[2])

        input_body = pbid_for_url + ',' + co_name + ',' + url_to_check 
        print input_body

        
        if (url_to_check in rts_url_set):
            if (pbid_for_url in rts_url_set[url_to_check]):
                print 'Pass'
                dupe_set.append([pbid_for_url,url_to_check,rts_url_set[url_to_check] ])
                pass
            else:
                print 'Append'
                rts_url_set[url_to_check].append(pbid_for_url)
        else:
            print 'Add!'
            rts_url_set[url_to_check] = [pbid_for_url]

        m = RawMessage()
        m.set_body(input_body) #put the message here

        q.write(m)

        counter = counter + 1
    except:
        pass




for row in web_data:
    try:
        pbid_for_url = row[0]
        co_name = row[1].replace(',','').encode('utf-8')
        url_to_check = clean_url(row[2])

        input_body = pbid_for_url + ',' + co_name + ',' + url_to_check 
        print input_body

        
        if (url_to_check in rts_url_set):
            if (pbid_for_url in rts_url_set[url_to_check]):
                print 'Pass'
                dupe_set.append([pbid_for_url,url_to_check,rts_url_set[url_to_check] ])
                pass
            else:
                print 'Append'
                rts_url_set[url_to_check].append(pbid_for_url)
        else:
            print 'Add!'
            rts_url_set[url_to_check] = [pbid_for_url]

        m = RawMessage()
        m.set_body(input_body) #put the message here

        q.write(m)

        counter = counter + 1
    except:
        pass



print str(counter) + " Messages Have Been Uploaded To SQS"


print "THE DUPES ARE: "
for item in dupe_set:
    print item