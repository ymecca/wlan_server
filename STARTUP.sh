#!/bin/bash

source /home/devnet/environments/wlan_sensor/bin/activate
nohup python -u /home/devnet/wlan_sensor/server/MAIN.py > /home/devnet/wlan_sensor/server/LOG/LOGFILE.log &

