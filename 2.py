fibonacci = [1, 2]

# Calculate the Fibonacci sequence until it reaches near 4 million

i = 0
while True:
    new_fibonacci_number = fibonacci[i] + fibonacci[i+1]
    if new_fibonacci_number < 4000000:
        fibonacci.append(new_fibonacci_number)
        i += 1
    else:
        break

# Filter out even numbers
even_fibonacci = []

for j in range (0, len(fibonacci)):
    if (fibonacci[j] % 2 == 0):
        even_fibonacci.append(fibonacci[j])

print(sum(even_fibonacci))