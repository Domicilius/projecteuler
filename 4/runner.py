#/usr/bin/python

result = 0
holder = 0

for i in range(99,1000):
    for j in range(99, 1000):
        holder = i * j
        if (str(holder) == str(holder)[::-1]):
            if (result < holder):
                result = holder

print result
