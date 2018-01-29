#!usr/bin/env python

DNASeq = raw_input("Enter sequence: ")

if len(DNASeq.strip()) >= 50:
        if DNASeq.find("TACGTACG") < 0:
            print("Adapter not found")
        elif DNASeq.find("TACGTACG") < 10:
            print(DNASeq.strip())
        else:
            if not len(DNASeq[DNASeq.find("TACGTACG"):len(DNASeq)-1]) >= 50:
                print("Too short after trimming")
            else:
                print(DNASeq[DNASeq.find("TACGTACG"):len(DNASeq)-1])
else:
    print("Too short before trimming")
