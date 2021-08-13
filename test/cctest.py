import requests 

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

