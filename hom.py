exec(open('util.py').read())
def hom(inp):
	
	sea =str(input("search term = "))
	url1 = "https://www.homedepot.com/b/Pick-Up-Today/N-5yc1vZ1z175a5/Ntk-google/Ntt-"
	url2 = sea
	url3 = "?NCNI-5&sortorder=asc&sortby=price&storeSelection=4620"
	url = url1+url2+url3
	#url = [url]
	num4([url,1])

	#https://www.homedepot.com/b/Tools/Pick-Up-Today/N-5yc1vZc1xyZ1z175a5/Ntk-elasticplus/Ntt-c%2Bclamp?NCNI-5&sortby=bestmatch&sortorder=none

inp = []
hom(inp)