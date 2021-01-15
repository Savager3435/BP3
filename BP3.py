import requests
from bs4 import BeautifulSoup
#TODO, add functionality to automaticlly install prereqs 

print('Welcome to:')
print("""\
    .______   .______    ____    _______ 
    |   _  \  |   _  \  |___ \  |   ____|
    |  |_)  | |  |_)  |   __) | |  |__   
    |   _  <  |   ___/   |__ <  |   __|  
    |  |_)  | |  |       ___) | |  |____ 
    |______/  | _|      |____/  |_______|
    
    By: devastator35
""")

# still working on fixing this, currently just reads the past value so once it has been ran twice
# the "n" command doesnt work
def again():
    rerun = input("run again? Y/N: ")
    if rerun == "y" or "Y":
        pricething()
    if rerun != "y" or "Y":
        exit()


def pricething():
    crypto = input("What crypto do you want info on: ")

    if crypto == "dev_exit":
        exit()
    else:

        URL = ('https://www.coindesk.com/price/' + crypto)
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')

    price = soup.find('div', attrs={'class': 'price-large'})

    returns = soup.find('div', attrs={'class': 'percent-change-medium'})

    print(crypto)
    print("Price:", price.text)
    print("24H Returns:", returns.text)

    again()


pricething()
