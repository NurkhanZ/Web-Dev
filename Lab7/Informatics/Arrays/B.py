n = int(input())
num = input()
list = num.split(" ")
for i in list:
    if int(i)%2==0:
        print(i, end=" ")
