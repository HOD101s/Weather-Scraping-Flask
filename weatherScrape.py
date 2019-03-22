import requests
from bs4 import BeautifulSoup

def scrape(city):
	city=city.replace(' ','-')
	URL="https://www.weather-forecast.com/locations/"+city
	webpage = requests.get(URL)
	if webpage.status_code==200:
		print("Connected")
		soup = BeautifulSoup(webpage.content,"html.parser")
		wdata=soup.find('span',class_="phrase").text
		wdata='<div class="alert alert-success" role="alert">'+wdata+'</div>'
	else:
		print("Failed to Connect")
		wdata='<div class="alert alert-danger" role="alert">The entered city is not valid</div>'
	return wdata
