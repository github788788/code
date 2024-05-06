exec(open('util.py').read())
def tes7(inp):
	
	import numpy as np

	# Assume 'array_data' is your NumPy array
	#array_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	array = []
	array.append(["1","2","3"])
	array.append(["a","b","c"])

	file = "0tes7.csv"
	write_data([file,array])

	data = load_data([file])
	print(data)
	#data = load_data()
	#write_data([array])
	
	
inp = []
tes7(inp)