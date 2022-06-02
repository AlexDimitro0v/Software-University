function solution(input) {
    let actorName = input[0];
    let academyPoints = Number(input[1]);
    let assessors = Number(input[2]);
    let index = 3;
    let givenPoints = 0;
    let nominated = false;

    for (let i = 0; i < assessors; i++) {
        let assessorName = input[index];
        index++;
        let assessorPoints = input[index]
        index++;
        givenPoints = (assessorName.length*assessorPoints)/2;
        academyPoints += givenPoints;
        if (academyPoints>1250.5){
            console.log(`Congratulations, ${actorName} got a nominee for leading role with ${academyPoints.toFixed(1)}!`)
            nominated = true;
            break;
        }
    }

    if(!nominated){
        console.log(`Sorry, ${actorName} you need ${(1250.5-academyPoints).toFixed(1)} more!`)
    }
}

solution();
