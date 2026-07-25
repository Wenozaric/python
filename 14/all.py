def runTest(myValue, mustValue, issue):
    if myValue == mustValue: print(f"-- {issue} -- Ответ одинаковый, равен {myValue} ✅")
    else: print(f"-- {issue} -- Ответ неверный, равен {myValue}, должен {mustValue} ❌")


#"0123456789ABCDEF"                      16
#"0123456789ABCDEFGHIJ"                  20
#"0123456789ABCDEFGHIJKLMNO"             25
#"0123456789ABCDEFGHIJKLMNOPQRST"        30

def a9143():
    last = 0
    for x in '0123456789ABCDEFGHIJKL':
        s = int(f"27{x}98966", 22) + int(f"26{x}33", 22) + int(f"522{x}5", 22)
        if s % 21 == 0:
            last = s // 21

    return last

def a9142():
    last = 0
    for x in "0123456789ABCDEFGHI":
        s = int(f"76{x}79645", 19) + int(f"35{x}42", 19) + int(f"332{x}6", 19)
        if s % 18 == 0:
            last = s // 18

    return last


runTest(a9143(), 279710450, 9143)
runTest(a9142(), 365875995, 9142)