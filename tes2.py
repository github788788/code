exec(open('util.py').read())

hold_button(["alt","tab",1,0])
for a in range(0,10):
	hold_button(["ctrl","f4",1,0])
	key([["down",1,0,1]])