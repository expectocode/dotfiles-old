#!/bin/bash
pamixer="/home/username/src/pamixer/pamixer"

VOLUME=$($pamixer --get-volume)
MUTE=$($pamixer --get-mute)
if [ "$MUTE" == "false" ]; then
  $pamixer --decrease 5
else
  $pamixer --decrease 5
fi
  VOLUME=$($pamixer --get-volume)
  volnoti-show $VOLUME
  mplayer /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga
