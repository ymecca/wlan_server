import pymysql, os, json

# read JSON file which is in the next parent folder
file = "/home/devnet/wlan_sensor/server/DATABASE/DATABASE.json"
json_data=open(file).read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host = 'localhost',user = 'grafana',passwd = 'grafana',db = 'WLAN_SENSOR')
cursor = con.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    TIME = validate_string(item.get("WLAN_TIME", None))
    MAC = validate_string(item.get("WLAN_HARDWARE_MAC", None))	
    IPV4 = validate_string(item.get("WLAN_IPV4", None))	
    DATARATE= validate_string(item.get("WLAN_RATE(Mbps)", None))	
    RX_SIGNAL = validate_string(item.get("WLAN_SIGNAL(dBm)", None))
    TX_POWER = validate_string(item.get("WLAN_TX_POWER(dBm)", None))	


    cursor.execute("INSERT INTO SENSOR_CLIENT (TIME, MAC, IPV4, DATARATE, RX_SIGNAL, TX_POWER) VALUES (%s, %s, %s, %s, %s, %s )", (TIME, MAC, IPV4, DATARATE, RX_SIGNAL, TX_POWER))

con.commit()
con.close()
