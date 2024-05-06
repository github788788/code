exec(open('util.py').read())
def gd(fi,se,th,be):
	bm = str(input("month = "))
	bd = str(input("day = "))
	br = []
	br.append(bd)
	br.append(bm)
	for a in range(0,len(br)):
		if len(br[a])==1:
			br[a] = "0"+br[a]
	ch = ["y","m","d"]
	da = ["2020",br[0],br[1]]
	li = [fi,se,th]
	fi = ""
	for a in range(0,len(li)):
		for b in range(0,len(ch)):
			if li[a]==ch[b]:
				fi = fi+da[b]
				if a<2:
					fi = fi+be
				break
	#print fi
	return fi
	#bt = br[1]+"/"+br[0]+"/"+"2020"
inp = []
gd(inp)