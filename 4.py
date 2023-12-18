first_number = [number for number in range (100, 1000)]
second_number = [number for number in range (100, 1000)]
palindrome = []

def multiply(fst, snd):
    return fst * snd

def main():
    for i in first_number:
        for j in second_number:
            ans = multiply(i, j)
            if str(ans) == str(ans)[::-1]:
                palindrome.append(ans)
    print(max(palindrome))
    
if __name__ == '__main__':
    main()