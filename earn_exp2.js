const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
const express = require('express');
const path = require('path');
const { exec } = require('child_process');

// Define the port and create the Express app
const app = express();
const port = 3000; // You can change this to any available port number

// Middleware to handle JSON requests
app.use(express.json());

// Basic route
//data = load_data("earn_500_final.xls")
base_html = load_data("earn_html.html")
//console.log(base_html)
app.get('/', (req, res) => {
    res.send(base_html);
});

// Start the server
app.listen(port, async () => {
    console.log(`Server is running at http://localhost:${port}/`);

    // Construct the URL
    const url = `http://localhost:${port}/`;

    // Use dynamic import to load the open module
    const { default: open } = await import('open');

    // Open the URL in Chrome
    const chromePath = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"';
    exec(`start "" ${chromePath} ${url}`, (error) => {
        if (error) {
            console.error(`Error opening Chrome: ${error.message}`);
        }
    });
});
