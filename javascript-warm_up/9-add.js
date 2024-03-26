#!/usr/bin/node

const add = (a, b) => {
    const result = a + b;
    console.log(result);
};

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
    add(arg1, arg2);
} else {
    console.log("Invalid input. Both arguments must be integers.");
}
