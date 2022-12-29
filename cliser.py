

import socket
s = socket.socket()
port = 40674
s.connect(('127.0.0.1', port))
print(s.recv(1024))
s.close()

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

from netmiko import ConnectHandler
CSR = {
   # "device_type":"cisco_ios",
    "device_type":"juniper junos",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "port": 22,
    "username":"developer",
    "password":"C1sco12345"
}
net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show ip int')
print(output)
output = net_connect.send_command('show ip int brief')
print(output)
output_clock = net_connect.send_command('show clock')
print(output_clock)
output_routes = net_connect.send_command('show ip ro')
print(output_routes)
output_runconfig = net_connect.send_command('show run')
print(output_runconfig)

net_connect.disconnect()
