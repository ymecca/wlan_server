import os
import subprocess as sp
import time
import WLAN_JSON_MYSQL

def WLAN_MOVE_FILE():
    try:
        print("MOVING JSON FILE TO DATABASE FOLDER")
        sp.getoutput('mv -f /home/devnet/wlan_sensor/client/*.json /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

    except:
        time.sleep(1)
        WLAN_MOVE_FILE()
	  
def WLAN_DELETE_FILE():
    try:
        print("DELETING JSON FILE")
        sp.getoutput('rm -rf /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

    except:
        time.sleep(1)
        WLAN_DELETE_FILE()	  
		
		
def WLAN_IMPORT_FILE():		
    print("TRYING TO IMPORT NEW JSON FILE TO THE DATABASE")

    try:
        WLAN_JSON_MYSQL.WLAN_MYSQL()

    except:
        time.sleep(5)
        WLAN_IMPORT_FILE()

if __name__ == '__main__':

  while True:

    WLAN_MOVE_FILE()
    WLAN_IMPORT_FILE()
    WLAN_DELETE_FILE()
    print("Counting down 30 seconds")
    time.sleep(70)

