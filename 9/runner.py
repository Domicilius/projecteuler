#/usr/bin/python

primitives = []

for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            if ((i*i) + (j*j) == (k*k)):
                primitives.append([i, j, k])

for each in range(len(primitives)):
    for i in range(100):
        if ((i*primitives[each][0]) + (i*primitives[each][1]) + (i*primitives[each][2])) == 1000:
            print "\n", (i*primitives[each][0])*(i*primitives[each][1])*(i*primitives[each][2])            
