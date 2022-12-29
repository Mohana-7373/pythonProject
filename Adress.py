import ifaddr
adapters = ifaddr.get_adapters()
for adapter in adapters:
    print("IP's of network adapter" + adapter.nice_name)
    for ip in adapter.ips:
        print("%s/%s"%(ip, ip.network_prefix))


import ifaddr
adapters = ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IPs of network adaptor"+ adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print("%s/%s" % (ip, ip.network_prefix))
    else:
        print("no ips configured")

print("\n")

import psutil
result1 = psutil.cpu_times()
print(result1)
print("\n")
result2 = psutil.cpu_stats()
print(result2)
print("\n")
result3 = psutil.cpu_freq()
print(result3)
print("\n")
result4 = psutil.disk_partitions()
print(result4)
print("\n")
result5 = psutil.net_io_counters(pernic=True)
print(result5)
print("\n")

import psutil
network_stats = psutil.net_io_counters(pernic=False)
bytes_sent = getattr(network_stats, 'bytes_sent')
bytes_recv = getattr(network_stats, 'bytes_recv')
print("Bytes Sent = {0} | Bytes Recived = {1}".format(bytes_sent,bytes_recv))
