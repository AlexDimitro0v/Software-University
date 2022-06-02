function solution(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let percent = Number(input[3])/100;

    let aquariumVolume = length*height*width*0.001;
    console.log(aquariumVolume*(1-percent))
}

solution(["85", "75", "47", "17"]);