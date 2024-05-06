exec(open('util.py').read())
def hob(inp):
	
	#sea =str(input("search term = "))
	
	inp = whi("search for? = ")

	url = []
	
	for a,val in enumerate(inp):
		sea = val

		url1 = "https://www.hobbylobby.com/search/?sort=price-asc&q="
		url2 = sea
		url3 = "%3Arelevance"
		lob = url1+url2+url3
		url.append(lob)

		url1 = "https://www.hobbytown.com/search?s="
		url2 = sea
		url3 = "&fl=46&o=LowestPrice&lg=fl"
		hob = url1+url2+url3
		url.append(hob)

		url1 = "https://www.michaels.com/search?q=" 
		url2 = sea 
		url3 = "&facetFilters%5B0%5D%5BfacetKey%5D=Get%20it%20Fast&facetFilters%5B0%5D%5BfacetValue%5D=Free%20Store%20Pickup&page=1&sortBy=Price%3A%20Low%20to%20High"
		mic = url1+url2+url3
		url.append(mic)


	if len(url)<=3:
		alt(1,1)
		opt2([url,0])

	if len(url)>3:
		num4([url,2])		


inp = []
hob(inp)