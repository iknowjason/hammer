#!/usr/bin/env python3
'''
Author:  Jason Ostrom
Description:  This script uses Faker to create fake names, email addresses, and passwords.  It then inserts this data into a MySQL DB.


'''
import random
import string
from faker import Faker
import pymysql
import datetime

db = pymysql.Connect("database", "root", "railsapp", "rackvuln_development" ) 

fake = Faker()

def insert_sql(vid, vname, vemail, vpassword, vcreated_at, vupdated_at):

    insert_stmt = (
  "INSERT INTO users (id, name, email, password, created_at, updated_at) "
  "VALUES (%s, %s, %s, %s, %s, %s)"
)

    data = (vid, vname, vemail, vpassword, vcreated_at, vupdated_at)

    try:
        with db.cursor() as cursor:
            retval = cursor.execute(insert_stmt, data)
            db.commit()
    finally:
        None

def randomPassword(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def makeEmail():
	extensions = ['com','net','org','gov']
	domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']

	winext = extensions[random.randint(0,len(extensions)-1)]
	windom = domains[random.randint(0,len(domains)-1)]

	acclen = random.randint(1,20)

	winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

	finale = winacc + "@" + windom + "." + winext
	return finale

index = 1
while index!=100:
    fname = fake.name()
    femail = makeEmail()
    fpassword = randomPassword(10)
    insert_sql(index, fname, femail, fpassword, datetime.date(2012, 3, 23), datetime.date(2012, 3, 23))
    index=index+1;

