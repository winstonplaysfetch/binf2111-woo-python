#!usr/bin/env python

#Get a DNA sequence from the user
print("This script will transcribe your DNA sequence")
userdna = raw_input("Enter DNA sequence: ")

#Replace A with T
newdna= userdna.replace("A","%temp%").replace("T","A").replace("%temp%","T")
#Replace G with C
transcripteddna = newdna.replace("G","%temp%").replace("C","G").replace("%temp%","C")

#print out transcribed sequence in reverse
print(str(transcripteddna[::-1]))