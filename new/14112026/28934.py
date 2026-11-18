from ipaddress import *

net = ip_network('191.89.109.206/255.255.224.0', False)

print(net[-2])