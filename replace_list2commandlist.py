#!/usr/bin/python
# coding: Shift_JIS

f = open('C:\list.txt')
line = f.readline()
 
while line:
    line = '"' + line
    line = line.replace('\n', '",')
    print(line)
    line = f.readline()
f.close
