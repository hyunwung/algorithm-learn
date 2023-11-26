# R ,T / C ,F / J,M / A, N
# 배열 안의 

def solution(survey, choices):
   
    answer = ''
    dicts = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    # dicts = {'R':0,'C':0,'J':0,'A':0}
    # dicts2= {'T':0,'F':0,'M':0,'N':0}
    for i in range(len(survey)):
    
        choices_value = choices[i]
        survey_item = survey[i]
        if choices_value >= 1 and choices_value <= 3:
        
            if choices_value == 1:
                dicts[str(survey_item[0])] += 3
            if choices_value == 2:
                dicts[str(survey_item[0])] += 2
            if choices_value == 3:
                dicts[str(survey_item[0])] += 1
        elif choices_value >= 5 and choices_value <= 7:
            
            if choices_value == 5:
                dicts[str(survey_item[1])] += 1
            if choices_value == 6:
                dicts[str(survey_item[1])] += 2
            if choices_value == 7:
                dicts[str(survey_item[1])] += 3
        else: continue
        
    li = list(dicts.items())

    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]:
            answer = answer + li[i+1][0]
        else:
            answer = answer + li[i][0]


solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])
# "TCMA"
