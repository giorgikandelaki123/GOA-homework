// 1)გადაიყვანეთ ტერნარში
// if (favoritePhrase === 'Love That!') {
//     console.log('I love that!');
// } else {
//     console.log("I don't love that!");
// }

let favoritePhrase
console.log(favoritePhrase === 'Love That!' ? 'I love that!' : "I don't love that!");


// 2)შექმენი ცვლადი სადაც შეინახავ რიცხვს,შეამოწმე ლუწია თ კენტი ტერნარით.
let number = 67;
console.log(number % 2 === 0 ? "ლუწია" : "კენტია");


// 3)შექმენი ცვლადი სადაც შეინახავ რიცხვს ტერნარით შეამოწმე
// თუ ეს რიცხვი არის 50 და 100 შუაში გამოიტანე --> good
// თუ ეს რიცვი არის 50 ზე ნაკლები გამოიტანე --> "not bad"
// თუ ეს რიცხვი არის 100 ზემეტი და 200 ზე ნაკლები გამოიტანე --"bed"
// სხვა შემთვევაში გამოიტანე --> "very bad"

let numberr = 75;

console.log(
    numberr >= 50 && numberr <= 100
        ? "good"
        : numberr < 50
            ? "not bad"
            : numberr > 100 && numberr < 200
                ? "bad"
                : "very bad"
);