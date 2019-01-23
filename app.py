import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = parsed["rates"]["GBP"]
	usd_rate = parsed["rates"]["USD"]
	eur_rate = parsed["rates"]["EUR"]
	czk_rate = parsed["rates"]["CZK"]

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

	result = czk_rate * 39

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
										result=result

										)

'''
@app.route('/convert', methods=['GET', 'POST'])
def convert():

	url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK"

	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	date = parsed["date"]

	gbp_rate = parsed["rates"]["GBP"]
	usd_rate = parsed["rates"]["USD"]
	eur_rate = parsed["rates"]["EUR"]
	czk_rate = parsed["rates"]["CZK"]

	result = input() * czk_rate

	return result
	'''


if __name__ == '__main__':
	app.run(debug=True)


'''
url = "http://data.fixer.io/api/latest?access_key=2923f7f32c2cefb141884314c1c32aff&symbols=USD,GBP,EUR,CZK"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
date = parsed["date"]

gbp_rate = parsed["rates"]["GBP"]
usd_rate = parsed["rates"]["USD"]
eur_rate = parsed["rates"]["EUR"]
czk_rate = parsed["rates"]["CZK"]
print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
print("On " + date + " EUR equals " + str(usd_rate) + " USD")
'''

'''
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weatcur.db'
db = SQLAlchemy(app)

class Currency(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		new_currency = request.form.get('currency')

		if new_currency:
			
			new_currency_obj = Currency(name=new_currency)
			db.session.add(new_currency_obj)
			db.session.commit()

	currencies = Currency.query.all()

	currency_data = []

	url = 'http://free.currencyconverterapi.com/api/v5/convert?q={}&compact=y'

	for currency in currencies:

		r = requests.get(url).json()
		print(r)
		currency = {
			'currency' : currency.name,
			'rate' : r['rates']
		}

		currency_data.append(currency)

	return render_template('index.html', currency_data=currency_data)

if __name__ == '__main__':
	app.run(debug=True)'''