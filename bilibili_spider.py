import requests
import xlwt
import urllib3

urllib3.disable_warnings()
kv = {'User-Agent': 'Mozilla/5.0'}

bilibili_workbook = xlwt.Workbook()
bilibili_worksheet = bilibili_workbook.add_sheet("bilibili番剧热榜")

codelist = []
for i in range(151):
    r = requests.get('https://api.bilibili.com/pgc/season/index/result?st=1&order=4&season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page='+str(i+1)+'&season_type=1&pagesize=20&type=1',headers=kv,verify=False)
    r.encoding = "utf-8"
    jsonlists = r.json()
    codelist.append(jsonlists)
    print(codelist)
titlelist = []
orderlist = []
coverlist = []
linklist = []
for n in range(151):
    dir = codelist[n]
    for m in range(20):
        title = dir["data"]["list"][m]["title"]
        order = dir["data"]["list"][m]["order"]
        cover = dir["data"]["list"][m]["cover"]
        link = dir["data"]["list"][m]["link"]
        print(title)
        print(order)
        print(cover)
        print(link)
        titlelist.append(title)
        orderlist.append(order)
        coverlist.append(cover)
        linklist.append(link)

for h in range(151*20):
    bilibili_worksheet.write(h,0,titlelist[h])
    bilibili_worksheet.write(h,1,orderlist[h])
    bilibili_worksheet.write(h,2,coverlist[h])bilibili_worksheet.write((n+1)*(m+1),0,title)
    bilibili_worksheet.write(h,3,linklist[h])

bilibili_workbook.save("C:/Users/lz139/Desktop/bilibili.xls")





