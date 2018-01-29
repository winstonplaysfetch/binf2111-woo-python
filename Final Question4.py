#! /usr/bin/env python

#Write a script that takes a protein sequence as raw input and calculates its molecular weight
input = "AMQQQ"

#Create a dict from file that contains amino acids as keys and their molecular weights as values.
weightsdict = {}
with open("aamw.txt") as file:
    for line in file:
        if line.startswith("#"):
            pass
        else:
            weightsdict[line.split()[0]] = line.split()[1]
#print weightsdict

#Create a list that contains the individual values of each amino acid
molvalues = []
for i in input.strip():
    molvalues.append(float(weightsdict.get(i)))
#print molvalues

#Add up all the values in the list
molsum = 0
for i in molvalues:
    molsum += i

print "Molecular Sum: " + str(molsum)
