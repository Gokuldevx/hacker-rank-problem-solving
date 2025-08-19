def designerPdfViewer(h, word):
    # Write your code here
    l = len(word)
    arr = []

    for i in range(l):
        s = ord(word[i]) - 97
        max_val = h[s]
        arr.append(max_val)

    max_height = max(arr)
    total = max_height * l
    return total
    
if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()

    result = designerPdfViewer(h, word)
    print(result)