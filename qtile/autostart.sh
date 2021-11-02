#!/bin/sh

picom &
feh --bg-fill ~/.config/.wallpapers/wallpaper.jpg

# Network
nm-applet &
# Hardware
udiskie -t &
# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &

