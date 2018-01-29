#!usr/bin/env python

#open file
with open("NC_007898.fna") as gcfile:
#open output file
    with open("newgcfile.txt", "a") as new_file:
#read by new line
        for line in gcfile.readlines():
#count gc if line starts with start codon
            if line.startswith(">"):
                print line
            elif line.startswith("ATG"):
#calculate
                gccount = line.count("C") + line.count("G")
                gcpercent = 10*(float(gccount)/float(len(line.strip())))
#print results
                print("The percent of Gs and Cs is: " + str(gcpercent))