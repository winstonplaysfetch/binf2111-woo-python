#! /usr/bin/env python

#open the FASTA file and start looping through lines
dnafile = "multiline-adapt.fna"

with open(dnafile) as fasta:
    name, DNASeq = None, []
    for line in fasta:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                tempdnaseq = (name+"/n"+''.join(DNASeq)) #join sequences in a temp variable (to use .find)

                if tempdnaseq.find("TACGTACG") < 0: #If it doesn't find an adapter
                    print("Adapter not found")
                elif tempdnaseq.find("TACGTACG") <= 10: #If adapter start in the first 10
                    print(tempdnaseq.strip())
                else:
                    if not len(tempdnaseq[tempdnaseq.find("TACGTACG"):len(tempdnaseq)-1]) >= 50: #If not enough trailing sequence
                        print("Too short after trimming")
                    else:
                        print(tempdnaseq[tempdnaseq.find("TACGTACG"):len(tempdnaseq)-1]) #if finds adapter, and enough trailing
            name=line
            DNASeq = []
        else:
            DNASeq.append(line)

    print(''.join(DNASeq)) #catches the last sequence (which would have printed anyway)
