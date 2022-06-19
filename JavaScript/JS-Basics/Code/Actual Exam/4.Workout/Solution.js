function solution(input) {
    let days = Number(input[0]);
    let km = Number(input[1]);
    let percent = Number(input[2])/100;
    let index = 3;
    let totalDistance = km;

    for (let i = 0; i < days; i++) {
        km += km * percent;
        totalDistance += km;
        percent = input[index++]/100;
    }

    let diff = Math.ceil(Math.abs(totalDistance-1000))

    if (totalDistance >= 1000){
        console.log(`You've done a great job running ${diff} more kilometers!`)
    }
    else{
        console.log(`Sorry Mrs. Ivanova, you need to run ${diff} more kilometers`)
    }
}

solution(["4",
    "100",
    "30",
    "50",
    "60",
    "80"])
;