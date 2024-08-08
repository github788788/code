# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

def my_python_script(data):
    # Your Python logic here
    result = process_data(data)  # Replace with your actual logic
    return result

@app.route('/', methods=['POST'])
def handle_request():
    data = request.json
    result = my_python_script(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)