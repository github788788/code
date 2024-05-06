exec(open('util.py').read())
def bac2(inp):
	tex = rea4(["bac","txt"])
	tex = tex.replace("--- double new line is splitter between sub and bod, sub is first line, then after double new line is bod ---\n","")
	print(tex)
	ide = "\n\n"
	ide2 = tex.find(ide)
	sub = tex[0:ide2]
	bod = tex[ide2:len(tex)]
	bod = bod.replace(ide,"")
	print ("sub",sub)
	print ("bod",bod)
inp = []
bac2(inp)