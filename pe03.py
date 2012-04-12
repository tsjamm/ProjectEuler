# pe03.py

# What is the largest prime factor of the number 600851475143 ?

n = 600851475143

i = 2

while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print n
