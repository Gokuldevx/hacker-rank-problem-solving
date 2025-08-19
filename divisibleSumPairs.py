def divisibleSumPairs(n, k, ar):
    # Write your code here
    sum = 0
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            sum = ar[i] + ar[j]
            if sum % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)

    print(result)