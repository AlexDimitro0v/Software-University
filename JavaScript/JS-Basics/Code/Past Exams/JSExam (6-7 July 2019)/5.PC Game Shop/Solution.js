function solution(input) {
    let n = Number(input[0]);
    let index = 1;
    let hearthstone = 0;
    let fornite = 0;
    let overwatch = 0;
    let others = 0;
    let counter = 0;

    for (let i = 0; i < n; i++) {
        let game = input[index++];
        counter ++;
        if(game === "Hearthstone"){
            hearthstone += 1;
        }
        else if (game === "Fornite"){
            fornite++;
        }
        else if (game === "Overwatch"){
            overwatch++;
        }
        else{
            others++;
        }
    }

    console.log(`Hearthstone - ${(hearthstone/counter*100).toFixed(2)}%`)
    console.log(`Fornite - ${(fornite/counter*100).toFixed(2)}%`)
    console.log(`Overwatch - ${(overwatch/counter*100).toFixed(2)}%`)
    console.log(`Others - ${(others/counter*100).toFixed(2)}%`)
}

solution(["3",
    "Hearthstone",
    "Diablo 2",
    "Star Craft 2"]);