#!/usr/bin/env python3
import json

req_file = "myjson.json"
file = open(req_file, 'r')
print(json.load(file))

file.close()

req_file = "myinfo.json"
my_dict = {'Name': 'Corey', 'Skills': ['Python', 'shell', 'yaml', 'AWS']}
fo = open(req_file, 'w')
json.dump(my_dict, fo, indent=4)

fo.close()
