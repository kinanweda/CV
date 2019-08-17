from flask import Flask, render_template, abort, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/getin')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        host='localhost',
        port = 2000
    )