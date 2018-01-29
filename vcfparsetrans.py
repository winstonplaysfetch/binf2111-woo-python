#! /usr/bin/env python

from collections import namedtuple
import re
#from Bio import SeqIO

#***************************************FUNCTIONS******************************************

#read and join the genomic FASTA
def readfasta(DNAfile):
    headers = []
    sequences = []
    seq = []
    with open(DNAfile) as infile:
        for line in infile:
            line = line.rstrip()
            if line.startswith(">"): #this determines header, ">" is only in fasta files, change this to .split()[] if necessary
                headers.append(line)
                if len(headers) != 1:
                    sequences.append(''.join(seq))
                    seq = []
            else:
                seq.append(line)# if line doesn't start with >, then header key is the line
    return ''.join(sequences)

#read the GFF(General Feature Format) and yield the coordinates, strand, and name of regions one by one
def read_gff(gff):
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

#read the VCF (Varient Call Format) and yield the coordinate, original sequence, and alternate sequence of each variant
def read_vcf(vcf_file):
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

#Makes a dictionary out of bacterial code, a template file.
def makeaminodict(aminocode):
    with open(aminocode) as code:
        for line in code:
            line = line.rstrip()
            if line.split()[0] == "AAs" : #create amino acid array
                AAs = []
                for char in line.split()[2]:
                    AAs.append(char)
            elif line.split()[0] == "Base1": #create base1 array
                Base1 = []
                for char in line.split()[2]:
                    Base1.append(char)
            elif line.split()[0] == "Base2": #create base2 array
                Base2 = []
                for char in line.split()[2]:
                    Base2.append(char)
            elif line.split()[0] == "Base3": #create base2 array
                Base3 = []
                for char in line.split()[2]:
                    Base3.append(char)
            else:
                pass
        bacterialdict = {}
        for i in range(0,len(AAs) -1):
            codon = Base1[i] + Base2[i] + Base3[i] #join the 3 bases to make a codon code,
            bacterialdict[codon] = AAs[i]  #set the key to codon and the value to the amino acids

        return bacterialdict

#breaks a dna sequence into codons, matches it to the template (amino acid) dictionary
def translate(dna, gencode):
    all_translations = []
    codons = []
    amino_acids = ''
    for frame in range(1,4):
        #split dna file into codons
        for i in range(frame - 1, len(dna)-2, 3):
            codon = dna[i:i+3]
            codons.append(codon)
        #match codons to amino acids
        for codon in codons:
            amino_acids = amino_acids + gencode.get(codon.upper(), 'x')
        #make a list out of the match amino acids
        all_translations.append(amino_acids)
    return all_translations

#Returns the reverse compliment of a DNA input
def reverse_compliment(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(dna)
    compliment_dna = ''.join([complement[base] for base in bases])
    reverse_dna = ''
    for n in reversed(compliment_dna):
        reverse_dna += n
    return reverse_dna


#******************************************MAIN**************************************************

fastafile = "NC_007898_cds.fna"
gff_file = "NC_007898.gff"
vcf_file = "BC17.vcf"
aminocodefile = "bacterialcode.txt"

#1: Get the genomic FASTA file and call your function to join it
sequence = readfasta(fastafile)

#2: Call your GFF reader and put each entry into dictionary (using namedtuples as compound keys and the sequence as values)
origseqDict = {}
with open(gff_file) as gff:
    for first, last, strand, name in read_gff(gff):
        cds = namedtuple("cds", ["start", "end", "dir", "id"]) 
        modfirst = int(first) - 1
        modlast = int(last) - 1
        # Create dict, values are the sequence between first/last
        origseqDict[cds(start=first, end=last, dir=strand, id=name)] = sequence[modfirst:modlast]
#print origseqDict.values()

#3: Call your VCF reader and check each variant to find if it falls inside a CDS region in your dictionary
codingSequence = {}
altCodingSequence = {}
for coord, orig, alt in read_vcf(vcf_file):
    for key in origseqDict.keys():
        if int(key.start) <= int(coord) and int(key.end) >= int(coord):
            codingSequence[origseqDict.get(key)] = key.dir
#4: Make a modified sequence that incorporates the "alternate" sequence where the original sequence was in your coding sequence
            sub = re.sub(orig, alt, origseqDict.get(key)) #find, replace, iterate
            altCodingSequence[sub] = key.dir
            if sub:
                sub = None

#5: Translate both the original and modified sequence and see if they are the same
#if the sequence is on the minus strand you'll have to reverse and complement AFTER you make the modified sequence, but BEFORE you translate
aminodict = (makeaminodict(aminocodefile))

#Translate all the things
origproteins = []
altproteins = []
for key, value in codingSequence.items():
    if key == "+":  # call translate
        origproteins.append(translate(key, aminodict))
    else: #reverse compliment
        reverse_key = reverse_compliment(key)
        origproteins.append(translate(reverse_key, aminodict))

for key, value in altCodingSequence.items():
    if key == "+":  # call translate
        altproteins.append(translate(key, aminodict))
    else:
        reverse_key = reverse_compliment(key)
        altproteins.append(translate(reverse_key, aminodict))

for i in range(len(origproteins)):
    print "Original: "
    print origproteins[i]
    print "Alternate: "
    print altproteins[i]

#This is how I'd compare them if any of this worked
'''
counter = 0
for i in range(len(origproteins)):
    counter += 1
    if origproteins[i] is altproteins[i]:
        print "base substitution had no significant impact"
        print counter
        print origproteins[i]
        print altproteins[i]
    else:
        print "base substitution has changed amino acid sequence"
        print counter
        print origproteins[i]
        print altproteins[i]
        '''

#Should yield about 80 hits, sequences where a substitution is made that effects the protein makeup

