#! /usr/bin/env python

import subprocess

inputfile = 'test.txt'
outputfile = 'popen_output.txt'

cmd1 = ['cut', '-f', '1,2,5'] #cannot have whitespaces inside ''
cmd2 = ['cut', '-f', '3']

c1 = subprocess.Popen(cmd1, stdin=open(inputfile, 'r'), stdout=subprocess.PIPE)
c2 = subprocess.Popen(cmd2, stdin=c1.stdout, stdout=subprocess.PIPE)
print ("Types of robots that hold things: ")
for line in iter(c2.stdout.readline, ''):
    print line.strip() + " holder robot"
c1.stdout.close()
c2.communicate()