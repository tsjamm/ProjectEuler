# pe06.py

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0
sum_temp = 0

for i in range (1, 101):
    sum_of_squares = sum_of_squares + ( i * i )
    sum_temp = sum_temp + i
square_of_sum = sum_temp * sum_temp
diff = square_of_sum - sum_of_squares

print diff
