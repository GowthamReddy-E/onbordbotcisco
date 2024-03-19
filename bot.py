import os
from webex_bot.webex_bot import WebexBot
from cdo import *
from fmc import *
from ftd import *
from help import *
from hi import *



webex_token = os.environ["WEBEX_TOKEN"]
bot = WebexBot(webex_token)

jenkins_url = "http://localhost:8080"
username = "gowthame"
api_token = "114b5b6cc08800e772f3f7db6e1c268883"


# Registered custom command with the bot:

bot.add_command(CDFMCCommand())
bot.add_command(FMCCommand())  
bot.add_command(FTDCommand())
bot.add_command(HICommand())
bot.add_command(HelpCommand())


bot.run()