exec(open('util.py').read())
def onl():

	ray = []
	
	new = []
	new.append("https://accounts.google.com/signin/v2/challenge/pwd?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=AddSession&cid=1&navigationDirection=forward&TL=AM3QAYbHi6gCreI2yQFoN3MgvZSkRzJNrRnjqex3hhloWa5OltRS6mbTrULOGQhx")
	new.append("")
	new.append("desk544")
	new.append([but3,[["enter"],0,3]])
	new.append("Desdes1!")
	ray.append(new)

	new = []
	new.append("https://mail.protonmail.com/login")
	new.append("")
	new.append("violin78")
	new.append([but3,[["tab"],0,0]])
	new.append("viovio")
	ray.append(new)

	new = []
	new.append("https://www.facebook.com") 
	new.append("")
	new.append("violin78@protonmail.com")
	new.append([but3,[["tab"],0,0]])
	#new.append("viovio")
	new.append("Viovio1!")
	ray.append(new)
	
	new = []
	new.append("https://www.quora.com/")
	new.append("")
	new.append("table65@mail.com")
	#new.append([but3,[["tab"],0,0]])
	new.append([but3,[["space"],0,0]])
	new.append("Tabtab1!")
	ray.append(new)
	
	new = []
	new.append("https://twitter.com/login")
	new.append("")
	#new.append("book34@protonmail.com")
	new.append("JamesSm70842741")
	new.append([but3,[["tab"],0,0]])
	new.append("Booboo1!")
	ray.append(new)

	
	tex2= ""
	for a in range(0,len(ray)):
		tex2 = tex2+ray[a][2]+"\n"+ray[a][4]+"\n"
		#mer.append(ray[a][1])
		#mer.append(ray[a][3])

	fil2 = "owl3.txt"
	fi = open(fil2, "w")
	fi.write(tex2)
	fi.close()
	

	url = []
	for a in range(0,len(ray)):
		url.append(ray[a][0])
	nu(url,1)
	pgu(len(url),0)
	"""inp = []
onl(inp)