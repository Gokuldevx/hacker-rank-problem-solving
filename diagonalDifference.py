def diagonalDifference(arr):
    # Write your code here
    lent = len(arr)
    sum1, sum2 = 0, 0
    
    for i in range(lent):
        sum1 += arr[i][i]
        sum2 += arr[i][lent - 1 - i]
        
    return abs(sum1 - sum2)
    

if __name__ == '__main__':
    
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)