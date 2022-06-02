function solution(input) {
    let seriesToWatch = input[0];
    let episodeDuration = Number(input[1]);
    let breakDuration = Number(input[2]);

    let lunchBreak = breakDuration * (1/8);
    let restBreak = breakDuration * (1/4);
    let totalBreakTime = breakDuration - lunchBreak - restBreak;

    let difference = Math.abs(totalBreakTime-episodeDuration);

    if (totalBreakTime >= episodeDuration){
        console.log(`You have enough time to watch ${seriesToWatch} and left with ${Math.ceil(difference)} minutes free time.`)
    }
    else {
        console.log(`You don't have enough time to watch ${seriesToWatch}, you need ${Math.ceil(difference)} more minutes.`)
    }
}

solution();