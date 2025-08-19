from statistics import median

def findMedian(arr):
    # Write your code here
    result = median(arr)
    return result

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
    print(result)
