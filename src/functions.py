import discord
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

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
        details["time"]=f"{start_hour}:{start_minute}"
        details["duration"]=timedelta(seconds=dur)
        ret.append(details)
        if(startTime<today):
            break
    return ret

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

async def cc_contest():
    url="https://www.codechef.com/api/list/contests/all?sort_by=END&sorting_order=desc&offset=0&mode=all"
    res=requests.get(url)
    res=res.json()
    future_contests=res['future_contests']
    results=[]
    for contest in future_contests:
        cc_contest={}
        cc_contest['name']=contest['contest_name']
        cc_contest['time']=contest['contest_start_date']
        cc_contest['dur']=contest['contest_end_date']
        results.append(cc_contest)
    return results

async def display_cf(ctx, result):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    await ctx.send(embed=embedVar)


