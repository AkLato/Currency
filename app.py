import requests
import json
from flask import Flask, render_template, request, flash, redirect, url_for, make_response, send_file
import pandas as pd
import io
from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK,BTC,RUB,CNY,PLN"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = round(parsed["rates"]["GBP"], 2)
	usd_rate = round(parsed["rates"]["USD"], 2)
	eur_rate = round(parsed["rates"]["EUR"], 2)
	czk_rate = round(parsed["rates"]["CZK"], 2)
	btc_rate = round(parsed["rates"]["BTC"], 2)
	rub_rate = round(parsed["rates"]["RUB"], 2)
	cny_rate = round(parsed["rates"]["CNY"], 2)
	pln_rate = round(parsed["rates"]["PLN"], 2)

	czk_btc = round(parsed["rates"]["CZK"] / parsed["rates"]["BTC"], 2)
	eur_btc = round(parsed["rates"]["EUR"] / parsed["rates"]["BTC"], 2)
	usd_btc = round(parsed["rates"]["USD"] / parsed["rates"]["BTC"], 2)
	rub_btc = round(parsed["rates"]["RUB"] / parsed["rates"]["BTC"], 2)
	cny_btc = round(parsed["rates"]["CNY"] / parsed["rates"]["BTC"], 2)
	pln_btc = round(parsed["rates"]["PLN"] / parsed["rates"]["BTC"], 2)

	return render_template('index.html', gbp_rate=gbp_rate, 
										usd_rate=usd_rate, 
										eur_rate=eur_rate, 
										czk_rate=czk_rate,
										btc_rate=btc_rate,
										czk_btc=czk_btc,
										eur_btc=eur_btc,
										usd_btc=usd_btc,
										rub_rate=rub_rate,
										cny_rate=cny_rate,
										pln_rate=pln_rate,
										rub_btc=rub_btc,
										cny_btc=cny_btc,
										pln_btc=pln_btc
										)




@app.route('/convert', methods=['GET', 'POST'])
def convert():

	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK,BTC,RUB,CNY,PLN"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = round(parsed["rates"]["GBP"], 2)
	usd_rate = round(parsed["rates"]["USD"], 2)
	eur_rate = round(parsed["rates"]["EUR"], 2)
	czk_rate = round(parsed["rates"]["CZK"], 2)
	btc_rate = round(parsed["rates"]["BTC"], 2)
	rub_rate = round(parsed["rates"]["RUB"], 2)
	cny_rate = round(parsed["rates"]["CNY"], 2)
	pln_rate = round(parsed["rates"]["PLN"], 2)

	czk_btc = round(parsed["rates"]["CZK"] / parsed["rates"]["BTC"], 2)
	eur_btc = round(parsed["rates"]["EUR"] / parsed["rates"]["BTC"], 2)
	usd_btc = round(parsed["rates"]["USD"] / parsed["rates"]["BTC"], 2)
	rub_btc = round(parsed["rates"]["RUB"] / parsed["rates"]["BTC"], 2)
	cny_btc = round(parsed["rates"]["CNY"] / parsed["rates"]["BTC"], 2)
	pln_btc = round(parsed["rates"]["PLN"] / parsed["rates"]["BTC"], 2)

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

		if currency == 'EUR' and end_currency == 'RUB':
			result = amount * rub_rate

		if currency == 'EUR' and end_currency == 'CNY':
			result = amount * cny_rate

		if currency == 'EUR' and end_currency == 'PLN':
			result = amount * pln_rate



		if currency == 'Kč' and end_currency == 'EUR':
			result = eur_rate/czk_rate * amount 

		if currency == 'Kč' and end_currency == 'GBP':
			result = gbp_rate/czk_rate * amount 

		if currency == 'Kč' and end_currency == 'USD':
			result = usd_rate/czk_rate * amount 

		if currency == 'Kč' and end_currency == 'RUB':
			result = rub_rate/czk_rate * amount 

		if currency == 'Kč' and end_currency == 'CNY':
			result = cny_rate/czk_rate * amount  

		if currency == 'Kč' and end_currency == 'PLN':
			result = pln_rate/czk_rate * amount 


		if currency == 'USD' and end_currency == 'EUR':
			result = amount / usd_rate  

		if currency == 'USD' and end_currency == 'GBP':
			result = amount * gbp_rate

		if currency == 'USD' and end_currency == 'Kč':
			result =  amount/usd_rate * czk_rate

		if currency == 'USD' and end_currency == 'RUB':
			result =  amount/usd_rate * rub_rate

		if currency == 'USD' and end_currency == 'CNY':
			result =  amount/usd_rate * cny_rate

		if currency == 'USD' and end_currency == 'PLN':
			result =  amount/usd_rate * pln_rate


		if currency == 'GBP' and end_currency == 'EUR':
			result = amount / gbp_rate  

		if currency == 'GBP' and end_currency == 'Kč':
			result =  amount/gbp_rate * czk_rate

		if currency == 'GBP' and end_currency == 'USD':
			result = amount/gbp_rate * usd_rate

		if currency == 'GBP' and end_currency == 'RUB':
			result = amount/gbp_rate * rub_rate

		if currency == 'GBP' and end_currency == 'CNY':
			result = amount/gbp_rate * cny_rate

		if currency == 'GBP' and end_currency == 'PLN':
			result = amount/gbp_rate * pln_rate


		if currency == 'RUB' and end_currency == 'EUR':
			result = amount / rub_rate  

		if currency == 'RUB' and end_currency == 'Kč':
			result =  amount/rub_rate * czk_rate

		if currency == 'RUB' and end_currency == 'USD':
			result = amount/rub_rate * usd_rate

		if currency == 'RUB' and end_currency == 'GBP':
			result = amount/rub_rate * gbp_rate

		if currency == 'RUB' and end_currency == 'CNY':
			result = amount/rub_rate * cny_rate

		if currency == 'RUB' and end_currency == 'PLN':
			result = amount/rub_rate * pln_rate


		if currency == 'CNY' and end_currency == 'EUR':
			result = amount / cny_rate  

		if currency == 'CNY' and end_currency == 'Kč':
			result =  amount/cny_rate * czk_rate

		if currency == 'CNY' and end_currency == 'USD':
			result = amount/cny_rate * usd_rate

		if currency == 'CNY' and end_currency == 'GBP':
			result = amount/cny_rate * gbp_rate

		if currency == 'CNY' and end_currency == 'RUB':
			result = amount/cny_rate * rub_rate

		if currency == 'CNY' and end_currency == 'PLN':
			result = amount/cny_rate * pln_rate


		if currency == 'PLN' and end_currency == 'EUR':
			result = amount / pln_rate  

		if currency == 'PLN' and end_currency == 'Kč':
			result =  amount/pln_rate * czk_rate

		if currency == 'PLN' and end_currency == 'USD':
			result = amount/pln_rate * usd_rate

		if currency == 'PLN' and end_currency == 'GBP':
			result = amount/pln_rate * gbp_rate

		if currency == 'PLN' and end_currency == 'RUB':
			result = amount/pln_rate * rub_rate

		if currency == 'PLN' and end_currency == 'CNY':
			result = amount/pln_rate * cny_rate

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
											rub_rate=rub_rate,
											cny_rate=cny_rate,
											pln_rate=pln_rate,
											rub_btc=rub_btc,
											cny_btc=cny_btc,
											pln_btc=pln_btc
											)
	return redirect(url_for('index'))


