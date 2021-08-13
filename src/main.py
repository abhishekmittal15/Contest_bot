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
async def on_message(ctx):
    result1 = await cf_contest()
    # result2 = await ac_contest(ctx)
    await display_cf(ctx, result1)
    # await ctx.send(result2)

bot.run(bot_token)
<<<<<<< HEAD:src/main.py
=======

Heyy there can u see this message ????
>>>>>>> f553c6a8cf25cb4211f144619b6941e5e91840c9:main.py
