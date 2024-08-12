// Execute the file content as JavaScript code
eval(fileContent);

const xlsx = require('xlsx');
const csvParse = require('csv-parse/lib/sync');

function loadData(inp) {
    const loadFile = inp[0];
    let loadedData = '';

    if (path.extname(loadFile) === '.xls' || path.extname(loadFile) === '.xlsx') {
        // Load Excel file
        const workbook = xlsx.readFile(loadFile);
        const sheet1 = workbook.Sheets[workbook.SheetNames[0]];
        const data = xlsx.utils.sheet_to_json(sheet1, { header: 1 });
        
        // Process data to remove empty values
        const newData = data.map(row => {
            const newRow = row.filter(val => val !== '');
            return newRow;
        });
        
        loadedData = newData;
    } else if (path.extname(loadFile) === '.csv') {
        // Load CSV file
        const fileContent = fs.readFileSync(loadFile, 'utf8');
        const records = csvParse(fileContent, { delimiter: ',' });
        loadedData = records;
    } else if (path.extname(loadFile) === '.json') {
        // Load JSON file
        const fileContent = fs.readFileSync(loadFile, 'utf8');
        loadedData = JSON.parse(fileContent);
    } else if (['.txt', '.py', '.js', '.html'].includes(path.extname(loadFile))) {
        // Load text file
        loadedData = fs.readFileSync(loadFile, 'utf8');
    }

    return loadedData;
}

// Example usage:
// console.log(loadData(['path/to/your/file.xlsx']));
