const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function host(inp) {
	var http = require('http');
	var querystring = require('querystring');
	var server = http.createServer().listen(3000);
	server.on('request', function (req, res) {
	    if (req.method == 'POST') {var body = '';}
	    req.on('data', function (data) {body += data;});
	    req.on('end', function () {
	        var post = querystring.parse(body);
	        console.log(post);
	        res.writeHead(200, {'Content-Type': 'text/plain'});
	        res.end('meow2 World\n');
	    });
	});
	console.log('Listening on port 3000');
//comments before final bracket
//http://localhost:3000/
}
inp = [];
host(inp)