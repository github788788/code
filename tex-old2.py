exec(open('util.py').read())
def tex(inp):

	sin = []
	sin.append(["tb","https://docs.google.com/spreadsheets/d/1E9umtnbKku8wBp-7sB3btIkVcvsE6x4QOjHTl2SgrWk/edit#gid=647722798"])
	
	sin.append(["wik","http://www.wikipedia.org"])
	sin.append(["gma","gmail.com"])
	
	sin.append(["com1","https://www.ebay.com/sch/177/i.html?_dcat=177&_fsrp=1&rt=nc&_from=R40&_nkw=8gb&_sacat=177&Features=Built%252Din%2520Microphone%7CBuilt%252Din%2520Webcam%7CBluetooth"])
	sin.append(["com2","https://www.ebay.com/sch/177/i.html?_dcat=177&_fsrp=1&rt=nc&_from=R40&_nkw=8gb&_sacat=177&Features=Built%252Din%2520Microphone%7CBuilt%252Din%2520Webcam%7CBluetooth&LH_ItemCondition=1000%7C1500%7C2000%7C2010%7C2020%7C2030%7C2500%7C3000&LH_BIN=1&LH_PrefLoc=3"])
	sin.append(["com3","https://www.ebay.com/sch/177/i.html?_dcat=177&_fsrp=1&rt=nc&_from=R40&LH_PrefLoc=3&LH_ItemCondition=1000%7C1500%7C2000%7C2010%7C2020%7C2030%7C2500%7C3000&_nkw=8gb&LH_BIN=1&_sacat=177&_sop=15&Features=Built%252Din%2520Microphone%7CBuilt%252Din%2520Webcam%7CBluetooth&Processor%2520Speed=2%252E00%252D2%252E49%2520GHz%7C2%252E50%252D2%252E99%2520GHz%7C3%252E00%252D3%252E49%2520GHz%7C3%252E50%252D3%252E99%2520GHz%7C!"])

	sin.append(["dri","https://drive.google.com/drive/my-drive"])
	sin.append(["gma","https://mail.google.com/drive/my-drive"])
	
	sin.append(["spy","https://www.tradingview.com/chart/?symbol=AMEX%3ASPY"])
	sin.append(["tra","https://www.tradingview.com/chart/?symbol=AMEX%3ASPY"])
	sin.append(["stu","https://www.librarypoint.org/room-request/"])
	sin.append(["roo","https://appointments.librarypoint.org/reserve/fx"])
	sin.append(["td","https://docs.google.com/spreadsheets/d/1TTBRfPwC-IYgAODPbZcbuXmBrladvemInp8wIUtMaW8/edit#gid=0"])
	sin.append(["tb","https://docs.google.com/spreadsheets/d/1E9umtnbKku8wBp-7sB3btIkVcvsE6x4QOjHTl2SgrWk/edit#gid=0"])
	sin.append(["qus","sv.quora.com"])
	sin.append(["kee","https://keep.google.com/"])
	sin.append(["lid","https://lindelltv.com/"])
	sin.append(["tra1","https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9374889703006423442027"])
	sin.append(["tra2","https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9361289703006479404844"])
	sin.append(["yts","https://studio.youtube.com/"])
	sin.append(["cha","https://www.librarypoint.org/ask/"])
	sin.append(["bin","http://www.bing.com"])
	sin.append(["reo",'https://www.reddit.com/user/reddit7295/'])		
	sin.append(["bie","https://www.youtube.com/watch?v=fbjnstRYIWw"])
	sin.append(["be1","https://www.youtube.com/watch?v=RYQk91Iuytw"])
	sin.append(["be2","https://www.youtube.com/watch?v=jPDiI-6b1UY"])
	sin.append(["be3","https://www.youtube.com/watch?v=wW_NwbcHHoQ"])
	sin.append(["y2m","y2mate.com"])

	dri = os.getcwd()
	dri = dri[0:dri.find("\\")]

	sin.append(["sh2",dri+"\\Users\\-\\0c\\sho.html"])
	sin.append(["web",dri+"\\Users\\-\\0c\\webf.html"])
	sin.append(["soc",dri+"\\Users\\-\\0c\\soc.html"])
	sin.append(["ale","https://www.youtube.com/watch?v=bIGwwg9E6yo"])
	sin.append(["ale","https://www.youtube.com/watch?v=lt994KTqFRI"])
	#"file:///A:/Users/-/Downloads/sho.html"
	#A:\Users\-\0c\sho.html
	sin.append(["gia","https://giantfood.com/"])
	sin.append(["caf","https://docs.google.com/spreadsheets/d/1Vud_RNLLOEAMeyHwLF0oY24Jp_s_8FqYmF8DMnyuvqA/edit?usp=drive_web&ouid=104040767578999883579"])
	sin.append(["sho","https://docs.google.com/spreadsheets/d/1huT9dhc7wjGdRBsMJ3WyASjr8pHN5S8D/edit#gid=1447211447"])
	sin.append(["gis","http://www.onlinegis.net/RichmondCountyVA/Map.html"])
	sin.append(["rum","https://rumble.com/c/BannonsWarRoom"])
	sin.append(["get","https://gettr.com/user/warroom"])
	sin.append(["insb","https://www.instagram.com/cnn/?hl=en"])
	sin.append(["fli","https://www.flixbus.com/"])
	sin.append(["new","https://www.google.com/search?q=investing.com+economic+calendar&client=firefox-b-1-d&ei=RBlHY8GNC72k5NoP4YacyAs&ved=0ahUKEwjBv6KKutv6AhU9ElkFHWEDB7kQ4dUDCA0&uact=5&oq=investing.com+economic+calendar&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBwgAEIAEEA0yCAgAEAgQBxAeMggIABAFEAcQHjoKCAAQRxDWBBCwA0oECEEYAEoECEYYAFC5AljACWCpCmgCcAF4AIAB4QGIAd4GkgEFNS4yLjGYAQCgAQHIAQjAAQE&sclient=gws-wiz"])
	sin.append(["ear","https://www.investing.com/earnings-calendar/"])
	sin.append(["fli2","https://shop.flixbus.com/search?departureCity=adcc1f7d-3bfe-471d-9946-28253814a09b&arrivalCity=eeff627f-2fda-4e75-8468-783d47955b3a&route=Washington%2C+D.C.-Boston%2C+MA&rideDate=09.07.2021&adult=1&_locale=en_US&features%5Bfeature.darken_page%5D=1&features%5Bfeature.enable_distribusion%5D=1&atb_pdid=b35b0de0-b461-46e6-a9bb-b0d2e420b946&_sp=4b259161-d799-4761-9a25-ddedbe6cc516#"])
	sin.append(["hag","hagaborg.livejournal.com"])
	sin.append(["exy","https://www.youtube.com/user/ExpressenTV/videos"])
	sin.append(["afy","https://www.youtube.com/c/aftonbladettv/videos"])
	sin.append(["ban","https://warroom.org/"])
	sin.append(["exp","expressen.se"])
	sin.append(["aft","aftonbladet.se"])
	sin.append(["upp","https://www.google.com/maps/place/Uppsala,+Sweden/@59.8332051,17.518366,30503m/data=!3m1!1e3!4m5!3m4!1s0x465fcbfb8532ab8d:0xaa4fe90a85820807!8m2!3d59.8585638!4d17.6389267"])
	sin.append(["kis","https://www.google.com/maps/place/Kista,+Stockholm,+Sweden/@59.4028122,17.9078838,6121m/data=!3m2!1e3!4b1!4m5!3m4!1s0x465f9e8955005cc9:0xffbb795f2bd6d2cf!8m2!3d59.4024341!4d17.9464824"])
	sin.append(["tad","https://www.timeanddate.com/"])
	sin.append(["gop","https://play.google.com/store?hl=en_US&gl=US"])
	sin.append(["hay","https://www.google.com/maps?q=haynesville,+va&um=1&ie=UTF-8&sa=X&ved=2ahUKEwivwa6jpMLxAhXTZc0KHeodAhoQ_AUoAXoECAEQAw"])
	sin.append(["fre","https://www.google.com/maps/place/Fredericksburg,+VA+22401/@38.2983398,-77.5249065,11909m/data=!3m1!1e3!4m5!3m4!1s0x89b6c1ebbaeae025:0x7fa6450a21a691a1!8m2!3d38.3031837!4d-77.4605399"])	
	sin.append(["was","https://www.google.com/maps/place/Washington,+DC/@38.8852879,-77.0859346,23627m/data=!3m1!1e3!4m5!3m4!1s0x89b7c6de5af6e45b:0xc2524522d4885d2a!8m2!3d38.9071923!4d-77.0368707"])
	sin.append(["sto","https://www.google.com/maps/place/Stockholm,+Sweden/@59.3258429,17.7025686,10z/data=!3m1!4b1!4m5!3m4!1s0x465f763119640bcb:0xa80d27d3679d7766!8m2!3d59.3293235!4d18.0685808"])
	sin.append(["got","https://www.google.com/maps/place/Gothenburg,+Sweden/@57.7065474,11.9681391,4067m/data=!3m1!1e3!4m5!3m4!1s0x464f8e67966c073f:0x4019078290e7c40!8m2!3d57.70887!4d11.97456"])
	sin.append(["lun","https://www.google.com/maps/place/Lund,+Sweden/@55.7067815,13.1279566,17057m/data=!3m2!1e3!4b1!4m5!3m4!1s0x4653907c03e75a3b:0x4019078290e7a70!8m2!3d55.7046601!4d13.1910073"])
	sin.append(["gco","https://github.com/GSA/code-gov"])
	sin.append(["gdo","https://github.com/deptofdefense"])
	sin.append(["edi","https://www.editey.com/"])
	sin.append(["cnn","cnn.com"])
	sin.append(["fox","foxnews.com"])
	sin.append(["str","thestreet.com"])
	sin.append(["msn","msnbc"])
	sin.append(["fed","https://www.fedex.com/fedextrack/?trknbr=773956040782&trkqual=12021~773956040782~FDEG"])
	sin.append(["edis","https://www.editey.com/file/1wTRYdual5m3r440dyN5ejZJVATovqkfW"])
	sin.append(["bla",""])
	sin.append(["you","youtube.com"])
	sin.append(["ban2","https://rumble.com/c/BannonsWarRoom"])
	sin.append(["youb","https://youtube.com/results?search_query=bianca+ingrosso"])
	sin.append(["youl","https://www.youtube.com/watch?v=PCmMgb351oo&t=312s"])
	sin.append(["par","https://www.google.com/maps/place/Paris,+France/@48.8587741,2.2069771,39684m/data=!3m1!1e3!4m5!3m4!1s0x47e66e1f06e2b70f:0x40b82c3688c9460!8m2!3d48.856614!4d2.3522219"])
	sin.append(["wea1","https://www.google.com/search?client=firefox-b-1-d&q=weather"])
	sin.append(["wea2","https://weather.com/weather/hourbyhour/l/9ef357d3fd3fd1eed1f22e93c2c56bf413feb4795f313c005d305d2d6195c9d8"])
	sin.append(["ind","indeed.com"])
	sin.append(["crw","https://washingtondc.craigslist.org"])
	sin.append(["crm","https://newyork.craigslist.org/mnh/"])

	log = []		
	log.append(['afe', '', '', '', 'https://www.aferry.com'])
	log.append(['ama', '', 'media788788@gmail.com', 'Medmed1!', 'https://www.amazon.com/gp/css/order-history?ref_=nav_AccountFlyout_order'])
	log.append(['ant', '', 'violin78', 'Medmed1!', 'https://mss.anthem.com/va/secure/claims.html#/claim'])
	log.append(['atl', '', 'mikaels', 'Vvbd63Vvbd63!', 'https://www.atlanticunionbank.com/?matchtype=p&network=g&device=c&adposition&keyword=atlantic+union+bank&gclid=CjwKCAjwoNuGBhA8EiwAFxomA-IVTR0LN_auLWy4skF8k6Yh4YotKwkTMlb1TdqlCJZsMVSXLcbPrhoCI0cQAvD_Bw'])
	log.append(['atl1', '', 'atlatl', 'Medmed1!', 'https://www.atlanticunionbank.com/?matchtype=p&network=g&device=c&adposition&keyword=atlantic+union+bank&gclid=CjwKCAjwoNuGBhA8EiwAFxomA-IVTR0LN_auLWy4skF8k6Yh4YotKwkTMlb1TdqlCJZsMVSXLcbPrhoCI0cQAvD_Bw'])
	log.append(['atl2', '', 'gocubs7', 'cubwsw', 'https://mail.protonmail.com/login'])
	log.append(['atl3', '', 'gocubs7', 'cubwsw', ''])
	log.append(['aws', '', 'violin78@protonmail.com', 'Viovio1!', 'https://github.com/login'])
	log.append(['cra', '', 'violin78@protonmail.com', 'Viovio1!', 'https://accounts.craigslist.org/login?rp=%2Flogin%2Fhome&rt='])
	log.append(['csn', '', '9007305411', '', 'https://tjanster.csn.se/bas/inloggning/mobilBankid.d'])
	log.append(['cvs', '', 'violin78@protonmail.com', 'Viovio1!', 'https://www.cvs.com/account/login'])
	log.append(['eba', '', 'media788788@gmail.com', 'Medmed1!', 'https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru'])
	log.append(['ed1', '', 'desk544', 'Desdes1!', 'https://www.editey.com'])
	log.append(['ed2', '', 'violin78@protonmail.com', 'Desdes1!', 'https://www.editey.com/file/1wTRYdual5m3r440dyN5ejZJVATovqkf'])
	log.append(['fac', '', 'violin78@protonmail.com', 'Viovio1!', 'https://www.facebook.com'])
	log.append(['fsk', '', '19900730-5411', '', 'https://idpx.forsakringskassan.se/external/authenticate/BID?TARGET=https://www.forsakringskassan.se/wps/myportal/privatpers/minasido'])
	log.append(['get', '', 'violin78@protonmail.com', 'Viovio1!', 'https://gettr.com'])
	log.append(['git', '', 'violin78@protonmail.com', 'Viovio1!', 'https://github.com/login'])
	log.append(['go1', '', 'desk544', 'passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=AddSession&cid=1&navigationDirection=forward&TL=AM3QAYbHi6gCreI2yQFoN3MgvZSkRzJNrRnjqex3hhloWa5OltRS6mbTrULOGQhx', 'https://accounts.google.com/signin/v2/challenge/pwd?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=AddSession&cid=1&navigationDirection=forward&TL=AM3QAYbHi6gCreI2yQFoN3MgvZSkRzJNrRnjqex3hhloWa5OltRS6mbTrULOGQh'])
	log.append(['go2', '', 'media475634', 'passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin', 'https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=Servicelogin'])
	log.append(['har', '', 'violin78@protonmail.com', 'Viovio1!', 'https://order.hardees.com/account/login'])
	log.append(['iex', '', 'violin78@protonmail.com', 'Viovio1!', 'https://iexcloud.io/cloud-login#'])
	log.append(['inc', '', 'violin78@protonmail.com', 'Viovio1!', 'instacart.com'])
	log.append(['ins', '', 'media788788@gmail.com', 'Medmed1!', 'instagram.com'])
	log.append(['lab', '', 'violin78@protonmail.com', 'Viovio1!', 'https://patient.labcorp.com'])
	log.append(['lin', '', 'violin78@protonmail.com', 'viovio', 'https://www.linkedin.com/login'])
	log.append(['low', '', 'violin78@protonmail.com', 'Viovio1!', 'https://www.lowes.com/u/login/oauth2/authorize?redirect_uri=https%3A%2F%2Fwww.lowes.com%2Fu%2Flogin%2Foauth2%2Fpostauthorize&scope=general-digital-access&client_id=loweswebclient&state=a0FRdUFhc2xtTXYyb0hIVjNFQ2R5S0I1VXRKNm1rWVFSeFpWenJBQUg1bFhKRnlNZkpoejB4MHN4bWgwNHVRdQ%3D%3D&code_challenge=GRXRQQKbK_o8WeXtwOOsDmk9xb17cuRIjfwca4llLs4&code_challenge_method=S256&redirect'])
	log.append(['meb', '', '', '', 'https://docs.google.com/spreadsheets/d/1HvFerQ8ctD767Oad4ZuZniNRQXD7i59b/edit?rtpof=tru'])
	log.append(['med', '', 'medicaid67', 'Medmed1!', 'https://commonhelp.dss.virginia.gov/CASWeb/faces/loginCAS.xhtml?MODULE_NAME=CMB&SERVICE_PROVIDER=COMMON_HELP&LANGUAGE=E'])
	log.append(['mwh', '', 'mwhos', 'mwhos123', 'https://mychart.mwhc.com/MyChart/Authentication/Login'])
	log.append(['nas', '', 'cello34@protonmail.com', 'Celcelcelcel1!', 'https://data.nasdaq.com/login'])
	log.append(['pat', '', 'violin78', 'Vioviovio2@', 'https://portal.patientfirst.com/Home/Inde'])
	log.append(['pla', '', 'violin78@protonmail.com', 'Viovio1!', 'https://www.flyplay.com/manage-booking'])
	log.append(['prc', '', 'gocubs7', 'cubwsw', 'https://mail.protonmail.com/login'])
	log.append(['prc2', '', 'cello34 ', 'celcel', 'https://mail.protonmail.com/login'])
	log.append(['prn', '', 'nova56', 'novnov', 'https://mail.protonmail.com/login'])
	log.append(['pro', '', 'violin78', 'viovio', 'https://mail.protonmail.com/login'])
	log.append(['prv', '', 'virginia67', 'virvir', 'https://mail.protonmail.com/login'])
	log.append(['quo', '', 'nova56@protonmail.com', 'Novnov1!', 'https://www.quora.com'])
	log.append(['rel', '', 'Emergency_Zebra_5972', 'Zebra_59', 'https://www.reddit.com/login'])
	log.append(['rel2', '', 'reddit7295', 'Redred2@', 'https://www.reddit.com/login'])
	log.append(['sk2', '', 'violin78@mail.com ', 'pas =vioviovio1', ''])
	log.append(['skv', '', '9007305411', '', 'https://m08-mg-local.idp.funktionstjanster.se/mg-local/auth/ccp11/grp/othe'])
	log.append(['sky', '', 'violin78@mail.com', 'vioviovio1', 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1605518694&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3A%2F%2Flw.skype.com%2Flogin%2Foauth%2Fproxy%3Fclient_id%3D360605%26redirect_uri%3Dhttps%253A%252F%252Fsecure.skype.com%252Fportal%252Flogin%253Freturn_url%253Dhttps%25253A%25252F%25252Fsecure.skype.com%25252Fportal%25252Foverview%26response_type%3Dpostgrant%26state%3Dceafc3abe521398a95d4997c&lc=1033&id=293290&mkt=en-US&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFlight6'])
	log.append(['sky2', '', 'violin78@mail.com', 'vioviovio1', 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1651348909&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3A%2F%2Flw.skype.com%2Flogin%2Foauth%2Fproxy%3Fclient_id%3D572381%26redirect_uri%3Dhttps%253A%252F%252Fweb.skype.com%252FAuth%252FPostHandler%26state%3Dbd4d509f-29bd-4470-8942-0f633699bce0&lc=1033&id=293290&mkt=en-US&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFlight6'])
	log.append(['spo', '', 'violin78@protonmail.com', 'viovio', 'https://accounts.spotify.com/en/login'])
	log.append(['swe', '', '', '', 'https://online.swedbank.se/app/ib/logga-i'])
	log.append(['tar', '', 'nova56@protonmail.com', 'Novnov1!', 'https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signi'])
	log.append(['tb', '', '', '', 'https://docs.google.com/spreadsheets/d/1E9umtnbKku8wBp-7sB3btIkVcvsE6x4QOjHTl2SgrWk/edit?usp=drive_web&ouid=10446590592562363995'])
	log.append(['tin', '', 'violin78@protonmail.com', 'Viovio1!', 'https://www.tinkercad.com/login'])
	log.append(['tra', '', 'violin78@protonmail.com', 'Viovio1!', 'https://www.tradingview.com'])
	log.append(['twi', '', 'media788788@gmail.com', 'Medmed1!', 'https://twitter.com/i/flow/login'])
	log.append(['unh', '', '', '', 'https://sverigeforunhcr.se/stod-oss/julklappar/gav'])
	log.append(['unh2', '', '', '', 'https://sverigeforunhcr.se/stod-oss/julklappar/gav'])
	log.append(['wal', '', 'violin78@protonmail.com', 'Viovio1!', 'https://www.walmart.com/account/login'])
	log.append(['wix', '', 'violin78@protonmail.com', 'Viovio1!', 'https://users.wix.com/signin?view=sign-up&sendEmail=true&originUrl=https:%2F%2Fwww.wix.com%2F&loginCompName=SignUp_H&postSignUp=https:%2F%2Fwww.wix.com%2Fnew%2Fintro%2F&referralInfo=SignUp_H&postLogin=https:%2F%2Fmanage.wix.com%2Faccount%2Froute&loginDialogContext=login&forceRender=tru'])
	log.append(['wor', '', 'violin78@protonmail.com', 'Viovio1!', 'https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fwordpress.com%2'])

	seq = []

	new = []
	nam = "pat"
	new = [nam]
	new.append([net,[0,["chr","r"]]])
	seq.append(new)

	

	new = []
	nam = "meb"
	new = [nam]
	seq.append(new)

	new = []
	nam = "tb"
	url = "https://docs.google.com/spreadsheets/d/1E9umtnbKku8wBp-7sB3btIkVcvsE6x4QOjHTl2SgrWk/edit?usp=drive_web&ouid=104465905925623639959"
	new = [nam]
	seq.append(new)


	new = []
	nam = "net"
	new = [nam]
	new.append([net,[0,["chr","r"]]])
	seq.append(new)

	new = []
	nam = "ner"
	new = [nam]
	new.append([net,[0,["chr","r"]]])
	seq.append(new)

	new = []
	nam = "nel"
	new = [nam]
	new.append([net,[0,["chr","s"]]])
	seq.append(new)

	new = []
	nam = "nru"
	new = [nam]
	new.append([ne72,["ru"]])
	seq.append(new)

	new = []
	nam = "ctl"
	new = [nam]
	new.append([hod3,["ctrl","9",1,0]])
	seq.append(new)

	new = []
	nam = "nlu"
	new = [nam]
	new.append([ne72,["lu"]])
	seq.append(new)

	new = []
	nam = "nrd"
	new = [nam]
	new.append([ne72,["rd"]])
	
	seq.append(new)

	new = []
	nam = "nld"
	new = [nam]
	new.append([ne72,["ld"]])	
	seq.append(new)

	new = []
	nam = "mlu"
	new = [nam]
	new.append([mot,["lu"]])
	seq.append(new)

	new = []
	nam = "mld"
	new = [nam]
	new.append([mot,["ld"]])	
	seq.append(new)

	new = []
	nam = "mru"
	new = [nam]
	new.append([mot,["ru"]])	
	seq.append(new)

	new = []
	nam = "mrd"
	new = [nam]
	new.append([mot,["rd"]])	
	seq.append(new)

	new = []
	nam = "mri"
	new = [nam]
	new.append([mot,["r"]])	
	seq.append(new)

	new = []
	nam = "mle"
	new = [nam]
	new.append([mot,["l"]])	
	seq.append(new)

	new = []
	nam = "csn"
	new = [nam]
	new.append("usn")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "med"	
	new = [nam]
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "tin"
	new = [nam]
	new.append([wai,[]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append([cf_est,["password",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "tra"
	new = [nam]
	new.append([wai,[]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append([cf_est,["password",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)	

	new = []
	nam = "wix"
	new = [nam]
	new.append([wai,[]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append([cf_est,["password",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)	

	new = []
	nam = "wor"
	url = "https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fwordpress.com%2F"
	new = [nam]
	new.append([wai,[]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append([cf_est,["password",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)	


	new = []
	nam = "rel"
	
	new = [nam]
	new.append([sle,[3]])
	new.append([cf_etst,["username"]])
	new.append("usn")
	new.append([cf_etst,["password"]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "spo"
	new = [nam]
	new.append([sle,[3]])
	new.append([hod3,["ctrl","a",1,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	new.append([sle,[3]])
	new.append([cf_ee5,["web player",0,0]])
	seq.append(new)

	new = []
	nam = "skv"
	url = "https://m08-mg-local.idp.funktionstjanster.se/mg-local/auth/ccp11/grp/other"
	new = [nam]
	new.append("usn")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "lab"
	new = [nam]
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "sk2"
	new = [nam]
	new.append([sta,["skype.lnk"]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "gom"
	new = [nam]
	new.append([sle,[1]])
	new.append([gom,[]])
	seq.append(new)

	new = []
	nam = "swe"
	new = [nam]
	new.append([sle,[1]])
	new.append("9007305411")
	new.append([cf3,["logga in",1]])
	new.append([but3,[["enter","esc"],1,0]])
	new.append([hod3,["shift","tab",1,0]])
	new.append([but3,[["enter"],0,0]])
	seq.append(new)
	
	new = []
	nam = "unh"
	
	amo = "1"
	ema = "violin78@protonmail.com"
	tel = "0731431617"
	num = "199007305411"
	car = "5168 1531 3323 9073"
	dat = "04-24"
	cod = "818"
	new = [nam]
	new.append([sle,[6]])
	new.append([cf_est3,["valfritt",1,3]])
	new.append([but3,[["down","down","tab"],0,1]])
	new.append(amo)
	new.append([but3,[["tab"],0,0]])
	new.append(ema)
	new.append([but3,[["tab"],0,0]])
	new.append(tel)
	new.append([but3,[["tab"],0,0]])
	new.append(num)
	new.append([but3,[["tab","tab","enter"],0,2]])
	new.append([cf_est3,["kortbe",1,1]])
	new.append([but3,[["down","tab","tab","enter"],0,10]])
	new.append([but3,[["tab"],0,0]])
	new.append(car)
	new.append([but3,[["tab"],0,0]])
	new.append(dat)
	new.append([but3,[["tab"],0,0]])
	new.append(cod)
	seq.append(new)
	
	new = []
	nam = "unh2"
	
	amo = "1"
	ema = "violin78@protonmail.com"
	tel = "0731431617"
	num = "199007305411"
	car = "5168 1577 6580 9269"
	dat = "11-26"
	cod = "124"
	new = [nam]
	new.append([sle,[6]])
	new.append([cf_est3,["valfritt",1,3]])
	new.append([but3,[["down","down","tab"],0,1]])
	new.append(amo)
	new.append([but3,[["tab"],0,0]])
	new.append(ema)
	new.append([but3,[["tab"],0,0]])
	new.append(tel)
	new.append([but3,[["tab"],0,0]])
	new.append(num)
	new.append([but3,[["tab","tab","enter"],0,2]])
	new.append([cf_est3,["kortbe",1,1]])
	new.append([but3,[["down","tab","tab","enter"],0,10]])
	new.append([but3,[["tab"],0,0]])
	new.append(car)
	new.append([but3,[["tab"],0,0]])
	new.append(dat)
	new.append([but3,[["tab"],0,0]])
	new.append(cod)
	seq.append(new)

	nam = "afe"
	new = [nam]
	new.append([sle,[3]])
	new.append([cf_etm3,["route",1]])
	new.append([sle,[2]])
	new.append(["Rostock - Trelleborg"])
	new.append([sle,[2]])
	new.append([but3,[["down","enter","enter"],1,0]])
	seq.append(new)
	
	nam = "cra"
	new = [nam]
	new.append([sle,[2]])
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)	
	
	new = []
	nam = "mwh"
	new = [nam]
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([sle,[1]])
	new.append([but3,[["enter"],0,0]])
	seq.append(new)
	
	new = []
	nam = "atl1"
	new = [nam]
	new.append([cf_ee5,["login",0,2]])
	new.append([but3,[["tab","tab"],0,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)	

	def atl3(inp):
		hod3(["ctrl","pageup",1,1])
		sle([5])
		cf_este3(["email me",1,2])
		hod3(["ctrl","pagedown",1,1])

	nam = "atl2"
	
	new = []
	new = [nam]
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([hod3,["ctrl","pageup",1,1]])
	new.append([sle,[5]])
	new.append([cf_este3,["email me",1,2]])
	new.append([hod3,["ctrl","pagedown",1,1]])

	seq.append(new)	

	nam = "ins"
	
	new = []
	new = [nam]
	new.append([cf_et5,["phone",1,0]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)	

	nam = "inc"
	
	new = []
	new = [nam]
	#cf_etste3(["log in",0,2])
	new.append([sle,[3]])
	new.append([cf_etste3,["log in"]])
	new.append([sle,[2]])
	new.append([key,[["tab",2,0,1]]])
	
	
	#cf_etste3(["log in"])
	
	#new.append([but3,[["tab","tab"],0,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)	

	nam = "eba"
	
	new = []
	new = [nam]
	new.append([sle,[3]])
	new.append([cf_et5,["account",1,1]])
	new.append("usn")
	new.append([but3,[["enter"],0,2]])
	new.append("pas")
	new.append([but3,[["enter"],0,2]])
	seq.append(new)

	nam = "pla"
	
	new = []
	new = [nam]
	new.append([sle,[3]])
	new.append([key,[["tab",3,0,1]]])
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,1]])
	seq.append(new)

	nam = "har"
	
	new = []
	new = [nam]
	new.append([sle,[3]])
	new.append([cf_et5,["email",1,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,2]])
	new.append("pas")
	new.append([key,[["tab",2,0,1],["space",1,0,3]]])
	new.append([key,[["tab",4,0,1],["enter",1,0,0]]])
	seq.append(new)

	nam = "git"
	
	new = []
	new = [nam]
	new.append([sle,[3]])
	new.append("usn")
	new.append([but3,[["tab"],0,2]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	nam = "aws"
	
	new = []
	new = [nam]
	new.append([sle,[3]])
	new.append("usn")
	new.append([but3,[["tab"],0,2]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	nam = "cvs"	
	new = []
	new = [nam]
	new.append([sle,[3]])
	new.append([cf_et5,["address",1,1]])
	new.append("book56@protonmail.com")
	new.append([but3,[["enter"],0,2]])
	new.append([but3,[["tab"],0,1]])
	new.append("Booboo1!")
	new.append([but3,[["enter"],0,2]])
	seq.append(new)

	nam = "nas"
	new = [nam]
	new.append([cf_et5,["email",1,1]])
	new.append("usn")
	new.append([key,[["tab",1,0,1],["enter",1,0,1]]])
	new.append("pas")
	new.append([key,[["tab",1,0,1],["enter",1,0,1]]])
	seq.append(new)

	nam = "ama"
	new = []
	new = [nam]
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)
	
	nam = "ed1"
	url = "file:///A:/Users/-/0c/webf.html"
	new = []
	new = [nam]
	new.append([cf_ee5,["login",0,2]])
	seq.append(new)

	nam = "ed2"
	new = []
	new = [nam]
	new.append([hod3,["ctrl","r",1,2]])
	seq.append(new)

	new = []
	nam = "lin"
	new = [nam]
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	new = []
	nam = "wal"
	new = [nam]
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	seq.append(new)

	usn = "---"
	pas = "---"
	url = "---"

	ope = []
	ope.append("pro")
	ope.append("ins")
	ope.append("go2")	
	ope.append("twi")
	ope.append("fac")
	ope.append("rel")	

	ope2 = []
	ope2.append("caf")
	ope2.append("kee")
	ope2.append("gma")
	for a,val in enumerate(ope):
		ope2.append(val)

	#run = whi("to run?")
	run = ["ope"]
	print(run)
	if "ope" in run:
		run.pop(run.index("ope"))
		run = run+ope
	if "ope2" in run:
		run.pop(run.index("ope2"))
		run = run+ope2
	mas =[]

	pri(seq)
	sye()

	for a,val in enumerate(run):
		for b,valb in enumerate(seq):
			#print("valb",valb)
			mat = valb[0]
			if val==mat:
				for c in range(1,len(valb)):
					mas.append(valb[c])
				for c,valc in enumerate(log):
					matc = valc[0]
					if matc==val:
						usn = valc[2]
						pas = valc[3]
						url = valc[4]
						break
				#break

	pri(mas)
	pri(run)
	sye()
	for a,val in enumerate(mas):
		func = val[0]
		inp2 = val[1]
		func(inp2)

inp = []
tex(inp)