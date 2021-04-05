#!/bin/sh

/opt/brave.com/brave/brave &
spotify &
/home/erhelito/applications/thunderbird/thunderbird &
sleep 30 && killall main.py && killall python
