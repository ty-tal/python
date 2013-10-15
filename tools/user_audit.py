#!/usr/bin/python2.7 -Wd
'''
file:user_audit.py
use: audits users table and compares current date to last password update
	   if last update exceeds threshold send a notice to users
author: ty.talmadge@gmail.com
date: 20131002
connector: mysqldb because the SQL only changes per table layout
'''
# define imported libraries
import datetime,MySQLdb,smtplib
# import mimetext if you want to include a copy of the password update policy
from email.mime.text import MIMEText

# turn mail function off and on
# 0 is off 1 is on
mail_on=0

# define today and lookback day
lookback_days=90
today_day=datetime.datetime.today()
today_holdout=datetime.date.today()
day_format="%Y-%m-%d"
hour_format="%H:%M:%S"
this_day=today_day.strftime(day_format)
this_hour=today_day.strftime(hour_format)
today="%s %s" % (this_day,this_hour)
lookback=datetime.timedelta(days=lookback_days)
holdout=today_holdout-lookback
threshhold_d="%s %s" % (holdout,this_hour)
threshhold=str(threshhold_d)

# define msg as multipart, application and message to be sent to listed users
audit_file="/path/to/audit_message.txt"
ap=open(audit_file, 'rb')
msg=MIMEText(ap.read())
ap.close()
me='application_name@mycompany.com'
application_name='Your_Application'

#connect to mysql database
audit_db = MySQLdb.connect(host="localhost",user="some_user",passwd="some_password",db="some_db_schema")
# create cursor object
cursor = audit_db.cursor() 
# query user table
cursor.execute("select name,full_name,password_created,email from users where password_created < '%s' order by name asc" % threshhold)
print "Auditing users starting %s and looking back %s days to %s.\n" % (today,lookback_days,threshhold)
print "The following users have not updated their passwords in the last %s days.\n " % lookback_days
# echo results if running in a scheduler, i.e. Control-M, Open-Scheduler, etc. so they will appear in sysout
# format the data so it is in readable columns
for row in cursor.fetchall():
    pw_format=str(row[2])
    if mail_on == '0':
	# send an email to the users displayed
	msg['Subject']='Password update reminder from %s' % application_name
	msg['From']=me
	msg['To']=row[3]
	sendme=smtplib.SMTP('mail_server')
	sendme=sendmail(me,[row[3]], msg.as_string())
	sendme.quit()
    else:
	print row[0].ljust(30), "	 ", row[1].ljust(30), "  ",pw_format.ljust(30), "  ", row[3].ljust(30)
    
# close the database connection
audit_db.close()
# print the done message
print "\nFinished auditing user table.\n"