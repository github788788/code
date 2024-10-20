from pprint import pprint
from pybea.client import BureauEconomicAnalysisClient
from bea_data.bea_data import getData



# Initialize the BEA client with your API key.
bea_client = BureauEconomicAnalysisClient(api_key='3BC954F2-774A-45BB-A5C3-05F5A0482C38')


dataset_list = bea_client.get_dataset_list()
pprint(dataset_list)



# Define parameters to get NIPA data
params = {
    'dataset': 'NIPA',    # Specify the NIPA dataset
    'table': 'T10101',    # Example table for GDP
    'frequency': 'A',      # Annual data
    'year': '2020',        # Example year
}

# Fetch the NIPA data using the appropriate method
nipa_data = bea_client.getData(**params)

# Pretty print the NIPA data
pprint(nipa_data)

