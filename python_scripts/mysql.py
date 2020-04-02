#!/usr/bin/python3
import pymysql
'''
This script selects the email address and users from users MySQL table
'''
db = pymysql.Connect("localhost", "<DB_USER>", "<DB_PASSWORD>", "<DB_NAME>" )

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
