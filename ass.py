#!/usr/bin/env python3.5
# Helper script during project development
import subprocess
import sys

# remove the contents of data/*
data_dir = "data/*"
cmdping = "sudo rm -rfv " + data_dir
p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
