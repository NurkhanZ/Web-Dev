n = int(input())
k = int(input())
if n == 1 and k != 1:
    print("NO")
elif n != 1 and k == 1:
    print("NO")
else:
    print("YES")