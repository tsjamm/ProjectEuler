# pe04.py

# Find the largest palindrome made from the product of two 3-digit numbers.

lpal = 0

for x in range (100, 1000):
    for y in range (100, x):
        n = x * y
        if n > lpal:
            s = str(n)
            if s == s[::-1]:
                lpal = x * y

print lpal
