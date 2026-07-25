import ipaddress

def runTest(myValue, mustValue, issue):
    if myValue == mustValue: print(f"-- {issue} -- Ответ одинаковый, равен {myValue} ✅")
    else: print(f"-- {issue} -- Ответ неверный, равен {myValue}, должен {mustValue} ❌")

def a9135():
    net = ipaddress.ip_network('154.141.198.190/255.255.192.0', strict=False)
    ipByted = [f'{byte:08b}' for byte in net[-1].packed]

    return sum(int(byte, 2) for byte in ipByted)

def a9134():
    net = ipaddress.ip_network('64.237.228.143/255.255.248.0', strict=False)
    ipByted = [f'{byte:08b}' for byte in net[0].packed]

    return sum(int(byte, 2) for byte in ipByted)

def a9133():
    net = ipaddress.ip_network('185.249.55.138/255.255.192.0', strict=False)
    ipByted = [f'{byte:08b}' for byte in net[-1].packed]

    return sum(int(byte, 2) for byte in ipByted)

def a9132():
    net = ipaddress.ip_network('189.163.226.71/255.255.255.240', strict=False)
    ipByted = [f'{byte:08b}' for byte in net[0].packed]

    return sum(int(byte, 2) for byte in ipByted)

runTest(a9135(), 805, 9135)
runTest(a9134(), 525, 9134)
runTest(a9133(), 752, 9133)
runTest(a9132(), 642, 9132)