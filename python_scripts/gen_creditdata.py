#!/usr/bin/env python3
'''
Author:  Jason Ostrom
Description:  This script parses the json files created from Credit Card Generator (http://ccardgenerator.com/).
Then inserts them into a MySQL DB

'''

import json
import pymysql
import datetime

files = ['cc_data/visa.json',
	'cc_data/mastercard.json',
	'cc_data/amex.json',
        'cc_data/discover.json'
]

db = pymysql.Connect("localhost", "<DB_USERNAME>", "<DB_PASSWORD>", "<DB_NAME>" )

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
        None

index = 1 
for file in files:

    with open(file, 'r') as f:
        data = f.read()

    string = data.replace(u'\xa0', u' ')

    obj = json.loads(string)

    for i in obj:

        ##def insert_sql(vid, vnetwork, vcardnumber, vname, vaddress, vcountry, vcvv, vexp, vuser_id, vcreated_at, vupdated_at):
        network = i['CreditCard']['IssuingNetwork'] 
        cardnumber = i['CreditCard']['CardNumber'] 
        name = i['CreditCard']['Name'] 
        address = i['CreditCard']['Address'] 
        country = i['CreditCard']['Country'] 
        cvv = i['CreditCard']['CVV'] 
        exp = i['CreditCard']['Exp'] 
        insert_sql(index, network, cardnumber, name, address, country, cvv, exp, 1, datetime.date(2012, 3, 23), datetime.date(2012, 3, 23))
        index += 1

print ("Counter: %d" % index)
db.close()
