a, b, c, d = list(map(int, input().split()))

def minf(a, b, c, d):
    c = min(min(a, b), min(c,d))
    print(c)
minf(a, b, c, d)