const fs = require('fs')
const path = require('path')

const createNewDirectory = 'file/'
// new folder absolute path
const dirPath = path.join(__dirname, createNewDirectory)

if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, 0744);
    // console.log(dirPath)
}

let i;
for (i = 65; i <= 90; i++) {
    const letter = String.fromCharCode(i);
    fs.open(createNewDirectory + letter +'.txt', 'r', function (err, fd) {
        if (err) {
            fs.writeFile(createNewDirectory + letter +'.txt', letter, function (err) {
                if (err) {
                    console.log(err);
                }
                console.log("The file was saved!");
            });
        } else {
            console.log("The file exists!");
        }
    });
}




