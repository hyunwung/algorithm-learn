def solution(a, b, n):
    answer = 0
    rest = 0
    if n % a != 0:
        rest = rest + n % a
    n = n // a

    answer = answer + n*b
    return answer

solution(4,2,20)
# 20 = 빈병

# 1 주는 콜라 갯수

# 2 받을 병 갯수

print(10%3)