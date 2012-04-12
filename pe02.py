# pe02.py

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

sum = 0
feb_term1 = 1
feb_term2 = 2

while feb_term2 <= 4000000:
    feb_term3 = feb_term1 + feb_term2
    if feb_term2 % 2 == 0:
        sum = sum + feb_term2
    feb_term1 = feb_term2
    feb_term2 = feb_term3

print "Sum of even Feb's is %d" % sum
