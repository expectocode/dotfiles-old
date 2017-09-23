current=`xdotool get_desktop`
next=$(($current+1))
#silent error if too far
i3next=$(~/scripts/xdotool_to_i3_ws.py $next)
i3-msg 'move container to workspace '$i3next
xdotool set_desktop $next
