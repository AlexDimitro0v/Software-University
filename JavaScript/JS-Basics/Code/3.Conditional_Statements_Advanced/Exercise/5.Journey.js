function solution(input) {
    let budget = Number(input[0]);
    let season = input[1];
    let destination;
    let moneySpent;
    let housing;

    if(budget<=100){
        destination = "Bulgaria";
        if (season === "summer") {
            moneySpent = budget * (30 / 100);
        } else if (season === "winter") {
            moneySpent = budget * (70 / 100);
        }
    }
    else if(budget>100 && budget<=1000){
        destination="Balkans";
        if(season==="summer"){
            moneySpent = budget*(40/100);
        }
        else if(season==="winter"){
            moneySpent = budget*(80/100);
        }
    }
    else if(budget>1000){
        destination="Europe";
        moneySpent=budget*(90/100)
    }



    switch(season){
        case "summer":
            if(destination==="Europe"){
                housing="Hotel"
            }
            else{
                housing = "Camp";
            }
            break;
        case "winter":
            housing = "Hotel";
            break;
    }

    console.log(`Somewhere in ${destination}\n${housing} - ${moneySpent.toFixed(2)}`)
}

solution();