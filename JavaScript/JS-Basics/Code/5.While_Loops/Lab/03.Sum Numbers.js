function solution(input) {
    let n = Number(input[0]);
    let sumNumber = 0;
    let index = 1;

    while(sumNumber<n){
        let number = Number(input[index])
        sumNumber += number;
        index++;
    }

    console.log(sumNumber);
}

solution(["100", "10", "20", "30", "40"]);