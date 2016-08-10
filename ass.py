#!/usr/bin/env python3
# Helper script during project development
import subprocess
import sys

data_dir = '/data/*'

def main(argv):
    subprocess.call('ls','-lsa', data_dir)


if __name__ == '__main__':
    main(sys.argv[1:])