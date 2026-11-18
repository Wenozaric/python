from ipaddress import *

net = ip_network('189.163.226.71/255.255.255.240', False)

print(net[0])