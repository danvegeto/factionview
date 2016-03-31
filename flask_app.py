import pandas
from dateutil.parser import parse
from flask import Flask, render_template

prices = pandas.read_csv('/home/danvegeto/factionview/prices.csv')

date_str = prices['date'][0]
date = parse(date_str)
date_str = '{:%m/%d/%Y}'.format(date)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/markets')
def markets():
    return render_template('markets.html', date=date_str)