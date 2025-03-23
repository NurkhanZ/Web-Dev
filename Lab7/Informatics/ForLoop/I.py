from math import ceil, sqrt
x = int(input())
count = 0
for i in range(1, ceil(x**(.5))+1):
    if (x % i == 0):
        count+=1
        if (i != ceil(sqrt(x))):
            count+=1
print(count)
