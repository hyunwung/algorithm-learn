function solution(arr1, arr2, signs){
	let answer=[];
    
    for (let i =0; i<arr1.length; i++){
        let add = [];
        for (let j = 0; j<arr1[i].length; j++){
            add.push(arr1[i][j]+arr2[i][j])
            
        }
        answer.push(add)
    }
    for (let i =0; i<signs.length; i++){
        for(let j=0; j<signs[i].length; j++){
            if(signs[i][j]==true){
            }
            else{
                answer[i][j] = answer[i][j]*-1
            }
        }
    }
	return answer;
}
let arr1=[[5,7,1],[2,3,5]];
let arr2=[[5,1,6],[7,5,6]];
let signs=[[true,true,false],[false,true,false]];
console.log(solution(arr1,arr2,signs))
