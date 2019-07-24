#!/usr/bin/env python2
import os
import sys


def traversingFolder(path, crack_file):
    files = os.listdir(path)
    for file in files:
        file = os.path.join(path, file)
        if os.path.isdir(file):
            if not os.listdir(file):
                continue
            else:
                traversingFolder(file, crack_file)
        else:
            doCheck(file, crack_file)


def doCheck(filepath, crack_file):
    lines = open(filepath, 'r').read().splitlines()

    for line in lines:
        x = os.system('7z e {0} -p{1}'.format(crack_file, line))
        if x == 0:
            print('[~] Password is : {0}\n\n'.format(line))
            exit(1)


traversingFolder(sys.argv[1], sys.argv[2])
print('[!] Password not found in the provided list!\n\n')
