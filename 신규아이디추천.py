import re

def solution(new_id):
    new_id=new_id.lower() # 1단계

    new_id=re.sub(r"[^a-z0-9-_.]","",new_id) # 2단계

    new_id=re.sub('\.\.+','.',new_id) # 3단계

    # 4단계
    new_id= new_id.strip('.')

    if new_id=='':
        new_id ='a'
    if len(new_id) >=16:
        new_id=new_id[:15]
        new_id=new_id.rstrip('.')
    #7단계
    if len(new_id)<=2:
        last_id = new_id[-1]
        while len(new_id)<3:
            new_id=new_id+last_id
    answer = new_id
    print(answer)
    #answer=''
    return answer