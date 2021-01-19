import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def price():
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

    global message
    message = price.text




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    def embedthing():
        embed = discord.Embed(title='BitcoinInfo')
        embed.set_thumbnail(
            url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png')
        embed.add_field(name='Price:', value=rprice, inline=True)
        embed.add_field(name='24H Return:', value=rreturn, inline=False)
        embed.add_field(name='24H Net:', value=rnet, inline=True)

    if message.content.startswith('$btc'):
        global crypto
        crypto = 'bitcoin'
        price()

        embed = discord.Embed(title='BitcoinInfo')
        embed.set_thumbnail(
            url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png')
        embed.add_field(name='Price:', value=rprice, inline=True)
        embed.add_field(name='24H Return:', value=rreturn, inline=False)
        embed.add_field(name='24H Net:', value=rnet, inline=True)
        await message.channel.send(embed=embed)

        print(rprice)


client.run('Your token here')
