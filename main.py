#%%
import os 
from discord.ext import commands
from discord.ext.commands.core import command
from functions import *
from dotenv import load_dotenv
load_dotenv()
# bot_token=os.getenv("DISCORD_TOKEN")
bot_token="ODA5ODczMDQ0MTA0OTM3NTIz.YCbbDA.9mwJu9qWgMmQvfLXZ2s4DGfKsJ4"

bot=commands.Bot(command_prefix="cf ")

# Like in the client case, I had a on ready function which informed me if the bot client connected to the server or not, what is the similar function in the case of bot ?
# @bot.command(name="")
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

@bot.command(name="contests",help="Lists the upcoming codeforces contests")
async def on_message(ctx):
    result=contest_list(ctx)
    print(result)
    await ctx.send(result)

bot.run(bot_token)