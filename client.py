import socket
import datetime
import time
from playsound import playsound

###> Local Machine
#True/False = 1 * 1sec * 86400 = 86.4K. But for excess space: 100K
MAX_SIZE = 100000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET = ipv4, SOCK_STREAM = TCP (streaming socket)
s.connect(("172.16.64.29", 3141)) # later on, change hostname param to this machine's IP
iterator = 1
LAST_HEARD = datetime.datetime.now()
print("current date time: ", LAST_HEARD)
while True:
    time.sleep(1)
    msg = s.recv(MAX_SIZE) #buffer byte-stream, decoded later
    val = msg.decode("utf-8") == "True"
    if(val):
        print("Alert Played. Someone knocked!")
        playsound("alert.mp3")
        LAST_HEARD = datetime.datetime.now()
    else:
        i+= 1
        if(i%1800 == 0):
            i = 1
            print("last heard: ", LAST_HEARD)