#!/bin/bash

killall python
killall iperf3

source /home/devnet/environments/wlan_sensor/bin/activate
sudo mysqld &
nohup python -u /home/devnet/wlan_sensor/server/MAIN.py > /home/devnet/wlan_sensor/server/LOG/LOGFILE.log &
nohup iperf3 -s -D &

