from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<tit>')
@app.route('/index/<tit>')
def index(tit):
    return render_template('base.html', title=tit )


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
