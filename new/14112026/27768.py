from ipaddress import *

net = ip_network('172.16.160.0/255.255.240.0')

k = 0
for ip in net:
    if f'{int(ip):b}'.count('1') % 2 == 0:
        k += 1

print(k)