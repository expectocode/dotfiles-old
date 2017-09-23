#!/bin/bash

pamixer="/home/username/src/pamixer/pamixer"
$pamixer --toggle-mute
VOLUME=$($pamixer --get-volume)
MUTE=$($pamixer --get-mute)
#notify-send $MUTE
if [ "$MUTE" = "false" ]; then # lol does this actually matter
	mplayer /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga
	notify-send $VOLUME
	volnoti-show $VOLUME
else
	notify-send $VOLUME "(m)"
	volnoti-show -m $VOLUME
fi
