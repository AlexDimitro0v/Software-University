function converter(input) {
    let usd = Number(input[0]);
    let convertRate = 1.79549;

    let bgn = usd*convertRate;

    console.log(bgn);
}

converter(["22"]);