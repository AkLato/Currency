import requests
import json
from flask import Flask, render_template, request, flash, redirect, url_for, make_response, send_file
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK,BTC"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = round(parsed["rates"]["GBP"], 2)
	usd_rate = round(parsed["rates"]["USD"], 2)
	eur_rate = round(parsed["rates"]["EUR"], 2)
	czk_rate = round(parsed["rates"]["CZK"], 2)
	btc_rate = round(parsed["rates"]["BTC"], 2)

	czk_btc = round(parsed["rates"]["CZK"] / parsed["rates"]["BTC"], 2)
	eur_btc = round(parsed["rates"]["EUR"] / parsed["rates"]["BTC"], 2)
	usd_btc = round(parsed["rates"]["EUR"] / parsed["rates"]["BTC"], 2)

	return render_template('index.html', gbp_rate=gbp_rate, 
										usd_rate=usd_rate, 
										eur_rate=eur_rate, 
										czk_rate=czk_rate,
										btc_rate=btc_rate,
										czk_btc=czk_btc,
										eur_btc=eur_btc,
										usd_btc=usd_btc,
										)




@app.route('/convert', methods=['GET', 'POST'])
def convert():

	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK,BTC"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = round(parsed["rates"]["GBP"], 2)
	usd_rate = round(parsed["rates"]["USD"], 2)
	eur_rate = round(parsed["rates"]["EUR"], 2)
	czk_rate = round(parsed["rates"]["CZK"], 2)
	btc_rate = round(parsed["rates"]["BTC"], 2)

	czk_btc = round(parsed["rates"]["CZK"] / parsed["rates"]["BTC"], 2)
	eur_btc = round(parsed["rates"]["EUR"] / parsed["rates"]["BTC"], 2)
	usd_btc = round(parsed["rates"]["EUR"] / parsed["rates"]["BTC"], 2)

	if request.method == "POST":
		currency = request.form.get('currencies', None)
		amount = request.form.get('amount', None, type=int)
		end_currency = request.form.get('end_currencies', None)

		if currency == end_currency:
			result = amount


		if currency == 'EUR' and end_currency == 'GBP':
			result = amount * gbp_rate

		if currency == 'EUR' and end_currency == 'Kč':
			result = amount * czk_rate

		if currency == 'EUR' and end_currency == 'USD':
			result = amount * usd_rate


		if currency == 'Kč' and end_currency == 'EUR':
			result = eur_rate/czk_rate * amount 

		if currency == 'Kč' and end_currency == 'GBP':
			result = gbp_rate/czk_rate * amount 

		if currency == 'Kč' and end_currency == 'USD':
			result = usd_rate/czk_rate * amount 


		if currency == 'USD' and end_currency == 'EUR':
			result = amount / usd_rate  

		if currency == 'USD' and end_currency == 'GBP':
			result = amount * gbp_rate

		if currency == 'USD' and end_currency == 'Kč':
			result =  amount/usd_rate * czk_rate


		if currency == 'GBP' and end_currency == 'EUR':
			result = amount / gbp_rate  

		if currency == 'GBP' and end_currency == 'Kč':
			result =  amount/gbp_rate * czk_rate

		if currency == 'GBP' and end_currency == 'USD':
			result = amount/gbp_rate * usd_rate

		result = round(result, 2)
		
		return render_template('index.html', currency=currency,
											 amount=amount,
											 end_currency=end_currency,
											 result= result,
											gbp_rate=gbp_rate, 
											usd_rate=usd_rate, 
											eur_rate=eur_rate, 
											czk_rate=czk_rate,
											czk_btc=czk_btc,
											eur_btc=eur_btc,
											usd_btc=usd_btc,
											)
	return redirect(url_for('index'))


import io
from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt


@app.route('/fig/')
def fig():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('ETH', 'USD', 'day', info='close', aggregate=1, limit=90)

	axis = fig.add_subplot(1, 1, 1)
	prices = []
	for value in r:
		price = value['close']
		price = int(price)
		prices.append(price)
	
	dates = []
	for value in r:
		date = value['time']
		date = date[5:]
		date = date[:5]
		date = date[:2] + date[2:]
		dates.append(date)

	axis.plot(dates, prices)
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::9])
	axis.tick_params(labelsize=16)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image/png')


@app.route('/figb/')
def figb():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('BTC', 'USD', 'day', info='close', aggregate=1, limit=90)

	axis = fig.add_subplot(1, 1, 1)
	prices = []
	for value in r:
		price = value['close']
		price = int(price)
		prices.append(price)
	
	dates = []
	for value in r:
		date = value['time']
		date = date[5:]
		date = date[:5]
		date = date[:2] + date[2:]
		dates.append(date)

	axis.plot(dates, prices)
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::9])
	axis.tick_params(labelsize=16)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'imageb/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='imageb/png')


@app.route('/figc/')
def figc():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('MKR', 'USD', 'day', info='close', aggregate=1, limit=90)

	axis = fig.add_subplot(1, 1, 1)
	prices = []
	for value in r:
		price = value['close']
		price = int(price)
		prices.append(price)
	
	dates = []
	for value in r:
		date = value['time']
		date = date[5:]
		date = date[:5]
		date = date[:2] + date[2:]
		dates.append(date)

	axis.plot(dates, prices)
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::9])
	axis.tick_params(labelsize=16)
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'imagec/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='imagec/png')

	
if __name__ == '__main__':
	app.run(debug=True)