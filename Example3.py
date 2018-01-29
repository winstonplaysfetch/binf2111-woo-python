#! /usr/bin/env python

#Convert the following for loop to a list comprehension

list = []
with open("aamw.txt") as file:
    list = [line.split()[0] for line in file if line[0] != "#"]

print list
