#!/usr/bin/python2.7 -Wd
'''
file: bulk_import.py
use: bulk imports list of users from csv file into mysql database
author: ty.talmadge@gmail.com
date: 20131001
connector: mysqldb because the SQL only changes per table layout
'''
# define imported libraries
import csv,MySQLdb
# define file to be imported
import_file="/path/to/import_names_sample.csv"

#connect to mysql database
app_db = MySQLdb.connect(host="localhost",user="some_user",passwd="some_password",db="some_db_schema")
# create cursor object
cursor = app_db.cursor() 

# open file and read from it
import_reader = csv.reader(file(import_file))
for row in import_reader:
    cursor.execute("INSERT INTO users(ID, PARENT, UNIT, NAME, FULL_NAME, PASSWORD, SUSPENDED, SUSPENDED_DATE, CREATED, CREATED_BY, MODIFIED, MODIFIED_BY, PASSWORD_CREATED, EMAIL ) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ", row)

# commit the insert statement
app_db.commit()
# close the database connection
cursor.close()
# print the done message
print "Finished bulk importing users from %s." % import_file