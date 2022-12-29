from getmac import get_mac_address as gma
print(gma())

import uuid
print(hex(uuid.getnode()))
print("The MAC address in formatted way is : ", end='')
print(':'.join(['{:02x}'.format((uuid.getnode()>>ele) & 0xff)
for ele in range(0,8*6,8)][::-1])) #negative indexing

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)