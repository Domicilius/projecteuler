#/usr/bin/python
count = 0

for i in range(0, 1000):
    if( i % 3 == 0 ):
        count += i
    elif(i % 5 == 0 ):
        count += i

print(count)
