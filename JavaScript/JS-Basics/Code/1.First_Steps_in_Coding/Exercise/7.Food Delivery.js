function solution(input) {
    let chickenMenus = Number(input[0]);
    let fishMenus = Number(input[1]);
    let vegetarianMenus = Number(input[2]);

    let totalPrice = chickenMenus*10.35+fishMenus*12.40+vegetarianMenus*8.15
    let dessertPrice = totalPrice*20/100
    let bill = totalPrice+dessertPrice+2.50
    console.log(bill)
}

solution(["9", "2", "6"]);