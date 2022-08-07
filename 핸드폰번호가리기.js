function solution(phone_number) {
    back_number = phone_number.slice(-4,phone_number)
    for (i = 0; i< phone_number.length-back_number.length ; i++){
        stars = ("*".repeat(i+1));
    }
    return stars+back_number;
}
solution("01033334444")