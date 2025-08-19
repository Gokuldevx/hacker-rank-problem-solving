def miniMaxSum(arr):
    total = sum(arr)
    max_val = max(arr)
    min_val = min(arr)

    max_sum = total - min_val
    min_sum = total - max_val

    print(min_sum, max_sum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
