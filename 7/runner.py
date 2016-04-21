#/usr/bin/python

primes = [2]
counter = 3
add = 0
while len(primes) < 10001:
    for i in primes:
        if(counter % i == 0):
            counter += 1
            add = 1
            break
    if (add == 1):
        add = 0
        continue
    else:
        primes.append(counter)


print primes[10000]
