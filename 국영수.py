n = int(input())

score_list = []

for i in range(n):
    [name,kor,eng,math] = map(str,input().split())
    score_list.append([name,int(kor),int(eng),int(math)])

sorted_score_list = sorted(score_list,key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in score_list:
    print(i[0])