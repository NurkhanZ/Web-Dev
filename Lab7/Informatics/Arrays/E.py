n = int(input())
list = list(map(int, input().split()))

def smth(list):
    for i in range(1,len(list)):
        if (list[i] < 0 and list[i-1] < 0) or (list[i] > 0 and list[i-1] > 0):
            print("YES")
            return 0
    print("NO")

smth(list)
