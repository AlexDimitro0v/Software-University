function solution(input) {
    let text = input[0];
    let totalSum = 0;  // make sure you initialize this to a number (i.e. 0)

    for (let i = 0; i < text.length; i ++) {
        switch(text[i]){
            case "a":
                totalSum += 1;
                break;
            case "e":
                totalSum += 2;
                break;
            case "i":
                totalSum += 3;
                break;
            case "o":
                totalSum += 4;
                break;
            case "u":
                totalSum += 5;
                break;
        }
    }
    console.log(totalSum)
}

solution(["beer"]);