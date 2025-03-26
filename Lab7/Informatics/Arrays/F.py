n = int(input())
b = list(map(int, input().split()))
count = 0

for i in range(1, n-1):
    if b[i] > b[i-1] and b[i] > b[i+1]:
        count += 1
print(count)