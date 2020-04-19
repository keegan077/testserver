from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!, this is a second test message"

@app.route('/helloworld')
def test():
    return "Another test!"

