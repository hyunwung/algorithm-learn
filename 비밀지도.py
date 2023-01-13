def solution(n, arr1, arr2):
    result = []
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
        d = ""
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                d = d + "#"
            else:
                if a[i][j] == "0":
                    d = d + " "
                if a[i][j] == "1":
                    d = d + "#"
        result.append(d)
    return result

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])

