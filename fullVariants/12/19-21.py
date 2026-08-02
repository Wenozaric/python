a = set()

def checkWin(cur1, cur2):
    a1 = cur1 + cur2 + 1
    a2 = cur1 * 2 + cur2
    a3 = cur1 + cur2 * 2
    if a1 >= 227 or a2 >= 227 or a3 >= 227: return True
    return False

def a19(cur1, cur2, step, base):
    if step == 1:
        b = checkWin(cur1, cur2)
        if b: a.add(base)

    if step < 1:
        a19(cur1 + 1, cur2, step + 1, base)
        a19(cur1 * 2, cur2, step + 1, base)
        a19(cur1, cur2 + 1, step + 1, base)
        a19(cur1, cur2 * 2, step + 1, base)


#for x in range(1, 210):
#    a19(17, x, 0, x)
#print(min(a))


b = set()

def getAll(cur1, cur2):
    return [[cur1 + 1, cur2], [cur1 * 2, cur2], [cur1, cur2 + 1], [cur1, cur2 * 2]]

def validVariant(var):
    win = False
    for variant in var: 
        if variant[0] + variant[1] >= 227: win = True
    return win

def a20(cur1, cur2, step, base):
    if step == 0:
        valid = checkWin(cur1, cur2)
        if not valid:
            a20(cur1 + 1, cur2, step + 1, base)
            a20(cur1 * 2, cur2, step + 1, base)
            a20(cur1, cur2 + 1, step + 1, base)
            a20(cur1, cur2 * 2, step + 1, base)
    if step == 1:
            a = checkWin(cur1, cur2)
            if not a:
                s1 = getAll(cur1 + 1, cur2)
                s2 = getAll(cur1 * 2, cur2)
                s3 = getAll(cur1, cur2 + 1)
                s4 = getAll(cur1, cur2 * 2)
                if validVariant(s1) and validVariant(s2) and validVariant(s3) and validVariant(s4):
                    b.add(base)

#for x in range(1, 210):
#    a20(17, x, 0, x)
#print(b)



def win(pos):
    return pos[0] + pos[1] >= 227

def VanyaGoodMove(v_pos):
    if win(v_pos):
        return True
    p2Move = getAll(v_pos[0], v_pos[1])
    
    if any(win(p2) for p2 in p2Move):
        return False
        
    for p2 in p2Move:
        v2Move = getAll(p2[0], p2[1])
        if not any(win(v2) for v2 in v2Move):
            return False
            
    return True

c = set()
for x in range(1, 210):
    p1Move = getAll(17, x)
    
    if any(win(p1) for p1 in p1Move):
        continue

    winVanya = True
    for p1 in p1Move:
        v1Move = getAll(p1[0], p1[1])
        if not any(VanyaGoodMove(v1) for v1 in v1Move):
            winVanya = False
            break
            
    if winVanya:
        c.add(x)

print(c)