n = int(input())
list = list(map(int, input().split()))
count = 0
for i in range(1,len(list)):
    if list[i] > list[i-1]:
        count += 1
print(count)