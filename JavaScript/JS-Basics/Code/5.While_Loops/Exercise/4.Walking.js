function solution(input) {
    let data = input[0];
    let isGoingHome=data;
    let index=1;
    let steps=0;
    while(steps<10000){
        if(isGoingHome==="Going home"){
            let finalSteps=steps+Number(data)
            if(finalSteps<10000){
                console.log(`${10000-steps-Number(data)} more steps to reach goal.`)
                return;
            }
        }

        if(data!=="Going home"){
            steps+=Number(data)
        }
        isGoingHome=data;
        data=input[index];
        index++;
    }
    console.log("Goal reached! Good job!")
    console.log(`${steps-10000} steps over the goal!`)
}

solution(["1500",
    "300",
    "2500",
    "3000",
    "Going home",
    "200"])
;