function solution(input) {
    let data = input[0]
    let index=1;
    let smallestNumber=Number.MAX_SAFE_INTEGER;
    while (data!=="Stop"){
        if(Number(data)>smallestNumber){
            smallestNumber=data;
        }
        data=input[index]
        index++;
    }
    console.log(smallestNumber);
}

solution(['100',
    '99',
    '80',
    '70',
    'Stop']);