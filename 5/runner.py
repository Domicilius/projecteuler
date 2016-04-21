#/usr/bin/python

def checkfactor20(n):
    for i in range(1, 21):
        if (n % i != 0):
            return False
    
    return True

base = 20
i = 1
result = 20


while not checkfactor20(result):
    result = base * i
    i += 1

print result
