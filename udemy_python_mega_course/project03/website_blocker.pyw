#!/usr/bin/python
#
# File:   website_blocker.pyw
# Author: Renato Jensen Filho
# Email:  renatojen@gmail.com
#
# THIS SCRIPT REQUIRES ADMIN PRIVILEGES
import sys
import time
from datetime import datetime as dt

if len(sys.argv) < 3:
   print("\n#### Script Usage ####\npython website_blocker.py starting_hour finishing_hour\ni.e.:\npython website_blocker.py 9 18")
   sys.exit()

#r before the string: rawstring, i.e. \n doesn't work 
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" if sys.platform.startswith("win") else "/etc/hosts"
redirect="127.0.0.1"
blocked_urls=["www.facebook.com", "facebook.com"]

while True:   
   if dt(dt.now().year,dt.now().month, dt.now().day, int(sys.argv[1])) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day, int(sys.argv[2])):
      #print("Working Hours...")
      with open(hosts_path, 'r+') as file:
         content=file.read()
         for url in blocked_urls:
            if url in content:
               pass
            else:
               file.write(redirect + " " + url + "\n")
               
   else:
      #print("Fun Hours...")
      with open(hosts_path, 'r+') as file:
         content=file.readlines()
         file.seek(0)
         for line in content:
            if not any(url in line for url in blocked_urls):
               file.write(line)            
         file.truncate()            
   time.sleep(5)