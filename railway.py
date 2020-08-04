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

    
    
    
