const fs = require('fs');
const path = require('path');
// Read the contents of the JavaScript file
const filePath = path.join(__dirname, 'util.js'); // Adjust the file extension and path as needed
const fileContent = fs.readFileSync(filePath, 'utf8');

const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 5000;

// Middleware to parse URL-encoded data
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Utility function to load data
const loadData = (fileNames) => {
    return fileNames.map(fileName => {
        try {
            const filePath = path.join(__dirname, fileName);
            return fs.readFileSync(filePath, 'utf8');
        } catch (error) {
            console.error(`Error reading file ${fileName}: ${error}`);
            return null;
        }
    });
};

// Serve the main page HTML
const mainPageHtml = loadData(['earn_html.html'])[0];

app.get('/', (req, res) => {
    res.send(mainPageHtml);
});

app.post('/', (req, res) => {
    const postReceived = req.body.symbol;
    const postAltered = postReceived.toUpperCase();
    const continueReverse = load_data(['earn_500_final.xls']);
    console.log(continueReverse);

    const fileToLoad = path.join('earn', `${postAltered}_prices_around_earnings.xls`);
    const prices = loadData([fileToLoad]);

    let toSendBack = [];
    for (let val of continueReverse) {
        if (val[1] === postAltered) {
            toSendBack.push(val);
            break;
        }
    }

    console.log('to send back = ', toSendBack);
    toSendBack.push(prices);

    res.json(toSendBack);
});

// Start the server and open the URL in Chrome
app.listen(port, () => {
    const url = `http://localhost:${port}/`;
    exec(`start chrome ${url}`, (err) => {
        if (err) {
            console.error(`Failed to open URL in Chrome: ${err}`);
        }
    });
    console.log(`Server is running at ${url}`);
});
