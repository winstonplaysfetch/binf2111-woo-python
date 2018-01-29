#! /usr/bin/env python

def gc_count(DNASeq):
    gccount = DNASeq.count("G") + DNASeq.count("C")
    gcpercent = (float(gccount) / float(len(DNASeq.strip()))) *100
    return gcpercent

userdna = raw_input("Enter DNA sequence: ")
print gc_count(userdna)