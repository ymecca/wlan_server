import os
import subprocess as sp
import time
import WLAN_JSON_ACTIVE_MYSQL
import WLAN_JSON_PASSIVE_MYSQL

def WLAN_PASSIVE_MOVE_FILE():
    try:
        print("\n\n###################################################\n\nO) MOVING JSON FILE FROM PASSIVE COLLECT TO THE DATABASE FOLDER")
        sp.getoutput('mv -f /home/devnet/wlan_sensor/client/DATABASE_PASSIVE.json /home/devnet/wlan_sensor/server/DATABASE/DATABASE_PASSIVE.json')

    except:
        time.sleep(1)
        print('----FAILED TO MOVE JSON FILE SKIPPING')
	  
def WLAN_ACTIVE_MOVE_FILE():
    try:
        print("O) MOVING JSON FILE FROM ACTIVE COLLECT TO THE DATABASE FOLDER")
        sp.getoutput('mv -f /home/devnet/wlan_sensor/client/DATABASE_ACTIVE.json /home/devnet/wlan_sensor/server/DATABASE/DATABASE_ACTIVE.json')

    except:
        time.sleep(1)
        print('----FAILED TO MOVE JSON FILE SKIPPING')	  
		
def WLAN_IMPORT_PASSIVE_FILE():		

    
    print("O) TRYING TO IMPORT NEW JSON PASSIVE FILE TO THE DATABASE")

    try:
       WLAN_JSON_PASSIVE_MYSQL.WLAN_MYSQL()
       print('----SUCCESS TO IMPORT')
       WLAN_DELETE_PASSIVE_FILE()

    except:
       print('----FAILED TO IMPORT. SKIPPING')
       time.sleep(1)
	   
def WLAN_IMPORT_ACTIVE_FILE():		

    
    print("O) TRYING TO IMPORT NEW JSON ACTIVE FILE TO THE DATABASE")

    try:
       WLAN_WLAN_JSON_ACTIVE_MYSQL.WLAN_MYSQL()
       print('----SUCCESS TO IMPORT')
       WLAN_DELETE_ACTIVE_FILE()

    except:
       print('----FAILED TO IMPORT. SKIPPING')
       time.sleep(1)	   

def WLAN_DELETE_PASSIVE_FILE():
    try:
        print("O) DELETING JSON FILE")
        sp.getoutput('rm -rf /home/devnet/wlan_sensor/server/DATABASE/DATABASE.json')

    except:
        time.sleep(1)
        print('----FAILED TO DELETE JSON FILE, SKIPPING') 
		

if __name__ == '__main__':

  while True:
    WLAN_PASSIVE_MOVE_FILE()
    WLAN_ACTIVE_MOVE_FILE()
    WLAN_IMPORT_PASSIVE_FILE()
    WLAN_IMPORT_ACTIVE_FILE()
    print("O) COUNTING DOWN 10 SECONDS\n\n###################################################")
    time.sleep(10)

