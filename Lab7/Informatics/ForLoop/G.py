x = int(input())
div = 0
for i in range(2, x+1):
    if x % i == 0:
        div = i
        break
print(div)