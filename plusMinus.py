def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos, neg, zer = 0, 0, 0
    for i in range(n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else: 
            zer += 1

    div1 = pos/n
    div2 = neg/n
    div3 = zer/n

    print(f"{div1:.6f}")
    print(f"{div2:.6f}")
    print(f"{div3:.6f}")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
