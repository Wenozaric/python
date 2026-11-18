from ipaddress import *

net = ip_network('185.249.55.138/255.255.192.0', False)

print(net[-1])