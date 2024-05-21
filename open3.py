exec(open('util.py').read())
def open2(inp):
	import pyperclip
	#"chrome" or "firefox"
	browser = "chrome"
	browser_index = ""
	if "chrome" in browser:
		browser_index = 2
	if "firefox" in browser:
		browser_index = 3
		
	storage = []
	storage.append(["drive","https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ec=asw-drive-hero-goto&ifkv=AaSxoQyTR1jLo_CA3AV9rvOLLJccSWhQDUux4zd05KvS9Va62ODHT1DQ-FK-Zrp_AW_0Ai9sWBhB&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1223926586%3A1713908316145016&theme=mn&ddm=0"])
	storage.append(["logins","https://docs.google.com/spreadsheets/d/1pveuTlsMCB5vKhEhwBA28IidJPkOokVk/edit#gid=1983355307"])
	storage.append(["reddit_questions","https://docs.google.com/spreadsheets/d/1qrySuja-rx_LoHcXIoLAidd1C92hqyeouNv2O7iWnDs/edit#gid=0"])
	storage.append(["keep","https://keep.google.com/"])
	storage.append(["gmail","https://mail.google.com/"])
	storage.append(["proton.me","https://account.proton.me/login"])
	storage.append(["reddit_login","https://www.reddit.com/login/"])
	storage.append(["reddit_notifications","https://www.reddit.com/notifications"])
	storage.append(["twitter_login","https://twitter.com/i/flow/login"])
	storage.append(["messenger","https://www.messenger.com"])
	storage.append(["chatgpt","https://auth.openai.com/authorize?client_id=TdJIcbe16WoTHtN95nyywh5E4yOo6ItG&scope=openid+email+profile+offline_access+model.request+model.read+organization.read+organization.write&response_type=code&redirect_uri=https%3A%2F%2Fchatgpt.com%2Fapi%2Fauth%2Fcallback%2Flogin-web&audience=https%3A%2F%2Fapi.openai.com%2Fv1&device_id=aaa1f3ab-045e-4b14-869d-1b7da8b2f8ac&prompt=login&state=sAYCYO4I26abKym8hhHX3fTHfjmYa-CrMlm-w7kTJKw&code_challenge=ul1ssINYqpK70A9EDPA-HbbXAmsvRgZzN6I6V0SGKFg&code_challenge_method=S256"])

	new = []
	new.append("drive")
	new.append("https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ec=asw-drive-hero-goto&ifkv=AaSxoQyTR1jLo_CA3AV9rvOLLJccSWhQDUux4zd05KvS9Va62ODHT1DQ-FK-Zrp_AW_0Ai9sWBhB&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1223926586%3A1713908316145016&theme=mn&ddm=0")
	chrome_operations = []
	firefox_operations = []
	chrome_operations.append([copy_paste2,["media788788",1]])
	chrome_operations.append([key,[["enter",1,0,5]]])
	chrome_operations.append([copy_paste2,["Medmed1!",1]])
	chrome_operations.append([key,[["enter",1,0,0]]])
	firefox_operations.append([])
	new.append(chrome_operations)
	new.append(firefox_operations)
	storage.append(new)


	inputs = ["drive"]
	run = []
	for a,val in enumerate(inputs):
		append_operations = storage.index(val[browser_index])
		for b,valb in enumerate(append_operations):
			run.append(valb)
		run.append([hold_button,["ctrl","pagedown",1,1]])

	for a,val in enumerate(run):
		function = val[0]
		inputs = val[1]
		function(inputs)



	urls_chrome_1 = []
	urls_chrome_1.append("https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ec=asw-drive-hero-goto&ifkv=AaSxoQyTR1jLo_CA3AV9rvOLLJccSWhQDUux4zd05KvS9Va62ODHT1DQ-FK-Zrp_AW_0Ai9sWBhB&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1223926586%3A1713908316145016&theme=mn&ddm=0")
	urls_chrome_1.append("https://docs.google.com/spreadsheets/d/1pveuTlsMCB5vKhEhwBA28IidJPkOokVk/edit#gid=1983355307")
	urls_chrome_1.append("https://docs.google.com/spreadsheets/d/1qrySuja-rx_LoHcXIoLAidd1C92hqyeouNv2O7iWnDs/edit#gid=0")
	urls_chrome_1.append("https://keep.google.com/")
	urls_chrome_1.append("https://mail.google.com/")
	urls_chrome_1.append("https://account.proton.me/login")

	urls_chrome_2 = []
	urls_chrome_2.append("https://www.reddit.com/login/")
	urls_chrome_2.append("https://www.reddit.com/notifications")
	urls_chrome_2.append("https://twitter.com/i/flow/login")
	urls_chrome_2.append("https://www.messenger.com")
	urls_chrome_2.append("https://auth.openai.com/authorize?client_id=TdJIcbe16WoTHtN95nyywh5E4yOo6ItG&scope=openid+email+profile+offline_access+model.request+model.read+organization.read+organization.write&response_type=code&redirect_uri=https%3A%2F%2Fchatgpt.com%2Fapi%2Fauth%2Fcallback%2Flogin-web&audience=https%3A%2F%2Fapi.openai.com%2Fv1&device_id=aaa1f3ab-045e-4b14-869d-1b7da8b2f8ac&prompt=login&state=sAYCYO4I26abKym8hhHX3fTHfjmYa-CrMlm-w7kTJKw&code_challenge=ul1ssINYqpK70A9EDPA-HbbXAmsvRgZzN6I6V0SGKFg&code_challenge_method=S256")

	urls_firefox_1 = urls_chrome_1.sort(key=lambda x: x[0], reverse=True)
	urls_firefox_2 = urls_chrome_2.sort(key=lambda x: x[0], reverse=True)

	base_html = """

<html>
chrome/edge opener
<center><input value="Open" class="btn btn-default text" type="button" onclick="open_all();" id="button"></center>
<script type="text/javascript">
//function open_all() {
var x = []
//function open_all(){

___url_inputs___

for (var i = 0; i < x.length; i++)
window.open(x[i]);
//}
//}
</script>
</html>

	"""
	html_url_2_1 = base_html
	html_url_2_2 = base_html

	new_to_1=""
	new_to_2=""
	for a,val in enumerate(urls_chrome_1):
		new_to_1 = new_to_1+"x.push(\""+val+"\");\n"
	for a,val in enumerate(urls_chrome_2):
		new_to_2 = new_to_2+"x.push(\""+val+"\");\n"
	
	html_url_2_1=html_url_2_1.replace("___url_inputs___",new_to_1)
	html_url_2_2=html_url_2_2.replace("___url_inputs___",new_to_2)

	write_data(["open2.1.html",html_url_2_1])
	write_data(["open2.2.html",html_url_2_2])	

	#end()

	to_open_with = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	#what_to_open = "file:///C:/Users/-/code/open.html"
	what_to_open = "file:///C:/Users/--/code/open2.1.html"
	subprocess.Popen([to_open_with, "--incognito",what_to_open])

	time.sleep(2)
	key([["escape",1,0,1]])
	hold_button(["win","left",1,1])
	time.sleep(2)
	hold_button(["ctrl","pagedown",1,1])
	hold_button(["ctrl","f4",1,1])
	#hold_button(["ctrl","f4",1,1])
	time.sleep(2)
	key([["escape",1,0,1]])
	#key([["esc",1,0,1]])
	#drive
	copy_paste2(["media788788",1])
	key([["enter",1,0,5]])
	copy_paste2(["Medmed1!",1])
	key([["enter",1,0,0]])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["alt","d",1,1])
	copy_paste2(["gmail.com",1])
	key([["enter",1,0,0]])
	#hold_button(["ctrl","r",1,0])
	hold_button(["ctrl","pagedown",1,0])	
	copy_paste2(["violin78",0])
	key([["tab",1,0,0]])
	copy_paste2(["viovio",0])	
	key([["enter",1,0,0]])
	#end of first half

	what_to_open = "file:///C:/Users/--/code/open2.2.html"
	subprocess.Popen([to_open_with, "--incognito",what_to_open])

	hold_2_buttons(["ctrl","shift","n",1,1])
	time.sleep(2)
	key([["escape",1,0,1]])
	hold_button(["win","right",1,1])
	time.sleep(2)
	hold_button(["ctrl","pagedown",1,1])
	hold_button(["ctrl","pagedown",1,1])
	hold_button(["ctrl","f4",1,1])
	#hold_button(["ctrl","f4",1,1])
	time.sleep(2)
	key([["escape",1,0,1]])
	#key([["esc",1,0,1]])
	#drive



	#start second half
	#hold_button(["ctrl","pagedown",1,0])
	key([["tab",4,0,2]])
	copy_paste2(["savant78",0])
	key([["tab",1,0,1]])
	copy_paste2(["savant77",0])
	key([["enter",1,0,0]])
	hold_button(["ctrl","pagedown",1,1])
	hold_button(["ctrl","r",1,1])
	hold_button(["ctrl","pagedown",1,2])
	#key([["tab",3,0,1]])
	key([["tab",1,0,1]])		
	key([["tab",1,0,1]])		
	key([["tab",1,0,1]])		
	copy_paste2(["oversight333",0])
	key([["enter",1,0,2]])	
	copy_paste2(["Oveove1!",0])
	key([["enter",1,0,2]])	
	hold_button(["ctrl","pagedown",1,0])
	key([["tab",6,0,1]])
	copy_paste2(["violin78@protonmail.com",0])
	key([["tab",1,0,1]])	
	copy_paste2(["Viovio1!",0])
	key([["enter",1,0,0]])	

	hold_button(["ctrl","pagedown",1,0])
	#key([["tab",6,0,1]])
	copy_paste2(["violin78@protonmail.com",0])
	key([["enter",1,0,3]])	
	copy_paste2(["viovioviovio1",0])
	key([["enter",1,0,0]])	


	end()

	hold_2_buttons(["ctrl","shift","n",1,1])

	subprocess.Popen([to_open_with, "--incognito",what_to_open])
	time.sleep(2)
	key([["escape",1,0,1]])
	hold_button(["win","right",1,1])

	
inp = []
open2(inp)