#! /usr/bin/env python

def gc_count(DNASeq):
    with open(DNASeq) as my_seqs:
        for line in my_seqs:
            gcount = line.count("G")
            ccount = line.count("C")
            gccount = gcount + ccount
            gcpercent = (float(gccount) / float(len(line.strip()))) * 100
            yield gcpercent

for percent in gc_count("myseqs.txt"):
    print percent

