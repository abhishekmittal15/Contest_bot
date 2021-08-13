#%%
import os 
import json
from discord.ext import commands
from discord.ext.commands.core import command
from functions import *
from dotenv import load_dotenv
import threading
load_dotenv()
bot_token=os.getenv("DISCORD_TOKEN")
bot=commands.Bot(command_prefix=";")

site_list = {"cf":"codeforces", "cc":"codechef" ,"ac":"atcoder"}

# Like in the client case, I had a on ready function which informed me if the bot client connected to the server or not, what is the similar function in the case of bot ?
# @bot.command(name="")
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

@bot.command(name="contests",help="Lists the upcoming codeforces contests")
async def contests_info(ctx):
    
    result_cf = await cf_contest()
    await display_cf(ctx, result_cf)
    
    result_ac = await cc_contest()
    await display_cc(ctx, result_ac)


@bot.command(name="conf", help="Configure the Channels to be used with different websites")
async def configure(ctx, website, channel):

    if website not in site_list:
        codes = ""
        for code in site_list:
            codes += f"`{code}` ({site_list[code]})\n"
        await ctx.send(f"The website code `{website}` does not exist.\nAvailable codes are:\n{codes}")
        return

    channel_id = channel[2:-1]

    f = open('data.json', "r")
    data = json.loads(f.read())
    f.close()
    
    if str(ctx.message.guild.id) not in data["guilds"]:
        data["guilds"][str(ctx.message.guild.id)] = {}    

    data["guilds"][str(ctx.message.guild.id)][website] = channel_id
    
    with open('data.json', 'w') as fp:
        json.dump(data, fp)

    await ctx.send(f"Updates for {site_list[website]} contests will be given in {channel}")


def checkTime():
    # This function runs periodically every 1 second
    threading.Timer(5, checkTime).start()

    now = datetime.now()

    f = open('data.json', "r")
    data = json.loads(f.read())
    f.close()

    data["last_updated"] = str(now.date())

    with open('data.json', 'w') as fp:
        json.dump(data, fp)

checkTime()


@bot.command(name="chan")
async def configure(ctx, name):
    await ctx.message.guild.create_text_channel(name)

@bot.listen('on_ready')
async def initialisation():
    print("CONNECTED")


bot.run(bot_token)