import time
from datetime import date, timedelta
import difflib
import smtplib
from email.mime.text import MIMEText

timestr = time.strftime("%Y%m%d")
yesterday = date.today() - timedelta(1)
csv_yest = yesterday.strftime('%Y%m%d') + '_usgscrc.csv'
csv_today = timestr + '_usgscrc.csv'

file1 = open(csv_yest, 'r')
file2 = open(csv_today, 'r')

diff = difflib.ndiff(file1.readlines(), file2.readlines())

delta = ''.join( x for x in diff if x.startswith('- ') or x.startswith('+ '))
with open('dailydelta.csv', 'w') as daily_delta:
	daily_delta.write(delta)

if delta == '':
	print "no changes found"
else:
	print delta 
	#if there is a difference, we will send an email to notify the user
	fp = open('dailydelta.csv', 'rb')
	msg = MIMEText(fp.read())
	fp.close()
	
	#add the to/from addresses here
	me = #from
	you = #to
	
	msg['Subject'] = 'The USGS-CRC DB has been updated'
	msg['From'] = me
	msg['To'] = you
	
	#define the smtp server.  modify [localhost] to be your smtp server
	s = smtplib.SMTP('[localhost]')
	s.sendmail(me, [you], msg.as_string())
	s.quit()