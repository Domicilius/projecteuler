#/usr/bin/python

check = list(str(2**1000))
count = 0
for i in range(len(check)):
    count += int(check[i])

print count
