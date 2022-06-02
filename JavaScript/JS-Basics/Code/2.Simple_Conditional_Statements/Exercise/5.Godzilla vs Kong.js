function solution(input){
    let budget = Number(input[0]);
    let statists = Number(input[1]);
    let priceForDressOfOneStat = Number(input[2]);

    let priceOfDecor = budget * 0.10;
    let totalPriceForStat = statists*priceForDressOfOneStat;

    if (statists > 150){
        totalPriceForStat = totalPriceForStat - totalPriceForStat * 0.1;
    }

    let totalPriceOfTheMovie = priceOfDecor + totalPriceForStat;
    let difference = Math.abs(totalPriceOfTheMovie-budget);

    if (totalPriceOfTheMovie <= budget){
        console.log("Action!");
        console.log(`Wingard starts filming with ${difference.toFixed(2)} leva left.`);
    }
    else{
        console.log("Not enough money!");
        console.log(`Wingard needs ${difference.toFixed(2)} leva more.`);
    }
}

solution(["15437.62", "186", "57.99"]);