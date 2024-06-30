#!/bin/bash

icon() {
	echo -n "+@fg=1;$1+@fg=0;"
}

percentage() {
	current=`echo $1 | sed 's/%//'`
	if [$current -le 25 ]; then
		echo -n "$(icon $2)"
	elif [$current -le 50 ]; then
		echo -n "$(icon $3)"
	elif [$current -le 75 ]; then
		echo -n "$(icon $4)"
	else
		echo -n "$(icon $5)"
	fi
}

sleep_sec=2
i=0

while :; do
	# Volume
	vol=`pamixer --get-volume`
	if [[ `pamixer --get-mute` == "true" ]]; then
		echo -n "$(icon 󰝟 ) $vol% "
	else
		echo -n "$(icon 󰕾 ) $vol% "
	fi

	# Battery
	if (( $i % 60 == 0 )); then
		bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT0 |
			grep percentage |
			sed 's/ *percentage: *//g'`

		state=`upower -i /org/freedesktop/UPower/devices/battery_BAT0 |
			grep state |
			sed 's/ state: *//'`
	fi
	if [ $state == "charging" -o $state == "fully-charged" ]; then
		echo -n "$(icon 󰁹 ) "
	else 
		echo -n "$(percentage $bat 󰁻  󰁾  󰂀  󰂂 ) "
	fi
	echo -n "$bat "

	# Date
	if (( $i % 60 == 0 )); then
		dte="$(date +"$(icon 󰸘 ) %d/%m/%Y $(icon 󱑍 ) %H:%M")"
	fi
	echo -e "$dte"

		sleep $sleep_sec
	if [[ $i -eq 240 ]]; then
		i = 0
	else
		((i += $sleep_sec))
	fi

done	
