#/usr/bin/python

sieve = [True] * 2000000
result = 0

for i in range(2, int((len(sieve) ** 0.5) +1)):
    for j in range(i+i, len(sieve), i):
        sieve[j] = False

for i in range(2, len(sieve)):
    if sieve[i]:
        result += i
print result
