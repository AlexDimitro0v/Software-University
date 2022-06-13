function solution(input) {
    let n = Number(input[0]);
    let index=1;
    let totalSum=0;
    let counter=0;
    for (let i = 0; i < n; i++) {
        let data = Number(input[index++])
        totalSum+=data;
        counter++;
    }
    console.log((totalSum/counter).toFixed(2))
}

solution(["2", "6", "4"]);