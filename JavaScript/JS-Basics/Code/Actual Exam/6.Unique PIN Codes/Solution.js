function solution(input) {
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1])
    let thirdNumber = Number(input[2])

    for (let i = 1; i <= firstNumber; i++) {
        for (let j = 1; j <= secondNumber; j++) {
            for (let k = 1; k <= thirdNumber; k++) {
                if (i % 2 === 0 && k % 2 === 0 && [2, 3, 5, 7].includes(j)) {
                    console.log(`${i} ${j} ${k}`)
                }
            }
        }
    }
}

solution(["8",
    "2",
    "8"]);