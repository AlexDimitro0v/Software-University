function solution(input) {
    let data = input[0];
    let salesNeeded=Number(data);
    let counter=0;
    let cardTransactions=0;
    let cardTransactionsNumber=0;
    let cashTransactions=0;
    let cashTransactionsNumber=0;
    let index=1;
    let moneyCollected=false;
    while(true){
        data=input[index++];
        if(data==="End"){
            break;
        }
        let salePrice = Number(data);
        counter++;
        if(counter%2===1){
            if(salePrice>100){
                console.log("Error in transaction!")
            }
            else{
                console.log("Product sold!")
                cashTransactions+=salePrice;
                cashTransactionsNumber++;
            }
        }
        else if(counter%2===0){
            if (salePrice<10){
                console.log("Error in transaction!")
            }
            else{
                console.log("Product sold!")
                cardTransactions+=salePrice;
                cardTransactionsNumber++;
            }
        }

        if(cardTransactions+cashTransactions>=salesNeeded){
            moneyCollected = true;
            break;
        }
    }
    if(moneyCollected){
        console.log(`Average CS: ${(cashTransactions/cashTransactionsNumber).toFixed(2)}`)
        console.log(`Average CC: ${(cardTransactions/cardTransactionsNumber).toFixed(2)}`)
    }
    else{
        console.log("Failed to collect required money for charity.")
    }
}

solution(["600", "86", "150", "98", "227", "End"]);