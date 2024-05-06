exec(open('util.py').read())
def rep(inp):
	
	fil = "rep.txt"
	tex = rea([fil])
	tex2 = tex.replace("\n\n","\n")
	print(tex2)
	wri2(["rep2.txt",tex2])
	sye()


	end = 0
	beg = 0
	ide = ""
	sto = "\n"
	inc = 0
	while(end<1):
		fin = tex.find(ide,beg)
		if fin<0:
			break
		fin2 = tex.find(sto,fin)
		#lin = tex[fin:fin2]
		lin = tex[fin:fin2]+sto
		inc = inc+1
		print(inc,lin)
		tex = tex.replace(lin,"")
		beg = fin2+1

	wri2([fil,tex])

inp = []
rep(inp)