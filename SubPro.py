import socket
import subprocess
import sys
from datetime import datetime

#subprocess.call('clear', shell=True)
remoteServer = input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)
print("-"*60)
print("please wait, scanning remote host", remoteServerIP)
print("-"*60)
t1 = datetime.now()
print(t1)
try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result==0:
            print("Port {}: open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("You Pressed Cntrl+C")
    sys.exit()
except socket.gaierror:
    print("Host name could not be resolved.Exiting ")
    sys.exit()
except socket.error:
    print("Couldn't connect to Server")
    sys.exit()