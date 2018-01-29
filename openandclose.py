# To future me: This script is a collection of examples, comment out parts which are not in use when testing.

# !/usr/bin/env python

# check if a user input filename exists 
import os

DNA_file_name = raw_input("Enter a file name: ")
DNA_file_name.strip(" ")
if os.path.exists("./" + DNA_file_name):
    print "Found file"
else:
    print "File not found"

# create a file object from dna.txt 
dna_file = open("dna.txt")

# access the file object using read method and print contents 
DNA_contents = dna_file.read()
print DNA_contents

# close the file
dna_file.close()

# open a file for writing 
dna_file = open("newfile.txt", "w")
dna_file.write("any string")
dna_file.close()

# now access the file using a with statement 
with open("dna.txt") as dna_file:
    print(dna_file.read())

# open a file using a with statement and print a slice 
with open("dna.txt") as dna_file:
    DNA_contents = dna_file.read()
    print (DNA_contents[0:9])

# open a multi line file using the read method and print 
with open("dnaseqs.txt") as dna_file:
    print dna_file.read()

# open a multi line file using the readlines method and print
with open("dnaseqs.txt") as dna_file:
    print dna_file.readlines()

# open a multi line file using the readlines method and loop 
with open("dnaseqs.txt") as dna_file:
    for line in dna_file.readlines():
        print line[0:9]

# open a multi line file, loop, and apply a condition 
with open("dnaseqs.txt") as dna_file:
    for line in dna_file.readlines():
        if line[0] == "A":
            print line.strip()
        else:
            print line[0:9]

# open a multi line file, loop, and apply a condition to write to a *different file
with open("dnaseqs.txt") as dna_file:
    with open("myfile.txt", "a") as output_file:
        for line in dna_file.readlines():
            if line[0] == "A":
                output_file.write(line.strip() + "/n")
            else:
                output_file.write(line[0:9] + "/n") 
