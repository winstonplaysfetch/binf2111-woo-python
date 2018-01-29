#! /usr/bin/env python

import subprocess
from itertools import islice

fastqfile = "BC20_BINF6350_Summer2014_13pm.fastq"

#The commands I want
cmd1 = ['fastx_clipper', '-v', '-Q33', '-a', 'CCTCTCTCGGGAGAGTCAGAT']
cmd2 = ['fastx_trimmer', 'Q33', '-f', '9', '-l', '289']
cmd3 = ['fastq_quality_filter', '-Q33', '-q', '20', '-p', '50']
# fastq_quality_trimmer will call that program. (also swap line 105)
#cmd4 = [] #['fastq_quality_trimmer', '-Q33', '-t', '20', '-l', '50']

#popen commands
print('running fastx_clipper\n')
c1 = subprocess.Popen(cmd1, stdin=open(fastqfile, 'r'), stdout=subprocess.PIPE)

print('running fastx_trimmer\n')
c2 = subprocess.Popen(cmd2, stdin=c1.stdout, stdout=subprocess.PIPE)

#print('running fastq_quality_filter')
#c3 = subprocess.Popen(cmd3, stdin=c2.stdout, stdout=subprocess.PIPE)

#print('running fastq quality trimmer')
#c4 = subprocess.Popen(cmd4, stdin=c3.stdout, stdout=open(fastqOUT, 'w'))

#**************************************************Functions********************************************
def quality(qualstring): #Reads in a string of unicode characters and gives them each a numerical value
    quals = [ord(char) - 33 for char in qualstring]
    return quals

def sliding_window(dna, n=8): #yields a window of 8 characters from a string
    it = iter(dna)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def read_fastq(cmd3):
    print('running fastq_quality_filter\n')
    c3 = subprocess.Popen(cmd3, stdin=c2.stdout, stdout=subprocess.PIPE)
    name, seq, qual = [None], [None], [None]

    print "FASTAQ Filter by Jennifer Daly"
    print "\nName"
    print "Sequence"
    print "Quality\n"

    #Iterable for fastq_trimmer
    for i, line in enumerate(iter(c3.stdout.readline, '')):
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

#**********************************************MAIN*******************************************************
counter = 0
for iname,iseq,iqual in read_fastq(cmd3):
    #Declare some variables
    readlength = int(iname.split(":")[2]) - int(iname.split(":")[1])
    qualities = quality(iqual)
    avgqual = sum(qualities) / len(qualities)
    counter += 1

    if readlength >= 50 and avgqual >= 20: #if length > 50 and quality of entire length >=20
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

    elif readlength >= 50 and avgqual < 20: #If sequence is long enough but is bad quality
        print iname
        print "Low quality sequence"
        if counter > 20:
            break
    elif readlength < 50: #If sequence is not long enough
        print iname
        print "Sequence is too short"
        if counter > 20:
            break
    else:
        print "I'm a stupid script because I skipped a sequence for no reason."
        print counter

#Using subprocess
c1.stdout.close()
c2.communicate()
c2.stdout.close()



