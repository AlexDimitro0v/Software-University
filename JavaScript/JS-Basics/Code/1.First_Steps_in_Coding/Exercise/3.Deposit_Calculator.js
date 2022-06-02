function deposit_calculator(input) {
    let depositSum = Number(input[0]);
    let depositPeriod = Number(input[1]);
    let interestRate = Number(input[2])/100;

    let deposit = depositSum + depositPeriod * ((depositSum*interestRate)/12);
    console.log(`${deposit.toFixed(2)}`);
}

deposit_calculator(["2350", "6", "7"]);