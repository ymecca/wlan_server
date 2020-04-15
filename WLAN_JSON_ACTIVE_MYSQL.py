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
       file = "/home/devnet/wlan_sensor/server/DATABASE/DATABASE_ACTIVE.json"
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
           DNS_UOL = WLAN_VALIDATE(item.get("WLAN_DNS_UOL", None))
           DNS_CISCO = WLAN_VALIDATE(item.get("WLAN_DNS_CISCO", None))
           DNS_BBC = WLAN_VALIDATE(item.get("WLAN_DNS_BBC", None))
           DNS_GOOGLE = WLAN_VALIDATE(item.get("WLAN_DNS_GOOGLE", None))
           ICMP_UOL = WLAN_VALIDATE(item.get("WLAN_ICMP_UOL", None))
           ICMP_CISCO = WLAN_VALIDATE(item.get("WLAN_ICMP_CISCO", None))
           ICMP_BBC = WLAN_VALIDATE(item.get("WLAN_ICMP_BBC", None))
           ICMP_GOOGLE = WLAN_VALIDATE(item.get("WLAN_ICMP_GOOGLE", None))
           HTTP_UOL = WLAN_VALIDATE(item.get("WLAN_HTTP_UOL", None))
           HTTP_CISCO = WLAN_VALIDATE(item.get("WLAN_HTTP_CISCO", None))
           HTTP_BBC = WLAN_VALIDATE(item.get("WLAN_HTTP_BBC", None))
           HTTP_GOOGLE = WLAN_VALIDATE(item.get("WLAN_HTTP_GOOGLE", None))
           DHCP_TIME = WLAN_VALIDATE(item.get("WLAN_DHCP_TIME", None))
           DHCP_STATUS = WLAN_VALIDATE(item.get("WLAN_DHCP_STATUS", None))
           IPERF_UP = WLAN_VALIDATE(item.get("WLAN_IPERF_UPLOAD", None))
           IPERF_DOWN = WLAN_VALIDATE(item.get("WLAN_IPERF_DOWNLOAD", None))
           SPEEDTEST_DOWN = WLAN_VALIDATE(item.get("WLAN_SPEEDTEST_DOWN", None))
           SPEEDTEST_UP = WLAN_VALIDATE(item.get("WLAN_SPEEDTEST_UP", None))
           SPEEDTEST_RTT = WLAN_VALIDATE(item.get("WLAN_SPEEDTEST_RTT", None))
		   
           cursor.execute("INSERT INTO WLAN_SENSOR_ACTIVE (ID, TIME, MAC, IPV4, IPERF_DOWN, IPERF_UP, DHCP_TIME, DHCP_STATUS, SPEEDTEST_DOWN, SPEEDTEST_UP, SPEEDTEST_RTT, ICMP_UOL, ICMP_GOOGLE, ICMP_CISCO, ICMP_BBC, DNS_UOL, DNS_GOOGLE, DNS_CISCO, DNS_BBC, HTTP_UOL, HTTP_CISCO, HTTP_GOOGLE, HTTP_BBC ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )", (ID, TIME, MAC, IPV4, IPERF_DOWN, IPERF_UP, DHCP_TIME, DHCP_STATUS, SPEEDTEST_DOWN, SPEEDTEST_UP, SPEEDTEST_RTT, ICMP_UOL, ICMP_GOOGLE, ICMP_CISCO, ICMP_BBC, DNS_UOL, DNS_GOOGLE, DNS_CISCO, DNS_BBC, HTTP_UOL, HTTP_CISCO, HTTP_GOOGLE, HTTP_BBC))

       con.commit()
       con.close()


if __name__ == '__main__':
    WLAN_MYSQL()

