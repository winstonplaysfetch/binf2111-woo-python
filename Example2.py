#! /usr/bin/env python

#write a script that makes it into a dictionary with the first field as the key and the second as the value

dict = {}

with open("example2file.txt") as file:
    for line in file:
        dict[line.split()[0]] = line.split()[1]

print dict


