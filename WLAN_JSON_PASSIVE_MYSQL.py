import pymysql, os, json, time

def WLAN_VALIDATE(val):
       if val != None:
            if type(val) is int:
                #for x in val:
            #   print(x)
                return str(val).encode('utf-8')
            else:
                return val


def WLAN_MYSQL():
       file = "/home/devnet/wlan_sensor/server/DATABASE/DATABASE_PASSIVE.json"
       json_data=open(file).read()
       WLAN_JSON_OBJ = json.loads(json_data)
       con = pymysql.connect(host = 'localhost',user = 'grafana',passwd = 'grafana',db = 'WLAN_SENSOR')
       cursor = con.cursor()

       # parse json data to SQL insert

       for i, item in enumerate(WLAN_JSON_OBJ):
           ID = WLAN_VALIDATE(item.get("WLAN_ID", None))
           TIME = WLAN_VALIDATE(item.get("WLAN_TIME", None))
           MAC = WLAN_VALIDATE(item.get("WLAN_HARDWARE_MAC", None))	
           IPV4 = WLAN_VALIDATE(item.get("WLAN_IPV4", None))	
           DATARATE= WLAN_VALIDATE(item.get("WLAN_RATE(Mbps)", None))	
           RX_SIGNAL = WLAN_VALIDATE(item.get("WLAN_SIGNAL(dBm)", None))
           TX_POWER = WLAN_VALIDATE(item.get("WLAN_TX_POWER(dBm)", None))	
           RETRIES = WLAN_VALIDATE(item.get("WLAN_RETRIES", None))	

           cursor.execute("INSERT INTO WLAN_SENSOR_PASSIVE (ID, TIME, MAC, IPV4, DATARATE, RX_SIGNAL, TX_POWER, RETRIES) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )", (ID, TIME, MAC, IPV4, DATARATE, RX_SIGNAL, TX_POWER, RETRIES))

       con.commit()
       con.close()


if __name__ == '__main__':
    WLAN_MYSQL()

