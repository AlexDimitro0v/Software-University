function solution(input) {
    let n = Number(input[0]);
    let data = input[1];
    let index=2;
    let totalAverageScore=0;
    let totalAverageCount=0;

    while (data!=="Finish"){
        let averageScore=0;
        let averageCount=0;
        for (let i = 0; i < n; i++) {
            let score = Number(input[index++]);
            totalAverageScore += score;
            totalAverageCount++;
            averageScore += score;
            averageCount++;
        }
        console.log(`${data} - ${(averageScore/averageCount).toFixed(2)}.`)

        data = input[index++];
    }
    console.log(`Student's final assessment is ${(totalAverageScore/totalAverageCount).toFixed(2)}.`)
}

solution(["3",
    "Arrays",
    "4.53",
    "5.23",
    "5.00",
    "Lists",
    "5.83",
    "6.00",
    "5.42",
    "Finish"])

;