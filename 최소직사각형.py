def solution(sizes):
    big = []
    small = []
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            big.append(sizes[i][1])
            small.append(sizes[i][0])
        else:
            big.append(sizes[i][0])
            small.append(sizes[i][1])
    return max(big)*max(small)
    
solution([[60, 50], [30, 70], [60, 30], [80, 40]])