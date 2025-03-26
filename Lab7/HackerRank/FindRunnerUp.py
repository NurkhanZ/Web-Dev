if __name__ == '__main__':
    max1 = max2 = -1000
    n = int(input())
    arr = map(int, input().split())
    for n in arr:
        if n > max1:
            max2 = max1 
            max1 = n
        elif n > max2 and n != max1:
            max2 = n
    print(max2)