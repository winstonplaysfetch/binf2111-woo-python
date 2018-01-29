#!usr/bin/env python

#Get a DNA sequence from the user
userdna = raw_input("Enter DNA sequence: ")

#Calculate and print the length of the sequence
print("Length of sequence: " + str(len(userdna.strip())))

# count Gs and Cs
gccount = userdna.count("C") + userdna.count("G")

# compute GC percentage
seqlen = len(userdna.strip())

gcpercent = 10*(float(gccount)/float(seqlen))
print("The percent of Gs and Cs is: " + str(gcpercent))
