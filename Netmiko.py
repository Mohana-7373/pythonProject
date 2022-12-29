from netmiko import ConnectHandler
'''
Router={
    "device_type": "cisco_ios",

    "ip":"sandbox-iosxe-latest-1.cisco.com",
   # "ip":"sandbox-iosxe-recomm-1.cisco.com",
    "port":22,#netkon--32,,SSH-port 223
    "username":"developer",
    "password":"C1sco12345"
}'''
with open('devices.txt') as  routers:
    for IP in routers:
        Router={
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            # "ip":"sandbox-iosxe-recomm-1.cisco.com",
            #"port": 22,  # netkon--32,,SSH-port 223
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**Router)
        print('Connecting to '+IP)
        print('-'*75)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*73)
net_connect.disconnect()#finally close the connection
