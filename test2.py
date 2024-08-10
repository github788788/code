exec(open('util.py').read())
#exec(open('test.py').read())

earn_list = os.listdir("earn")
for a,val in enumerate(earn_list):
    if "historical_prices_yahoo" in val:
        array = load_data(["earn\\"+val])
        array.append(array[0])
        array = array[1:len(array)]
        array = array[::-1]
        #save_file = "earn\\"+val
        save_file = val
        write_data([save_file,array])
        
        #pri(array[0:20])


