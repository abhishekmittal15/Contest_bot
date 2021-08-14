import discord
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import json

from helpers import *

site_list = {"cf":"codeforces", "cc":"codechef" ,"ac":"atcoder"}

# fetch info functions

# name link date time duration

# codeforces
async def cf_contest():
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
        details["link"]="https://codeforces.com/contest/"+str(id)
        details["date"] = f"{start_day}/{start_month}/{start_year}"
        details["time"]= convert_to_12hr(f"{start_hour}:{start_minute}")
        details["duration"]= get_duration(timedelta(seconds=dur))
        ret.append(details)
        if(startTime<today):
            break
    ret = sort_by_time(ret)
    return ret

# atcoder
async def ac_contest():
    url="https://atcoder.jp/contests/"

    results=[]
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'html.parser')
    upcoming=soup.find(id="contest-table-upcoming")
    upcoming=upcoming.tbody
    contests=upcoming.find_all('tr')
    for i in contests:
        contest={}
        fields=i.find_all('td')
        contest['time']=fields[0].time.text
        contest['name']=fields[1].a.text
        contest['duration']=fields[2].text
        results.append(contest)
    results = sort_by_time(results)
    return results

# codechef
async def cc_contest():
    url="https://www.codechef.com/api/list/contests/all?sort_by=END&sorting_order=desc&offset=0&mode=all"
    res=requests.get(url)
    res=res.json()
    future_contests=res['future_contests']
    results=[]
    for contest in future_contests:
        cc_contest={}
        cc_contest['link']="https://www.codechef.com/"+contest['contest_code']
        cc_contest['name']=contest['contest_name']
        # cc_contest['start_time']=contest['contest_start_date']
        # cc_contest['end_time']=contest['contest_end_date']
        start_time = convert_to_date(contest["contest_start_date"])
        end_time = convert_to_date(contest["contest_end_date"])

        cc_contest["date"] = start_time.strftime("%d/%m/%Y")
        cc_contest["time"] = convert_to_12hr(start_time.strftime("%H:%M"))
        cc_contest["duration"] = get_duration(end_time - start_time)

        results.append(cc_contest)
        
    results = sort_by_time(results)
    return results



# display function
async def display_contests(ctx, result, website):

    channel = get_channel(ctx, website)
    
    if not len(result):
        await channel.send("No contests available.")
        return

    await channel.send(f"{site_list[website]} contests:")

    for contest in result:
        time_val = f"{contest['date']} at {contest['time']} ({contest['duration']})" 

        embedVar = discord.Embed(description=f"[{contest['name']}]({contest['link']})", color=0x00ff00)
        embedVar.add_field(name="Time", value=time_val, inline=False)
        
        await channel.send(embed=embedVar)