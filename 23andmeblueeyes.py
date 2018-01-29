#! /usr/bin/env python

blueeyepanel = "blueeyepanel.txt" #change this file to required panel
blueeyetest = "blueeye-23andMe.txt" #change this file to compare a person's 23 and me

print "This script compares a 23-and-me file to the panel for blue eyes. Results below: "

#open template file, store contents in panel
#Given file format: GG, rs123456, blue eyes
with open(blueeyepanel) as blueeyefile:
    panel = {}
    for line in blueeyefile:
        panel_lines = line.split(", ")
        if "BEH" in panel_lines[2]:
            panel[panel_lines[1]] = panel_lines[0]
    #un-comment below to show the panel dictionary
    #print panel

#open file to compare to, store contents in file
#Given file format: #rsid chromosome position genotype\n rs4778138 15 28335820 GG
with open(blueeyetest) as bluefile:
    file = {}
    for line in bluefile:
        if line.startswith("#"):
            pass
        else:
            file_lines = line.split()
            file[file_lines[0]] = file_lines[3]
    #un-comment below to show the 23-and-me file dictionary
    #print file

#find corresponding IDs in comparison file, match genes for those IDs, count and print results.
count = 0
for key in panel:
    for key2 in file:
        if key in key2: #IDs match
            print "Your " + panel_lines[2].rstrip("\n") + " genotype is: "
            if panel[key] in file[key2]: #if genes match
                print file[key2]
                count += 1
                print "This allele is positive for the blue eye genotype."
            else:
                print "This allele is negative for the blue eye genotype."
print "Total matching alleles: " + str(count)












