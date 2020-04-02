#!/usr/bin/env python
'''
Author:  Jason Ostrom
Description:  This script creates some fake email addresses by defining a function that returns one email address.


'''
import random
import string
import csv

def makeEmail():
	extensions = ['com','net','org','gov']
	domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']

	winext = extensions[random.randint(0,len(extensions)-1)]
	windom = domains[random.randint(0,len(domains)-1)]

	acclen = random.randint(1,20)

	winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

	finale = winacc + "@" + windom + "." + winext
	return finale

email_addy = makeEmail()
print ("email: %s" % email_addy)
