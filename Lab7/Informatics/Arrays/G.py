n = int(input())
b = list(map(int, input().split()))
for i in range(int(n/2)):
    c = b[i]
    b[i] = b[n - i - 1]
    b[n - i - 1] = c
print(*b)