def simpleArraySum(ar):
     # Write your code here
    return sum(ar)

if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)

