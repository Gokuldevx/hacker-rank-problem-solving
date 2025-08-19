def findDigits(n):
    # Write your code here
    
    digits = []
    count = 0
    num = n

    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    
    for i in range(len(digits)):
        if digits[i] == 0:
            continue
        elif num % digits[i] == 0:
            count += 1

    return count

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)
        print(result)


# 11
# 123456789
# 114108089
# 110110015
# 121
# 33
# 44
# 55
# 66
# 77
# 88
# 106108048