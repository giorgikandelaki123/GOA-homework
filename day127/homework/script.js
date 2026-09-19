// 1
let age = Number(prompt("Enter your age:"));
let price = Number(prompt("Enter ticket price:"));

if (age < 0 || price < 0) {
    console.log("Invalid age or ticket price");
} else {
    let finalPrice;

    if (age < 7) {
        finalPrice = 0;
    } else if (age < 18) {
        finalPrice = price * 0.5;
    } else if (age < 60) {
        finalPrice = price;
    } else {
        finalPrice = price * 0.7;
    }

    console.log("Final price:", finalPrice);

    if (age < 18 || age >= 60) {
        console.log("You have a discount");
    }
}


// 2
let username = "Goga";
let password = "Goa2026";
let ages = 20;

if (username === "" || password === "") {
    console.log("Fill in all fields");
} else if (username === "Goga" && password === "Goa2026") {
    console.log("Login successful");
} else if (username === "Goga") {
    console.log("Incorrect password");
} else {
    console.log("Incorrect username");
}

if (age < 18) {
    console.log("Access denied");
}


// 3
let prices = 250;
let agees = 22;
let isMember = true;

let discount = 0;

if (price < 0) {
    console.log("Invalid price");
} else {
    if (isMember && prices > 200) {
        discount = 25;
    } else if (isMember || age < 18) {
        discount = 10;
    } else if (agees >= 60 && prices > 100) {
        discount = 15;
    }

    let finalPrice = prices - discount;

    console.log("Initial price:", prices);
    console.log("Discount:", discount);
    console.log("Final price:", finalPrice);
}


// 4
let number = Number(prompt("Enter a number:"));

if (number === 0) {
    console.log("Zero");
} else if (number > 0) {
    if (number > 100) {
        console.log("Large positive number");
    } else {
        console.log("Small positive number");
    }
} else {
    if (number % 2 === 0) {
        console.log("Negative even number");
    } else {
        console.log("Negative odd number");
    }
}

if (number >= 10 && number <= 20) {
    console.log("Special range");
}


// 5
let name = "Goga";
let math = 85;
let english = 90;
let programming = 95;

let average = (math + english + programming) / 3;

console.log("Name:", name);
console.log("Average:", average);

if (math < 50 || english < 50 || programming < 50) {
    console.log("Failed");
} else if (math >= 90 && english >= 90 && programming >= 90) {
    console.log("Excellent student");
} else if (average >= 80 && math >= 70) {
    console.log("Very good student");
} else {
    console.log("Needs improvement");
}


// 6
let agee = Number(prompt("Enter your age:"));
let height = Number(prompt("Enter your height in cm:"));

if (agee < 0 || height < 0) {
    console.log("Invalid data");
} else if (agee >= 12 && height >= 140) {
    console.log("You can ride");

    if (agee >= 18 && height >= 180) {
        console.log("VIP access");
    }
} else {
    console.log("You cannot ride");
}


// 7
let numbers = 45;

if (numbers >= 10 && numbers <= 50) {
    console.log("Inside range");
} else {
    console.log("Outside range");
}

if (numbers % 2 === 0 && numbers > 20) {
    console.log("Special even number");
}

if (numbers % 2 !== 0 && numbers < 30) {
    console.log("Special odd number");
}

if (numbers === 25 || numbers === 50) {
    console.log("Exact match");
}