import discord
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

# fetch info functions

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
        details["time"]=f"{start_day}/{start_month}/{start_year} at {start_hour}:{start_minute}"
        details["duration"]=timedelta(seconds=dur)
        ret.append(details)
        if(startTime<today):
            break
    return ret

# atcoder
async def ac_contest(ctx):
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
        cc_contest['time']=contest['contest_start_date']
        cc_contest['duration']=contest['contest_end_date']
        results.append(cc_contest)
    return results


# display functions

# display codeforces
async def display_cf(ctx, result):

    # await ctx.send(result[0])

    for contest in result:
        embedVar = discord.Embed(title=contest["name"], color=0x00ff00)
        embedVar.add_field(name="Time", value=contest["time"], inline=False)

        td = contest["duration"]

        # days = td.days
        hours = td.seconds // 3600
        minutes = (td.seconds // 60) % 60
        
        duration = f"{hours} hr {minutes} min"

        embedVar.add_field(name="Duration", value=duration, inline=False)
        await ctx.send(embed=embedVar)
