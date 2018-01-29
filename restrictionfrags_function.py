#! /usr/bin/env python

#FUNCTIONS
def makelist(genomefile): #appends each file line to seq[] array
    seq =[]
    for line in genomefile:
        line = line.strip()
        if line.startswith(">"):
            pass
        else:
            seq.append(line)
    return seq

def restrictionsite(joinedfile, pattern): #Define a restriction site pattern,
    rfrags = joinedfile.split(pattern)
    rfrags[0] = rfrags[-1] + rfrags[0]
    del rfrags[-1]
    return rfrags

def formatfasta(rfrags): #Print each fragment with its own FASTA header line
    for i in range(0, len(rfrags)):
        print "> Fragment " + str(i+1) + ": " + str(len(rfrags[i])) + " nucleotides.\n"
        print rfrags[i]

#FUNCTION CALLS
with open("NC_007898.fasta") as dnafile: #open the file
    wholejoin = ''.join(makelist(dnafile)) #Make a list, join the list
    formatfasta(restrictionsite(wholejoin, "CTGCAG")) #define restriction site pattern, print results formatted to FASTA
