from ipaddress import *

net = ip_network('111.222.0.124/255.255.224.0', False)

for ip in net:
    if (f'{int(ip):b}'.count('1') * f'{int(ip):b}'.count('0')) % 2 == 0:
        print(ip)