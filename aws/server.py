from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    text = request.form['text']
    return text.upper()

# def hello():
#     return render_template('greeting.html', say=request.form['say'], to=request.form['to'])

if __name__ == '__main__':
    if app.debug = True:
        app.run()
