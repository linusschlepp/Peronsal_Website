import datetime

from flask import Flask, render_template
from dateutil.relativedelta import relativedelta

app = Flask(__name__)


def year_delta():
    print(type(relativedelta(datetime.datetime.now(), datetime.datetime(2000,6,14,0,0,0,0))))
    return str(relativedelta(datetime.datetime.now(), datetime.datetime(2000,6,14,0,0,0,0)).years)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', age=year_delta())

@app.route('/test')
def test():  # put application's code here
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
