function solution(input) {
    let data = input[0];
    let totalProfit = 0;
    let index=1;
    let dailyTarget = Number(data);

    while (true){
        if (data === "closed"){
            break;
        }
        data = input[index++];
        switch (data) {
            case "haircut":
                let haircut = input[index++];
                switch (haircut) {
                    case "mens":
                        totalProfit += 15;
                        break;
                    case "ladies":
                        totalProfit += 20;
                        break;
                    case "kids":
                        totalProfit += 10;
                        break;
                }
                break;
            case "color":
                let color = input[index++];
                switch (color) {
                    case "touch up":
                        totalProfit += 20;
                        break;
                    case "full color":
                        totalProfit += 30;
                        break;
                }
                break;
        }
        if (totalProfit >= dailyTarget) {
            break;
        }
    }
    let diff = Math.abs(totalProfit-dailyTarget);

    if (totalProfit >= dailyTarget){
        console.log("You have reached your target for the day!");
    }
    else{
        console.log(`Target not reached! You need ${diff}lv. more.`)
    }
    console.log(`Earned money: ${totalProfit}lv.`)
}

solution(["50",
    "color",
    "full color",
    "haircut",
    "ladies"])
;