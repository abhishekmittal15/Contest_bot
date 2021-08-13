#%%
import os 
import asyncio
from discord.ext import commands
from discord.ext.commands.core import command
from functions import *
from dotenv import load_dotenv
load_dotenv()
bot_token=os.getenv("DISCORD_TOKEN")

bot=commands.Bot(command_prefix=";")

# Like in the client case, I had a on ready function which informed me if the bot client connected to the server or not, what is the similar function in the case of bot ?
# @bot.command(name="")
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

@bot.command(name="contests",help="Lists the upcoming codeforces contests")
async def contests_info(ctx):
    result_ac = await cc_contest()
    await display_cc(ctx, result_ac)


@bot.listen('on_ready')
async def initialisation():
    print("CONNECTED")


bot.run(bot_token)