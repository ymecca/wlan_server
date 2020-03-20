import os
import subprocess as sp
import time
import WLAN_JSON_MYSQL

def WLAN_MOVE_FILE():
    try:
        print("\n\n###################################################\n\nO) MOVING JSON FILE TO DATABASE FOLDER")
        sp.getoutput('mv -f /home/devnet/wlan_sensor/client/DATABASE.json /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

    except:
        time.sleep(1)
        print('----FAILED TO MOVE JSON FILE SKIPPING')
	  
def WLAN_DELETE_FILE():
    try:
        print("O) DELETING JSON FILE")
        sp.getoutput('rm -rf /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

    except:
        time.sleep(1)
        print('----FAILED TO DELETE JSON FILE, SKIPPING') 
		
		
def WLAN_IMPORT_FILE():		

    
    print("O) TRYING TO IMPORT NEW JSON FILE TO THE DATABASE")

    try:
       WLAN_JSON_MYSQL.WLAN_MYSQL()
       print('----SUCCESS TO IMPORT')
       WLAN_DELETE_FILE()

    except:
       print('----FAILED TO IMPORT. SKIPPING')
       time.sleep(1)


if __name__ == '__main__':

  while True:

    WLAN_MOVE_FILE()
    WLAN_IMPORT_FILE()
    print("O) COUNTING DOWN 10 SECONDS\n\n###################################################")
    time.sleep(10)

