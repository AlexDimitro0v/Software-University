function solution(input) {
    let index = 0;
    let mostPoints = 0;
    let winner = ""

    while(true){
        let playerName = input[index];
        index++;
        let totalPoints = 0;
        if (playerName === "Stop"){
            break;
        }
        for (let i = 0; i < playerName.length; i++) {
            let n = Number(input[index++]);
            let charCode = Number(playerName.charCodeAt(i))
            if (n === charCode){
                totalPoints += 10;
            }
            else{
                totalPoints += 2;
            }
        }
        if (totalPoints >= mostPoints){
            mostPoints = totalPoints;
            winner = playerName;
        }
    }
    console.log(`The winner is ${winner} with ${mostPoints} points!`)
}

solution(["Ivan", "73", "20", "98", "110", "Ivo", "80", "65", "87", "Stop"]);
