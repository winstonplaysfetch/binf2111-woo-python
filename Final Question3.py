#! /usr/bin/env python

#produce a dict from the file aamw.txt, which has comment lines and lines of data in the format
dict1 = {}
with open("aamw.txt") as file:
    for line in file:
        if line.startswith("#"):
            pass
        else:
            dict1[line.split()[0]] = line.split()[1]
print dict1

#produce a dict from the string "ATGCTACG"
# where the first four characters are the nucleic acids and the next four characters are their complement

#string = "ABCDABCD" #To check if keys/values match up
string = "ATGCTACG"
list1 = string[0:4]
list2 = string[4:8]
dict2 = {list1[i]:list2[i] for i in range(0,4)}
print dict2

