#! /usr/bin/env python

inputDNA = "NC_007898_cds.fna"

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

with open('NC_007898_cds.fna') as fp:
    counter = 0
    for name, seq in read_fasta(fp):
        print name, seq
        counter += 1
        if counter >=10:
            break
