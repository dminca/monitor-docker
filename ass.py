#!/usr/bin/env python3.5
# Helper script during project development
import subprocess
import sys

# remove the contents of data/*
data_dir = "data/*"

def rmv():
    cmdping = "sudo rm -rfv " + data_dir
    p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()

def remove_containers():
    rmv_containers = "docker compose down -v --remove-orphans"
    p = subprocess.Popen(rmv_containers, shell=True, stderr=subprocess.PIPE)
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()

if sys.argv[1] == 'rf':
    rmv()
elif sys.argv[1] == 'down':
    #print(sys.argv)
    remove_containers()
else:
    exit()
