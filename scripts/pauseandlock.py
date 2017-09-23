#!/usr/bin/env python3
import dbus
import subprocess

subprocess.run('/home/tanuj/scripts/lock.sh')

import argparse
parser = argparse.ArgumentParser('pause all mpris, lock, optional sleep')
parser.add_argument('-s','--sleep',required=False,action='store_true')

bus = dbus.SessionBus()
playrs = [b for b in bus.list_names() if b.startswith('org.mpris')]
player_obs = [bus.get_object(p,'/org/mpris/MediaPlayer2') for p in playrs]
for ob in player_obs:
    ob.Pause(dbus_interface='org.mpris.MediaPlayer2.Player')

if parser.parse_args().sleep:
    subprocess.run('sudo systemctl suspend',shell=True)
