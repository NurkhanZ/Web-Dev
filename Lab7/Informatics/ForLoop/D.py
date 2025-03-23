x, d = input(), int(input())
count = 0
for char in x:
    if int(char) == d:
        count += 1
print(count)