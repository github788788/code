exec(open('util.py').read())
exec(open('open_operations.py').read())

#pri(storage)
#exit()

browser1 = []
browser1.append("gmail")
browser1.append("drive")
browser1.append("reddit_questions")
browser1.append("logins")
browser1.append("keep")
browser1.append("chatgpt")
browser1.append("speechnotes")

browser2 = []
browser2.append("reddit_new_notifications")
browser2.append("reddit_old_notifications")
browser2.append("twitter_login")
browser2.append("messenger")
browser2.append("protonmail")
browser2.append("chatgpt")
browser2.append("speechnotes")

urls1 = []
urls2 = []
operations1 = []
operations2 = []
for a,val in enumerate(browser1):
	browser_value = val
	#print (storage_value,"---",storage_url)
	for b,valb in enumerate(storage):
		storage_value = valb[0]
		if storage_value==browser_value:
			print(storage_value,browser_value)
			urls1.append(valb[1])
			for c,valc in enumerate(valb[2]):
				operations1.append(valc)
			
			#print(valb[2])
pri(operations1)
#exit()
for a,val in enumerate(browser2):
	browser_value = val
	#print (storage_value,"---",storage_url)
	for b,valb in enumerate(storage):
		storage_value = valb[0]
		if storage_value==browser_value:
			print(storage_value,browser_value)
			urls2.append(valb[1])
			for c,valc in enumerate(valb[2]):
				operations2.append(valc)
			operations2.append([hold_button,["ctrl","pagedown",1,1]])

				
pri(urls1)
pri(urls2)
gen_html([urls1,"browser1.html"])
subprocess_open([0,"file:///C:/Users/--/code/browser1.html","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
time.sleep(1)	
hold_button(["win","left",1,1])
hold_button(["ctrl","pagedown",1,1])
hold_button(["ctrl","f4",1,1])
for a,val in enumerate(operations1):
	print(val)
	val[0](val[1])

time.sleep(1)	
gen_html([urls2,"browser2.html"])
subprocess_open([0,"file:///C:/Users/--/code/browser2.html","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])	
time.sleep(1)	
hold_button(["win","right",1,1])
hold_button(["ctrl","pagedown",1,1])
hold_button(["ctrl","f4",1,1])	
for a,val in enumerate(operations2):
	print(val)
	val[0](val[1])


#def open6(inp):
	
	
	
#inp = []
#open6(inp)