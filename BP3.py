import requests
from bs4 import BeautifulSoup

print('Welcome to:')
print("""\
    .______   .______    ____    _______ 
    |   _  \  |   _  \  |___ \  |   ____|
    |  |_)  | |  |_)  |   __) | |  |__   
    |   _  <  |   ___/   |__ <  |   __|  
    |  |_)  | |  |       ___) | |  |____ 
    |______/  | _|      |____/  |_______|
         BP3 Experimental Edition
  
    By: devastator35
""")


# yes this is terrible, but it works
def again():
    rerun = input("run again? Y/N: ")
    if rerun == "y":
        pricething()
    elif rerun == "Y":
        pricething()
    elif rerun == "n":
        exit()
    elif rerun == "N":
        exit()


def pricething():
    crypto = input("What crypto do you want info on: ")
    # need to add an exception catcher here
    if crypto == "dev_exit":
        exit()
    else:

        url = ('https://www.coindesk.com/price/' + crypto)
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    price = soup.find('div', attrs={'class': 'price-large'})
    returns = soup.find('div', attrs={'class': 'percent-change-medium'})
    net = soup.find('div', attrs={'class': 'price-change-medium'})
    try:
        print("Price:", price.text)
        print("24H Returns:", returns.text)
        print("24H  Change:", net.text)
    except AttributeError:
        print('Error:', crypto, 'is not a supported currency')

    again()


pricething()
