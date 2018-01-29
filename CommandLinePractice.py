#! /usr/bin/env python

# test in terminal: "python CommandLinePractice.py -a ATGCATCG -b BC30 -e -33 -l 289 -p 50 -s ATG -S ATT -t 20"

import sys #[file name, arg1, arg2, arg3] Expects three arguments: FASTA file, GFF file and VCF file
import getopt #getopt.getopt(args, options[, long_options])
import argparse

#Example of sys.argv
print("Start sys.argv test:")
print("Argument List: ")
str(sys.argv[1:3])
print("fastx_clipper -v -Q " + str(sys.argv[1]) + ' -a ' + str(sys.argv[2]) + ' -i ' + str(sys.argv[3]) + ' .fastq -o ' + str(sys.argv[3]) + ' clipTrP1.fastq')
print("ARGV: ", sys.argv[1])

#Example of getopt
print("\n\n Start getopt test")
enc = "33"
thresh = "20"
percent = "50"

options, remainder = getopt.getopt(sys.argv[1:], 'a:b:e:l:p:s:S:t: ', ['adapter=', 'base=', 'enc=', 'length=', 'percent=', 'start=', 'stop=', 'thresh='])
print("Options: ", options)

for opt, arg in options:
    if opt in ('-a', '--adapter'):
        adapter = arg
        print("Adapter: ", adapter)
    elif opt in ('-b', '--base'):
        base = arg
        print("File base name: ", base)
    elif opt in ('-e', '--enc'):
        enc = arg
        print("Q-Score Encoding: ", enc)
    elif opt in ('-l', '--length'):
        length = arg
        print("Min Length: ", length)
    elif opt in ('-p', '--percent'):
        percent = arg
        print("Percent: ", percent)
    elif opt in ('-s', '--start'):
        start = arg
        print("Start: ", start)
    elif opt in ('-S', '--stop'):
        stop = arg
        print("Stop: ", stop)
    elif opt in ('-t', '--thresh'):
        thresh = arg
        print("Thresh: ", thresh)


#Example of argparse
print("\n\n Start argparse test")
parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('-a', '--adapter', required=True, action='store', help='adapter')
parser.add_argument('-b', '--base', required=True,action='store',help='filebasename')
parser.add_argument('-e', '--enc', required=True,action='store', type=int,help='quality encodings')
parser.add_argument('-l', '--length', required=True,action='store',help='min length')
parser.add_argument('-p', '--percent', required=True,action='store',help='percent')
parser.add_argument('-s', '--start', required=True,action='store',help='start')
parser.add_argument('-S', '--stop', required=True,action='store',help='stop')
parser.add_argument('-t', '--thresh', required=True,action='store',help='thresh')

args = parser.parse_args()

if args.adapter: print("flag adapter")
if args.base: print("flag base")
if args.enc: print("flag end")
if args.length: print("flag length")
if args.percent: print("flag percent")
if args.start: print("flag start")
if args.stop: print("flag stop")
if args.thresh: print("flag thresh")
