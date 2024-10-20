exec(open('util.py').read())
def bea2(inp):
	

	import requests

	# Define the URL for the BEA API
	url = "https://apps.bea.gov/api/data/"

	# Define the parameters for the API call
	params = {
	    'UserID': 'B1B06B4B-D6F8-492B-8FE4-352501E2652A',  # Replace with your BEA API key
	    'method': 'GetReleaseDates',
	    'datasetname': 'NIPA',  # For National Income and Product Accounts
	    'ResultFormat': 'JSON'
	}

	# Make the API request
	response = requests.get(url, params=params)

	# Check if the request was successful
	if response.status_code == 200:
	    data = response.json()
	    print(data)
	else:
	    print(f"Error: {response.status_code} - {response.text}")

	
inp = []
bea2(inp)