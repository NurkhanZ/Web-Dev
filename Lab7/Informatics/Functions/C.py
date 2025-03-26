def xor(x, y):
    if (x == 1 and y == 1) or (x == 0 and y == 0):
        print(0)
    else:
        print(1)

x, y = list(map(int, input().split()))
xor(x, y)