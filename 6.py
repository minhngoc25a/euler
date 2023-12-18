sum_square = 0
squared_sum = 0

for i in range(1, 101):
    sum_square += i ** 2
    squared_sum += i
    
squared_sum **= 2
print(sum_square - squared_sum)
    