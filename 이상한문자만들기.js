function solution(s){
    let arr = s.split(" ");
    console.log(arr)
    // try, hello world 
    let answer = "";
    for(let i = 0; i<arr.length; i++){
        for(let j = 0; j<arr[i].length; j++){
            if(j%2 !==0){
                answer = answer + arr[i][j].toLowerCase();
            }else{
                answer = answer + arr[i][j].toUpperCase();
            }
        }
        if (i<arr.length){
            answer = answer + " ";
        }
    }
    console.log(answer)
    return answer
}

// function solution(s) {
//     let str = s.split(" ");
//     var answer = [];
//     for (let i = 0; i<s.length; i++){
//         if(i%2 == 0){
//             answer.push(s[i].toUpperCase())
            
//         }
//         else if(i%2 != 0){
//             answer.push(s[i])
            
//         }
//     }
//     console.log(answer.join(""))
//     return answer.join("");
// }
solution("try hello world")

