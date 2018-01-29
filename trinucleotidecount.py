#! /usr/bin/env python

def trinucleotidecount(dna):
    counts = {}
    for base1 in ['A', 'T', 'G', 'C']:
        for base2 in ['A', 'T', 'G', 'C']:
            for base3 in ['A', 'T', 'G', 'C']:
                trin = base1 + base2 + base3
                count = dna.count(trin)
                if count > 0:
                    #counts[key] = value
                    counts[trin] = count
    return counts

print trinucleotidecount("AATTGGCC")

