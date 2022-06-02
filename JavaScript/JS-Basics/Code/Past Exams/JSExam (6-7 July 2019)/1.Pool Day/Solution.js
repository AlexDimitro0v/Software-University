function solution(input) {
    const numberOfPeople = Number(input[0]);
    const entryFee = Number(input[1])
    const chairPrice = Number(input[2])
    const umbrellaPrice = Number(input[3])

    const totalEntryFee = numberOfPeople*entryFee
    const totalChairPrice = Math.ceil(75/100*numberOfPeople)*chairPrice
    const totalUmbrellaPrice = Math.ceil(numberOfPeople/2)*umbrellaPrice

    console.log(`${(totalUmbrellaPrice+totalChairPrice+totalEntryFee).toFixed(2)} lv.`)
}


solution(["21", "5.50", "4.40", "6.20"])