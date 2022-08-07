function solution(a, b) {
    var answer = 0;

    if(a<b){
        c = b-a+1
        for (let i=0; i<c; i++){
            value = c+i
            answer=answer+value
            
        }
    }
    else if(b<a){
        c = a-b+1
        
        for (let i=0; i<c; i++){
            value = c+i
            answer=answer+value
            
        }
    }
    else if (a==b){
        return a
    }
    console.log(answer)
    return answer;
}
solution(3,6)