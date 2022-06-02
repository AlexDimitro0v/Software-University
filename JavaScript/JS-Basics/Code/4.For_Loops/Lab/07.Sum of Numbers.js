function solution(input) {
    let n = input[0];
    let totalSum = 0;

    for (const number of n) {
        totalSum += Number(number);
    }

    console.log(`The sum of the digits is:${totalSum}`)
}

solution(["123"]);