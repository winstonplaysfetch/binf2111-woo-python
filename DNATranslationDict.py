#! /usr/bin/env python

#Reads FASTA files into a dictionary
def join_fasta(DNAfile):
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
    return (headers, sequences)

#Makes a dictionary out of bacterial code, a template file.
def makeaminodict(bactcode):
    with open(bactcode) as code:
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

        return bacterialdict #return dict[codon] = amino acid


#breaks a dna sequence (from fasta file) into codons, matches it to the template (amino acid) dictionary
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


#*******************MAIN*************************************************
print "DNA Translation Dictionary by Jennifer Daly"
codefile = "bacterialcode.txt"
fastafile = "NC_007898_cds.fna"


#1. Create amino acid dictionary
aminodict = (makeaminodict(codefile))
#print aminodict #Print aminodict for troubleshooting


#2. Create sequence arrays
headers, sequences = join_fasta(fastafile)
#theSequenceString = ''.join(sequences)
#for i in range(0,len(headers)): print headers[i] + '\n' + sequences[i] #Print theSequence for troubleshooting


#3. Match contents of theSequence to the amino acid dictionary to create a protein profile, print to screen.
for i in range(0,len(headers)-1):
    proteins = translate(sequences[i], aminodict)
    print headers[i]
    print proteins



