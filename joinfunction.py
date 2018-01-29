#! /usr/bin/env python

#this function reads FASTA files into a string of things.
#Exception: if the headers are not unique
#Exception: sequences will not output in the same order they were inputed.

#inputDNA = raw_input("Enter file name: ")
inputDNA = "NC_007898_cds.fna"

def single_fasta(DNAfile):
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

headers, sequences = single_fasta(inputDNA)
for i in range(0,100):
    print headers[i]
    print sequences[i]



'''
#print file to system
joinseq = single_fasta(inputDNA)
for key, value in joinseq.items():
    print key + "\n" + value + "\n"
'''


'''
sequences = {}
    with open(DNAfile) as infile:
        for line in infile:
            line = line.rstrip()
            if line.startswith(">"): #this determines header, ">" is only in fasta files, change this to .split()[] if necessary
                header = line
                sequences[header] = '' #sets value to '' (empty)
            else:
                sequences[header] += line #if line doesn't start with >, then header key is the line
    return sequences
'''
