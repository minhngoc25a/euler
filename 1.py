multiples_of_three = []
multiples_of_five = []

for i in range(1, 1000):
    if (i % 3 == 0):
        multiples_of_three.append(i)
    if (i % 5 == 0):
        multiples_of_five.append(i)

multiples_of_three_and_five = multiples_of_three + list(set(multiples_of_five) - set(multiples_of_three))

print(sum(multiples_of_three_and_five))