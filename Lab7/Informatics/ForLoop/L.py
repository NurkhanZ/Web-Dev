binary = input()
base = 1
res = 0
for char in binary[::-1]:
    res += int(char) * base
    base = base * 2
print(res)