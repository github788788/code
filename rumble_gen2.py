exec(open('util.py').read())
def rumble_gen2(inp):
	documentation = []

	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__person_position__")
	new.append("__description__")
	new.append("__embed_url__")
	new.append("__rumble_url__")
	documentation.append(new)
	new = []
	new.append("arizona")
	new.append("lankford")
	new.append("us senator")
	new.append("130 thousand illegal votes were cast in Nevada")
	new.append("https://rumble.com/embed/v4spnbx/?pub=3i4h9q")
	new.append("https://rumble.com/v4v6n4l-nevada-130-thousand-illegal-votes-were-cast-in-nevada.html")
	documentation.append(new)
	new = []
	new.append("michigan")
	new.append("Jim Runestad")
	new.append("(R) Michigan State Senator")
	new.append("Explanation of Voter Michigan Fraud")
	new.append("https://rumble.com/embed/v4qvtai/?pub=3i4h9q")
	new.append("https://rumble.com/embed/v4qvtai/?pub=3i4h9q")
	documentation.append(new)
	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__person_position__")
	new.append("__description__")
	new.append("__embed_url__")
	new.append("__rumble_url__")
	documentation.append(new)
	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__person_position__")
	new.append("__description__")
	new.append("__embed_url__")
	new.append("__rumble_url__")
	documentation.append(new)

	documentation2 = []
	for a,val in enumerate(documentation):
		state_check = val[0]
		if "__state__" in state_check:
			continue
		match = 0
		for b in range(0,len(documentation2)):
			valb = documentation2[b]
			state_check2 = valb[0]
			if state_check==state_check2: 
				match = 1
				documentation2[b].append(val)
				break
		if match==0:
			documentation2.append([state_check,val])

	pri(documentation2)
	#end()
	final_html = """
	<html><body id="body_main">\n\t
	"""
	for a,val in enumerate(documentation2):
		state_row = 1
		state = val[0]
		final_html = final_html+"""
		<div id="
		"""+state+"-"+str(state_row)+"""
		" class="gjs-grid-row">\n\t\t<div id="
		"""+state+"-col-header"+""""
		class="gjs-grid-column"><div id="
		"""+state+"-title"+"""
		">"""+state+"\n"+"</div></div>"
		for b,valb in enumerate(val):
			try:
				embed_url= valb[4]
			except:
				continue
			final_html = final_html+"""
			<iframe id="arizona1" src="
			"""+embed_url+"""
			"></iframe>
			"""

		final_html = final_html+"</div>"
	final_html = final_html+"\n</body></html>"
	print(final_html)
inp = []
rumble_gen2(inp)