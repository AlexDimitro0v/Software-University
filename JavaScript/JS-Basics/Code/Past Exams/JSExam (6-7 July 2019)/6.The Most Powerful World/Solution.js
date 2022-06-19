function solution(input) {
    let word = input[0];
    let index = 1;
    let mostPowerfulWord = ""
    let mostPoints = 0;

    while (word!=="End of words"){
        let firstLetter = word[0];
        let totalScore = 0;
        for (let i = 0, n = word.length; i < n; i++) {
            let asciiValue = word.charCodeAt(i);
            totalScore += asciiValue;
        }
        if (['a', 'e', 'i', 'o', 'u', 'y'].includes(firstLetter.toLowerCase())){
            totalScore = totalScore * word.length
        }
        else{
            totalScore = Math.floor(totalScore/word.length)
        }
        if (totalScore>mostPoints){
            mostPowerfulWord = word;
            mostPoints = totalScore
        }
        word = input[index++];
    }
    console.log(`The most powerful word is ${mostPowerfulWord} - ${mostPoints}`)
}

solution(["But",
    "Some",
    "People",
    "Say",
    "It's",
    "LOVE",
    "End of words"])
;