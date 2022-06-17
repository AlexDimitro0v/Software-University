function solution(input) {
    let footballTeam = input[0];
    let gamesPlayed = Number(input[1]);
    let index = 2;
    let totalPoints = 0;
    let winningGames = 0;
    let drawGames = 0;
    let lostGames = 0;

    if(gamesPlayed===0){
        console.log(`${footballTeam} hasn't played any games during this season.`)
    }
    else{
        for (let i = 1; i<=gamesPlayed; i++) {
            let gamesOutcome = input[index++];
            if(gamesOutcome === "W"){
                totalPoints += 3;
                winningGames += 1;
            }
            else if (gamesOutcome === "D"){
                totalPoints += 1;
                drawGames += 1;
            }
            else if (gamesOutcome === "L"){
                lostGames += 1;
            }
        }

        console.log(`${footballTeam} has won ${totalPoints} points during this season.`);
        console.log("Total stats:")
        console.log(`## W: ${winningGames}`);
        console.log(`## D: ${drawGames}`);
        console.log(`## L: ${lostGames}`);
        console.log(`Win rate: ${(winningGames/gamesPlayed*100).toFixed(2)}%`)
    }
}

solution(["Liverpool", "10", "W", "D", "D", "W", "L", "W", "D", "D", "W", "W"]);