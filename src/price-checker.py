import requests; 
from bs4 import BeautifulSoup
import smtplib
import time 
URL = 'Enter Url'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}


def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = float(soup.find(id='priceblock_ourprice').get_text()[1:6]) 

    if(price < 70.00):
        sendMail()

    print(title.strip())
    print(price)

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email', 'qmnlclpuyjltymug')
    subject = 'The price of your chosen product has fallen'
    body = 'congrats'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'from',
        'to',
        msg
    )
    print('Email has been sent')
    server.quit()

while(True):
    checkPrice()
    time.sleep(10)
