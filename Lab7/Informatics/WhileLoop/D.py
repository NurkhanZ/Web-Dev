n = int(input())
i = n
while(i > 0):
    if i == 1:
        print("YES")
        break
    if i / 2 == 1:
        print("YES")
        break
    if i <= 0.5:
        print("NO")
        break
    i = i / 2
