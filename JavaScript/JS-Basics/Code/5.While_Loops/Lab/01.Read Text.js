function solution(input) {
    let text = input[0];
    let index=1;        // Always keep the index outside the loop

    while(text!=="Stop"){
        console.log(text);
        text = input[index]
        index++;
    }
}

solution();