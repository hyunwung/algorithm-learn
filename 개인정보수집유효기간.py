from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    terms_list = {}
    today_lst = list(map(int,today.split('.'))) # 오늘 날짜 리스트로 변환
    print(today_lst)
    today_string=today.split('.')
    todays = datetime.strptime('-'.join(today_string), '%Y-%m-%d')
    
    for i in terms:
        terms_list[i.split(' ')[0]]=i.split(' ')[1]
    for i,val in enumerate(privacies):
        val_month = int(terms_list.get(val.split(' ')[1]))
        temp_month = int(val.split(' ')[0].split('.')[1])
        temp_year =int(val.split(' ')[0].split('.')[0])
        temp_day =int(val.split(' ')[0].split('.')[2])
        new_month = val_month + temp_month
        if new_month > 12:
            new_year_count = new_month // 12
            new_year = str(temp_year+new_year_count)
            new_month = '0'+str(int(new_month % 12))
            new_day = '0'+str(int(val[2]))
            new_pri = [new_year,new_month,new_day]
        
            newdays = datetime.strptime('-'.join(new_pri), '%Y-%m-%d')
            if todays >= newdays:
                answer.append(i+1)
        else:
            new_pri = [str(temp_year),str(new_month),'0'+str(temp_day)]
            newdays = datetime.strptime('-'.join(new_pri), '%Y-%m-%d')
           
            if todays >= newdays:
                answer.append(i+1)
    return answer

solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])