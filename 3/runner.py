#/usr/bin/python
n = 600851475143
factors = []
d = 2

# if n gets lower than 1 we don't care any more
while n > 1:

    # if n is cleanly divisible by d
    # add n to the factors list and set n to be the dividend
    while n % d == 0:
        factors.append(d)
        n /= d
    # progress with loop
    d = d + 1

    # if the new d^2 is bigger than n
    # we're done looking, because we've checked all the integers
    # before d as well 
    if d*d > n:
        if n > 1: factors.append(n)
        break

print factors
