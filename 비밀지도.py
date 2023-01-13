def solution(n, arr1, arr2):
    answer = []
    a = []
    b = []
    for i in arr1:
        if len(bin(i)[2:]) < n:
            c = n-len(bin(i)[2:])
            a.append((c * "0") + bin(i)[2:])
        else:
            a.append(bin(i)[2:])
    for i in arr2:
        if len(bin(i)[2:]) < n:
            c = n - len(bin(i)[2:])
            b.append((c * "0") + bin(i)[2:])
        else:
            b.append(bin(i)[2:])
    for i in range(len(a)):
        for j in a[i]:
            print(j)
            break

    print(a)
    print(b)
    return answer

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])

