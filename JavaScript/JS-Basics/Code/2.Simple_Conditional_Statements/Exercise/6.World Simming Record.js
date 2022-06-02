function solution(input) {
    let record = Number(input[0]);
    let distance = Number(input[1]);
    let timeForOneMeter = Number(input[2]);

    let totalTime = distance * timeForOneMeter
    let additionalTIme = Math.floor(distance/15)*12.5
    let timeNeeded = totalTime + additionalTIme

    let difference = Math.abs(timeNeeded-record)

    if (timeNeeded < record) {
        console.log(`Yes, he succeeded! The new world record is ${timeNeeded.toFixed(2)} seconds.`)
    }
    else{
        console.log(`No, he failed! He was ${difference.toFixed(2)} seconds slower.`)
    }
}

solution(["55555.67", "3017", "5.03"]);