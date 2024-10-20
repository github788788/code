from pprint import pprint
from pybea.client import BureauEconomicAnalysisClient

# Initalize the new Client.
bea_client = BureauEconomicAnalysisClient(api_key='3BC954F2-774A-45BB-A5C3-05F5A0482C38')
#bea_client = BureauEconomicAnalysisClient(api_key='')

# Grab the Dataset List.
dataset_list = bea_client.get_dataset_list()
pprint(dataset_list)
"""
# Define parameters to get NIPA data
params = {
    'TableName': 'T10101',  # Example table for GDP (you can adjust this as needed)
    'Frequency': 'A',       # Annual data
    'Year': '2020',         # Example year (change as needed)
    'Dataset': 'NIPA'       # Specify NIPA dataset
}

# Fetch the NIPA data
nipa_data = bea_client.get_nipa_data(**params)

# Pretty print the NIPA data
pprint(nipa_data)
"""