function solution(input) {
    let pages = input[0];
    let pagesPerHour = input[1];
    let days = input[2];

    let hoursNeeded = pages/pagesPerHour;
    let hoursPerDay = hoursNeeded/days;

    console.log(hoursPerDay);
}

solution(["212", "20", "2"]);