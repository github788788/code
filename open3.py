exec(open('util.py').read())
exec(open('open_operations.py').read())
def open3(inp):
	import pyperclip
	#"chrome" or "firefox"
	browser = "chrome"
	browser_index = ""
	if "chrome" in browser:
		browser_index = 2
	if "firefox" in browser:
		browser_index = 3

	inputs = []
	inputs.append("drive")
	inputs.append("logins")	
	inputs.append("reddit_questions")
	inputs.append("keep")
	inputs.append("gmail")
	inputs.append("proton.me")
	inputs.append("reddit_login")
	inputs.append("reddit_notifications")
	inputs.append("twitter_login")
	inputs.append("messenger")
	inputs.append("chatgpt")

	run = []
	for a in range(0,len(inputs)):
		val = inputs[a]
		#print("val",val)
		#continue
		#generate html file to open the next 6 urls?
		if a==0 or a+1==6 or a+1==12:	
			urls_to_load = []
			for b in range(a,a+6):
				to_load = inputs[b]
				for c in range(0,len(storage)):
					if storage[c][0]==to_load:
						urls_to_load.append(storage[c][1])
						break
			gen_html([urls_to_load,"html_to_open.html"])
		#now add opening that html file to the run list?
		#if a==0:
			to_open_with = ""
			what_to_open = ""
			if "chrome" in browser:
				to_open_with = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				#what_to_open = "file:///C:/Users/-/code/open.html"
				what_to_open = "file:///C:/Users/--/code/open2.1.html"
			if "firefox" in browser:
				skip = "skip"
			run.append([subprocess_open,[5,what_to_open,to_open_with]])
			run.append([hold_button,["ctrl","pagedown",1,1]])
			run.append([hold_button,["ctrl","f4",1,1]])
		for b,valb in enumerate(storage):
			check = valb[0]
			#print(valb)
			#print(val,check)
			if check==val:
				append_operations = valb[browser_index]
				#print(append_operations)
				for c,valc in enumerate(append_operations):
					run.append(valc)
				break	
		run.append([hold_button,["ctrl","pagedown",1,1]])
	#end()
	pri(run)
	#end()
	for a,val in enumerate(run):
		function = val[0]
		inputs = val[1]
		function(inputs)

	
inp = []
open3(inp)