function solution(input) {
    let data = input[0]
    let index=1;
    let biggestNumber=Number.MIN_SAFE_INTEGER;
    while (data!=="Stop"){
        if(Number(data)>biggestNumber){
            biggestNumber=data;
        }
        data=input[index]
        index++;
    }
    console.log(biggestNumber);
}

solution(['100',
    '99',
    '80',
    '70',
    'Stop']);