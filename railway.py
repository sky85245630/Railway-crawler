import requests
from bs4 import BeautifulSoup
# import html5lib
import time


url = 'https://www.railway.gov.tw/tra-tip-web/tip'
# 存車站名車＆代碼
staDic = {}
# 取得時間
today = time.strftime('%Y/%m/%d')

sTime = '06:00'
eTime = '12:00'

def getTrip():
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤'+url)
        return

    soup = BeautifulSoup(resp.text,'html5lib')
    # 取得車站名
    stations = soup.find(id = 'cityBot').ul.find_all('li')

    for station in stations:
        # 把stationName指向為station按鈕裡面的文字
        stationName = station.button.text
        stationId = station.button['title']
        staDic[stationName] = stationId

    # 去找到驗證的csrf
    csrf = soup.find(id = 'queryForm').find('input',{'name':'_csrf'})['value']

    # 建立傳送
    formData = {
        'trainTypeList': 'ALL',
        'transfer': 'ONE',
        'startOrEndTime': 'true',
        'startStation':staDic['松山'],
        'endStation':staDic['新營'],
        'rideDate':today,
        'startTime':sTime,
        'endTime':eTime
    }
    
    # 去POST資料進去接下來就會到第二頁
    queryUrl = soup.find(id='queryForm')['action']
    qResp = requests.post('https://www.railway.gov.tw'+queryUrl,data = formData)
    qSoup = BeautifulSoup(qResp.text,'html5lib')
    trs = qSoup.find_all('tr','trip-column')
    for tr in trs:
        td = tr.find_all('td')
        print('%s : %s, %s' & (td[0].ul.li.a.text , td[1].text , td[2].text))

getTrip()
