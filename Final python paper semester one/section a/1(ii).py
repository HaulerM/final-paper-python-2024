integers=[4,7,2,9,12,15]
odd_sum= 0
for num in integers:
    if num % 2 != 0:
        odd_sum += num
        print('Sum of odd numbers:',odd_sum)