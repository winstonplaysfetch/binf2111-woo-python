#! /usr/bin/env python

# list = [expression for item in list if conditional]
# dict = {value: key for key, value in dict if conditional}

inputDNA = "NC_007898.fasta"

def getname(DNAfile):
    with open(DNAfile) as infile:
        name = [line.strip() for line in infile if line[0] == ">"]
        return name

def getseq(DNAfile):
    with open(DNAfile) as infile:
        sequence = [line.strip() for line in infile if line[0] != ">"]
        seq = ''.join(sequence)
        return seq


#**************MAIN*******************************
print getname(inputDNA)
print "\n"
print getseq(inputDNA)