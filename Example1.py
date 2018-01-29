#! /usr/bin/env python

#Convert the script so that the GC calculation is performed in a function rather than in the main script.

def gcpercent(gccount):
    return (float(gccount) / float(len(DNASeq.strip()))) * 100

DNASeq = raw_input("Give me a DNA sequence:")
gcount = DNASeq.count("G")
ccount = DNASeq.count("C")
gccount = gcount + ccount
print gcpercent(gccount)

