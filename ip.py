import os,ipaddress

os.system('cls') #os.system will clear the console at the start of the execution

while True:
    ip = input('Enter IP Addresss:')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Vaild')
    except:
        print('-'*50)
        print('IP is Not Vaild')
    finally:
        if ip == 'mango':
            print('Script Finished')
            break

print(os.system("ipconfig"))
print("***********************************************")

import socket
s= socket.socket()
print("Socket Succesfully Created")
port = 40674
s.bind(('', port))
print("socket binded to %s" %(port))
s.listen(5)
print(("socket is listeninig"))
while True:
    c, addr = s.accept()
    print('Got connection From', addr)
    c.send(b'Thank you for connecting')
    c.close()

