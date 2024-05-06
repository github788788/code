exec(open('util.py').read())
def gen(inp):
	out = []
	inp = inp
	tex = str(rea4(["bas","py"]))
	out.append(len(tex))
	dis(out)
	ide = "\ndef"
	sta = 0
	qui =0
	inc =0
	while(qui<1):
		fin = tex.find(ide,sta)
		end = tex.find(ide,fin+1)
		new = tex[fin:end]
		nam = new[0:new.find("(")]
		nam = nam.replace("\n","")
		nam = nam.replace("def ","")
		inc = inc+1
		print (inc,fin,end,nam)
		if end<0:
			break
		fol = "C:\\Users\\-\\0c2\\"
		fil = fol+nam+".py"

		new = "exec(open('util.py').read())"+new
		new = new+"inp = []\n"+nam+"(inp)"
		out = open(fil,"w")
		out.write(new)
		out.close()
		sta = end
inp = []
gen(inp)