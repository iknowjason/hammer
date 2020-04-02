#!/usr/bin/env python3
'''
Author:  Jason Ostrom
Description:  This script re-freshes the data by deleting any rows in each table.


'''
import pymysql

db = pymysql.Connect("database", "root", "railsapp", "rackvuln_development" ) 

sql_delete_query1 = """DELETE from users"""
sql_delete_query2 = """DELETE from creditcards"""

def delete_sql(statement):

    try:
        with db.cursor() as cursor:
            retval = cursor.execute(statement)
            db.commit()
    finally:
        None

delete_sql(sql_delete_query1)
delete_sql(sql_delete_query2)
