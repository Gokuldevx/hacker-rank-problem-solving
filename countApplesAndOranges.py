def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # s - starting point od Sam house
    # t - ending location of sam house
    # a - location of apple tree
    # b - location of orange tree

    apple_pos =[]
    orange_pos = []
    n = len(apples)
    m = len(oranges)
    apple_count, orange_count = 0, 0

    for i in range(n):
      pos1 = apples[i] + a
      apple_pos.append(pos1)  

      if apple_pos[i] >= s and apple_pos[i] <= t:
         apple_count += 1   

    for j in range(m):
       pos2 = oranges[j] + b
       orange_pos.append(pos2)

       if orange_pos[j] >= s and orange_pos[j] <= t:
         orange_count += 1

    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

  