exec(open('util.py').read())
def har(inp):
	
	#sea =str(input("search term = "))
	
	inp = whi("search for? = ")

	url = []
	
	for a,val in enumerate(inp):
		sea = val

		#https://www.harborfreight.com/search?q=
		#tire
		#&order=price-low&current=1

		url1 = "https://www.harborfreight.com/search?q="
		url2 = sea
		url3 = "&order=price-low&current=1"
		har = url1+url2+url3
		url.append(har)	
		
		url1 = "https://www.lowes.com/search?searchTerm="
		url2 = sea
		url3 = "&sortMethod=sortBy_priceLowToHigh&inStock=1&rollUpVariants=0"
		low = url1+url2+url3
		url.append(low)

		url1 = "https://www.homedepot.com/b/Pick-Up-Today/N-5yc1vZ1z175a5/Ntk-google/Ntt-"
		url2 = sea
		url3 = "?NCNI-5&sortorder=asc&sortby=price&storeSelection=4620"
		hom = url1+url2+url3
		url.append(hom)


	if len(url)<=3:
		alt(1,1)
		opt2([url,0])

	if len(url)>3:
		num4([url,2])		


inp = []
har(inp)