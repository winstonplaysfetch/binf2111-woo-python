#! /usr/bin/env python

#Prints the reverse compliment of a DNA input

# dna = raw_input("Enter a DNA sequence: ").
dna = 'CTATGTATACATCAGTACGTCCTTTCGTATAGAAATTAGAAAGACTTAAAAAAGTTGAATACTCAGTTGATTT'

def compliment(dna):
    #Define base complements
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    #Make dna uppercase
    dna = dna.upper()
    #Make the dna string into a list
    bases = list(dna)
    #Find the complement of the dna list by matching to compliment dict
    bases = [complement[base] for base in bases]
    #Re-join the dna list into a string
    _dna = ''.join(bases)
    return _dna

print "The compliment of your DNA input: "
print compliment(dna)
print "Reversed: "
reverse = ''
for n in reversed(compliment(dna)):
    reverse += n
print reverse

'''
def reverse_compliment(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(dna)
    compliment_dna = ''.join([complement[base] for base in bases])
    reverse_dna = ''
    for n in reversed(compliment_dna):
        reverse_dna += n
    return reverse_dna

print reverse_compliment(dna)
'''
