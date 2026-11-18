from ipaddress import *

net = ip_network('46.29.170.214/255.255.128.0', False)

for ip in net:
    d = [int(x) for x in str(ip).split('.')]
    maxD = max(d)
    y = 0
    #print(ip)
    #print(maxD)
    for x in d:
        if x != maxD: y += x
    #print(y)
    if y == maxD: print(ip)