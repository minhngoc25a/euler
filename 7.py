num = 1
count = 0
while num > 0:
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            count += 1
            break
    if count == 10001:
        print(num)
        break
    num += 1