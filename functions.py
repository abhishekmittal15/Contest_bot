import requests
from datetime import datetime, timedelta

async def contest_list(message):
    url="https://codeforces.com/api/contest.list"
    res=requests.get(url)
    res=res.json()
    contests=res["result"]

    today=datetime.today()
    for contest in contests:
        id=contest["id"]
        name=contest["name"]
        startTime=contest["startTimeSeconds"]
        dur=contest["durationSeconds"]
        startTime=datetime.fromtimestamp(startTime)
        start_year=startTime.year
        start_month=startTime.month
        start_day=startTime.day
        start_hour=startTime.hour
        start_minute=startTime.minute
        await message.channel.send(f"{name} is at {start_hour}:{start_minute} on {start_day}/{start_month}/{start_year} for {timedelta(seconds = dur)} ")
        if(startTime<today):
            break
