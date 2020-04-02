#!/usr/bin/env python3
'''
Author:  Jason Ostrom
Description:  This script creates a fake name and prints it 
'''

from faker import Faker
fake = Faker()

fname = fake.name()
print ("Name: %s" % fname)

