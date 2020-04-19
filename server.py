from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!, this is a second test message"

@app.route('/hello')
@app.route('/hello/<name>')
def test(name=None):
    return render_template("helloworld.html", name=name)

