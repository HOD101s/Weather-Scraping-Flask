from flask import Flask, render_template,request
from weatherScrape import scrape
import datetime

now = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('weatherPage.html',city="",date="",currentClimate = "")

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	return render_template('weatherPage.html',city=text,date=now.strftime("%Y-%m-%d %H:%M"),currentClimate=scrape(text))

app.run()