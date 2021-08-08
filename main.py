#%%
import os 
import discord 
from functions import *
from dotenv import load_dotenv
load_dotenv()
bot_token=os.getenv("DISCORD_TOKEN")

client=discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if(message.author==client.user):
        return 
    content=message.content

    if(content.startswith("-")):
        content=content[1:]
        if(content=="contests"):
            await contest_list(message)

client.run(bot_token)