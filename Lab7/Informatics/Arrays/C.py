n = int(input())
num = input()
list = num.split(" ")
count = len(list)
for i in list:
    if int(i) <= 0:
        count -= 1
print(count)
