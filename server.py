import socket
import time
import numpy as np
##> Raspberry Pi.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET = ipv4, SOCK_STREAM = TCP (streaming socket)
s.bind((socket.gethostname(), 1999))
s.listen(5)
clientsocket, address = s.accept()
print(f"Connection from {address} has been established")
i = 0

while True:
    time.sleep(2)
    clientsocket.send(bytes(f"{np.random.randint(0, 9) < 5}", "utf-8"))### modified in the raspian