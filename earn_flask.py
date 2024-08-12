exec(open('util.py').read())
main_page_html = load_data(["earn_html.html"])
from flask import Flask, request, render_template
from flask import Flask, render_template, request, jsonify
import data
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post_received = request.form['symbol']
        post_altered = post_received.upper()
        continue_reverse = load_data(["earn_500_final.xls"])
        print(continue_reverse)
        file_to_load = "earn\\"+post_altered+"_prices_around_earnings.xls"
        prices = load_data([file_to_load])
        #print(prices)
        to_send_back=[]
        for a,val in enumerate(continue_reverse):
            symbol = val[1]
            if post_altered==symbol:
                #to_send_back=val
                to_send_back.append(val)
                break
        print("to send back = ",to_send_back)
        to_send_back.append(prices)
        #end()
        return(to_send_back)    
    #return render_template('index.html')
    return(main_page_html)
if __name__ == '__main__':
    #app.run(debug=True)
    port = 5000
    url = "http://localhost:"+str(port)+"/"
    subprocess_open([0,url,"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
    app.run(debug=True, port=port)
