const fs = require('fs');

function readFile(filePath) {
    console.log('Reading file:', filePath);
    fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) {
            console.error('An error occurred:', err);
            return;
        }
        console.log('File content:', data);
    });
}

if (process.argv.length !== 3) {
    console.error('Usage: node script_name.js file_path');
} else {
    const filePath = process.argv[2];
    readFile(filePath);
}
