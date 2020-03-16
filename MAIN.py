import os
import subprocess as sp
print("Copying JSON FILE TO DATABASE FOLDER")
sp.getoutput('mv -f /home/devnet/wlan_sensor/client/*.json /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

import time
import WLAN_JSON_MYSQL

while True:


    print("IMPORT NEW JSON FILE TO THE DATABASE")
    WLAN_JSON_MYSQL.WLAN_MYSQL()
    print("Deleting JSON FILE")
    sp.getoutput('rm -rf /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')
    print("Counting down 70 seconds")
    time.sleep(70)
    print("Copying JSON FILE TO DATABASE FOLDER")
    sp.getoutput('mv -f /home/devnet/wlan_sensor/client/*.json /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')
