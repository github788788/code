exec(open('util.py').read())
#exec(open('test.py').read())

import pandas as pd

# Define the data

data = load_data(["earn_500_final.xls"])

"""
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "Los Angeles"]
]
"""

# Convert data to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Generate HTML table
html_table = df.to_html(index=False, classes='sortable', border=0)

# HTML template with DataTables
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sortable Table</title>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready(function() {{
            $('.sortable').DataTable();
        }});
    </script>
</head>
<body>
    <h1>Sortable Table</h1>
    {html_table}
</body>
</html>
"""

# Save to file
with open('sortable_table.html', 'w') as file:
    file.write(html_template)

print("HTML file with sortable table created successfully.")
