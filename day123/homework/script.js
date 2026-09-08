// 2
let ricxvi1 = 20;
let ricxvi2 = 5;

console.log(ricxvi1 + ricxvi2)
console.log(ricxvi1 - ricxvi2)
console.log(ricxvi1 * ricxvi2)
console.log(ricxvi1 / ricxvi2)
console.log(ricxvi1 % ricxvi2)
console.log(ricxvi1 ** ricxvi2)

// 3
const name = "Giorgi";
const surname = "Kandelaki"
const address = "Tbilisi"

console.log(
    "My name is " + name +
    ", my surname is " + surname +
    " and I live in " + address
);

// 4
let cemisaxeli = "   Gio   "
let pasuxi = cemisaxeli.trim().toUpperCase()

console.log(pasuxi)


// 5
let teqsti = "   HELLO   "
let pasux = teqsti.trim().toLowerCase()

console.log(pasux)

// 6
let text = "   Hello,   my name is Goga.   "
let result = text.trim().replace("Hello", "Hi")

console.log(result)

// 7
let message = "JavaScript is hard. JavaScript is interesting. I love JavaScript."
let newMessage = message.replaceAll("JavaScript", "JS")

console.log(newMessage)


// 9
let username = "   GogaChalauri   "
let pasuxia = username.trim().slice(0, 5)

console.log(pasuxia)


// 10
let sityvebi = "I like cats. Cats are cute. My cat is sleeping."
let gacema = sityvebi
    .replaceAll("cats", "dogs")
    .replaceAll("Cats", "Dogs")
    .replaceAll("cat", "dog")

console.log(gacema)

// 11
let winadadeba = "JavaScript is one of the most popular programming languages"
let resulti = winadadeba.slice(0, 25) + "..."

console.log(resulti)

// 12
let code = "AB-12-CD-34"
let resultia = code.replaceAll("-", "*")
let resulto = resultia.slice(0, -2) + "##"

console.log(resulto);

// 13
let email = "   goga.chalauri@gmail.com   "

let resultebi = email.trim().split("@")[0].replaceAll(".", "_")

console.log(resultebi)

// 14
let input = "   Hello!!! My name is Goga!!! I love JS!!!   "
let results = input.trim()

results = results.replaceAll("!!!", "!")
results = results.slice(0, 20) + "..."

console.log(results)

// 15
let phone = " +995-599-12-34-56 "
let resultebis = phone.trim()

resultebis = resultebis.replaceAll("-", "")
resultebis = resultebis.slice(-9)

console.log(resultebis)

// 16
let sentence = "I love JavaScript"
let resultss = sentence.replaceAll(" ", "")

console.log(resultss.length)

// 17
let textebi = "   JavaScript is GREAT!!! JavaScript is POWERFUL!!!   "
let resultebinaxva = textebi.trim();

resultebinaxva = resultebinaxva.replaceAll("JavaScript", "JS")
resultebinaxva = resultebinaxva.replaceAll("!!!", "!")
resultebinaxva = resultebinaxva.slice(0, 30) + "..."

console.log(resultebinaxva)