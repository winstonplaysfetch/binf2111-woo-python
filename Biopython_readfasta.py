#! /usr/bin/env python

input_file = "NC_007898_cds.fna"
output_file = "biopython.txt"

from Bio import SeqIO

def read_fasta(input_file):
    with open(output_file) as out_file:
        for seq_record in SeqIO.parse(input_file, "fasta"):
            name = seq_record.id
            sequence = repr(seq_record.seq)
            length = len(seq_record)
            yield name, sequence, length

with open('NC_007898_cds.fna') as fp:
    counter = 0
    for name, seq, qual in read_fasta(fp):
        print name, seq, qual
        counter += 1
        if counter >= 10:
            break

