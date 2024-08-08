exec(open('util.py').read())
main_page_html = load_data(["post2.html"])
from flask import Flask, request, render_template
from flask import Flask, render_template, request, jsonify
import data
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        exec(open('data.py').read())
                
        #data2 = []
        #data2.append(["meow","cat"])
        #data2.append(["bark","dog"])

        to_send_back = data2[1][1]
        return(to_send_back)    
    #return render_template('index.html')
    return(main_page_html)

if __name__ == '__main__':
    #app.run(debug=True)
    port = 5000
    url = "http://localhost:"+str(port)+"/"
    subprocess_open([0,url,"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
    app.run(debug=True, port=port)
