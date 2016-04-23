#/usr/bin/python

def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return (3*n)+1

def findlengthofchain(n):
    result = [n]
    
    while result[len(result)-1] != 1:
        result.append(collatz(result[len(result)-1]))

    return len(result)


bigresult = 0
bigholder = 0
index = 0

for i in range(1, 1000000):
    bigholder = findlengthofchain(i)
    if bigholder > bigresult:
        bigresult = bigholder
        index = i

print index
