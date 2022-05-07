import requests
import json

ip = input("IP: ")
if not ip.isdigit():
    print("请输入正确格式的IP！")
    exit(1)
username = input("UserName: ")
password = input("PassWord: ")

device = {
   "ip": f"{ip}",
   "username": f"{username}",
   "password": f"{password}",
   "port": "443",
}

headers = {
      "Accept" : "application/yang-data+json",
      "Content-Type" : "application/yang-data+json",
   }
module = "Cisco-IOS-XE-native:native/interface/GigabitEthernet=2"
url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, auth=(device['username'], device['password']), verify=False).json()
print(response)
print(response.status_code)

if (response.status_code == 204):
   print("Successfully deleted interface")
else:
   print("Issue with deleting interface")
