function solution(input) {
    let username = input[0];
    let passw = input[1];
    let data = input[2];
    let index = 3;

    while(data!==passw){
        data = input[index];
        index++;
    }
    console.log(`Welcome ${username}!`)
}

solution();