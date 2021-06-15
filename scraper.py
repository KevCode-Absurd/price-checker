
#Importing libraries
import requests
from bs4 import BeautifulSoup
#Helps you send emails
import smtplib

#Fetching Url from Amazon
URL = 'https://www.amazon.in/gp/product/B08CGJ5K3V/ref=s9_acss_bw_cg_NavnOP_2d1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=ME64NBR33E6VNYXKVG7E&pf_rd_t=101&pf_rd_p=382f2f5b-6a88-4d15-b917-43c1b1ed7ce5&pf_rd_i=26297682031'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

def check_price():

    #Requesting and parsing page HTML
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Getting the title and prices from Amazon
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()

    #Prices are in rupees (₹ 78,070.00), we remove the symbol and the space and remove the decimal point and decimals.
    converted_price = (price[2:-3])

    #Remove the comma and convert to float
    converted_price_final = float(converted_price[0:2] + converted_price[3:-1])

    #Checking if the price has gone below your desired price.
    if (converted_price_final < 77000):
        send_mail()
    
    print(title.strip())
    print(converted_price_final)


#Function for sending emails
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    sever.ehlo()

    
    server.login('kevin@gmail.com', '7ipvwewxonqekvsimz')

    subject = 'Price Fell Down!'
    body = 'Check the Amazon link: https://www.amazon.in/gp/product/B08CGJ5K3V/ref=s9_acss_bw_cg_NavnOP_2d1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=ME64NBR33E6VNYXKVG7E&pf_rd_t=101&pf_rd_p=382f2f5b-6a88-4d15-b917-43c1b1ed7ce5&pf_rd_i=26297682031'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('kevin@gmail.com', 'kevin1@gmail.com', msg)

    print("Hey, an email has been sent.")

    server.quit()


check_price()