# BP3

![Bot Profile Picture](https://images-ext-2.discordapp.net/external/hFZr30Jkd-GQ-MjcxGGWcPd8lbA_Raj0YGZnQbZ0Olw/%3Fsize%3D128/https/cdn.discordapp.com/avatars/790680677078532107/07e222e50bb47958248deec3f06858f4.png)

Discord Bot and Python Script for getting crypto-prices, if you just want to webscrape the prices from the command line look at the plain "BP3" File. 
Look in the "Prerequisite" folder for the batch files, run the coresponding one to install the prerequisites for each python script  

## **BP3 Script Information** 
Have swicthed from Coindesk to CoinMarketCap. Results are webscraped from CoinMarketCap and although not always exact, prices are updated much more frequently than before. 
Although changing to CoinMarketCap has brought many advantages there is one drawback, you will have to enter the full coin name rather than just the symbol.
To instead of btc you would have to enter bitcoin.

To use it run the **prereq.batch** file to ensure you have installed all prerequisites.

There used to be an issue that would cause the re-run functionality to ignore user-input after being ran once. It has been fixed but you can still stop the script by typing
**"dev_exit"**.

## **BP3 Discord Bot Information**


Currently supports Bitcoin, Ethereum, XRP, Stellar, and Chainlink a lot more are planned

Results are webscraped from Coindesk, and results may not be 100% accurate but they will usually be pretty close to the real prices. 
CHANGING TO COINMARKETCAP IS IN PROGRESS.

When setting up the bot for your own usage you will need to create a new discord application and create your own discord bot token. The area to input your token is at the very bottom of the **DiscordBot_Public** file.  

To trigger a command use the "$" prefix. Commands are NOT case sensitive.  

![Embed example](https://i.imgur.com/zJRiC4z.png)

All of the commands for the discord bot are:
  
	  $supported- 
    displays a list of the currently supported currencies 
  
  All of the information is Price, 24 Hour Returns and 24 Hour Net Change
  
	  $btc - 
    displays an embed with various Bitcoin information
  
	  $eth - 
    displays an embed with various Ethereum information  
	  
	  $doge - 
	displays an embed with various Dogecoin information

	  $lite -
	displays an embed with various Litecoin information
	 
	  $xrp - 
    displays an embed with various XRP information
  
	  $chainlink
    displays an embed of various Chainlink Information

![enter image description here](https://i.imgur.com/nQk8ldX.png)

Converts a given amount of crypto to USD. When converting **ALL** coinbase currencies are supported
  
	  $convert {currency} {ammount} - 
    displays an embed of various Bitcoin information
        

## Adding your own crypto
Adding support for another crypto to the BP3 Discord bot is fairly easy. 
Currently the Discord bot uses Coindesk for webscraping prices but changing to a 
service with more coins is planned. (Normal BP3 has already transitioned)
Until it is changed you will be limited to Coindesk currencies. 
### Template:

    if message.content.startswith('$btc'):
    
    price('bitcoin')
    
    await dembed('Bitcoin',
    
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png',
    
    message.id)
Simply replace the bitcoin instances with whatever currency you are adding. The URL is used for adding a picture within the discord embed, so use a relavent picture.
