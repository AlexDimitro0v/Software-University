function numbersEndingInSeven() {
    for (let i = 1; i < 1001; i++) {
        if(i%10===7){
            console.log(i);
        }
    }
}

numbersEndingInSeven();