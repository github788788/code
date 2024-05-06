exec(open('util.py').read())
def imr(inp):
	inp = inp
	from PIL import Image
	fol = os.getcwd()+"\\imr"
	lis = os.listdir(fol)
	print (fol)
	sye()
	#fil = "cat"
	typ = "jpg"
	div = 2
	for a,val in enumerate(lis):
		fil = fol+"\\"+val+"."+typ
	
		#ima = Image.open(fil+"."+typ)
		ima = Image.open(fil)
		dim = ima.size
		print(dim)
		#print(type(ima.size))
		wid = dim[0]
		hei = dim[1]
		print (wid,hei) 
		#sye()
		wid2 = int(wid/div)
		hei2 = int(hei/div)

		print(wid2,hei2)
		#sye()
		nam = fil+"_"+str(div)+"."+typ
		print (nam)
		new_image = ima.resize((wid2, hei2))
		new_image.save(nam)
inp = []
imr(inp)