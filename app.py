import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK,BTC"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = parsed["rates"]["GBP"]
	usd_rate = parsed["rates"]["USD"]
	eur_rate = parsed["rates"]["EUR"]
	czk_rate = parsed["rates"]["CZK"]
	btc_rate = parsed["rates"]["BTC"]

	gbp_rate3 = round(gbp_rate, 3)
	usd_rate3 = round(usd_rate, 3)
	eur_rate3 = round(eur_rate, 3)
	czk_rate3 = round(czk_rate, 3)

	czk_eur = eur_rate / czk_rate
	czk_gbp = gbp_rate / czk_rate
	czk_usd = usd_rate / czk_rate

	czk_eur4 = round(czk_eur, 4)
	czk_gbp4 = round(czk_gbp, 4)
	czk_usd4 = round(czk_usd, 4)

	czk_btc = czk_rate / btc_rate
	eur_btc = eur_rate / btc_rate
	usd_btc = usd_rate / btc_rate

	czk_btc2 = round(czk_btc, 2)
	eur_btc2 = round(eur_btc, 2)
	usd_btc2 = round(usd_btc, 2)
	

	return render_template('index.html', gbp_rate=gbp_rate, 
										usd_rate=usd_rate, 
										eur_rate=eur_rate, 
										czk_rate=czk_rate,
										gbp_rate3=gbp_rate3,
										usd_rate3=usd_rate3,
										eur_rate3=eur_rate3,
										czk_rate3=czk_rate3,
										czk_eur4=czk_eur4,
										czk_gbp4=czk_gbp4,
										czk_usd4=czk_usd4,
										czk_btc=czk_btc,
										eur_btc=eur_btc,
										usd_btc=usd_btc,
										czk_btc2=czk_btc2,
										eur_btc2=eur_btc2,
										usd_btc2=usd_btc2
										)

@app.route('/convert', methods=['GET', 'POST'])
def convert():

	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK,BTC"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = parsed["rates"]["GBP"]
	GBP = gbp_rate
	usd_rate = parsed["rates"]["USD"]
	USD = usd_rate
	eur_rate = parsed["rates"]["EUR"]
	EUR = eur_rate
	czk_rate = parsed["rates"]["CZK"]
	Kč = czk_rate
	btc_rate = parsed["rates"]["BTC"]

	gbp_rate3 = round(gbp_rate, 3)
	usd_rate3 = round(usd_rate, 3)
	eur_rate3 = round(eur_rate, 3)
	czk_rate3 = round(czk_rate, 3)

	czk_eur = eur_rate / czk_rate
	czk_gbp = gbp_rate / czk_rate
	czk_usd = usd_rate / czk_rate

	czk_eur4 = round(czk_eur, 4)
	czk_gbp4 = round(czk_gbp, 4)
	czk_usd4 = round(czk_usd, 4)

	czk_btc = czk_rate / btc_rate
	eur_btc = eur_rate / btc_rate
	usd_btc = usd_rate / btc_rate

	czk_btc2 = round(czk_btc, 2)
	eur_btc2 = round(eur_btc, 2)
	usd_btc2 = round(usd_btc, 2)

	if request.method == "POST":
		currency = request.form.get('currencies', None)
		amount = request.form.get('amount', None, type=int)
		end_currency = request.form.get('end_currencies', None)

		if currency and amount and end_currency!=None:

			if currency == 'EUR' and end_currency == 'EUR':
				result = amount 

			if currency == 'EUR' and end_currency == 'GBP':
				result = eur_rate * amount * gbp_rate

			if currency == 'EUR' and end_currency == 'Kč':
				result = eur_rate * amount * czk_rate

			if currency == 'EUR' and end_currency == 'USD':
				result = eur_rate * amount * usd_rate

			
			if currency == 'Kč' and end_currency == 'EUR':
				result = eur_rate/czk_rate * amount 

			if currency == 'Kč' and end_currency == 'GBP':
				result = gbp_rate/czk_rate * amount 

			if currency == 'Kč' and end_currency == 'Kč':
				result = amount 

			if currency == 'Kč' and end_currency == 'USD':
				result = usd_rate/czk_rate * amount 


			if currency == 'USD' and end_currency == 'EUR':
				result = amount / usd_rate  

			if currency == 'USD' and end_currency == 'GBP':
				result = amount * gbp_rate

			if currency == 'USD' and end_currency == 'Kč':
				result =  amount/usd_rate * czk_rate

			if currency == 'USD' and end_currency == 'USD':
				result = amount 


			if currency == 'GBP' and end_currency == 'EUR':
				result = amount / gbp_rate  

			if currency == 'GBP' and end_currency == 'GBP':
				result = amount 

			if currency == 'GBP' and end_currency == 'Kč':
				result =  amount/gbp_rate * czk_rate

			if currency == 'GBP' and end_currency == 'USD':
				result = amount/gbp_rate * usd_rate
			
			
			
			return render_template('index.html', currency=currency,
												 amount=amount,
												 end_currency=end_currency,
												 result= result,
												gbp_rate=gbp_rate, 
												usd_rate=usd_rate, 
												eur_rate=eur_rate, 
												czk_rate=czk_rate,
												gbp_rate3=gbp_rate3,
												usd_rate3=usd_rate3,
												eur_rate3=eur_rate3,
												czk_rate3=czk_rate3,
												czk_eur4=czk_eur4,
												czk_gbp4=czk_gbp4,
												czk_usd4=czk_usd4,
												czk_btc=czk_btc,
												eur_btc=eur_btc,
												usd_btc=usd_btc,
												czk_btc2=czk_btc2,
												eur_btc2=eur_btc2,
												usd_btc2=usd_btc2
												)

	return render_template('index.html' )

if __name__ == '__main__':
	app.run(debug=True)