from python-bea import BEA

# Replace 'YOUR_API_KEY' with your actual BEA API key
api_key = '3BC954F2-774A-45BB-A5C3-05F5A0482C38'

# Create an instance of the BEA class
bea = BEA(api_key)

# Define parameters for the GDP data request
params = {
    'datasetname': 'NIPA',
    'TableName': 'T10101',  # GDP table
    'Frequency': 'A',  # Annual data
    'Year': '2020',  # Example year
}

# Fetch the data
gdp_data = bea.get_data(**params)

# Print the GDP data
print(gdp_data)
