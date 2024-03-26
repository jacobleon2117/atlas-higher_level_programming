#!/usr/bin/node

exports.converter = function(base) {
    (function convert(num) {
        const charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        if (num >= base) {
            convert(Math.floor(num / base));
        }
        process.stdout.write(charset[num % base]);
    })(this);
    console.log();
};
