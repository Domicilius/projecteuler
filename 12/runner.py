#/usr/bin/python

def factors(n):
    result = []
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            result.append(i)
            result.append(n/i)
   
    return list(set(result))

count = 0
trianglecount = 0


while len(factors(trianglecount)) < 500:
    print len(factors(trianglecount))
    count += 1
    trianglecount += count

print factors(trianglecount)
print trianglecount
