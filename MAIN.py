import os
import subprocess as sp
import time
import WLAN_JSON_MYSQL

def WLAN_MOVE_FILE():
    try:
        print("\n\n###################################################\n\nMOVING JSON FILE TO DATABASE FOLDER")
        sp.getoutput('mv -f /home/devnet/wlan_sensor/client/*.json /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

    except:
        time.sleep(1)
        print('----FAILED TO MOVE JSON FILE SKIPPING')
	  
def WLAN_DELETE_FILE():
    try:
        print("DELETING JSON FILE")
        sp.getoutput('rm -rf /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

    except:
        time.sleep(1)
        print('----FAILED TO DELETE JSON FILE, SKIPPING') 
		
		
def WLAN_IMPORT_FILE():		

    
    print("TRYING TO IMPORT NEW JSON FILE TO THE DATABASE")

    try:
       WLAN_JSON_MYSQL.WLAN_MYSQL()
       print('SUCCESS TO IMPORT, GOING TO COUNTING DOWN')

    except:
       print('----FAILED TO IMPORT. RESTARTING THE PROCESS')
       time.sleep(1)


if __name__ == '__main__':

  while True:

    WLAN_MOVE_FILE()
    WLAN_IMPORT_FILE()
    WLAN_DELETE_FILE()
    print("COUNTING DOWN 15 SECONDS\n\n###################################################")
    time.sleep(15)

