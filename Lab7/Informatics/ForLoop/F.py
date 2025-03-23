x = input()
s = ""
for char in x[::-1]:
    s += str(int(char)%10)
print(int(s))