@app.route('/fig14eth/')
def fig14eth():
	from cryptocompy import coin, price

	fig14eth = plt.figure(figsize=(15, 7.5))
	r = price.get_historical_data('ETH', 'USD', 'day', info='close', aggregate=1, limit=14)
	axis = fig14eth.add_subplot(1, 1, 1)

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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::2])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, 60, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig14eth)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image14eth/png'
	img = io.BytesIO()
	fig14eth.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image14eth/png')


@app.route('/fig30eth/')
def fig30eth():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	r = price.get_historical_data('ETH', 'USD', 'day', info='close', aggregate=1, limit=30)
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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::3])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, 60, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image30eth/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image30eth/png')


@app.route('/fig90eth/', methods=['GET', 'POST'])
def fig90eth():
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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::10])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, 60, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image90eth/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image90eth/png')


@app.route('/fig300eth/')
def fig300eth():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('ETH', 'USD', 'day', info='close', aggregate=1, limit=300)

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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::30])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image300eth/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image300eth/png')

@app.route('/fig900eth/', methods=['GET', 'POST'])
def fig900eth():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))

	r = price.get_historical_data('ETH', 'USD', 'day', info='close', aggregate=1, limit=900)

	axis = fig.add_subplot(1, 1, 1)
	prices = []
	for value in r:
		price = value['close']
		price = int(price)
		prices.append(price)
	
	dates = []
	for value in r:
		date = value['time']
		date = date[:10]
		date = date[:2] + date[2:]
		dates.append(date)

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::133])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image900eth/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)

	return send_file(img, mimetype='image900eth/png')

@app.route('/fig14btc/')
def fig14btc():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('BTC', 'USD', 'day', info='close', aggregate=1, limit=14)

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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::2])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, 2000, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image14btc/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image14btc/png')

@app.route('/fig30btc/')
def fig30btc():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('BTC', 'USD', 'day', info='close', aggregate=1, limit=30)

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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::3])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, 2000, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image30btc/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image30btc/png')


@app.route('/fig90btc/')
def fig90btc():
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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::10])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, 2000, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image90btc/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image90btc/png')

@app.route('/fig300btc/')
def fig300btc():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('BTC', 'USD', 'day', info='close', aggregate=1, limit=300)

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

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::30])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image300btc/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image300btc/png')

@app.route('/fig900btc/')
def fig900btc():
	from cryptocompy import coin, price

	fig = plt.figure(figsize=(15, 7.5))
	
	r = price.get_historical_data('BTC', 'USD', 'day', info='close', aggregate=1, limit=900)

	axis = fig.add_subplot(1, 1, 1)
	prices = []
	for value in r:
		price = value['close']
		price = int(price)
		prices.append(price)
	
	dates = []
	for value in r:
		date = value['time']
		date = date[:10]
		date = date[:2] + date[2:]
		dates.append(date)

	axis.plot(dates, prices, 'm')
	xticks = axis.get_xticks()
	axis.set_xticks(xticks[::133])
	axis.tick_params(labelsize=16)
	axis.fill_between(dates, prices, facecolor='blue', alpha=0.5)
	plt.margins(0)
	plt.style.use('seaborn-darkgrid')
	canvas = FigureCanvas(fig)
	output = io.BytesIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image900btc/png'
	img = io.BytesIO()
	fig.savefig(img)
	img.seek(0)
	return send_file(img, mimetype='image900btc/png')

	
if __name__ == '__main__':
	app.run(debug=True)