import requests
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup

# Function to scrape the cryptocurrency prices
def scrape_prices():
    # Use BeautifulSoup to parse the HTML of the website
    html = requests.get("https://www.example.com/crypto-prices").text
    soup = BeautifulSoup(html, "html.parser")

    # Extract the prices from the HTML
    prices = {}
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if tds:
            coin = tds[0].text
            price = tds[1].text
            prices[coin] = price

    return prices

# Function to send an email
def send_email(to, prices):
    # Create the email message
    msg = EmailMessage()
    msg.set_content("Cryptocurrency prices:\n\n" + "\n".join(["{}: {}".format(coin, price) for coin, price in prices.items()]))
    msg["Subject"] = "Cryptocurrency Prices"
    msg["From"] = "your_email@example.com"
    msg["To"] = to

    # Send the email
    with smtplib.SMTP("smtp.example.com") as smtp:
        smtp.login("your_email@example.com", "your_password")
        smtp.send_message(msg)

# Scrape the prices and send them to the specified email address
prices = scrape_prices()
send_email("your_email@example.com", prices)
