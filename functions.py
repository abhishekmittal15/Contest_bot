import discord
import requests
from datetime import datetime, timedelta

async def contest_list(ctx):
    url="https://codeforces.com/api/contest.list"
    res=requests.get(url)
    res=res.json()
    contests=res["result"]

    today=datetime.today()
    ret=[]
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
        details={}
        details["name"]=name
        details["start"]=f"{start_hour}:{start_minute}"
        details["duration"]=timedelta(seconds=dur)
        ret.append(details)
        if(startTime<today):
            break
    return ret
