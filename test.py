import json
import requests
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app,"/")

@ask.launch
def newLaunch():
	welcome = "Welcome to crypto pricer. Do you want to continue in knowing the crypto currency prices?"
	return question(welcome)

@ask.intent('YesIntent')
def getCryptoRates():
	url = "https://api.coinmarketcap.com/v1/ticker/?limit=6&convert=INR"
	req = requests.get(url)
	jsonObj = json.loads(req.content)
	price_details = ""
	for i in range(0,len(jsonObj)):
		price_details += "The price of " + jsonObj[i]['name'] + " currently is $" + jsonObj[i]['price_usd'] + ". "
	return statement(price_details)

@ask.intent('NoIntent')
def NoIntent():
	text = "Okay no problem! Will hopefully serve you soon! Bye!"
	return statement(text)

if __name__ == '__main__':
	app.run(debug=True)

#https://u8t5g0546m.execute-api.us-east-1.amazonaws.com/dev


#6D4WWyBZl04uNsIeOjUfqaaMTBLhObQaX2PWoP-o4Nns
