exec(open('util.py').read())
main_page_html = load_data(["stock_new.html"])
def stock_new(inp):
	from flask import Flask, render_template
	app = Flask(__name__)
	@app.route('/')
	def index():
	    #html = load_data(["stock_new.html"])
	    return (main_page_html)



	@app.route('/handle_post', methods=['POST'])
	def process(): 
		return ("meow")

	if __name__ == '__main__':
	    port = 5000
	    url = "http://localhost:"+str(port)+"/"
	    subprocess_open([0,url,"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
	    app.run(debug=True, port=port)


 		
inp = []
stock_new(inp)


"""

	@app.route('/your_route', methods=['GET', 'POST'])
	def your_function():
	    if request.method == 'POST':
	        # Handle POST request logic here
	        # ...
	        return 'Form submitted successfully!'
	    else:
	        # Handle GET request (display form)
	        return render_template('your_template.html')	    



	    if request.method == 'POST':
	        name = request.form['name']
	        # Do something with the data
	        return redirect(url_for('greet', name=name))
	    else:
	    """
