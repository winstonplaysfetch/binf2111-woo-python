#! /usr/bin/env python

import random

def lottery():
    for i in xrange(6):
        yield random.randint(1,40)

    yield random.randint(1,15)

for random_number in lottery():
    print "Next lottery number: %d" %random_number
