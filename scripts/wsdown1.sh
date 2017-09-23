current=`xdotool get_desktop`
next=$(($current-1))
xdotool set_desktop $next
