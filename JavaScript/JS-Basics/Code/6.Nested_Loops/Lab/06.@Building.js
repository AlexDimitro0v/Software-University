function solution(input) {
    let floorsNumber = Number(input[0]);
    let roomsNumber = Number(input[1]);

    for (let i = floorsNumber; i >= 1; i--) {
        let buf = '';
        for (let j = 0; j < roomsNumber ; j++) {
            if (i===floorsNumber){
                buf+=`L${i}${j} `
            }
            else{
                if(i%2===0){
                    buf+=`O${i}${j} `
                }
                else if (i%2===1){
                    buf+=`A${i}${j} `
                }
            }
        }
        console.log(buf)
    }
}

solution(["9", "5"]);