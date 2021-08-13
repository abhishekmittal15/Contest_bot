import requests
from bs4 import BeautifulSoup


url="https://atcoder.jp/contests/"

result=[]
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
    contest['eligibility']=fields[3].text
    result.append(contest)

