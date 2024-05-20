exec(open('util.py').read())
def test(inp):
	
	alt_win81(["All Videos",2])
	#cf(["monetized"])
	#key([["enter",1,1,1]])

	for a in range(0,10):
		how_many_clicks = a
		cf(["unique views"])
		key([["enter",how_many_clicks,0,1]])
		key([["esc",1,0,1]])
		key([["tab",1,0,1]])
		key([["enter",1,0,1]])
		key([["tab",4,0,1]])
		key([["enter",1,0,1]])
		click_logo4(["iframe_url_logo.png",1])
		key([["tab",1,1,1]])
		hold_button(["ctrl","c",1,1])
		click_logo4(["close2.png",1])
		start_file(["test.txt",1])
		hold_button(["ctrl","v",1,1])
		key([["enter",1,0,1]])
		alt_win81(["All Videos",1])


inp = []
test(inp)