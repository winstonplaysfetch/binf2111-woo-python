#! /usr/bin/env python

def windowfunction(dna, window_size):
    n = window_size
    for i in range(len(dna)):  # calculate start and stop
        start = max(0, i - n)
        stop = min(len(dna), i + n) + 1
        window = dna[start:stop]
        print window

windowfunction("AATTGGCC", 3)
