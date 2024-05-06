exec(open('util.py').read())
def teso(inp):

	from parsel import Selector
	cwd = os.getcwd()
	fea =cwd+"\\ear" 
	#nam = "ear-11-14"
	nam = "wmt"
	fil = nam+".html"
	loc = fea+"\\"+fil
	f =open(loc,'r',encoding='utf-8')
	doc = f.read()
	f.close()
	sel = Selector(doc)
	def ges(inp):
		bac = ""
		for a,val in enumerate(inp):
			bac = bac+val
		return bac
	"""
	par1 = "/html/body/div[5]/section/div[4]/table/tbody/tr["
	par2 = "___"
	par3 = "]/td[2]/span"
	"""

	par1 = "/html/body/div[2]/div/div[2]/div[1]/table/tbody/tr["
	par2 = "___"
	par3 = "]/td[1]"
	par4 = "/text()"
	par = [par1,par2,par3,par4]
	com = ges(par)
	par3 = "]/td[2]/a"
	par = [par1,par2,par3,par4]
	sym = ges(par)
	par3 = "]/td[7]"
	par = [par1,par2,par3,par4]
	cap = ges(par)
	get = [com,sym,cap]
	qui = 0
	num = -1
	mas = []
	while(qui<1):
		num = num+1
		app = []
		for a,val in enumerate(get):
			loc = val.replace("___",str(num))
			bac = sel.xpath(loc).getall()
			#print (type(bac))
			try:
				bac = bac[0]
			except:
				naw = "naw"
			app.append(bac)
		mas.append(app)
		#num = int(num)
		if num>5:
			if len(app[1])==0:
				break
	pri(mas)
	new = []
	new.append(["K","000"])
	new.append(["M","000000"])
	new.append(["B","000000000"])
	new.append([".",""])
	fix = 2
	for a,val in enumerate(mas):
		val2 = val[fix]
		val3 = rep([val2,new])
		try:
			val3 = int(val3)
			val3 = val3/100000000000
		except:
			naw = "naw"
		mas[a][fix]=val3
		#print(mas[a])
	pri(mas)	

inp = []
teso(inp)