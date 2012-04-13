# pe10.py

# Find the sum of all the primes below two million.

from math import sqrt

def isprime(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1

count = 2 
p = 2     # 2 already counted
psum = 2  # starting from 3 (see below, p+1)

while count < 2000000:
    p = p + 1
    if isprime(p) == 1:
        psum = psum + p
    count = count + 1

print psum
