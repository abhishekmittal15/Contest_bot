from datetime import datetime
import json
import pytz
import tzlocal

def convert_to_12hr(tm):
    d = datetime.strptime(tm, "%H:%M")
    return d.strftime("%I:%M %p")

def to_local_time(t):
    local_timezone = tzlocal.get_localzone() # get pytz tzinfo
    local_time = t.replace(tzinfo=pytz.utc).astimezone(local_timezone)

    return local_time

def convert_to_date(s):
    datetime_object = datetime.strptime(s, '%d %b %Y %H:%M:%S')
    return datetime_object

def get_duration(dur):
    
    seconds = dur
    s = ""

    days = seconds // 86400
    if days > 0:
        s += f"{days} d "
        seconds = seconds % 86400

    hours = seconds // 3600
    if hours > 0:
        s += f"{hours} hr "
        seconds = seconds % 3600

    minutes = seconds // 60
    if minutes > 0:
        s += f"{minutes} min "
        seconds = seconds % 60

    return s


def sort_by_time(contests):
    
    contests = sorted(contests, key= lambda x: datetime.strptime(x["date"] + " " + x["time"], '%d/%m/%Y %I:%M %p'))
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