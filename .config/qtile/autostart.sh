#!/bin/sh

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom -b --experimental-backends &
volumeicon &
/usr/bin/emacs --daemon &
nitrogen --restore
