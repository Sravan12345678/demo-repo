import sys
sys.stdout.reconfigure(encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup
import html5lib
import smtplib
from email.message import EmailMessage

old_price = None
def trackprice():
    global old_price
    url = 'https://www.amazon.in/Asian-shoes-Sports-Firozi-Indian/dp/B01MSOPR4M/?_encoding=UTF8&pd_rd_w=188jx&content-id=amzn1.sym.432a6768-34b2-45a5-826b-a3b36997892e&pf_rd_p=432a6768-34b2-45a5-826b-a3b36997892e&pf_rd_r=GAFBAZVT7FDZT7H40N0N&pd_rd_wg=eW8Zp&pd_rd_r=ac50b552-6abc-46e3-a853-e32710bd3545&ref_=pd_hp_d_atf_dealz_mlc&th=1&psc=1'


    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}
    response = requests.get(url,headers = headers)

    soup = BeautifulSoup(response.content,'html5lib')
    mobile_price = soup.find('span',attrs={'class' : 'a-price-whole'})
    mobile_price = int(mobile_price.text)
    print(mobile_price)
    if old_price is None:
        old_price  = mobile_price
    if mobile_price > old_price:
        send_mail(mobile_price)
        return False
    return True

def send_mail(MobilePrice):
    sender_email = "pannerusravankumar1234@gmail.com"
    app_password = "nvab morf frgk sgkl"  # 16-char app password
    receiver_email = "pannerusravankumar1234@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Mobile Price Automation"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"Mobile Price is {MobilePrice}!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

while trackprice():
    print("I am tracking")