#! /usr/bin/env python

import types

def fibanocci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

if type(fibanocci()) == types.GeneratorType:
    print "Yep that's a generator"

counter = 0
for n in fibanocci():
    print n
    counter += 1
    if counter == 10:
        break