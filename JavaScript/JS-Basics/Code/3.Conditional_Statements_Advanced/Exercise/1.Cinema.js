function solution(input) {
    let cinemaProjection = input[0];
    let cinemaRows = Number(input[1]);
    let cinemaColumns = Number(input[2]);

    let revenue = cinemaRows * cinemaColumns
    if(cinemaProjection==="Premiere"){
        revenue=revenue*12
    }
    else if(cinemaProjection==="Normal"){
        revenue = revenue*7.50
    }
    else if(cinemaProjection==="Discount"){
        revenue=revenue*5
    }

    console.log(`${revenue.toFixed(2)} leva`)
}

solution();