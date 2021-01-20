import requests
from bs4 import BeautifulSoup
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def price(crypto):
    url = ('https://www.coindesk.com/price/' + crypto)
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    price = soup.find('div', attrs={'class': 'price-large'})
    returns = soup.find('div', attrs={'class': 'percent-change-medium'})
    net = soup.find('div', attrs={'class': 'price-change-medium'})

    global rprice
    rprice = price.text

    global rreturn
    rreturn = returns.text

    global rnet
    rnet = net.text


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global crypto

    if message.content.startswith('$supported'):
        await message.channel.send('Currently supported are: Bitcoin, Ethereum, XRP, Stellar and Chainlink')

    async def dembed(name, image, mloc):

        embed = discord.Embed(title=name)
        embed.set_thumbnail(url=image)
        embed.add_field(name='Price:', value=rprice, inline=True)
        embed.add_field(name='24H Return:', value=rreturn, inline=False)
        embed.add_field(name='24H Net:', value=rnet, inline=True)
        channel = mloc
        await message.channel.send(embed=embed)

    if message.content.startswith('$btc'):
        price('bitcoin')

        await dembed('Bitcoin','https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png', message.id)

        print('Bitcoin:', rprice)

    if message.content.startswith('$eth'):
        price('ethereum')

        await dembed('Ethereum', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg', message.id)

        print('Ethereum:', rprice)

    if message.content.startswith('$xrp'):
        price('xrp')

        await dembed('XRP', 'https://upload.wikimedia.org/wikipedia/commons/2/29/Xrp-symbol-black-128.png', message.id)

        print('XRP:', rprice)

    if message.content.startswith('$stellar'):
        price('stellar')

        await dembed('Stellar', 'https://upload.wikimedia.org/wikipedia/commons/5/56/Stellar_Symbol.png', message.id)

        print('Stellar:', rprice)

    if message.content.startswith('$chainlink'):
        price('chainlink')

        await dembed('Chainlink', 'https://d141qf1r21kfi0.cloudfront.net/static/img/coins/200x200/1975.png', message.id)

        print('Chainlink:', rprice)




client.run('YOUR TOKEN HERE')
