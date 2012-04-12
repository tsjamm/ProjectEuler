# pe05.py

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

flag = 0
n = 0

while flag == 0:
    n = n + 1
    flag = 1
    for i in range (1, 21):
        if n % i != 0:
            flag = 0
            break

print n
