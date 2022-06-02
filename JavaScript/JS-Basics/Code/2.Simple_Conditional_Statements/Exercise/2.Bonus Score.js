function solution(input) {
    let points = Number(input[0]);
    let bonusPoints;
    if (points <= 100) {
        bonusPoints = 5
    }
    else if (points > 100 && points <= 1000) {
        bonusPoints = points*20/100
    }
    else if (points > 1000) {
        bonusPoints = points*10/100
    }

    if (points % 2 === 0) {
        bonusPoints += 1
    }

    if (points % 10 === 5) {
        bonusPoints += 2
    }

    console.log(bonusPoints)
    console.log(points+bonusPoints)
}

solution(["15875"]);