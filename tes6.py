exec(open('util.py').read())
def tes6(inp):
	
	import pandas as pd

	# Replace 'file_path.xls' with the path to your Excel file
	file_path = '0last_edited.xls'

	# Read the Excel file into a DataFrame
	df = pd.read_excel(file_path)
	print(df)
	end()

	# Convert DataFrame to NumPy array
	array_data = df.values

	print(array_data)
	
	
inp = []
tes6(inp)