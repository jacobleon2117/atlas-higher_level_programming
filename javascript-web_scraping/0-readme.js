#!/usr/bin/node

function readFile(filePath) {
    console.log('Reading file:', filePath);
    fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) {
            console.error('An error occurred:', err);
            return;
        }
        const trimmedContent = data.trim(); // Trim leading and trailing whitespace
        console.log('File content:', trimmedContent);
    });
}
