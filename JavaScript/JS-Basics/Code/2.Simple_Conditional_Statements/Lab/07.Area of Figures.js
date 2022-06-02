function solution(input) {
    let figure = input[0];
    if (figure==="square"){
        let side = Number(input[1])
        console.log(side*side)
    }

    else if (figure ==="rectangle"){
        let a = Number(input[1])
        let b = Number(input[2])
        console.log(a*b)
    }

    else if (figure === "circle"){
        let radius = Number(input[1])
        let area = Math.pow(radius, 2) * Math.PI
        console.log(area)
    }

    else if (figure === "triangle"){
        let a = Number(input[1])
        let height = Number(input[2])
        console.log((a*height)/2)
    }
}

solution();