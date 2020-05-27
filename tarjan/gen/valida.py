#!/usr/bin/env python2

from limiti import *

from sys import argv, exit, stderr
import os

def usage():
    print >> stderr, "Usage: %s file_input.txt" % \
        os.path.basename(argv[0])
    exit(1)

def run(f):
    assert(len(f) >= 1)
    prima = [int(x) for x in f[0].split()]
    assert(len(prima) == 2)
    N, M = prima
    assert(1 <= N and N <= MAXN)
    assert(1 <= M and M <= MAXM)
    for i in xrange(M):
        riga = [int(x) for x in f[i+1].split()]
        assert(len(riga) == 2)
        a, b = riga
        assert(1 <= a and a <= MAXN)
        assert(1 <= b and b <= MAXN)
    return 0 # Input corretto

if __name__ == "__main__":
    if len(argv) < 2:
        usage()

    f = open(argv[1]).readlines()
    exit(run(f))


