import requests
import json

# Replace 'YOUR_API_KEY' with your actual BEA API key
api_key = 'YOUR_API_KEY'
url = 'https://api.bea.gov/api/data/'

# Set the parameters for the request
params = {
    'UserID': '3BC954F2-774A-45BB-A5C3-05F5A0482C38',
    'method': 'GetData',
    'datasetname': 'NIPA',

}

# Make the request to the BEA API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Print the GDP data
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {response.status_code}, {response.text}")
