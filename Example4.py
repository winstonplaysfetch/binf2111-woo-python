#! /usr/bin/env python

import collections

DNASeq = raw_input("Enter the sequence: ")
codons = []

last_codon_start = len(DNASeq) - 2
for start in range(0, last_codon_start, 3):
    codons.append(DNASeq[start:start + 3])

c = collections.Counter(codons)
print(c.most_common(5))