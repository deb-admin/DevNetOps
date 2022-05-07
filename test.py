import requests
import json
from pprint import pprint

device = {
   "ip": "$1",
   "username": "$2",
   "password": "$2",
   "port": "9443",
}

headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
   }

module = "ietf-interfaces:interfaces"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"

payload = {
   "interface": [
    {
      "name": "Loopback10000",
      "description": "Adding loopback10000",
      "type": "iana-if-type:softwareLoopback",
      "enabled": "true",
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.0.2.60",
            "netmask": "255.255.255.255"
          }
        ]
      }
    }
  ]
 }
requests.packages.urllib3.disable_warnings()
response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(device['username'], device['password']), verify=False)

if (response.status_code == 201):
   print("Successfully added interface")
else:
   print("Issue with adding interface")
