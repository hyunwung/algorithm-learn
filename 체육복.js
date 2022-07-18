function solution(n, lost, reserve) {
    students = []
    for (let i=0; i<n; i++){
        students.push(i+1)
    }
    for (let i=0; i<reserve.length; i++){
        if(lost.indexOf(reserve[i]+1)!=-1){
            lost.splice(lost.indexOf(i,reserve[i]+1))
            console.log(lost)
        }
        else if(lost.indexOf(reserve[i]-1)!=-1){
            lost.splice(lost.indexOf(i,reserve[i]-1))
            console.log(lost)
        }
        else{
            console.log(lost)
        }
    }
    answer=students.filter(x => !lost.includes(x));
    
    return answer.length;
}
solution(7,[2,3],[1,7,5])