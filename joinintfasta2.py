#!usr/bin/env python

dnafile = "multiline-adapt.fna"

def joinfasta(dnafile): #from generators1 slide
    names = []
    seqs = []
    name, seq = None, []
    for line in dnafile:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                name = line
                seq = []
                names.append(name)
                seqs.append(''.join(seq))
        else:
            seq.append(line)
    #names.append(name)
    #seqs.append(''.join(seq))
    return (names, seqs)

print joinfasta(dnafile)

'''
with open(dnafile) as fasta:
        name, seq = None, []
        for line in fasta:
            line = line.rstrip()
            if line.startswith(">"):
                if name:
                    print(name+"/n"+''.join(seq))
                name=line
                seq = []
            else:
                seq.append(line)
    return seq
'''