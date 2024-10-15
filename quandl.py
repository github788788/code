#exec(open('util.py').read())
#def quandl(inp):
	
import sys
import quandl

data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")
sys.exit()

import quandl

# Set your API key directly
quandl.ApiConfig.api_key = 'xmefpKkxybsUgCpGhtqX'

# Fetch data using a valid dataset code
data = quandl.get("EOD/MSFT")  # Example dataset; replace with a valid dataset code

# Print the first few rows of the data
print(data.head())

	
#inp = []
#quandl(inp)