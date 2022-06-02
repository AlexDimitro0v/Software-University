function solution(input) {
    let tripPrice = Number(input[0]);
    let puzzles = Number(input[1]);
    let dolls = Number(input[2]);
    let teddyBears = Number(input[3]);
    let minions = Number(input[4]);
    let trucks = Number(input[5])

    let totalSum = puzzles*2.60+dolls*3+teddyBears*4.10+minions*8.20+trucks*2;
    let toysNumber = puzzles+dolls+teddyBears+minions+trucks;

    if(toysNumber >= 50) {
        totalSum = totalSum - totalSum*0.25;
    }

    totalSum = totalSum - totalSum * 0.10;
    let difference = Math.abs(totalSum-tripPrice)

    if (totalSum >= tripPrice) {
        console.log(`Yes! ${(difference).toFixed(2)} lv left.`);
    }

    else {
        console.log(`Not enough money! ${(difference).toFixed(2)} lv needed.`)
    }
}

solution();