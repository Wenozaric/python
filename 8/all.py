def runTest(myValue, mustValue, issue):
    if myValue == mustValue: print(f"-- {issue} -- Ответ одинаковый, равен {myValue} ✅")
    else: print(f"-- {issue} -- Ответ неверный, равен {myValue}, должен {mustValue} ❌")


def a9104():
    a = sorted('солнце')

    last = 0
    count = 0
    for a1 in a:
        for a2 in a:
            for a3 in a:
                for a4 in a:
                    for a5 in a:
                        for a6 in a:
                            count += 1
                            b = a1 + a2 + a3 + a4 + a5 + a6
                            if b[0] != 'ц' and b[0] != 'н' and b.count('ц') == 1 and b.count('н') == 1:
                                last = count
    return last

def a9103():
    a = sorted('цветок')
    count = 0
    total = 0

    for a1 in a:
        for a2 in a:
            for a3 in a:
                for a4 in a:
                    for a5 in a:
                        for a6 in a:
                            count += 1
                            b = a1 + a2 + a3 + a4 + a5 + a6
                            if count % 2 == 1 and b.count('е') == 0 and b.count('к') == 0 and b.count('о') == 2 and b.count('ц') == 1:
                                total += 1
    return total


runTest(a9104(), 38619, 9104)
runTest(a9103(), 240, 9103)