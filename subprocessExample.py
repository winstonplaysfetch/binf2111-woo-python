#! /usr/bin/env python

import subprocess

#subprocess.call('ls','-l')

def callsomethings(fastqname):
    #Add extensions to fastqname
    fastqfile = fastqname + '.fastq'
    fastxclipOUT = fastqname + '.clipTrP1.fastq'
    fastxtrimOUT = fastqname + 'trim.fastq'
    fastqfilterOUT = fastqname + 'qualfilt.fastq'
    fastqtrimOUT = fastqname + 'qualtrim.fastq'

    print('fastx_clipper: ')
    subprocess.call(['fastx_clipper', '-v', '-Q33', '-a', 'CCTCTCTCGGGAGAGTCAGAT', fastqfile, '-o', fastxclipOUT])

    print('fastx_trimmer: ')
    subprocess.call(['fastq_quality_filter', '-v', 'Q33', '-f', 'g', '-l', '289', '-i', fastxclipOUT, '-o', fastxtrimOUT])

    print('Fastq_quality_filter: ')
    subprocess.call(['fastq_quality_trimmer', '-v', '-Q33', '-q', '20', '-p', '50', '-i', fastxtrimOUT, '-o', fastqfilterOUT])

    print('fastq_quality_trimmer')
    subprocess.call(['fastq_quality_trimmer', '-v', '-Q33', '-t', '20', '-l', '50', '-i', fastqfilterOUT, '-o', fastqtrimOUT])

    print('Finished processing')

    samfile = fastqname + '.sam'
    return samfile

#subprocess.call([bowtie2-build NC_007898.fasta NC_007898])
#subprocess.call([bowtie2 -S NC_007898 fastqtriOUT samfile])

print callsomethings("BC20")
print callsomethings("BC21")
