def solution(dartResult):
    answer = 0
    n = len(dartResult)

    # 현재 위치
    i = 0

    while i < n:
        # 현재 문자
        char = dartResult[i]

        # 점수 추출
        if char.isdigit():
            score = int(char)
            # 두 자리 수의 경우
            if i + 1 < n and dartResult[i + 1].isdigit():
                score = 10
                i += 1

        # 보너스 계산
        i += 1
        if char == 'D':
            score **= 2
        elif char == 'T':
            score **= 3

        # 옵션 계산
        if i < n and dartResult[i] in ('*', '#'):
            if dartResult[i] == '*':
                score *= 2
                if i >= 2:
                    answer += int(dartResult[i - 2])  # 이전 점수를 두 배로 만듦
            elif dartResult[i] == '#':
                score *= -1
            i += 1

        # 최종 점수에 더하기
        answer += score

    return answer

print(solution("1S#2D*3T"))