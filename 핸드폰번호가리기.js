function solution(phone_number) {
    var answer = '';
    back_number = phone_number.slice(-4,phone_number)
    console.log(phone_number.length)
    for (i = 0; i< phone_number.length-back_number.length ; i++){
        stars = ("*".repeat(i+1));
    }
    console.log(stars+back_number)
    return stars+back_number;
}
solution("01033334444")