s = input().split(',')

with open("input.txt", "wt") as f:
    for x in s:
        print(x, end=' ', file=f)
    print('\n', file=f)
    print(len(s), file=f)
