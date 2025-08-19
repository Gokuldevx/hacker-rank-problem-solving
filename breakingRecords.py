def breakingRecords(scores):
    # Write your code here
    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1

    return max_count, min_count

if __name__ == '__main__':

    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
