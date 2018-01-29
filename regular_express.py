#! /usr/bin/env python

#regular expressions
import re

dnafile = "fasta.txt"
headers = []
proteins = []

count = 1
with open(dnafile) as fasta:
    name, seq = None, []
    for line in fasta:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                proteins.append(''.join(seq))
                headers.append(name)
                count += 1
            name = line
            seq = []
        else:
            seq.append(line)

#Search for pattern
pattern = "RRRR" #Can use regular expressions ex: (A|V|C)?A.

filter_headers = []
filter_proteins = []

count2 = 0
for i in range(0, len(proteins)):
    match = re.search(pattern, proteins[i], re.I)
    if match:
        filter_headers.append(headers[i])
        filter_proteins.append(proteins[i])
        count2 += 1
        print headers[i]
        print proteins[i]
        print "You have %d of %d structures remaining" %(count2, count)

#Sub for pattern
sub_pattern = "VVV"

final_head = []
final_prot = []

for j in range(0, len(filter_proteins)):
    sub = re.sub(pattern, sub_pattern, filter_proteins[j]) #find, replace, iterate
    if sub:
        final_head.append(filter_headers[j])
        final_prot.append(filter_proteins[j])
        print filter_headers[j]
        print sub
        sub = None

