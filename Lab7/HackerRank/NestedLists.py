if __name__ == '__main__':
    students, res = [], []
    min1 = min2 = 100000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students = sorted(students, key=lambda x: x[1])
    for n in students:
        if n[1] < min1:
            min2 = min1 
            min1 = n[1]
        elif n[1] < min2 and n[1] != min1:
            min2 = n[1]
    for name in students:
        if min2 == name[1]:
            res.append(name[0])
    res = sorted(res)
    print(*res, sep='\n')