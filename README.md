# BP3

![Bot Profile Picture](https://images-ext-2.discordapp.net/external/hFZr30Jkd-GQ-MjcxGGWcPd8lbA_Raj0YGZnQbZ0Olw/%3Fsize%3D128/https/cdn.discordapp.com/avatars/790680677078532107/07e222e50bb47958248deec3f06858f4.png)

Discord Bot and Python Script for getting crypto-prices, if you just want to webscrape the prices from the command line look at the plain "BP3" File. 
Look in the "Prerequisite" folder for the batch files, run the coresponding one to install the prerequisites for each python script  

## **BP3 Script Information** 
Supports any currency coindesk supports. Results are webscraped from Coindesk and although not always exact, prices are updated everytime the script is ran.  

To use it run the prereq.batch file to install all prerequisites. Then open a new terminal where the script is located by erasing the adress of the folder and typing "cmd". 
Once the terminal is open type BP3.py and follow the directions on the screen.

Currently there is an issue that causes the re-run functionality to ignore userinput after being ran once. To stop the script you can type
"dev_exit" and the script will end. 

## **Discord Bot Information** 
Bot is being rewritten because the old code was very bad

Currently supports only Bitcoin although a lot more are planned
Results are webscraped from Coindesk, results may not be 100% accurate but they will be fairly close

When setting up the bot for your own usage you will need to create a new discord application and create your own discord bot token. The token input is at the very bottom of the 
DiscordBot_Public file.  

To trigger a command use the "$" prefix. Commands are NOT case sensitive.  

All of the commands for the discord bot are:

  $btc - 
    displays an embed of various Bitcoin information


To come soon is 24 hour returns, and improved discord embeds. 
