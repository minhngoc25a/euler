numbers = []
with open('8.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        for j, number in enumerate(line):
            numbers.append(number)

numbers = [m for m in numbers if m != '\n']
numbers = [int(n) for n in numbers]
    
multiples = []

for k in range(len(numbers)):
    try:
        ans = numbers[k]
        for l in range(1, 13):
            ans *= numbers[k + l]
        multiples.append(ans)
    except:
        break


answer = max(multiples, default=0)
print(answer)