import socket
import time

##> Raspberry Pi.
import RPi.GPIO as GPIO

#GPIO SETUP
sound = 17
global_sound = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)
GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime=100)  # let us know when the pin goes HIGH or LOW
def callback(sound):
        if GPIO.input(sound):
            print("Sound Detected!")
            global_sound = True
            
GPIO.add_event_callback(sound, callback)  # assign function to GPIO PIN, Run function on chang
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET = ipv4, SOCK_STREAM = TCP (streaming socket)
s.bind((socket.gethostname(), 1999))
s.listen(5)
clientsocket, address = s.accept()
print(f"Connection from {address} has been established")
i = 0

while True:
    time.sleep(2)
    clientsocket.send(bytes(f"{global_sound}", "utf-8"))### modified in the raspian

GPIO.cleanup()
