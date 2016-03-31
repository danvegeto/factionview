import os
import pandas
from dateutil.parser import parse
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/politics')
def politics():
	return render_template('politics.html')

@app.route('/markets')
def markets():

	dir_name = os.path.dirname(os.path.realpath(__file__))

	prices = pandas.read_csv(dir_name + '/static/markets/data/prices.csv')

	date_str = prices['date'][0]
	date = parse(date_str)
	date_str = '{:%m/%d/%Y}'.format(date)

	return render_template('markets.html', date=date_str)

