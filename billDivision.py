def bonAppetit(bill, k, b):
    # Write your code here
    total = sum(bill)
    anna_bill = 0
    fair_return = 0
    for i in range(n):
        if i == k:
            continue
        else:
            anna_bill += bill[i]
    fair_share = anna_bill / 2
    if fair_share == b:
        print("Bon Appetit")
    else:
        fair_return = int(b - fair_share)
        print(fair_return)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
