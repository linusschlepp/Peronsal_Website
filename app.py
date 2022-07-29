import datetime
import requests
from forms import ContactForm
from flask import Flask, render_template, request
from dateutil.relativedelta import relativedelta
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['POST'])
def contact_me():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        subject = request.form['subject']
    #  send_mail(subject=subject, message=message)
    #  return render_template('thankyou.html')
    else:
        return render_template('index.html', form=form)


def year_delta():
    print(type(relativedelta(datetime.datetime.now(), datetime.datetime(2000, 6, 14, 0, 0, 0, 0))))
    return str(relativedelta(datetime.datetime.now(), datetime.datetime(2000, 6, 14, 0, 0, 0, 0)).years)


@app.route('/')
def hello_world():  # put application's code here
    form = ContactForm()
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        subject = request.form['subject']
    return render_template('index.html', age=year_delta(), form=form)


@app.route('/test')
def test():  # put application's code here
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
