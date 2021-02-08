#Modules 
import socket 
from colorama import init, Fore
import time
import os
import sys
#Coded By T.me/Sadult | Github.com/Sadult
# Colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
# Code
os.system('clear')
print('''
   _____           _       _ _   
  / ____|         | |     | | |  
 | (___   __ _  __| |_   _| | |_ 
  \___ \ / _` |/ _` | | | | | __|
  ____) | (_| | (_| | |_| | | |_ 
 |_____/ \__,_|\__,_|\__,_|_|\__|
                                 
                                 

''') 
time.sleep(2.1)
os.system('clear')
os.system('neofetch')
time.sleep(4.1)
os.system('clear')
print(f'''{GREEN}
_____           _      _____                                 
|  __ \         | |    / ____|                                
| |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
|  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|        
''')
print(f'''{GRAY}
               [!] Coded By :
                  [+] mercads.ir
                  [+] github.com/sadult
                  [+] t.me/sadult
''')
print(f'''{GRAY}
               [!] V 1.1
               [!] This script scans from port 1 to 9999, you can customize its values in line 64.
''')
print("               -----------------------------------------------------------------------------")         
def is_port_open(host, port):
    # creates a new socket
    s = socket.socket()
    try:
        s.connect((host, port))
        s.settimeout(0.2)
    except:
        return False
    else:
        # the connection was established, port is open!
        return True
# get the host from the user
host = input("Enter the host:")
# iterate over ports, from 1 to 14444
for port in range(1, 9999):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
		
print("END")
