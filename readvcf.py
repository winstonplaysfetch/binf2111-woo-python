#! /usr/bin/env python

def read_vcf(vcf_file): # splits out first, last, strand and identifier from GFF
    with open(vcf_file) as vcf:
        for line in vcf:
            #If it's not a comment line
            if line[0] == "#":
                pass
            else:
                coord = line.split()[1]
                orig = line.split()[3]
                alt = line.split()[4]
                if alt.count(","):
                    alt = alt.split(",")[0]
                yield coord, orig, alt

counter = 0
for coord, orig, alt in read_vcf("BC17.vcf"):
    print coord, orig, alt
    counter += 1
    if counter >= 100:
        break