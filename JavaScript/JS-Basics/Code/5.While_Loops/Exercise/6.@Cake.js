function solution(input) {
    let cakeLength = input[0];
    let cakeHeight = input[1];
    let cakePieces = cakeLength*cakeHeight;
    let data = input[2];
    let index=3;
    while(data!=="STOP"){
        let pieces = Number(data)
        cakePieces -= pieces; // First subtract as we have the variable outside the loop
        if(cakePieces<0){
            console.log(`No more cake left! You need ${Math.abs(cakePieces)} pieces more.`)
            return;
        }
        else if(cakePieces===0){
            break;
        }
        data=input[index];
        index++;
    }

    console.log(`${cakePieces} pieces are left.`)
}

solution(["10", "10", "20", "20", "20", "20", "20"]);