import requests
from bs4 import BeautifulSoup


crypto = input("Enter the crypto you want the price of: ")


URL = ('https://www.coindesk.com/price/' + crypto)
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

price = soup.find('div', attrs = {'class':'price-large'})

returns = soup.find('div', attrs={'class':'percent-change-medium'})

print(crypto,":")
print(price.text)
print(returns.text)

again = input("Go again? Y/N: ")

if again == "Y":
    import BP3.py
if again == "y":
    import BP3.py
if again == "n":
    exit()
if again == "N":
    exit()
