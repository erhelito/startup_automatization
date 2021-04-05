#!/bin/sh

###        info :        ###
### here, you put all the application's path you want to launch at your computer's startup ###

/opt/brave.com/brave/brave &
spotify &
/home/erhelito/applications/thunderbird/thunderbird &




sleep 30 && killall main.py && killall python
