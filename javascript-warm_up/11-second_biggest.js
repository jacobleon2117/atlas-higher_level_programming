#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const findSecondLargest = (arr) => {
    if (arr.length < 2) {
        return 0;
    }
    
    const sortedArr = arr.sort((a, b) => b - a);
    
    let secondLargest = sortedArr[1];
    
    return secondLargest;
};

console.log(findSecondLargest(args));
