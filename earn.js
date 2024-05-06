const fs = require('fs');
const utils = fs.readFileSync('util.js', 'utf-8');eval(utils);
function earn(inp) {
	
	//xls_loaded = load_data(["earn\\2024-04-01.xls"])
	xls_loaded = load_data(["earn\\0final.xls"])
	//pri([xls_loaded])
	for(var a=0;a<xls_loaded.length;a++){
		console.log(xls_loaded[a])
		console.log(xls_loaded[a].length)
		console.log(xls_loaded[a][3])
		}
	
	
	
//comments before final bracket
}
inp = [];
earn(inp)