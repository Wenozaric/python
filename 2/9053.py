print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( ( (w == (not x))<= (not (z <= w))) or not y) == 0: print(x, y, z, w)

#xwyz