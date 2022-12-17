import requests
from bs4 import BeautifulSoup

# Set the URL of the website you want to scrape
url = "https://www.google.com/search?q=btc+price+usd&sxsrf=ALiCzsbwA1lsMqdB_7JRru-RNx70oRniGg%3A1671110687137&source=hp&ei=HyCbY56NBvS5z7sP4LWVgAo&iflsig=AJiK0e8AAAAAY5suLylD9bXQtQ3H-UOTwEQHkFzGasbs&oq=btc+price&gs_lcp=Cgdnd3Mtd2l6EAEYADIQCAAQgAQQsQMQgwEQRhCCAjILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICC4QsQMQgwE6CAgAELEDEIMBOhQILhCABBCxAxCDARDHARDRAxDUAjoICAAQgAQQsQM6EQguEIAEELEDEIMBEMcBENEDOgsILhCxAxDHARDRAzoFCC4QgAQ6CAguEIAEENQCOgQIIxAnUABYoRdg0SRoAHAAeACAAYwBiAHQBpIBAzcuMpgBAKABAQ&sclient=gws-wiz"

# Send a GET request to the website and parse the response
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the element on the page that contains the BTC price
price_element = soup.find("span", {"class": "BNeawe iBp4i AP7Wnd"})

# Extract the text from the element and convert it to a floating point number
price = float(price_element.text.replace(",", ""))

# Print the BTC price
print("The current price of BTC is: $%.2f" % price)
