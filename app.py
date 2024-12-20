from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/length')
def length():
    return render_template('length.html')


@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/temp')
def temp():
    return render_template('temp.html')

if __name__ == '__main__':
    app.run(debug=True)
