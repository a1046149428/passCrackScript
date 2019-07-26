#!/usr/bin/env python2
import os
import sys


def doCheck(password, crack_file):
    x = os.system('7z e {0} -p{1}'.format(crack_file, password))
    if x == 0:
        print('[~] Password is : {0}\n\n'.format(password))
        exit(1)


for n in range(1000000):
    doCheck(n, sys.argv[1])
print('[!] Password not found in the provided list!\n\n')
