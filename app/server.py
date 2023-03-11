from flask import Flask, render_template, url_for
from flask_login import current_user

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def index():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port=8080)

