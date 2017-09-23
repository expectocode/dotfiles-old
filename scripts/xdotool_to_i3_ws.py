#!/usr/bin/env python3
import subprocess
import sys

#curdtop = subprocess.check_output('DISPLAY=:0 xdotool get_desktop',shell=True).decode().strip()
curdtop = int(sys.argv[1])

allWS = [w for w in subprocess.check_output('i3-msg -t get_workspaces | jq -r ".[].name"',subprocess.STDOUT,shell=True).decode().split('\n') if w != '']

if curdtop < 0 or curdtop >= len(allWS):
    exit()

print(allWS[curdtop])
