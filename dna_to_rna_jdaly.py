#!usr/bin/env python

#Get a DNA sequence from the user
userdna = raw_input("Enter DNA sequence: ")

#Calculate and print the length of the sequence
print("Length of sequence: " + str(len(userdna.strip())))

#Count number of "T" characters and print
print("Number of Thymine bases: " + str(userdna.count("T")))

#Convert the DNA sequence to RNA, store it and print it.
userrna = userdna.replace("T","U")
print("RNA sequence: " + userrna)





#for x in xrange(len(userdna),0):
#    print()
