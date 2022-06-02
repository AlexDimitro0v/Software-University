function solution(input) {
    let book = input[0];
    let data = input[1];
    let booksSum=0;
    let index=2;
    while(data!=="No More Books"){
        if(data===book){
            console.log(`You checked ${booksSum} books and found it.`)
            return;
        }
        data=input[index];
        booksSum++;
        index++;
    }
    console.log("The book you search is not here!")
    console.log(`You checked ${booksSum} books.`)
}

solution(["The Spot",
    "Hunger Games",
    "Harry Potter",
    "Torronto",
    "Spotify",
    "No More Books"]);