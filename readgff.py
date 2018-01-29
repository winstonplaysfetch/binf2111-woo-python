#! /usr/bin/env python

from collections import namedtuple

def read_gff(gff_file): # splits out first, last, strand and identifier from GFF
    with open(gff_file) as gff:
        for line in gff:
            #If it's not a comment line
            if line[0] == "#":
                pass
            #And it's not a CDS line
            elif line.split()[2] != "CDS":
                pass
            else:
                first = line.split()[3]
                last = line.split()[4]
                strand = line.split()[6]
                info = line.split()[8]
                nametag = info.split(";")[3]
                name = nametag.split("=")[1]
                yield first, last, strand, name


counter = 0
for first, last, strand, name in read_gff("NC_007898.gff"):
    print first, last, strand, name
    counter += 1
    if counter >= 100:
        break

