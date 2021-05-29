import requests
from bs4 import BeautifulSoup

# TODO, add functionality to automaticlly install prereqs

print('Welcome to:')
print("""\
    .______   .______    ____  
    |   _  \  |   _  \  |___ \  
    |  |_)  | |  |_)  |   __) |  
    |   _  <  |   ___/   |__ <   
    |  |_)  | |  |       ___) | 
    |______/  | _|      |____/  

    By: devastator35
""")


# Yes this is poorly done, but it does work
def again():
    global rerun
    rerun = input("run again? Y/N: ")
    if rerun == "Y" or "y" or "N" or "n":
        if rerun == 'y':
            pricething()
        else:
            exit()
    else:
        print('Error: Invalid Input')


def pricething():
    crypto = input("What crypto do you want info on: ")

    if crypto == "dev_exit":
        exit()
    else:

        url = ('https://coinmarketcap.com/currencies/' + crypto)

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    price = soup.find('div', attrs={'class': 'priceValue___11gHJ'})

    returns = soup.find('span', attrs={'class': 'sc-1v2ivon-0 fJLBDK'})

    marketcap = soup.find('div', attrs={'class': 'statsValue___2iaoZ'})
    marketcapchange = soup.find('span', attrs={'class': 'qe1dn9-0 RYkpI'})


    print(crypto + ": ")
    print("")
    print("PRICE (USD): " + price.text)
    print("24 HOUR CHANGE: " + returns.text)
    print("")
    print("VOLUME (USD): " + marketcap.text)
    print("VOLUME CHANGE: " + marketcapchange.text)
    print("")


    again()


try:
    pricething()
except AttributeError:
    print("BP3 was unable to process that input, try using a valid crypto or the full name instead of the symbol.")
