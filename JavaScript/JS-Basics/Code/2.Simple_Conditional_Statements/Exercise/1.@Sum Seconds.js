function solution(input) {
    let contestant1 = Number(input[0]);
    let contestant2 = Number(input[1]);
    let contestant3 = Number(input[2]);

    let totalSeconds = contestant1+contestant2+contestant3
    let seconds = totalSeconds % 60 // get the seconds
    let minutes = Math.floor(totalSeconds/60) // get the minutes
    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`)
    }
    else {
        console.log(`${minutes}:${seconds}`)
    }
}

solution(["14", "12", "10"]);
