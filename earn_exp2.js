const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
const express = require('express');
const path = require('path');
const { exec } = require('child_process');

// Define the port and create the Express app
const app = express();
const port = 3000; // You can change this to any available port number
// Middleware to parse JSON bodies
app.use(express.json());

// Middleware to parse URL-encoded bodies (for form submissions)
app.use(express.urlencoded({ extended: true }));

// Basic route
//data = load_data("earn_500_final.xls")
base_html = load_data("earn_html.html")
//console.log(base_html)
/*
app.get('/', (req, res) => {
    res.send(base_html);
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '', 'earn_html.html'));
});
*/

app.route('/')
    .get((req, res) => {
        // Serve the HTML file (assuming you have index.html in the 'public' directory)
        res.sendFile(path.join(__dirname, '','earn_html.html'));
    })
    .post((req, res) => {
        const postReceived = req.body.symbol;
        const post_altered = postReceived.toUpperCase();
        //const postAltered = postReceived.toUpperCase();
        data = load_data("earn_500_final.xls")
        //console.log(data)
        console.log(post_altered)
        let toSendBack = [];
        for (let a = 0; a < data.length; a++) {
            val = data[a]
            var symbol = val[1] 
            //console.log(symbol);
            if (symbol==post_altered){
                console.log(data[a])
                //toSendBack = [data[a]]
                //toSendBack.push(data[a])
                toSendBack = data[a]
                break
            }
        }        
        //prices = load_data("earn_500_final.xls")
        console.log(toSendBack)
        res.json(toSendBack);
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
