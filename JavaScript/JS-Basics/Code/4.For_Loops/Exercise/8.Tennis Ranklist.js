function solution(input) {
    let tournaments = Number(input[0]);
    let startingPoints = Number(input[1]);
    let points=0;
    let index=2;
    let winners=0;
    for (let i = 0; i < tournaments; i++) {
        let finishPhase = input[index];
        index ++;

        if (finishPhase==="W"){
            winners += 1
            points += 2000;
            startingPoints += 2000;
        }
        else if (finishPhase==="F"){
            points += 1200;
            startingPoints += 1200;
        }
        else if (finishPhase==="SF"){
            points += 720;
            startingPoints += 720;
        }
    }

    console.log(`Final points: ${Math.floor(startingPoints)}`)
    console.log(`Average points: ${Math.floor(points/tournaments)}`)
    console.log(`${((winners/tournaments)*100).toFixed(2)}%`)
}

solution(["4", "750", "SF", "W", "SF", "W"]);