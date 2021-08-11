/* 
Write a recursive function that, given a number  n, returns the sum of the digits of the
number n.
*/

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

function Main() {
  readline.question("Enter number:", (number) => {
    console.log(typeof number);
    let sum = sumOfDigits(parseInt(number));
    console.log(`The sum of digits in the number ${number} is ${sum} `);
    readline.close();
  });
}

function sumOfDigits(number) {
  if (number <= 1) return 1;
  return number + sumOfDigits(number - 1);
}
Main();
