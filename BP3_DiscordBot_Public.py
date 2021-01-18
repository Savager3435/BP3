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


    global message
    message = price.text


bot = commands.Bot(command_prefix="$")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$btc'):
        global crypto
        crypto = 'bitcoin'
        price()
        await message.channel.send(rprice)
        print (rprice)


client.run('YOUR DISCORD BOT TOKEN HERE')
