function solution(input) {
    let hours = Number(input[0]);
    let minutes = Number(input[1])+15;

    if (minutes >= 60 ) {
        hours = hours + 1;
        if (hours > 23) {
            hours = 0;
        }
    }

    minutes = minutes % 60;
    if (minutes < 10){
        console.log(`${hours}:0${minutes}`);
    }
    else {
        console.log(`${hours}:${minutes}`);
    }
}

solution(["1", "46"]);