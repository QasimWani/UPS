import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET = ipv4, SOCK_STREAM = TCP (streaming socket)
s.connect((socket.getHostname(), 2718)) # later on, change hostname param to this machine's IP
msg = s.recv(1024) #buffer byte-stream, decoded later
print(msg.decode("utf-8"))