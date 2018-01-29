#! /usr/bin/env python

from itertools import islice

def sliding_window(dna, n=8): #yields a window of 8 characters from a string
    it = iter(dna)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def read_fastq(fastq): #Reads in information from a fastq file, yields 3 strings
    name, seq, qual = [None], [None], [None]
    for i, line in enumerate(fastq):
        line = line.strip()
        if i % 4 == 0: #set name (description)
            name = line
        elif i % 4 == 1: #set sequence
            seq = line
        elif i % 4 == 3: #set what's going to be used to determine the quality of sequence
            qual = line
            yield name,seq,qual
            name, seq, qual = [None], [None], [None]
        else:
            pass #for when I enter line 2(name 2) out of [0,1,2,3,4]


def quality(qualstring): #Reads in a string of unicode characters and gives them each a numerical value
    quals = [ord(char) - 33 for char in qualstring]
    return quals


#******************************************MAIN*************************************
print "FASTAQ Filter by Jennifer Daly"
print "\nName"
print "Sequence"
print "Quality\n"

'''
#Test sliding_window functionality
slidingwindow = sliding_window("AAATTTGGGCCCAAATTTGGGCCC", 5)
print next(slidingwindow)
print next(slidingwindow)
print next(slidingwindow)
print next(slidingwindow)
'''

#Initialize some things
infile = "BC_30.fastq"
counter = 0 #counter to stop script from reading the entire file, to change edit lines 71, 78, 83
with open(infile) as infastq:
    for iname,iseq,iqual in read_fastq(infastq):
        #Declare some variables
        readlength = iname.split()[2]
        qualities = quality(iqual)
        avgqual = sum(qualities) / len(qualities)
        counter += 1

        if int(readlength.split('=')[1]) >= 50 and avgqual >= 20: #if length > 50 and quality of entire length >=20
            qualitylist = []
            print iname
            print iseq
            for window in sliding_window(iqual): #Calculate a sliding quality
                thequality = quality(window)
                if thequality <= 18:
                    pass #(skip and call next window, because that's bad quality)
                else:
                    qualitylist.append(sum(thequality) /8)
                    if counter > 20:
                        break
            print qualitylist

        elif int(readlength.split('=')[1]) >= 50 and avgqual < 20: #If sequence is long enough but is bad quality
            print iname
            print "Low quality sequence"
            if counter > 20:
                break
        elif int(readlength.split('=')[1]) < 50: #If sequence is not long enough
            print iname
            print "Sequence is too short"
            if counter > 20:
                break
        else:
            print "I'm a stupid script because I skipped a sequence for no reason."
            print counter



