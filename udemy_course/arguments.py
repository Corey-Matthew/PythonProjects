#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print (f"Usage: {sys.argv[0]}  <required_string>  <lower/upper/title>")
    sys.exit()
string = sys.argv[1]
action = sys.argv[2]

if action == 'lower':
    print(string.lower())
elif action == 'upper':
    print(string.upper())

elif action == 'title':
    print(string.title())

else:
    print("You must choose one of three actions: lower/upper/title.")
