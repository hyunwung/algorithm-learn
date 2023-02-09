def solution(a, b, n):
    answer = []
    while (n>=a):
        dummy = n % a
        n = (n // a) * b
        answer.append(n)
        n = n + dummy

    return sum(answer)

solution(3,1,20) # 나눌 갯수 # 콜라 주는 갯수 # 총 병의 갯수
# 20 = 빈병

# 1 주는 콜라 갯수

# 2 받을 병 갯수