function solution(input) {
    let givenNumber = Number(input[0]);

    if(givenNumber<=100 && givenNumber>=-100 && givenNumber!==0){
        console.log("Yes")
    }
    else{
        console.log("No")
    }
}

solution();