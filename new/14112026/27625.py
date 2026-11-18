from ipaddress import *

net = ip_network('172.16.96.0/255.255.224.0')


k = 0
for ip in net:
    if f'{int(ip):b}'.count('1') % 2 == 0:
        k += 1

print(k)