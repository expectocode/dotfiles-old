#!/usr/bin/env python3
import dbus
bus = dbus.SessionBus()
playrs = [b for b in bus.list_names() if b.startswith('org.mpris')]
player_ob = bus.get_object(playrs[0],'/org/mpris/MediaPlayer2')
player_ob.PlayPause(dbus_interface='org.mpris.MediaPlayer2.Player')
