exec(open('util.py').read())
def fit(ray):
	inp = []
	inp.append("entity = ")
	inp = fol2(inp)
	sea = inp[0][1]

	twi = "https://twitter.com/search?q="+sea+"&src=typed_query"
	fac = "https://www.facebook.com/search/top?q="+sea
	ins = "https://www.google.com/search?q=instagram "+sea

	urr = []
	urr.append(twi)
	urr.append(fac)
	urr.append(ins)
	num4([urr,1])

	#print(inp)
inp = []
fit(inp)