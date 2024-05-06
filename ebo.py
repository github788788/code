exec(open('util.py').read())
def ebo(inp):
	inp =str(input("ebay search = "))
	url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+inp+"&_sacat=0&_sop=15"
	url = [url]
	num4([url,1])

inp = []
ebo(inp)