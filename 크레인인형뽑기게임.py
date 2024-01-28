def solution(board, moves):
    answer = 0
    result_stack = []
 
    for val in moves:
        for stack in board:
            if stack[val-1] == 0:
                continue
            else:
                result_stack.append(stack[val-1])
                stack[val-1] = 0
                if len(result_stack) > 1:
                    if result_stack[-1] == result_stack[-2]:
                        result_stack.pop(-1)
                        result_stack.pop(-1)
                        answer += 2
                break
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])
# 4