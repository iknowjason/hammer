#!/usr/bin/env python3
import json
'''
This script parses the 'visa.json' file from credit card generator (https://ccardgenerator.com)
and prints the data
'''
with open('cc_data/visa.json', 'r') as f:
    data = f.read()

string = data.replace(u'\xa0', u' ')

obj = json.loads(string)

for i in obj:
    print ("%s" % i)
