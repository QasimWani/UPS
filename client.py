import socket
###> Local Machine
#True/False = 1 * 1sec * 86400 = 86.4K. But for excess space: 100K
MAX_SIZE = 100000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET = ipv4, SOCK_STREAM = TCP (streaming socket)
s.connect((socket.gethostname(), 1999)) # later on, change hostname param to this machine's IP
while True:
    msg = s.recv(MAX_SIZE) #buffer byte-stream, decoded later
    print(msg.decode("utf-8"))