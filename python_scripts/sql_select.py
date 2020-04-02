#!/usr/bin/env python3
import pymysql
'''
This scripts queries the users and email addresses from the users table in MySQL
'''
db = pymysql.connect("localhost", "<DB_NAME>", "<DB_PASSWORD>", "<DB_NAME>" )

search = []
try:
    with db.cursor() as cursor:

        ### Using a while loop
        sql = "SELECT `users`.email, `users`.name FROM `users`"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

        ### Using the cursor as iterator
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    db.close()
