# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/process" method="post">
            <input type="text" name="data" />
            <input type="submit" />
        </form>
    '''

@app.route('/process', methods=['POST'])
def process():
    data = request.form['data']
    return jsonify({"received_data": data})

if __name__ == '__main__':
    app.run()