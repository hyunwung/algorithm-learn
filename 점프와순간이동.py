def solution(a):
    answer = a
    c = 0
    while True:
        if answer % 2 == 0:
            answer = answer // 2
        else:
            answer = answer - 1
            c = c + 1
        if answer == 0:
            break
    return c

# def solution(a):
#     return bin(a).count("1")

solution(5000)