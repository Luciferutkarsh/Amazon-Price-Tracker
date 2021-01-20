import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL=input('\n Kindly Enter the Amazon Product Link you want to Track the price of :- \t ')
# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"
}


# send a request to fetch HTML of the page
#userLink=input('Kindly Enter the Amazon Product Link you want to Track the price of')

# create the soup object


# change the encoding to utf-8
#print(soup.prettify())

# function to check if the price has dropped below 20,000
def check_price():
  page = requests.get(URL, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  #print(price)

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 20000):
    send_mail()

  #using strip to remove extra spaces in the title
  print(title.strip())




# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('luciferutkarsh@gmail.com', 'vwijubkqnfegukgz')

  subject = 'Price Fell Down || Lucifer Utkarsh '
  body = " Check the amazon link  "+URL+"\n It's amazing Check it out "

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'luciferutkarsh@gmail.com',
    'aditya.ankur.adi@gmail.com',
    msg
  )
  #print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

check_price()