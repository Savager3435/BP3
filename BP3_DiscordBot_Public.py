import requests
from bs4 import BeautifulSoup
import discord

client = discord.Client()

version = 0.1


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#BITCOIN PRICE

URL = 'https://www.coindesk.com/price/bitcoin'
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

price = soup.find('div', attrs={'class': 'price-large'})

#ETHER PRICE
etherURL = 'https://www.coindesk.com/price/ethereum'
rEther = requests.get(etherURL)

soup = BeautifulSoup(rEther.content, 'html.parser')

Etherprice = soup.find('div', attrs={'class': 'price-large'})


#XPR PRICE
XPRUrl = 'https://www.coindesk.com/price/xrp'
rXPR = requests.get(XPRUrl)

soup = BeautifulSoup(rXPR.content, 'html.parser')

XPRprice = soup.find('div', attrs={'class': 'price-large'})


#STELLA PRICE
StellarUrl = 'https://www.coindesk.com/price/stellar'
rStellar = requests.get(StellarUrl)

soup = BeautifulSoup(rStellar.content, 'html.parser')

StellarPrice = soup.find('div', attrs={'class': 'price-large'})

#Random Stuff

SupportedCurrencys = "Bitcoin, Ether, XRP and Stellar are currently supported. " \
                     "Chainlink is planned."

@client.event
async def on_message(message):
    if message.author == client.user:
        return



    if message.content.startswith('$info'):
        await message.channel.send('This is a bot created by Devastator35#7251 to show the price of various crypto '
                                   'currencies. '
                                   'PRICES ARE NOT ALWAYS EXACT.')

    if message.content.startswith('$supported'):
        await message.channel.send(SupportedCurrencys)

    if message.content.startswith('$bitcoin'):
        Bitcoinembed = discord.Embed(title="Bitcoin Price", url="https://www.coindesk.com/price/bitcoin",
                              description="Price of Bitcoin", color=0x171717)
        Bitcoinembed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png")
        Bitcoinembed.add_field(name="BTC -> USD ", value=price.text, inline=True)
        await message.channel.send(embed=Bitcoinembed)

    if message.content.startswith('$eth'):
        EtherEmbed = discord.Embed(title="Ethereum Price", url="https://www.coindesk.com/price/ethereum",
                                   description="Price of Ethereum", color=0x171717)
        EtherEmbed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ethereum_logo_2014.svg/628px-Ethereum_logo_2014.svg.png")
    EtherEmbed.add_field(name="ETH -> USD ", value=Etherprice.text, inline=True)
    await message.channel.send(embed=EtherEmbed)

    if message.content.startswith('$stellar'):

        stellarEmbed = discord.Embed(title="Stellar Price", url="https://www.coindesk.com/price/stellar",
                                     description="Price of Stellar", color=0x171717)
        stellarEmbed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/5/56/Stellar_Symbol.png")
    stellarEmbed.add_field(name="Stellar -> USD ", value=StellarPrice.text, inline=True)
    await message.channel.send(embed=stellarEmbed)

    if message.content.startswith('$xpr'):
        await message.channel.send('XPR:')
        await message.channel.send(XPRprice.text)


# PUT YOUR DISCORD BOT TOKEN HERE 
client.run('')
