function solution(input) {
    let height = Number(input[0]);
    let width = Number(input[1]);
    let percent = Number(input[2])/100;
    let index = 3;
    let totalPaint = 0;
    let totalSpace = (height*width*4);
    let finalSpace = Math.ceil(totalSpace - totalSpace*percent)

    while (true){
        let command = input[index++];
        if (command === "Tired!"){
            break;
        }
        let paintedWall = Number(command);
        finalSpace -= paintedWall
        if (finalSpace < 0){
            console.log(`All walls are painted and you have ${Math.abs(finalSpace)} l paint left!`);
            return;
        }
        else if (finalSpace === 0){
            console.log("All walls are painted! Great job, Pesho!");
            return;
        }
    }
    console.log(`${finalSpace} quadratic m left.`)
}

solution(["2",
    "3",
    "25",
    "6",
    "7",
    "8"]);