function solution(input) {
    let length = input[0];
    let width = input[1];
    let height = input[2];
    let data = input[3];
    let index=4;
    let boxArea = length*width*height;

    while(data!=="Done"){
        boxArea-=data;
        if(boxArea<0){
            console.log(`No more free space! You need ${Math.abs(boxArea)} Cubic meters more.`)
            return;
        }
        data=input[index];
        index++;
    }
    console.log(`${boxArea} Cubic meters left.`)
}

solution(["10",
    "10",
    "2",
    "20",
    "20",
    "20",
    "20",
    "122"])

;