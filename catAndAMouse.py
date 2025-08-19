def catAndMouse(x, y, z):
    x = abs(z - x)
    y = abs(z - y)

    if x > y:
        return "Cat B"
    
    elif x < y:
        return "Cat A"
    
    else:
        return "Mouse C"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)