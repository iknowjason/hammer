#!/usr/bin/env python3
import pymysql
import datetime
'''
This script inserts a fake record into MySQL
'''

db = pymysql.Connect("localhost", "<DB_USER>", "<DB_PASSWORD>", "<DB_NAME>" )

def insert_sql(vid, vnetwork, vcardnumber, vname, vaddress, vcountry, vcvv, vexp, vuser_id, vcreated_at, vupdated_at):

    insert_stmt = (
  "INSERT INTO creditcards (id, network, cardnumber, name, address, country, cvv, exp, user_id, created_at, updated_at) "
  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
)

    data = (vid, vnetwork, vcardnumber, vname, vaddress, vcountry, vcvv, vexp, vuser_id, vcreated_at, vupdated_at)

    try:
        with db.cursor() as cursor:
            retval = cursor.execute(insert_stmt, data)
            #print ("Completed!: %s" % retval)
            db.commit()
    finally:
        db.close()

insert_sql(7, 'Visa', 2456786171821826, 'Jason Ostrom', '4500 Narrowbrook Drive', 'USA', 87676, '07-1-2024', 1, datetime.date(2012, 3, 23), datetime.date(2012, 3, 23))
