exec(open('util.py').read())
def low(inp):
	
	sea =str(input("search term = "))
	url1 = "https://www.lowes.com/search?searchTerm="
	url2 = sea
	url3 = "&sortMethod=sortBy_priceLowToHigh&inStock=1&rollUpVariants=0"
	url = url1+url2+url3
	#url = [url]
	#url = [url]
	num4([url,1])
	
	

inp = []
low(inp)