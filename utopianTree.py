def utopianTree(n):
    # Write your code here
    h = 1
    
    for i in range(n):
        if i % 2 == 0:
            h *= 2
        else:
            h += 1
    return h

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        result = utopianTree(n)

        print(result)