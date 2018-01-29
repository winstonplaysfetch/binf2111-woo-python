#! /usr/bin/env python

#Open a plastid DNA file and join the lines (this is a genome, so, single sequence)
genomefile = open("NC_007898.fasta")

#Create a list
seq =[]

#Append each sequence line to the
for line in genomefile:
    line = line.strip()
    if line.startswith(">"):
        pass
    else:
        seq.append(line)

#Join the list
wholejoin = ''.join(seq)
genomefile.close()

#Define a restriction site pattern
rfrags = wholejoin.split("CTGCAG")
rfrags[0] = rfrags[-1] + rfrags[0]
del rfrags[-1]

#Print each fragment with its own FASTA header line
for i in range(0, len(rfrags)):
    print "> Fragment " + str(i+1) + ": " + str(len(rfrags[i])) + " nucleotides.\n"
    print rfrags[i]


#alternative script
#frags = []
#while fullseq.find("CTGCAG") > 0:
#    frag_end = fullseq.find("CTGCAG") + 5
#    rfrag = fullseq]0:frag_end]
#    frag_start =fullseq.find("CTGCAG") + 5
#    fullseq = fullseq]frag_start:len(fullseq) - 1]
#    frags.append(rfrag)

#frags.append(rfrag)
#frags[0] = frags[-1] + frags[0]
#del frags[-1]

#challenge
#with open("NC_007898.fasta", "w") as outfile:
#    for i in range(0, len(frags)):
#        outfile.write("> Fragment " + str(i + 1) + ": " + str(len(frags[i])) + "nucleotides.\n")
#        numlines = len(frags[i]) /80
#        if (len(frags[i]) % 80 != 0):
#            numlines += 1
#        for j in range(0,numlines):
#            outfile.write(frags[i] [80*j:80*(j+1)-1] + "\n")

