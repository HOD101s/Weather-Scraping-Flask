import requests
from bs4 import BeautifulSoup

def scrape(city):
	URL = "https://www.weather-forecast.com/locations/"
	city = '-'.join(city.split())
	URL+=city
	webpage = requests.get(URL)
	if webpage.status_code==requests.codes.ok:
		print("Connected")
		soup = BeautifulSoup(webpage.content, "html.parser")
		wdata = soup.find('span',class_="phrase").text
		wdata = '<div class="alert alert-success" role="alert">'+wdata+'</div>'
		return wdata
	else:
		print("Failed to Connect")
		return '<div class="alert alert-danger" role="alert">The entered city is not valid.</div>'