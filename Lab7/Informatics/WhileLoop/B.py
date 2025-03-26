n = int(input())
div, i = 0, 2
while(i < n+1):
    if n % i == 0:
        div = i
        break
    i= i+1
print(div)
