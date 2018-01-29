#! /usr/bin/env python

def read_fastq(fastq):
    name, seq, qual = [None], [None], [None]
    for i, line in enumerate(fastq):
        line = line.strip()
        if i % 4 == 0:
            name = line
        elif i % 4 == 1:
            seq = line
        elif i % 4 == 3:
            qual = line
            yield name, seq, qual
            name, seq, qual = [None], [None], [None]
        else:
            pass

with open('BC_30.fastq') as fp:
    counter = 0
    for name, seq, qual in read_fastq(fp):
        print name, seq, qual
        counter += 1
        if counter >= 10:
            break