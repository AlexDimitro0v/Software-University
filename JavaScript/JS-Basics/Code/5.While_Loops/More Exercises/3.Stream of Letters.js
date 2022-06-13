function solution(input) {
    let data = input[0];
    let index=1;
    let counter=0;
    let timesC=0;
    let timesO=0;
    let timesN=0;
    let word="";
    let text="";
    while(data!=="End"){
        if ((/[a-zA-Z]/).test(data)) {
            if (data === "c" || data === "o" || data === "n") {
                if(data==="c"){
                    timesC++;
                    if(timesC<2){
                        counter++;
                    }
                    else{
                        word+=data
                        data=input[index++];
                        continue;
                    }
                }
                else if(data==="o"){
                    timesO++;
                    if(timesO<2){
                        counter++;
                    }
                    else{
                        word+=data
                        data=input[index++];
                        continue;
                    }
                }
                else if (data==="n"){
                    timesN++;
                    if(timesN<2){
                        counter++;
                    }
                    else{
                        word+=data
                        data=input[index++];
                        continue;
                    }
                }

                if(counter===3){
                    counter=0;
                    timesN=0;
                    timesC=0;
                    timesO=0;
                    word=word+" ";
                    text+=word;
                    word=""
                    data=input[index++];
                    continue;
                }

            }
            else{
                word+=data;
            }
        }
        data=input[index++];
    }
    console.log(text)
}


solution(["%", "!", "c", "^", "B", "`", "o", "%", "o", "o", "M", ")", "{", "n", "\\", "A", "End"]);