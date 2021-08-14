from datetime import datetime
import json

def convert_to_12hr(tm):
    d = datetime.strptime(tm, "%H:%M")
    return d.strftime("%I:%M %p")

def convert_to_date(s):
    datetime_object = datetime.strptime(s, '%d %b %Y %H:%M:%S')
    return datetime_object

def get_duration(dur):
    
    hours = dur.seconds // 3600
    minutes = (dur.seconds // 60) % 60
    return f"{hours} hr {minutes} min"


def sort_by_time(contests):
    


    return contests

def get_channel(ctx, code):

    f = open('data.json', "r")
    data = json.loads(f.read())
    f.close()

    if str(ctx.message.guild.id) in data["guilds"] and code in data["guilds"][str(ctx.message.guild.id)]:
        for channel in ctx.guild.channels:
            if str(channel.id) == data["guilds"][str(ctx.message.guild.id)][code]:
                return channel
    
    return ctx.message.channel