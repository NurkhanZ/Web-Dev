n = int(input())
num = input()
list = num.split(" ")
for i in list[::2]:
    print(i, end=" ")
