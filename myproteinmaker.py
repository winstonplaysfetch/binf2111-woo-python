#! /usr/bin/env python
#http://pythonforbiologists.com/index.php/applied-python-for-biologists/applied-python-4/

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# a function to translate a dna sequence in 3 forward frames
def translate(dna, gencode):
    all_translations = []
    for frame in range(1,4):
        #split dna file into codons
        codons = []
        for i in range(frame - 1, len(dna)-2, 3):
            codon = dna[i:i+3]
            codons.append(codon)
        #match codons to amino acids
        amino_acids = ''
        for codon in codons:
            amino_acids = amino_acids + gencode.get(codon.upper(), 'x')
        #make a list out of the match amino acids
        all_translations.append(amino_acids)
    return all_translations


#codons = split_into_codons('actgatcgtagctagctagc')
print translate('actgatcgtagctagctagc', gencode)

'''
class example:

def translate(dnaseq, bacterialdict):
    proteinseq = []

    #define start/stop
    stop = len(dnaseq) -2

    for start in range(0, stop, 3):
        codon = dnaseq[start:start+3]
        amino_acid = bacterialdict[codon]
        proteinseq.append(amino_acid)
        ''.join(proteinseq)

        return proteinseq

'''