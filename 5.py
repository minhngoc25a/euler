
a = 1
while True:
    count = 0
    for i in range(1, 21):
        if a % i == 0:
            count += 1
        else:
            break
    if count == 20:
        print(a)
        break
    a += 1