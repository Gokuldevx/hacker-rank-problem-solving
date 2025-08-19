def compareTriplets(a, b):
    # Write your code here
    alice, bob = 0, 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice,bob

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)