import math
# num = 1

# def is_prime(n):
#     if n == 1:
#         return False
#     elif n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True

# count = 0
# while True:
#     if is_prime(num):
#         count += 1
#     if count == 10001:
#         print(num)
#         break
#     num += 1

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

limit = 10001
count = 1
candidate = 1

while True:
    candidate += 2
    if isPrime(candidate):
        count += 1
    if count == limit:
        break
print(candidate)