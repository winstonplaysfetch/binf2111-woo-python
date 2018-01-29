#!usr/bin/env python

with open("multiline-adapt.fna") as infile:
    lines = infile.readlines()
    sequence = []
    for i in range(0, len(lines)):
        if lines[i][0:1] != "<":
            sequence.append(lines[i].strip("/n"))
    print ''.join(sequence)

