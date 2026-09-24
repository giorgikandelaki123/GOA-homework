// 1
let number = Number(prompt("შეიყვანე რიცხვი:"));

switch (true) {
    case number > 0 && number % 2 === 0:
        console.log("positive even");
        break;

    case number > 0 && number % 2 !== 0:
        console.log("positive odd");
        break;

    case number < 0 && number % 2 === 0:
        console.log("negative even");
        break;

    case number < 0 && number % 2 !== 0:
        console.log("negative odd");
        break;

    default:
        console.log("0");
}


// 2
function sayMyInfo() {
    console.log("სახელი: გიორგი");
    console.log("გვარი: კანდელაკი");
    console.log("ასაკი: 12");
    console.log("თბილისი");
}

sayMyInfo();
sayMyInfo();
sayMyInfo();


// 3
function myInfo(name, surname, parchusPrice) {
    console.log("hello my name is " + name + " my surname is " + surname + " and parchusPrice is " + parchusPrice + "!");
}

myInfo("Giorgi", "Kandelaki", 50);
myInfo("luka", "jobava", 30);
myInfo("Gegi", "wkadua", 70);