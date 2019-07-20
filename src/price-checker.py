import requests; 
from bs4 import BeautifulSoup


URL = 'https://www.amazon.co.uk/Dell-SE2219H-21-5-LED-backlit-Monitor/dp/B07HS74H5P/ref=sr_1_1?crid=969YI153MGUK&keywords=dell+se2219h+21.5+inch+ips+led-backlit+lcd+2019+monitor&qid=1563629970&s=gateway&sprefix=dell+se22%2Caps%2C185&sr=8-1'




headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle').get_text()

print(title.strip())

