# -*- coding: utf-8 -*-
import re

file = open('save.py', 'r')

for eachline in file:
##    print(eachline)
    if type(eachline).__name__!="utf-8":
        print(eachline)
    if re.match("^ +print(\".+)$", eachline):
        print(eachline)

string = ""

print("hello world")
