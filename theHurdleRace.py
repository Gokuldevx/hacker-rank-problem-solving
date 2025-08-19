def hurdleRace(k, height):
    # Write your code here
    max_val = max(height)
    doses = max_val - k
    
    if doses < 0:
        return 0
    else:
        return doses

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)
    print(result)